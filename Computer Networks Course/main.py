import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from serverclient import client

class MYUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)   #主界面大小
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 50, 371, 51)) #离左，离上，text长度，text宽度
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(0)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 171, 41))  #请输入url字符串的位置

        self.label.setFont(font)
        self.label.setObjectName("label")



        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 170, 400, 500))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(font)
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 300, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(500, 170, 500, 500))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setAcceptRichText(True)
        self.textBrowser_2.setFont(font)


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 130, 300, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 50, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.url)
        self.pushButton.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 121, 41))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Client"))
        self.label.setText(_translate("MainWindow", "请输入url"))
        self.label_2.setText(_translate("MainWindow", "响应的Headers"))
        self.label_3.setText(_translate("MainWindow", "文档内容"))
        self.pushButton.setText(_translate("MainWindow", "GET"))
        self.label_4.setText(_translate("MainWindow", "http(s)://"))


    def url(self):
        h,b=client(self.textEdit.toPlainText())
        url=self.textEdit.toPlainText()
        print(repr(url))
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser.setText(h) #headers
        self.textBrowser_2.setText('#'+b)   #body



if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv) # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    my=MYUI()
    window=QtWidgets.QMainWindow()  #设为主窗口
    my.setupUi(window)
    window.show()   #显示在屏幕上
    app.exec_() #退出程序