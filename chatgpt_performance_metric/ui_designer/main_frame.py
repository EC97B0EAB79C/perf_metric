# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.golden_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.golden_lineEdit.setObjectName("golden_lineEdit")
        self.horizontalLayout.addWidget(self.golden_lineEdit)
        self.refresh_pushButton = QtWidgets.QPushButton(self.frame)
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 591, 455))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_11.addLayout(self.formLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scenario_allcheck_pushButton = QtWidgets.QPushButton(self.frame)
        self.scenario_allcheck_pushButton.setObjectName("scenario_allcheck_pushButton")
        self.horizontalLayout_4.addWidget(self.scenario_allcheck_pushButton)
        self.scenario_alluncheck_pushButton = QtWidgets.QPushButton(self.frame)
        self.scenario_alluncheck_pushButton.setObjectName("scenario_alluncheck_pushButton")
        self.horizontalLayout_4.addWidget(self.scenario_alluncheck_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.analyze_pushButton = QtWidgets.QPushButton(self.frame)
        self.analyze_pushButton.setObjectName("analyze_pushButton")
        self.horizontalLayout_4.addWidget(self.analyze_pushButton)
        self.save_pushButton = QtWidgets.QPushButton(self.frame)
        self.save_pushButton.setObjectName("save_pushButton")
        self.horizontalLayout_4.addWidget(self.save_pushButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addWidget(self.frame)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.alg_checkBox_1 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_1.setObjectName("alg_checkBox_1")
        self.verticalLayout_5.addWidget(self.alg_checkBox_1)
        self.alg_checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_2.setObjectName("alg_checkBox_2")
        self.verticalLayout_5.addWidget(self.alg_checkBox_2)
        self.alg_checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_3.setObjectName("alg_checkBox_3")
        self.verticalLayout_5.addWidget(self.alg_checkBox_3)
        self.alg_checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_4.setObjectName("alg_checkBox_4")
        self.verticalLayout_5.addWidget(self.alg_checkBox_4)
        self.alg_checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_5.setObjectName("alg_checkBox_5")
        self.verticalLayout_5.addWidget(self.alg_checkBox_5)
        self.alg_checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_6.setObjectName("alg_checkBox_6")
        self.verticalLayout_5.addWidget(self.alg_checkBox_6)
        self.alg_checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.alg_checkBox_7.setEnabled(True)
        self.alg_checkBox_7.setObjectName("alg_checkBox_7")
        self.verticalLayout_5.addWidget(self.alg_checkBox_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.allcheck_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.allcheck_pushButton.setObjectName("allcheck_pushButton")
        self.horizontalLayout_3.addWidget(self.allcheck_pushButton)
        self.alluncheck_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.alluncheck_pushButton.setObjectName("alluncheck_pushButton")
        self.horizontalLayout_3.addWidget(self.alluncheck_pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.logtextbrowser = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logtextbrowser.sizePolicy().hasHeightForWidth())
        self.logtextbrowser.setSizePolicy(sizePolicy)
        self.logtextbrowser.setObjectName("logtextbrowser")
        self.verticalLayout_4.addWidget(self.logtextbrowser)
        self.log_clear_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.log_clear_pushButton.setObjectName("log_clear_pushButton")
        self.verticalLayout_4.addWidget(self.log_clear_pushButton)
        self.horizontalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Golden Path"))
        self.refresh_pushButton.setText(_translate("MainWindow", "Refresh"))
        self.scenario_allcheck_pushButton.setText(_translate("MainWindow", "Test Scenario All Check"))
        self.scenario_alluncheck_pushButton.setText(_translate("MainWindow", "Test Scenario All Uncheck"))
        self.analyze_pushButton.setText(_translate("MainWindow", "Analyze"))
        self.save_pushButton.setText(_translate("MainWindow", "Save"))
        self.groupBox.setTitle(_translate("MainWindow", "Framwork"))
        self.alg_checkBox_1.setText(_translate("MainWindow", "all-MiniLM-L6-v2"))
        self.alg_checkBox_2.setText(_translate("MainWindow", "all-mpnet-base-v2"))
        self.alg_checkBox_3.setText(_translate("MainWindow", "paraphrase-MiniLM-L6-v2"))
        self.alg_checkBox_4.setText(_translate("MainWindow", "distiluse-base-multilingual-cased-v2"))
        self.alg_checkBox_5.setText(_translate("MainWindow", "paraphrase-mpnet-base-v2"))
        self.alg_checkBox_6.setText(_translate("MainWindow", "all-distilroberta-v1"))
        self.alg_checkBox_7.setText(_translate("MainWindow", "Ragas"))
        self.allcheck_pushButton.setText(_translate("MainWindow", "All Check"))
        self.alluncheck_pushButton.setText(_translate("MainWindow", "All Uncheck"))
        self.label_2.setText(_translate("MainWindow", "Log"))
        self.log_clear_pushButton.setText(_translate("MainWindow", "Log Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())