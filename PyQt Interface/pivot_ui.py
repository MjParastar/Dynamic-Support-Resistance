from PyQt5 import QtCore, QtGui, QtWidgets
import pivot_bg_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 481, 441))
        Form.setFixedSize(481, 441) 

        self.groupBox.setStyleSheet("border : 1px solid black ;\n"
"background-color : #1e272e ;\n"
"\n"
"margin : 0px ;\n"
"padding : 0px ;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 461, 171))
        self.label.setStyleSheet("background-image: url(:/pivot_background/pivot_background.jpeg);\n"
"border-radius : 50% ;\n"
"background-position : center ;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 81, 51))
        self.label_2.setStyleSheet("border : 1px solid white ;\n"
"border-radius : 50% ;\n"
"background-color : white ;\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"font-weight : bold ;\n"
"border-radius : 50% ;")
        self.label_2.setObjectName("label_2")
        self.close_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.close_lineedit.setGeometry(QtCore.QRect(130, 210, 113, 22))
        self.close_lineedit.setStyleSheet("background-color : white ;")
        self.close_lineedit.setObjectName("close_lineedit")
        self.high_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.high_lineedit.setGeometry(QtCore.QRect(130, 270, 113, 22))
        self.high_lineedit.setStyleSheet("background-color : white ;")
        self.high_lineedit.setObjectName("high_lineedit")
        self.low_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.low_lineedit.setGeometry(QtCore.QRect(130, 330, 113, 22))
        self.low_lineedit.setStyleSheet("background-color : white ;")
        self.low_lineedit.setObjectName("low_lineedit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 81, 51))
        self.label_3.setStyleSheet("border : 1px solid white ;\n"
"border-radius : 50% ;\n"
"background-color : white ;\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"font-weight : bold ;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 320, 81, 51))
        self.label_4.setStyleSheet("border : 1px solid white ;\n"
"border-radius : 50% ;\n"
"background-color : white ;\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"font-weight : bold ;")
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 190, 191, 241))
        self.groupBox_2.setStyleSheet("background-color : #FDA7DF ;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.Pivot_Label = QtWidgets.QLabel(self.groupBox_2)
        self.Pivot_Label.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.Pivot_Label.setStyleSheet("font: 63 8pt \"Montserrat SemiBold\";\n"
"box-sizing : border-box ;\n"
"font-size : 15px ;\n"
"border : none ;\n"
"background-color : #6F1E51 ;\n"
"border-radius : 15px ;")
        self.Pivot_Label.setObjectName("Pivot_Label")
        self.s1_value = QtWidgets.QLabel(self.groupBox_2)
        self.s1_value.setGeometry(QtCore.QRect(20, 120, 71, 16))
        self.s1_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.s1_value.setText("")
        self.s1_value.setObjectName("s1_value")
        self.s2_value = QtWidgets.QLabel(self.groupBox_2)
        self.s2_value.setGeometry(QtCore.QRect(100, 120, 71, 16))
        self.s2_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.s2_value.setText("")
        self.s2_value.setObjectName("s2_value")
        self.s3_value = QtWidgets.QLabel(self.groupBox_2)
        self.s3_value.setGeometry(QtCore.QRect(60, 140, 71, 16))
        self.s3_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.s3_value.setText("")
        self.s3_value.setObjectName("s3_value")
        self.Support_Label = QtWidgets.QLabel(self.groupBox_2)
        self.Support_Label.setGeometry(QtCore.QRect(10, 80, 171, 31))
        self.Support_Label.setStyleSheet("font: 63 8pt \"Montserrat SemiBold\";\n"
"box-sizing : border-box ;\n"
"font-size : 15px ;\n"
"border : none ;\n"
"background-color : #6F1E51 ;\n"
"border-radius : 15px ;")
        self.Support_Label.setObjectName("Support_Label")
        self.pivot_value = QtWidgets.QLabel(self.groupBox_2)
        self.pivot_value.setGeometry(QtCore.QRect(60, 50, 71, 16))
        self.pivot_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.pivot_value.setText("")
        self.pivot_value.setObjectName("pivot_value")
        self.Resistance_Label = QtWidgets.QLabel(self.groupBox_2)
        self.Resistance_Label.setGeometry(QtCore.QRect(10, 160, 171, 31))
        self.Resistance_Label.setStyleSheet("font: 63 8pt \"Montserrat SemiBold\";\n"
"box-sizing : border-box ;\n"
"font-size : 15px ;\n"
"border : none ;\n"
"background-color : #6F1E51 ;\n"
"border-radius : 15px ;")
        self.Resistance_Label.setObjectName("Resistance_Label")
        self.r1_value = QtWidgets.QLabel(self.groupBox_2)
        self.r1_value.setGeometry(QtCore.QRect(20, 200, 71, 16))
        self.r1_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.r1_value.setText("")
        self.r1_value.setObjectName("r1_value")
        self.r2_value = QtWidgets.QLabel(self.groupBox_2)
        self.r2_value.setGeometry(QtCore.QRect(100, 200, 71, 16))
        self.r2_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.r2_value.setText("")
        self.r2_value.setObjectName("r2_value")
        self.r3_value = QtWidgets.QLabel(self.groupBox_2)
        self.r3_value.setGeometry(QtCore.QRect(60, 220, 71, 16))
        self.r3_value.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.r3_value.setText("")
        self.r3_value.setObjectName("r3_value")
        self.pushButton_submit = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_submit.setGeometry(QtCore.QRect(90, 390, 93, 28))
        self.pushButton_submit.setStyleSheet("background-color : #009432 ;\n"
"font-weight : bold ;\n"
"border : 1px solid black ;\n"
"border-radius : 50% ;\n"
"")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_submit.clicked.connect(self.calculate_pivot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def calculate_pivot(self):
        try:
                Close = float(self.close_lineedit.text())
                High = float(self.high_lineedit.text())
                Low = float(self.low_lineedit.text())

                Pivot = (Close + High + Low) / 3
                Resistance1 = 2 * Pivot - Low
                Resistance2 = Pivot + (High - Low)
                Resistance3 = Resistance1 + (High - Low)
                Support1 = 2 * Pivot - High
                Support2 = Pivot - (High - Low)
                Support3 = Support1 - (High - Low)

                self.pivot_value.setText(f"{Pivot:.4f}")
                self.r1_value.setText(f"{Resistance1:.4f}")
                self.r2_value.setText(f"{Resistance2:.4f}")
                self.r3_value.setText(f"{Resistance3:.4f}")
                self.s1_value.setText(f"{Support1:.4f}")
                self.s2_value.setText(f"{Support2:.4f}")
                self.s3_value.setText(f"{Support3:.4f}")

        except ValueError:
                self.pivot_value.setText("خطا!")
                self.r1_value.setText("")
                self.r2_value.setText("")
                self.r3_value.setText("")
                self.s1_value.setText("")
                self.s2_value.setText("")
                self.s3_value.setText("")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "   Close "))
        self.label_3.setText(_translate("Form", "   High"))
        self.label_4.setText(_translate("Form", "   Low"))
        self.Pivot_Label.setText(_translate("Form", "  Pivot)"))
        self.Support_Label.setText(_translate("Form", "  Support)"))
        self.Resistance_Label.setText(_translate("Form", " Resistance)"))
        self.pushButton_submit.setText(_translate("Form", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())