# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingame.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_maingame(object):
    def setupUi(self, maingame):
        if not maingame.objectName():
            maingame.setObjectName(u"maingame")
        maingame.resize(600, 600)
        maingame.setMinimumSize(QSize(600, 600))
        maingame.setMaximumSize(QSize(600, 600))
        self.label = QLabel(maingame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -40, 221, 111))
        self.backButton = QPushButton(maingame)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(500, 490, 80, 24))
        self.gridLayoutWidget = QWidget(maingame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 40, 561, 441))
        self.container = QGridLayout(self.gridLayoutWidget)
        self.container.setObjectName(u"container")
        self.container.setContentsMargins(0, 0, 0, 0)
        self.boardcontainer = QWidget(self.gridLayoutWidget)
        self.boardcontainer.setObjectName(u"boardcontainer")

        self.container.addWidget(self.boardcontainer, 0, 0, 1, 1)


        self.retranslateUi(maingame)

        QMetaObject.connectSlotsByName(maingame)
    # setupUi

    def retranslateUi(self, maingame):
        maingame.setWindowTitle(QCoreApplication.translate("maingame", u"Form", None))
        self.label.setText(QCoreApplication.translate("maingame", u"GAME GOES HERE", None))
        self.backButton.setText(QCoreApplication.translate("maingame", u"Back", None))
    # retranslateUi

