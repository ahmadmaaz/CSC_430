# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from peer import start,send_button
from message_emitter import MessageEmitter
from sendWidget import Widget as sendWidget
from receiveWidget import Widget as receiveWidget
import threading
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 582)
        MainWindow.setMinimumSize(QtCore.QSize(458, 582))
        MainWindow.setMaximumSize(QtCore.QSize(458, 582))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet("QGroupBox{background-color:#fcfdff;border:0px}\n"
"QLineEdit{border:1px solid #d8d9dc; border-radius:5px;}\n"
"QPushButton{border-radius:5px; background-color:#ffffff;color: #004dfc; padding:7px;}\n"
"QListWidget{border:0px;background-color:#808080;}\n"
"QPushButton:hover{\n"
"     background-color:#f3f6fb;\n"
"}\n"
"QPushButton:pressed{\n"
"     background-color:#004dfc;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messageList = QtWidgets.QListWidget(self.groupBox)
        self.messageList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.messageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.messageList.setObjectName("messageList")
        self.verticalLayout_3.addWidget(self.messageList)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/sources/attach.ico"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input = QtWidgets.QLineEdit(self.groupBox_2)
        self.input.setStyleSheet("QLineEdit{ padding:2px; }")
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.send_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.send_btn.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.send_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sources/arrow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_btn.setIcon(icon)
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout.addWidget(self.send_btn)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #
        self.send_btn.clicked.connect(self.sendData)

        self.emitter = MessageEmitter()  
        self.emitter.msg.connect(self.update_text_edit)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HZA-Messenger"))
        self.input.setPlaceholderText(_translate("MainWindow", "Enter your message here "))
        self.send_btn.setText(_translate("MainWindow", "Send"))
    def sendData(self):
        receive_thread = threading.Thread(target=send_button,args=(self.input.text(),self.emitter,))
        receive_thread.start()
    def update_text_edit(self,message):
        widget= sendWidget()
        if(message[0]=="1"):
            widget=receiveWidget()
        widget.label_2.setText(message[1:])
        item=QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.messageList.addItem(item)
        self.messageList.setItemWidget(item,widget)
        self.messageList.setMinimumWidth(widget.width())
        self.messageList.setCurrentRow(self.messageList.count()-1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    start(ui.emitter)
    MainWindow.show()
    sys.exit(app.exec_())
