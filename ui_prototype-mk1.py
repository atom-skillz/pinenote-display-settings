#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prototype-mk1mVEyyv.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 0))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lyRotation = QGridLayout()
        self.lyRotation.setObjectName(u"lyRotation")
        self.pbRotation0 = QPushButton(self.centralwidget)
        self.pbRotation0.setObjectName(u"pbRotation0")
        self.pbRotation0.setAutoFillBackground(False)
        self.pbRotation0.setFlat(False)

        self.lyRotation.addWidget(self.pbRotation0, 0, 1, 1, 1)

        self.pbRotation180 = QPushButton(self.centralwidget)
        self.pbRotation180.setObjectName(u"pbRotation180")

        self.lyRotation.addWidget(self.pbRotation180, 2, 1, 1, 1)

        self.pbRotation90 = QPushButton(self.centralwidget)
        self.pbRotation90.setObjectName(u"pbRotation90")

        self.lyRotation.addWidget(self.pbRotation90, 1, 2, 1, 1)

        self.pbToggleAutoRot = QPushButton(self.centralwidget)
        self.pbToggleAutoRot.setObjectName(u"pbToggleAutoRot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbToggleAutoRot.sizePolicy().hasHeightForWidth())
        self.pbToggleAutoRot.setSizePolicy(sizePolicy)

        self.lyRotation.addWidget(self.pbToggleAutoRot, 1, 1, 1, 1)

        self.pbRotation270 = QPushButton(self.centralwidget)
        self.pbRotation270.setObjectName(u"pbRotation270")

        self.lyRotation.addWidget(self.pbRotation270, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.lyRotation)

        self.lyBacklight = QVBoxLayout()
        self.lyBacklight.setObjectName(u"lyBacklight")
        self.lyBkWarm = QVBoxLayout()
        self.lyBkWarm.setObjectName(u"lyBkWarm")
        self.lyBkWarm.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pbWarmUp = QPushButton(self.centralwidget)
        self.pbWarmUp.setObjectName(u"pbWarmUp")
        sizePolicy.setHeightForWidth(self.pbWarmUp.sizePolicy().hasHeightForWidth())
        self.pbWarmUp.setSizePolicy(sizePolicy)

        self.lyBkWarm.addWidget(self.pbWarmUp, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.lbWarm = QLabel(self.centralwidget)
        self.lbWarm.setObjectName(u"lbWarm")
        sizePolicy.setHeightForWidth(self.lbWarm.sizePolicy().hasHeightForWidth())
        self.lbWarm.setSizePolicy(sizePolicy)
        self.lbWarm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lyBkWarm.addWidget(self.lbWarm, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pbWarmDown = QPushButton(self.centralwidget)
        self.pbWarmDown.setObjectName(u"pbWarmDown")
        sizePolicy.setHeightForWidth(self.pbWarmDown.sizePolicy().hasHeightForWidth())
        self.pbWarmDown.setSizePolicy(sizePolicy)

        self.lyBkWarm.addWidget(self.pbWarmDown, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.lyBacklight.addLayout(self.lyBkWarm)

        self.lnBacklight = QFrame(self.centralwidget)
        self.lnBacklight.setObjectName(u"lnBacklight")
        self.lnBacklight.setFrameShape(QFrame.Shape.HLine)
        self.lnBacklight.setFrameShadow(QFrame.Shadow.Sunken)

        self.lyBacklight.addWidget(self.lnBacklight)

        self.lyBkCold = QVBoxLayout()
        self.lyBkCold.setObjectName(u"lyBkCold")
        self.pbColdUp = QPushButton(self.centralwidget)
        self.pbColdUp.setObjectName(u"pbColdUp")
        sizePolicy.setHeightForWidth(self.pbColdUp.sizePolicy().hasHeightForWidth())
        self.pbColdUp.setSizePolicy(sizePolicy)

        self.lyBkCold.addWidget(self.pbColdUp, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.lbCold = QLabel(self.centralwidget)
        self.lbCold.setObjectName(u"lbCold")
        sizePolicy.setHeightForWidth(self.lbCold.sizePolicy().hasHeightForWidth())
        self.lbCold.setSizePolicy(sizePolicy)

        self.lyBkCold.addWidget(self.lbCold, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pbColdDown = QPushButton(self.centralwidget)
        self.pbColdDown.setObjectName(u"pbColdDown")
        sizePolicy.setHeightForWidth(self.pbColdDown.sizePolicy().hasHeightForWidth())
        self.pbColdDown.setSizePolicy(sizePolicy)

        self.lyBkCold.addWidget(self.pbColdDown, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.lyBacklight.addLayout(self.lyBkCold)


        self.horizontalLayout.addLayout(self.lyBacklight)

        self.lyOthers = QVBoxLayout()
        self.lyOthers.setObjectName(u"lyOthers")
        self.lyWaveforms = QVBoxLayout()
        self.lyWaveforms.setObjectName(u"lyWaveforms")
        self.lbWaveforms = QLabel(self.centralwidget)
        self.lbWaveforms.setObjectName(u"lbWaveforms")
        sizePolicy.setHeightForWidth(self.lbWaveforms.sizePolicy().hasHeightForWidth())
        self.lbWaveforms.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.lbWaveforms.setFont(font)
        self.lbWaveforms.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lyWaveforms.addWidget(self.lbWaveforms, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pbWaveform1 = QPushButton(self.centralwidget)
        self.pbWaveform1.setObjectName(u"pbWaveform1")

        self.lyWaveforms.addWidget(self.pbWaveform1)

        self.pbWaveform2 = QPushButton(self.centralwidget)
        self.pbWaveform2.setObjectName(u"pbWaveform2")

        self.lyWaveforms.addWidget(self.pbWaveform2)

        self.pbWaveform3 = QPushButton(self.centralwidget)
        self.pbWaveform3.setObjectName(u"pbWaveform3")

        self.lyWaveforms.addWidget(self.pbWaveform3)

        self.pbWaveform4 = QPushButton(self.centralwidget)
        self.pbWaveform4.setObjectName(u"pbWaveform4")

        self.lyWaveforms.addWidget(self.pbWaveform4)


        self.lyOthers.addLayout(self.lyWaveforms)

        self.lyWindowModes = QVBoxLayout()
        self.lyWindowModes.setObjectName(u"lyWindowModes")
        self.lbWindowModes = QLabel(self.centralwidget)
        self.lbWindowModes.setObjectName(u"lbWindowModes")
        sizePolicy.setHeightForWidth(self.lbWindowModes.sizePolicy().hasHeightForWidth())
        self.lbWindowModes.setSizePolicy(sizePolicy)

        self.lyWindowModes.addWidget(self.lbWindowModes, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cbWindowModes = QComboBox(self.centralwidget)
        self.cbWindowModes.setObjectName(u"cbWindowModes")

        self.lyWindowModes.addWidget(self.cbWindowModes)


        self.lyOthers.addLayout(self.lyWindowModes)

        self.lyScale = QVBoxLayout()
        self.lyScale.setObjectName(u"lyScale")
        self.lbScale = QLabel(self.centralwidget)
        self.lbScale.setObjectName(u"lbScale")
        sizePolicy.setHeightForWidth(self.lbScale.sizePolicy().hasHeightForWidth())
        self.lbScale.setSizePolicy(sizePolicy)

        self.lyScale.addWidget(self.lbScale, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cbScaleList = QComboBox(self.centralwidget)
        self.cbScaleList.setObjectName(u"cbScaleList")

        self.lyScale.addWidget(self.cbScaleList)


        self.lyOthers.addLayout(self.lyScale)

        self.pushAdaptiveSync = QPushButton(self.centralwidget)
        self.pushAdaptiveSync.setObjectName(u"pushAdaptiveSync")

        self.lyOthers.addWidget(self.pushAdaptiveSync)

        self.pushFRefresh = QPushButton(self.centralwidget)
        self.pushFRefresh.setObjectName(u"pushFRefresh")

        self.lyOthers.addWidget(self.pushFRefresh)


        self.horizontalLayout.addLayout(self.lyOthers)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PineNote Display Settings", None))
        self.pbRotation0.setText(QCoreApplication.translate("MainWindow", u"\udb82\udc86", None))
        self.pbRotation180.setText(QCoreApplication.translate("MainWindow", u"\udb86\udd99", None))
        self.pbRotation90.setText(QCoreApplication.translate("MainWindow", u"\udb81\udc68", None))
        self.pbToggleAutoRot.setText(QCoreApplication.translate("MainWindow", u"\udb81\udc78", None))
        self.pbRotation270.setText(QCoreApplication.translate("MainWindow", u"\udb81\udc66", None))
        self.pbWarmUp.setText(QCoreApplication.translate("MainWindow", u"\ueaf4", None))
        self.lbWarm.setText(QCoreApplication.translate("MainWindow", u"25% W", None))
        self.pbWarmDown.setText(QCoreApplication.translate("MainWindow", u"\ueaf3", None))
        self.pbColdUp.setText(QCoreApplication.translate("MainWindow", u"\ueaf4", None))
        self.lbCold.setText(QCoreApplication.translate("MainWindow", u"00% C", None))
        self.pbColdDown.setText(QCoreApplication.translate("MainWindow", u"\ueaf3", None))
        self.lbWaveforms.setText(QCoreApplication.translate("MainWindow", u"Waveforms", None))
        self.pbWaveform1.setText(QCoreApplication.translate("MainWindow", u"Waveform 1", None))
        self.pbWaveform2.setText(QCoreApplication.translate("MainWindow", u"Waveform 2", None))
        self.pbWaveform3.setText(QCoreApplication.translate("MainWindow", u"Waveform 3", None))
        self.pbWaveform4.setText(QCoreApplication.translate("MainWindow", u"Waveform 4", None))
        self.lbWindowModes.setText(QCoreApplication.translate("MainWindow", u"Window Modes", None))
        self.lbScale.setText(QCoreApplication.translate("MainWindow", u"Scales", None))
        self.pushAdaptiveSync.setText(QCoreApplication.translate("MainWindow", u"Adaptive Sync: OFF", None))
        self.pushFRefresh.setText(QCoreApplication.translate("MainWindow", u"Force Refresh", None))
    # retranslateUi

