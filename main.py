import sys
from PyQt5 import QtWidgets
import numpy as np
from bone3d_ui import Ui_MainWindow
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vedo import Plotter, Mesh, Points
import vedo
from enum import Enum


class SelectionMode(Enum):
    surface_mode = 1
    draw_spline_mode = 2


class Bone3dFunction(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # parameter
        self.current_mode = SelectionMode.surface_mode  # initial with selection mode
        self.drawmode = False
        self.cpoints = []
        self.points = None
        self.spline = None
        self.selected_ids = np.array([]).astype(int)
        self.tol = 0.008
        self.top_pts = []
        self.topline = None
        self.old_ids = []
        self.mesh = None
        self.save_mesh_name = ""
        self.drill_radius = 1
        # setup ui
        self.ui = self.setupUi(program)

        self.frame = QtWidgets.QFrame()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        vedo.settings.use_parallel_projection = True
        # Create renderer and add the vedo objects and callbacks
        self.plt = Plotter(qt_widget=self.vtkWidget)

        self.plt.add_callback("left mouse click", self.onLeftClick)
        self.plt.add_callback("right mouse click", self.onRightClick)
        self.plt.add_callback('MouseMove', self.onMouseMove)
        # Set-up the rest of the Qt window
        self.layout_3d_field.addWidget(self.vtkWidget)

        # connect function to pyqt button
        self.button_select.clicked.connect(self.change_to_selection_mode)
        self.button_crop.clicked.connect(self.change_to_crop_mode)
        self.button_smooth.clicked.connect(self.change_to_smooth_mode)
        self.button_delete.clicked.connect(self.change_to_delete_mode)
        self.button_fill.clicked.connect(self.change_to_fill_mode)
        self.button_drill.clicked.connect(self.handle_drill_mode)
        self.button_undo.clicked.connect(self.handle_undo_button)
        self.button_load_file.clicked.connect(self.handle_browse_file)
        self.button_save_model.clicked.connect(self.handle_save_file)
        self.line_edit_name_model.textChanged.connect(self.handle_name_model)
        self.button_3d_printing.clicked.connect(self.handle_3d_printing)
        self.spinbox_radius.valueChanged.connect(
            self.handle_drill_radius_value_change)

    def handle_drill_radius_value_change(self):
        self.drill_radius = self.spinbox_radius.value()

    def handle_3d_printing(self):
        if (self.mesh is not None):
            extrude_mesh = self.mesh.clone().extrude(10)
            self.re_create_mesh(extrude_mesh)

    def handle_name_model(self):
        if (self.mesh is not None):
            self.save_mesh_name = self.line_edit_name_model.text()

    def handle_browse_file(self):
        if (self.mesh is not None):
            self.plt.clear()
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self.ui, 'Import STL file', '', 'file (*.stl)')
        if (fname != None and fname[0] != ""):
            self.mesh = Mesh(fname[0])
            self.mesh.cellcolors = np.ones([self.mesh.ncells, 3])*125
            self.ori_mesh = self.mesh.clone()
            self.plt += [self.mesh]
            self.plt.show(axes=1)

    def handle_save_file(self):
        if (self.mesh is not None):
            if (self.save_mesh_name != ""):
                self.mesh.write(self.save_mesh_name + '.stl')
                file = str(QtWidgets.QFileDialog.getExistingDirectory(
                    self.ui, "Select Directory"))
                self.mesh.write(file+'/'+self.save_mesh_name + '.stl')

    def handle_undo_button(self):
        self.plt.remove([self.mesh])
        self.mesh = self.ori_mesh.clone()
        self.selected_ids = np.array([]).astype(int)
        self.plt.add(self.mesh).render()

    def change_to_selection_mode(self):
        threshold = self.mesh.clone().threshold(
            "CellsRGBA", 0, 1, on='cells')
        self.re_create_mesh(threshold)

    def handle_drill_mode(self):
        center = self.mesh.center_of_mass()
        drill = vedo.Cylinder(
            pos=(center[0], center[1], center[2]), r=self.drill_radius, height=1500)
        self.mesh.cut_with_mesh(drill, invert=True)
        self.re_create_mesh(self.mesh)

    def re_create_mesh(self, new_mesh):
        self.plt.remove([self.mesh])
        new_mesh.write('temp.stl')
        self.mesh = Mesh('temp.stl')
        self.mesh.cellcolors = np.ones([self.mesh.ncells, 3])*125
        self.selected_ids = np.array([]).astype(int)
        self.plt.add([self.mesh]).render()

    def change_to_crop_mode(self):
        if (self.mesh is not None):
            self.mesh.cellcolors = np.ones([self.mesh.ncells, 3])*125
            self.plt.render()
            self.current_mode = SelectionMode.draw_spline_mode

    def change_to_smooth_mode(self):
        if (self.mesh is not None):
            threshold_mesh = self.mesh.clone().smooth(niter=100).threshold(
                "CellsRGBA", 0, 1, on='cells')
            new_threshold_mesh = vedo.merge(self.mesh.clone(), threshold_mesh)
            self.re_create_mesh(new_threshold_mesh)

    def change_to_delete_mode(self):
        if (len(self.selected_ids) > 0):
            self.mesh.delete_cells(self.selected_ids)
            self.selected_ids = np.array([]).astype(int)
            self.plt.render()

    def change_to_fill_mode(self):
        filled_hole = self.mesh.clone().delete_cells(
            self.selected_ids).fill_holes(size=50)
        self.re_create_mesh(filled_hole)

    def onLeftClick(self, event):
        if self.current_mode == SelectionMode.surface_mode:
            msh = event.actor
            if not msh:
                return
            pt = event.picked3d
            pts = Points(self.mesh.closest_point(pt, n=50), r=5)
            sph = vedo.fit_sphere(pts)
            sph_bounds = sph.GetBounds()
            ids = self.mesh.find_cells_in(xbounds=(sph_bounds[0], sph_bounds[1]), ybounds=(
                sph_bounds[2], sph_bounds[3]), zbounds=(sph_bounds[4], sph_bounds[5]))
            self.selected_ids = np.append(self.selected_ids, ids)
            for i in ids:
                self.mesh.cellcolors[i] = [0, 255, 0, 255]

    def handleHighLight(self, event):
        # check current cursor is able to pick
        pt = event.picked3d
        if pt is None:
            return
        pts = Points(self.mesh.closest_point(pt, n=50), r=5)
        sph = vedo.fit_sphere(pts)
        sph_bounds = sph.GetBounds()
        ids = self.mesh.find_cells_in(xbounds=(sph_bounds[0], sph_bounds[1]), ybounds=(
            sph_bounds[2], sph_bounds[3]), zbounds=(sph_bounds[4], sph_bounds[5]))
        self.mesh.cellcolors = np.ones([self.mesh.ncells, 3])*125
        for i in self.selected_ids:
            self.mesh.cellcolors[i] = [0, 255, 0, 255]
        for i in ids:
            if (i not in self.selected_ids):
                self.mesh.cellcolors[i] = [250, 250, 0, 255]
            self.plt.render()

    def onRightClick(self, evt):
        if self.current_mode == SelectionMode.draw_spline_mode:
            self.drawmode = not self.drawmode
            if self.spline:
                vedo.printc("Cutting the mesh please wait..", invert=True)
                tol = self.mesh.diagonal_size()/2            # size of ribbon
                pts = self.spline.points()
                # compute normal vector
                n = vedo.fit_plane(pts, signed=True).normal
                rib = vedo.Ribbon(pts - tol*n, pts + tol*n, closed=True)
                self.mesh.cut_with_mesh(rib)
                self.plt.clear()
                self.cpoints, self.points, self.spline = [], None, None
                self.top_pts, self.topline = [], None
                self.re_create_mesh(self.mesh)

                self.current_mode = SelectionMode.surface_mode

    def onMouseMove(self, event):
        if self.current_mode == SelectionMode.surface_mode:
            self.handleHighLight(event)
        elif self.current_mode == SelectionMode.draw_spline_mode:
            if self.drawmode:
                if event.actor:
                    self.top_pts.append(event.picked3d)
                    self.topline = Points(self.top_pts, r=4)
                    self.topline.c("red5").pickable(False)

                self.plt.remove(
                    [self.points, self.spline, self.topline])
                # make this 2d-screen point 3d:
                cpt = self.plt.compute_world_coordinate(event.picked2d)
                self.cpoints.append(cpt)
                self.points = vedo.Points(self.cpoints, r=8).c('black')
                if len(self.cpoints) > 2:
                    self.spline = vedo.Line(
                        self.cpoints, closed=True).lw(5).c('red5')
                    self.plt.add(
                        [self.points, self.spline, self.topline]).render()

    def onClose(self):
        # Disable the interactor before closing to prevent it
        # from trying to act on already deleted items
        self.vtkWidget.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("bone 3d")
    program = QtWidgets.QMainWindow()
    window = Bone3dFunction()
    program.show()
    # app.aboutToQuit.connect(program.onClose)  # <-- connect the onClose event
    # app.exec_()
    sys.exit(app.exec_())
