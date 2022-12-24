#pyinstaller --onefile --icon=ocr.ico --noconsole play_guess.py
from PyQt5 import QtWidgets
import sys
from guess import Ui_MainWindow
from guesswin2 import Ui_mainWindoweasy
from guess_midle import Ui_MainWindowmidle
from guesshard import Ui_MainWindowhard
from random import randint


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.radioButton.clicked.connect(lambda: self.show_mywindow())
        self.ui.btn_easy_2.clicked.connect(lambda: self.show_mywindow2())
        self.ui.btn_easy_3.clicked.connect(lambda: self.show_mywindow3())
    def show_mywindow(self):
        self.ui.pushButton.clicked.connect(self.show_mywindoweasy)
        self.ui.pushButton.clicked.connect(self.close)

    def show_mywindoweasy(self):
        self.ui2 = mywindow2()
        self.ui2.show()

    def show_mywindow2(self):
        self.ui.pushButton.clicked.connect(self.show_mywindoweasy2)
        self.ui.pushButton.clicked.connect(self.close)

    def show_mywindoweasy2(self):
        self.ui2 = mywindow3()
        self.ui2.show()
    def show_mywindow3(self):
        self.ui.pushButton.clicked.connect(self.show_mywindoweasy3)
        self.ui.pushButton.clicked.connect(self.close)

    def show_mywindoweasy3(self):
        self.ui2 = mywindow4()
        self.ui2.show()


class mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.ui2 = Ui_mainWindoweasy()
        self.ui2.setupUi(self)
        self.ui2.btn_nazad.clicked.connect(self.show_mywindoweasy2)
        self.ui2.btn_nazad.clicked.connect(self.close)
        self.ui2.btn_proverka.clicked.connect(self.proverka)
        self.ui2.pushButton_3.clicked.connect(self.newgame)
        self.i = 5
        global x
        x = randint(0, 20)

    def proverka(self):
        #print(x)
        proverka = int(self.ui2.lineEdit_3.text())
        if 0 <= proverka <= 20:
            if proverka > x:
                self.ui2.l_otvet.setText('Много. Попробуйте ещё!')
            elif proverka < x:
                self.ui2.l_otvet.setText('Мало. Попробуйте ещё!')
            else:
                self.ui2.l_otvet.setText('Вы победили!')

        else:
            self.ui2.l_otvet.setText('Ошибка!')
        self.i -= 1
        self.ui2.label_3.setText(str(self.i))
        if int(self.i) < 0:
            self.i = 0
            self.ui2.label_3.setText(str(self.i))
            self.ui2.l_otvet.setText('Вы проиграли! \n Загаданное число: ' + str(x))

    def newgame(self):
        global x
        x = randint(0, 20)
        self.i = 5
        self.ui2.label_3.setText(str(self.i))



    def show_mywindoweasy2(self):
        self.ui = mywindow()
        self.ui.show()


class mywindow3(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow3, self).__init__()
        self.ui2 = Ui_MainWindowmidle()
        self.ui2.setupUi(self)
        self.ui2.btn_nazad.clicked.connect(self.show_mywindoweasy3)
        self.ui2.btn_nazad.clicked.connect(self.close)
        self.ui2.btn_proverka.clicked.connect(self.proverka)
        self.ui2.pushButton_3.clicked.connect(self.newgame)
        self.a = 10
        global y
        y = randint(0, 100)

    def proverka(self):
        #print(y)
        proverka = int(self.ui2.lineEdit_3.text())
        if 0 <= proverka <= 100:
            if proverka > y:
                self.ui2.l_otvet.setText('Много. Попробуйте ещё!')
            elif proverka < y:
                self.ui2.l_otvet.setText('Мало. Попробуйте ещё!')
            else:
                self.ui2.l_otvet.setText('Вы победили!')

        else:
            self.ui2.l_otvet.setText('Ошибка!')
        self.a -= 1
        self.ui2.i_chislo.setText(str(self.a))
        if int(self.a) < 0:
            self.a = 0
            self.ui2.i_chislo.setText(str(self.a))
            self.ui2.l_otvet.setText('Вы проиграли! \n Загаданное число: ' + str(y))

    def newgame(self):
        global y
        y = randint(0, 100)
        self.a = 10
        self.ui2.i_chislo.setText(str(self.a))

    def show_mywindoweasy3(self):
        self.ui = mywindow()
        self.ui.show()


class mywindow4(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow4, self).__init__()
        self.ui2 = Ui_MainWindowhard()
        self.ui2.setupUi(self)
        self.ui2.btn_nazad.clicked.connect(self.show_mywindoweasy4)
        self.ui2.btn_nazad.clicked.connect(self.close)
        self.ui2.btn_proverka.clicked.connect(self.proverka)
        self.ui2.pushButton_3.clicked.connect(self.newgame)
        self.a = 10
        global y
        y = randint(0, 100)

    def proverka(self):
        #print(y)


        proverka = int(self.ui2.lineEdit_3.text())
        if 0 <= proverka <= 100:
            if proverka > y:
                self.ui2.l_otvet.setText('Много. Попробуйте ещё!')
            elif proverka < y:
                self.ui2.l_otvet.setText('Мало. Попробуйте ещё!')
            else:
                self.ui2.l_otvet.setText('Вы победили!')

        else:
            self.ui2.l_otvet.setText('Ошибка!')
        self.a -= 1
        self.ui2.i_chislo.setText(str(self.a))
        if int(self.a) < 0:
            self.a = 0
            self.ui2.i_chislo.setText(str(self.a))
            self.ui2.l_otvet.setText('Вы проиграли! \n Загаданное число: ' + str(y))

    def newgame(self):
        global y
        y = randint(0, 100)
        self.a = 10
        self.ui2.i_chislo.setText(str(self.a))

    def show_mywindoweasy4(self):
        self.ui = mywindow()
        self.ui.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.show()
    w.show_mywindow()
    w.show_mywindow2()
    sys.exit(app.exec_())
