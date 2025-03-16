import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from App_Manager import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stethoscope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #1e1e2f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(30, 20, 731, 531))
        self.Tabs.setStyleSheet("QTabBar::tab:selected {\n"
"    background-color: rgb(255, 124, 17);\n"
" border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color:  #1e1e2f;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"   background-color: #1e1e2f;\n"
"    border: none;\n"
"padding-right: 2px;\n"
"padding-left:2px;\n"
" margin-right: 10px;\n"
"margin-left: 10px;\n"
"color:white\n"
"}")
        self.Tabs.setObjectName("Tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.groupBox = QtWidgets.QGroupBox(self.tab1)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 411, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tab1_fever = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_fever.setGeometry(QtCore.QRect(20, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_fever.setFont(font)
        self.tab1_fever.setObjectName("tab1_fever")
        self.tab1_cough = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_cough.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_cough.setFont(font)
        self.tab1_cough.setObjectName("tab1_cough")
        self.tab1_sob = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_sob.setGeometry(QtCore.QRect(20, 130, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_sob.setFont(font)
        self.tab1_sob.setObjectName("tab1_sob")
        self.tab1_urination = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_urination.setGeometry(QtCore.QRect(20, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_urination.setFont(font)
        self.tab1_urination.setObjectName("tab1_urination")
        self.tab1_thirst = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_thirst.setGeometry(QtCore.QRect(20, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_thirst.setFont(font)
        self.tab1_thirst.setObjectName("tab1_thirst")
        self.tab1_weight_loss = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_weight_loss.setGeometry(QtCore.QRect(20, 210, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_weight_loss.setFont(font)
        self.tab1_weight_loss.setObjectName("tab1_weight_loss")
        self.tab1_swelling = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_swelling.setGeometry(QtCore.QRect(20, 350, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_swelling.setFont(font)
        self.tab1_swelling.setObjectName("tab1_swelling")
        self.tab1_joint_pain = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_joint_pain.setGeometry(QtCore.QRect(20, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_joint_pain.setFont(font)
        self.tab1_joint_pain.setObjectName("tab1_joint_pain")
        self.tab1_stiffness = QtWidgets.QCheckBox(self.groupBox)
        self.tab1_stiffness.setGeometry(QtCore.QRect(20, 320, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_stiffness.setFont(font)
        self.tab1_stiffness.setObjectName("tab1_stiffness")
        self.tab1_diagnose = QtWidgets.QPushButton(self.groupBox, clicked = lambda: if_then_diagnose(self))
        self.tab1_diagnose.setGeometry(QtCore.QRect(210, 380, 151, 41))
        self.tab1_diagnose.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 124, 17);;\n"
"    border-radius: 12px;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    text-align: center;\n"
"    width: 100%;\n"
"    border: 0;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e6c800; \n"
"}\n"
"\n"
"")
        self.tab1_diagnose.setIconSize(QtCore.QSize(20, 20))
        self.tab1_diagnose.setObjectName("tab1_diagnose")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 180, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tab1_diag = QtWidgets.QLabel(self.groupBox_2)
        self.tab1_diag.setGeometry(QtCore.QRect(40, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab1_diag.setFont(font)
        self.tab1_diag.setStyleSheet("color: red;")
        self.tab1_diag.setObjectName("tab1_diag")
        self.tab1_reset = QtWidgets.QPushButton(self.tab1, clicked = lambda: tab1_reset(self))
        self.tab1_reset.setGeometry(QtCore.QRect(630, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab1_reset.setFont(font)
        self.tab1_reset.setStyleSheet("QPushButton {\n"
"    background-color: #E0115F; \n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #B00D4C;\n"
"    border: 1.2px inset gray;\n"
"}\n"
"")
        self.tab1_reset.setObjectName("tab1_reset")
        self.label_4 = QtWidgets.QLabel(self.tab1)
        self.label_4.setGeometry(QtCore.QRect(590, 20, 131, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("heart.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 20, 411, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tab2_fever = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_fever.setGeometry(QtCore.QRect(20, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_fever.setFont(font)
        self.tab2_fever.setObjectName("tab2_fever")
        self.tab2_cough = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_cough.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_cough.setFont(font)
        self.tab2_cough.setObjectName("tab2_cough")
        self.tab2_sob = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_sob.setGeometry(QtCore.QRect(20, 130, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_sob.setFont(font)
        self.tab2_sob.setObjectName("tab2_sob")
        self.tab2_urination = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_urination.setGeometry(QtCore.QRect(20, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_urination.setFont(font)
        self.tab2_urination.setObjectName("tab2_urination")
        self.tab2_thirst = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_thirst.setGeometry(QtCore.QRect(20, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_thirst.setFont(font)
        self.tab2_thirst.setObjectName("tab2_thirst")
        self.tab2_weight_loss = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_weight_loss.setGeometry(QtCore.QRect(20, 210, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_weight_loss.setFont(font)
        self.tab2_weight_loss.setObjectName("tab2_weight_loss")
        self.tab2_swelling = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_swelling.setGeometry(QtCore.QRect(20, 350, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_swelling.setFont(font)
        self.tab2_swelling.setObjectName("tab2_swelling")
        self.tab2_joint_pain = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_joint_pain.setGeometry(QtCore.QRect(20, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_joint_pain.setFont(font)
        self.tab2_joint_pain.setObjectName("tab2_joint_pain")
        self.tab2_stiffness = QtWidgets.QCheckBox(self.groupBox_3)
        self.tab2_stiffness.setGeometry(QtCore.QRect(20, 320, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_stiffness.setFont(font)
        self.tab2_stiffness.setObjectName("tab2_stiffness")
        self.tab2_diagnose = QtWidgets.QPushButton(self.groupBox_3, clicked = lambda: semantic_diagnose(self))
        self.tab2_diagnose.setGeometry(QtCore.QRect(210, 380, 151, 41))
        self.tab2_diagnose.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 124, 17);;\n"
"    border-radius: 12px;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    text-align: center;\n"
"    width: 100%;\n"
"    border: 0;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e6c800; \n"
"}\n"
"\n"
"")
        self.tab2_diagnose.setIconSize(QtCore.QSize(20, 20))
        self.tab2_diagnose.setObjectName("tab2_diagnose")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab2)
        self.groupBox_4.setGeometry(QtCore.QRect(450, 180, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tab2_diag = QtWidgets.QLabel(self.groupBox_4)
        self.tab2_diag.setGeometry(QtCore.QRect(40, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab2_diag.setFont(font)
        self.tab2_diag.setStyleSheet("color: red;")
        self.tab2_diag.setObjectName("tab2_diag")
        self.tab2_reset = QtWidgets.QPushButton(self.tab2, clicked = lambda: tab2_reset(self))
        self.tab2_reset.setGeometry(QtCore.QRect(630, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab2_reset.setFont(font)
        self.tab2_reset.setStyleSheet("QPushButton {\n"
"    background-color: #E0115F; \n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #B00D4C;\n"
"    border: 1.2px inset gray;\n"
"}\n"
"")
        self.tab2_reset.setObjectName("tab2_reset")
        self.label_5 = QtWidgets.QLabel(self.tab2)
        self.label_5.setGeometry(QtCore.QRect(590, 20, 131, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("heart.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.Tabs.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab3)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 20, 321, 251))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tab3_first_name = QtWidgets.QLineEdit(self.groupBox_5)
        self.tab3_first_name.setGeometry(QtCore.QRect(150, 40, 141, 31))
        self.tab3_first_name.setObjectName("tab3_first_name")
        self.tab3_last_name = QtWidgets.QLineEdit(self.groupBox_5)
        self.tab3_last_name.setGeometry(QtCore.QRect(150, 80, 141, 31))
        self.tab3_last_name.setObjectName("tab3_last_name")
        self.tab3_age = QtWidgets.QLineEdit(self.groupBox_5)
        self.tab3_age.setGeometry(QtCore.QRect(150, 130, 141, 31))
        self.tab3_age.setObjectName("tab3_age")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab3)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 20, 371, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.tab3_fever = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_fever.setGeometry(QtCore.QRect(20, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_fever.setFont(font)
        self.tab3_fever.setObjectName("tab3_fever")
        self.tab3_cough = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_cough.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_cough.setFont(font)
        self.tab3_cough.setObjectName("tab3_cough")
        self.tab3_sob = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_sob.setGeometry(QtCore.QRect(20, 130, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_sob.setFont(font)
        self.tab3_sob.setObjectName("tab3_sob")
        self.tab3_urination = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_urination.setGeometry(QtCore.QRect(20, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_urination.setFont(font)
        self.tab3_urination.setObjectName("tab3_urination")
        self.tab3_thirst = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_thirst.setGeometry(QtCore.QRect(20, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_thirst.setFont(font)
        self.tab3_thirst.setObjectName("tab3_thirst")
        self.tab3_weight_loss = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_weight_loss.setGeometry(QtCore.QRect(20, 210, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_weight_loss.setFont(font)
        self.tab3_weight_loss.setObjectName("tab3_weight_loss")
        self.tab3_swelling = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_swelling.setGeometry(QtCore.QRect(20, 350, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_swelling.setFont(font)
        self.tab3_swelling.setObjectName("tab3_swelling")
        self.tab3_joint_pain = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_joint_pain.setGeometry(QtCore.QRect(20, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_joint_pain.setFont(font)
        self.tab3_joint_pain.setObjectName("tab3_joint_pain")
        self.tab3_stiffness = QtWidgets.QCheckBox(self.groupBox_6)
        self.tab3_stiffness.setGeometry(QtCore.QRect(20, 320, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_stiffness.setFont(font)
        self.tab3_stiffness.setObjectName("tab3_stiffness")
        self.tab3_diagnose = QtWidgets.QPushButton(self.groupBox_6)
        self.tab3_diagnose.setGeometry(QtCore.QRect(210, 380, 151, 41))
        self.tab3_diagnose.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 124, 17);;\n"
"    border-radius: 12px;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    padding: 10px 15px;\n"
"    text-align: center;\n"
"    width: 100%;\n"
"    border: 0;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e6c800; \n"
"}\n"
"\n"
"")
        self.tab3_diagnose.setIconSize(QtCore.QSize(20, 20))
        self.tab3_diagnose.setObjectName("tab3_diagnose")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab3)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 290, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.tab3_diag = QtWidgets.QLabel(self.groupBox_7)
        self.tab3_diag.setGeometry(QtCore.QRect(40, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab3_diag.setFont(font)
        self.tab3_diag.setStyleSheet("color: red;")
        self.tab3_diag.setObjectName("tab3_diag")
        self.tab3_reset = QtWidgets.QPushButton(self.tab3, clicked = lambda: tab3_reset(self))
        self.tab3_reset.setGeometry(QtCore.QRect(190, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab3_reset.setFont(font)
        self.tab3_reset.setStyleSheet("QPushButton {\n"
"    background-color: #00A86B; \n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #00804D;\n"
"    border: 1.2px inset gray;\n"
"}\n"
"")
        self.tab3_reset.setObjectName("tab3_reset")
        self.Tabs.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CDSS"))
        self.groupBox.setTitle(_translate("MainWindow", "Symptoms"))
        self.tab1_fever.setText(_translate("MainWindow", "Fever"))
        self.tab1_cough.setText(_translate("MainWindow", "Cough"))
        self.tab1_sob.setText(_translate("MainWindow", "Shortness of Breath"))
        self.tab1_urination.setText(_translate("MainWindow", "Frequent Urination"))
        self.tab1_thirst.setText(_translate("MainWindow", "Excessive Thirst"))
        self.tab1_weight_loss.setText(_translate("MainWindow", "Unexplained Weight Loss"))
        self.tab1_swelling.setText(_translate("MainWindow", "Swelling "))
        self.tab1_joint_pain.setText(_translate("MainWindow", "Joint Pain"))
        self.tab1_stiffness.setText(_translate("MainWindow", "Morning Stiffness"))
        self.tab1_diagnose.setText(_translate("MainWindow", "Diagnose"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Diganosis"))
        self.tab1_diag.setText(_translate("MainWindow", "No Disease"))
        self.tab1_reset.setText(_translate("MainWindow", "Reset"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab1), _translate("MainWindow", "If-Then"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Symptoms"))
        self.tab2_fever.setText(_translate("MainWindow", "Fever"))
        self.tab2_cough.setText(_translate("MainWindow", "Cough"))
        self.tab2_sob.setText(_translate("MainWindow", "Shortness of Breath"))
        self.tab2_urination.setText(_translate("MainWindow", "Frequent Urination"))
        self.tab2_thirst.setText(_translate("MainWindow", "Excessive Thirst"))
        self.tab2_weight_loss.setText(_translate("MainWindow", "Unexplained Weight Loss"))
        self.tab2_swelling.setText(_translate("MainWindow", "Swelling "))
        self.tab2_joint_pain.setText(_translate("MainWindow", "Joint Pain"))
        self.tab2_stiffness.setText(_translate("MainWindow", "Morning Stiffness"))
        self.tab2_diagnose.setText(_translate("MainWindow", "Diagnose"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Diganosis"))
        self.tab2_diag.setText(_translate("MainWindow", "No Disease"))
        self.tab2_reset.setText(_translate("MainWindow", "Reset"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab2), _translate("MainWindow", "Semantic Network"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Patient Frame"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Symptoms"))
        self.tab3_fever.setText(_translate("MainWindow", "Fever"))
        self.tab3_cough.setText(_translate("MainWindow", "Cough"))
        self.tab3_sob.setText(_translate("MainWindow", "Shortness of Breath"))
        self.tab3_urination.setText(_translate("MainWindow", "Frequent Urination"))
        self.tab3_thirst.setText(_translate("MainWindow", "Excessive Thirst"))
        self.tab3_weight_loss.setText(_translate("MainWindow", "Unexplained Weight Loss"))
        self.tab3_swelling.setText(_translate("MainWindow", "Swelling "))
        self.tab3_joint_pain.setText(_translate("MainWindow", "Joint Pain"))
        self.tab3_stiffness.setText(_translate("MainWindow", "Morning Stiffness"))
        self.tab3_diagnose.setText(_translate("MainWindow", "Diagnose"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Diganosis"))
        self.tab3_diag.setText(_translate("MainWindow", "No Disease"))
        self.tab3_reset.setText(_translate("MainWindow", "New Patient"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab3), _translate("MainWindow", "Frames"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
