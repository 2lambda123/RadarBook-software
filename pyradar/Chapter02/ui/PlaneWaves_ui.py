# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chapter02\PlaneWaves.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 680)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/python_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.frequency = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequency.sizePolicy().hasHeightForWidth())
        self.frequency.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frequency.setFont(font)
        self.frequency.setObjectName("frequency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.frequency)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.relative_permittivity = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relative_permittivity.sizePolicy().hasHeightForWidth())
        self.relative_permittivity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.relative_permittivity.setFont(font)
        self.relative_permittivity.setObjectName("relative_permittivity")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.relative_permittivity)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.relative_permeability = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relative_permeability.sizePolicy().hasHeightForWidth())
        self.relative_permeability.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.relative_permeability.setFont(font)
        self.relative_permeability.setObjectName("relative_permeability")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.relative_permeability)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.conductivity = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conductivity.sizePolicy().hasHeightForWidth())
        self.conductivity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.conductivity.setFont(font)
        self.conductivity.setObjectName("conductivity")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.conductivity)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.propagation_constant = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propagation_constant.sizePolicy().hasHeightForWidth())
        self.propagation_constant.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.propagation_constant.setFont(font)
        self.propagation_constant.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.propagation_constant.setObjectName("propagation_constant")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.propagation_constant)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.attenuation_constant = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attenuation_constant.sizePolicy().hasHeightForWidth())
        self.attenuation_constant.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.attenuation_constant.setFont(font)
        self.attenuation_constant.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.attenuation_constant.setObjectName("attenuation_constant")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.attenuation_constant)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.phase_constant = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_constant.sizePolicy().hasHeightForWidth())
        self.phase_constant.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.phase_constant.setFont(font)
        self.phase_constant.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.phase_constant.setObjectName("phase_constant")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.phase_constant)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.wave_impedance = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wave_impedance.sizePolicy().hasHeightForWidth())
        self.wave_impedance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.wave_impedance.setFont(font)
        self.wave_impedance.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wave_impedance.setObjectName("wave_impedance")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.wave_impedance)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.skin_depth = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skin_depth.sizePolicy().hasHeightForWidth())
        self.skin_depth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.skin_depth.setFont(font)
        self.skin_depth.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.skin_depth.setObjectName("skin_depth")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.skin_depth)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.wavelength = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavelength.sizePolicy().hasHeightForWidth())
        self.wavelength.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.wavelength.setFont(font)
        self.wavelength.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wavelength.setObjectName("wavelength")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.wavelength)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.phase_velocity = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_velocity.sizePolicy().hasHeightForWidth())
        self.phase_velocity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.phase_velocity.setFont(font)
        self.phase_velocity.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.phase_velocity.setObjectName("phase_velocity")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.phase_velocity)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(16, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.time = QtWidgets.QScrollBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time.setFont(font)
        self.time.setOrientation(QtCore.Qt.Horizontal)
        self.time.setObjectName("time")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.time)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plane Waves"))
        self.label_6.setText(_translate("MainWindow", "Input"))
        self.label.setText(_translate("MainWindow", "Frequency (Hz)"))
        self.frequency.setText(_translate("MainWindow", "300.0e6"))
        self.label_2.setText(_translate("MainWindow", "Relative Permittivity"))
        self.relative_permittivity.setText(_translate("MainWindow", "4.3"))
        self.label_3.setText(_translate("MainWindow", "Relative Permeability"))
        self.relative_permeability.setText(_translate("MainWindow", "1.0"))
        self.label_4.setText(_translate("MainWindow", "Conductivity (S/m)"))
        self.conductivity.setText(_translate("MainWindow", "0.01"))
        self.label_5.setText(_translate("MainWindow", "Output"))
        self.label_7.setText(_translate("MainWindow", "Propagation Constant (1/m):"))
        self.propagation_constant.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "Attenuation Constant (Np/m):"))
        self.attenuation_constant.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Phase Constant (rad/m):"))
        self.phase_constant.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "Wave Impedance (Ohms):"))
        self.wave_impedance.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "Skin Depth (m):"))
        self.skin_depth.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Wavelength (m):"))
        self.wavelength.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "Phase Velocity (m/s):"))
        self.phase_velocity.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "Time Step"))

import Libs.resources_rc
