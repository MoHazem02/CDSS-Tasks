from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("headache.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #1e1e2f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 401, 411))
        self.groupBox.setObjectName("groupBox")
        self.Symptom1 = QtWidgets.QCheckBox(self.groupBox)
        self.Symptom1.setGeometry(QtCore.QRect(40, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Symptom1.setFont(font)
        self.Symptom1.setObjectName("Symptom1")
        self.Symptom2 = QtWidgets.QCheckBox(self.groupBox)
        self.Symptom2.setGeometry(QtCore.QRect(40, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Symptom2.setFont(font)
        self.Symptom2.setObjectName("Symptom2")
        self.Symptom3 = QtWidgets.QCheckBox(self.groupBox)
        self.Symptom3.setGeometry(QtCore.QRect(40, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Symptom3.setFont(font)
        self.Symptom3.setObjectName("Symptom3")
        self.Symptom4 = QtWidgets.QCheckBox(self.groupBox)
        self.Symptom4.setGeometry(QtCore.QRect(40, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Symptom4.setFont(font)
        self.Symptom4.setObjectName("Symptom4")
        self.Symptom5 = QtWidgets.QCheckBox(self.groupBox)
        self.Symptom5.setGeometry(QtCore.QRect(40, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Symptom5.setFont(font)
        self.Symptom5.setObjectName("Symptom5")
        self.Diagnose_button = QtWidgets.QPushButton(self.groupBox)
        self.Diagnose_button.setGeometry(QtCore.QRect(270, 330, 86, 31))
        self.Diagnose_button.setMaximumSize(QtCore.QSize(86, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Diagnose_button.setFont(font)
        self.Diagnose_button.setStyleSheet("background-color: #00A86B;\n"
"      color: white;\n"
"      border: none;\n"
"      padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.Diagnose_button.setObjectName("Diagnose_button")
        self.Reset_button = QtWidgets.QPushButton(self.groupBox)
        self.Reset_button.setGeometry(QtCore.QRect(50, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Reset_button.setFont(font)
        self.Reset_button.setStyleSheet("background-color: #E0115F;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.Reset_button.setObjectName("Reset_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 100, 291, 411))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Diagnosis1 = QtWidgets.QLabel(self.groupBox_2)
        self.Diagnosis1.setGeometry(QtCore.QRect(30, 70, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diagnosis1.setFont(font)
        self.Diagnosis1.setObjectName("Diagnosis1")
        self.Diagnosis2 = QtWidgets.QLabel(self.groupBox_2)
        self.Diagnosis2.setGeometry(QtCore.QRect(30, 110, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diagnosis2.setFont(font)
        self.Diagnosis2.setObjectName("Diagnosis2")
        self.Diagnosis3 = QtWidgets.QLabel(self.groupBox_2)
        self.Diagnosis3.setGeometry(QtCore.QRect(30, 150, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Diagnosis3.setFont(font)
        self.Diagnosis3.setObjectName("Diagnosis3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.Diagnose_button.clicked.connect(self.diagnose)
        self.Reset_button.clicked.connect(self.reset)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bayesian CDSS"))
        self.groupBox.setTitle(_translate("MainWindow", "Symptoms"))
        self.Symptom1.setText(_translate("MainWindow", "Headache"))
        self.Symptom2.setText(_translate("MainWindow", "Sneezing"))
        self.Symptom3.setText(_translate("MainWindow", "Nausea"))
        self.Symptom4.setText(_translate("MainWindow", "Cough"))
        self.Symptom5.setText(_translate("MainWindow", "Stomach "))
        self.Diagnose_button.setText(_translate("MainWindow", "Diagnose"))
        self.Reset_button.setText(_translate("MainWindow", "Reset"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Diagnosis"))
        self.Diagnosis1.setText(_translate("MainWindow", "Migraine:"))
        self.Diagnosis2.setText(_translate("MainWindow", "Seasonal Allergies:"))
        self.Diagnosis3.setText(_translate("MainWindow", "Gastroenteritis:"))
        self.label.setText(_translate("MainWindow", "BAYESIAN CDSS"))

    def diagnose(self):
        # Prior probabilities
        priors = {
            "Migraine": 0.15,
            "Seasonal Allergies": 0.25,
            "Food Poisoning": 0.10,
            "Bronchitis": 0.20,
            "Gastroenteritis": 0.30
        }

        # Conditional probabilities
        conditionals = {
            "Headache": {"Migraine": 0.80, "Seasonal Allergies": 0.10, "Food Poisoning": 0.05, "Bronchitis": 0.30, "Gastroenteritis": 0.15},
            "Sneezing": {"Migraine": 0.05, "Seasonal Allergies": 0.90, "Food Poisoning": 0.02, "Bronchitis": 0.10, "Gastroenteritis": 0.05},
            "Nausea": {"Migraine": 0.40, "Seasonal Allergies": 0.05, "Food Poisoning": 0.85, "Bronchitis": 0.10, "Gastroenteritis": 0.80},
            "Cough": {"Migraine": 0.10, "Seasonal Allergies": 0.20, "Food Poisoning": 0.05, "Bronchitis": 0.90, "Gastroenteritis": 0.15},
            "Stomach pain": {"Migraine": 0.20, "Seasonal Allergies": 0.05, "Food Poisoning": 0.90, "Bronchitis": 0.15, "Gastroenteritis": 0.85}
        }

        # Selected symptoms
        symptoms = {
            "Headache": self.Symptom1.isChecked(),
            "Sneezing": self.Symptom2.isChecked(),
            "Nausea": self.Symptom3.isChecked(),
            "Cough": self.Symptom4.isChecked(),
            "Stomach pain": self.Symptom5.isChecked()
        }

        # Calculate posterior probabilities
        posteriors = priors.copy()
        for condition in posteriors:
            for symptom, present in symptoms.items():
                if present:
                    posteriors[condition] *= conditionals[symptom][condition]
                else:
                    posteriors[condition] *= (1 - conditionals[symptom][condition])

        # Normalize probabilities
        total = sum(posteriors.values())
        for condition in posteriors:
            posteriors[condition] /= total

        # Get top 3 conditions
        top_conditions = sorted(posteriors.items(), key=lambda x: x[1], reverse=True)[:3]

        # Update UI
        self.Diagnosis1.setText(f"{top_conditions[0][0]}: {top_conditions[0][1]*100:.2f}%")
        self.Diagnosis2.setText(f"{top_conditions[1][0]}: {top_conditions[1][1]*100:.2f}%")
        self.Diagnosis3.setText(f"{top_conditions[2][0]}: {top_conditions[2][1]*100:.2f}%")

    def reset(self):
        self.Symptom1.setChecked(False)
        self.Symptom2.setChecked(False)
        self.Symptom3.setChecked(False)
        self.Symptom4.setChecked(False)
        self.Symptom5.setChecked(False)
        self.Diagnosis1.setText("Migraine:")
        self.Diagnosis2.setText("Seasonal Allergies:")
        self.Diagnosis3.setText("Gastroenteritis:")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())