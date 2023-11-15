# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bone3d.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(973, 609)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_load_file = QPushButton(self.widget_3)
        self.button_load_file.setObjectName(u"button_load_file")

        self.verticalLayout_2.addWidget(self.button_load_file)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_edit_name_model = QLineEdit(self.widget_2)
        self.line_edit_name_model.setObjectName(u"line_edit_name_model")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_name_model.sizePolicy().hasHeightForWidth())
        self.line_edit_name_model.setSizePolicy(sizePolicy)
        self.line_edit_name_model.setAlignment(Qt.AlignCenter)
        self.line_edit_name_model.setPlaceholderText(u"Save Model Name")

        self.horizontalLayout_2.addWidget(self.line_edit_name_model)

        self.button_save_model = QPushButton(self.widget_2)
        self.button_save_model.setObjectName(u"button_save_model")

        self.horizontalLayout_2.addWidget(self.button_save_model)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.button_3d_printing = QPushButton(self.widget_3)
        self.button_3d_printing.setObjectName(u"button_3d_printing")

        self.verticalLayout_2.addWidget(self.button_3d_printing)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(450, 400))
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labe_mesh_tool = QLabel(self.widget_4)
        self.labe_mesh_tool.setObjectName(u"labe_mesh_tool")

        self.verticalLayout_3.addWidget(self.labe_mesh_tool)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.button_select = QPushButton(self.widget_4)
        self.button_select.setObjectName(u"button_select")

        self.verticalLayout_3.addWidget(self.button_select)

        self.button_crop = QPushButton(self.widget_4)
        self.button_crop.setObjectName(u"button_crop")

        self.verticalLayout_3.addWidget(self.button_crop)

        self.button_smooth = QPushButton(self.widget_4)
        self.button_smooth.setObjectName(u"button_smooth")

        self.verticalLayout_3.addWidget(self.button_smooth)

        self.button_delete = QPushButton(self.widget_4)
        self.button_delete.setObjectName(u"button_delete")

        self.verticalLayout_3.addWidget(self.button_delete)

        self.button_fill = QPushButton(self.widget_4)
        self.button_fill.setObjectName(u"button_fill")

        self.verticalLayout_3.addWidget(self.button_fill)

        self.button_drill = QPushButton(self.widget_4)
        self.button_drill.setObjectName(u"button_drill")

        self.verticalLayout_3.addWidget(self.button_drill)

        self.button_undo = QPushButton(self.widget_4)
        self.button_undo.setObjectName(u"button_undo")

        self.verticalLayout_3.addWidget(self.button_undo)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_3d = QWidget(self.centralwidget)
        self.widget_3d.setObjectName(u"widget_3d")
        self.layout_3d_field = QVBoxLayout(self.widget_3d)
        self.layout_3d_field.setObjectName(u"layout_3d_field")

        self.horizontalLayout.addWidget(self.widget_3d)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 973, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_load_file.setText(QCoreApplication.translate("MainWindow", u"Load File(.stl)", None))
        self.line_edit_name_model.setText("")
        self.button_save_model.setText(QCoreApplication.translate("MainWindow", u"Save Model(.stl)", None))
        self.button_3d_printing.setText(QCoreApplication.translate("MainWindow", u"3D Printing", None))
        self.labe_mesh_tool.setText(QCoreApplication.translate("MainWindow", u"Mesh Tool", None))
        self.button_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.button_crop.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.button_smooth.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.button_fill.setText(QCoreApplication.translate("MainWindow", u"Fill", None))
        self.button_drill.setText(QCoreApplication.translate("MainWindow", u"Drill", None))
        self.button_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
    # retranslateUi

