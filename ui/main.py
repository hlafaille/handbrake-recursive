# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.movies_list = QListWidget(self.groupBox)
        self.movies_list.setObjectName(u"movies_list")

        self.gridLayout_2.addWidget(self.movies_list, 1, 0, 1, 2)

        self.browse_directories_button = QPushButton(self.groupBox)
        self.browse_directories_button.setObjectName(u"browse_directories_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browse_directories_button.sizePolicy().hasHeightForWidth())
        self.browse_directories_button.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.browse_directories_button, 0, 1, 1, 1)

        self.directory_path = QLineEdit(self.groupBox)
        self.directory_path.setObjectName(u"directory_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.directory_path.sizePolicy().hasHeightForWidth())
        self.directory_path.setSizePolicy(sizePolicy2)
        self.directory_path.setReadOnly(True)

        self.gridLayout_2.addWidget(self.directory_path, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.file_extensions_table = QListWidget(self.groupBox_2)
        QListWidgetItem(self.file_extensions_table)
        QListWidgetItem(self.file_extensions_table)
        QListWidgetItem(self.file_extensions_table)
        QListWidgetItem(self.file_extensions_table)
        self.file_extensions_table.setObjectName(u"file_extensions_table")

        self.gridLayout_3.addWidget(self.file_extensions_table, 1, 0, 1, 4)

        self.whitelist = QRadioButton(self.groupBox_2)
        self.whitelist.setObjectName(u"whitelist")
        self.whitelist.setEnabled(False)

        self.gridLayout_3.addWidget(self.whitelist, 0, 1, 1, 1)

        self.file_extension = QLineEdit(self.groupBox_2)
        self.file_extension.setObjectName(u"file_extension")

        self.gridLayout_3.addWidget(self.file_extension, 0, 2, 1, 1)

        self.blacklist = QRadioButton(self.groupBox_2)
        self.blacklist.setObjectName(u"blacklist")
        self.blacklist.setChecked(True)

        self.gridLayout_3.addWidget(self.blacklist, 0, 0, 1, 1)

        self.add_file_extension = QPushButton(self.groupBox_2)
        self.add_file_extension.setObjectName(u"add_file_extension")

        self.gridLayout_3.addWidget(self.add_file_extension, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.progress = QProgressBar(self.tab)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(0)
        self.progress.setTextVisible(False)

        self.gridLayout_4.addWidget(self.progress, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_7.addWidget(self.checkBox, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_9 = QRadioButton(self.groupBox_3)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_6.addWidget(self.radioButton_9, 6, 1, 1, 1)

        self.radioButton_12 = QRadioButton(self.groupBox_3)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout_6.addWidget(self.radioButton_12, 9, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_6.addWidget(self.radioButton_6, 3, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_6.addWidget(self.radioButton_4, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 12, 1, 1, 1)

        self.radioButton_10 = QRadioButton(self.groupBox_3)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout_6.addWidget(self.radioButton_10, 7, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_6.addWidget(self.radioButton_3, 0, 1, 1, 1)

        self.radioButton_13 = QRadioButton(self.groupBox_3)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout_6.addWidget(self.radioButton_13, 10, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.groupBox_3)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_6.addWidget(self.radioButton_7, 4, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.gridLayout_6.addWidget(self.radioButton_5, 2, 1, 1, 1)

        self.radioButton_8 = QRadioButton(self.groupBox_3)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_6.addWidget(self.radioButton_8, 5, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.groupBox_3)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout_6.addWidget(self.radioButton_11, 8, 1, 1, 1)

        self.radioButton_14 = QRadioButton(self.groupBox_3)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.gridLayout_6.addWidget(self.radioButton_14, 11, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.begin_encoding_button = QPushButton(self.tab_2)
        self.begin_encoding_button.setObjectName(u"begin_encoding_button")

        self.gridLayout_5.addWidget(self.begin_encoding_button, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select A Directory", None))
        self.browse_directories_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"File Extensions", None))

        __sortingEnabled = self.file_extensions_table.isSortingEnabled()
        self.file_extensions_table.setSortingEnabled(False)
        ___qlistwidgetitem = self.file_extensions_table.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"txt", None));
        ___qlistwidgetitem1 = self.file_extensions_table.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"srt", None));
        ___qlistwidgetitem2 = self.file_extensions_table.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"jpg", None));
        ___qlistwidgetitem3 = self.file_extensions_table.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"png", None));
        self.file_extensions_table.setSortingEnabled(__sortingEnabled)

        self.whitelist.setText(QCoreApplication.translate("MainWindow", u"Whitelist", None))
        self.file_extension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: txt, png, tif", None))
        self.blacklist.setText(QCoreApplication.translate("MainWindow", u"Blacklist", None))
        self.add_file_extension.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Directory", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Preset File", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Load From GUI", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Encoder", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"H265 NVENC", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"VP8", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"X265", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"X264 10-Bit", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"MPEG4", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"X264", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"VP9", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"X265 10-Bit", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"H264 NVENC", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"X265 12-Bit", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"MPEG2", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"Theora", None))
        self.begin_encoding_button.setText(QCoreApplication.translate("MainWindow", u"Begin Encoding", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Preset", None))
    # retranslateUi

