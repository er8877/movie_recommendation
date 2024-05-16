from PyQt5 import QtCore, QtGui, QtWidgets
from recommend_class import movie_recommendation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 650)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color:#0B132B\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 60, 361, 51))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:#6FFFE9;\n"
"color:#1C2541;\n"
"border:5px solid #5BC0BE;\n"
"border-radius:20px\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(170, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"background-color:#6FFFE9;\n"
"color:#1C2541;\n"
"border:5px solid #5BC0BE;\n"
"border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#5BC0BE\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./door-open-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.lineEdit_movie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_movie.setGeometry(QtCore.QRect(400, 190, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(14)
        self.lineEdit_movie.setFont(font)
        self.lineEdit_movie.setStyleSheet("QLineEdit{\n"
"background-color:#6FFFE9;\n"
"color:#1C2541;\n"
"border:3px solid #5BC0BE;\n"
"border-radius:12px\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:#5BC0BE\n"
"}")
        self.lineEdit_movie.setText("")
        self.lineEdit_movie.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_movie.setObjectName("lineEdit_movie")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 210, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:#6FFFE9;\n"
"color:#1C2541;\n"
"border:3px solid #5BC0BE;\n"
"border-radius:20px\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton_offers = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_offers.setGeometry(QtCore.QRect(360, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_offers.setFont(font)
        self.pushButton_offers.setStyleSheet("QPushButton{\n"
"background-color:#6FFFE9;\n"
"color:#1C2541;\n"
"border:5px solid #5BC0BE;\n"
"border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#5BC0BE\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./tick-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_offers.setIcon(icon1)
        self.pushButton_offers.setObjectName("pushButton_offers")
        self.listWidget_movies = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_movies.setGeometry(QtCore.QRect(220, 360, 400, 230))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_movies.setFont(font)
        self.listWidget_movies.setStyleSheet("QListWidget{\n"
"background-color:#6FFFE9;\n"
"color:#1C2541;\n"
"border:5px solid #5BC0BE;\n"
"border-radius:20px;\n"
"padding:15px\n"
"}")
        self.listWidget_movies.setObjectName("listWidget_movies")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 531, 591))
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:#3A506B;\n"
"border:3px solid #6FFFE9;\n"
"border-radius:30px\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.pushButton_exit.raise_()
        self.lineEdit_movie.raise_()
        self.label_2.raise_()
        self.pushButton_offers.raise_()
        self.listWidget_movies.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.movies_model = movie_recommendation()
        
        self.pushButton_offers.clicked.connect(self.get_recommends)
        
        self.pushButton_exit.clicked.connect(lambda:MainWindow.close())

    def get_recommends(self):
            self.listWidget_movies.clear()
            
            movie_name = self.lineEdit_movie.text()
            try:
                    
                recommends = self.movies_model.recommend(movie_name)
                self.listWidget_movies.addItems(recommends)
                
            except:
                print("please enter the correct name of the movie")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "movie recommendation"))
        self.label.setText(_translate("MainWindow", "Movie Recommendatoim"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Enter your movie : "))
        self.pushButton_offers.setText(_translate("MainWindow", "Offer me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
