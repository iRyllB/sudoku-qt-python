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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_maingame(object):
    def setupUi(self, maingame):
        if not maingame.objectName():
            maingame.setObjectName(u"maingame")
        maingame.resize(600, 600)
        maingame.setMinimumSize(QSize(600, 600))
        maingame.setMaximumSize(QSize(600, 600))
        self.label = QLabel(maingame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 180, 221, 111))

        self.retranslateUi(maingame)

        QMetaObject.connectSlotsByName(maingame)
    # setupUi

    def retranslateUi(self, maingame):
        maingame.setWindowTitle(QCoreApplication.translate("maingame", u"Form", None))
        self.label.setText(QCoreApplication.translate("maingame", u"GAME GOES HERE", None))
    # retranslateUi

