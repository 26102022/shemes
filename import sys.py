import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanavas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PyQt6.QtCore import QSize, Qt, QRect


#from MplForWidget_bak import MyMplCanvas #отрисовка графика
from matplotlib.backends.backend_qt import NavigationToolbar2QT as NavigationToolbar

#from MyGraphics import plot_graph_smart

#from my_bot import TextBot
#from text_bot_gui_with_mpl_bak import Ui_MainWindow
qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    

        # добавление шаблона размещения на виджет
        self.companovka_for_mpl = QVBoxLayout(self.widget)
        # получение объекта класса холста с нашим рисунком
        self.canavas = MyMplCanavas(self.fig)
        # Размещение экземпляра класса холста в шаблоне размещения
        self.companovka_for_mpl.addWidget(self.canavas)
        # получение объекта класса панели управления холста
        self.toolbar = NavigationToolbar(self.canavas, self)
        # Размещение экземпляра класса панели управления в шаблоне размещения
        self.companovka_for_mpl.addWidget(self.toolbar)


class MyMplCanavas(FigureCanavas):
    def __init__(self, fig, parent = None):
        self.fig =fig
        FigureCanavas.__init__(self, self.fig)
        FigureCanavas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanavas.updateGeometry(self)
def main():
    '''
    функция для инициализации и отображения нашего основного окна приложения
    '''
    #Класс QApplication руководит управляющей логикой ГПИ и основными настройками.
    #Здеь мы создаем экземпляр класса QAplication передавая ему аргументы из коммандной строки.
    app = QApplication(sys.argv) # где sys.argv список аргументов командной строки, передаваемых сценарию Python.
    #Здсь мы создаем экземпляр класса MainWindow.
    main = MainWindow()
    main.show()
    #Метод show() отображает виджет на экране.Виджет сначала создаётся в памяти, и
    #только потом(с помощью метода show) показывается на экране.
    sys.exit(app.exec_())
    #exec_ запускает цикл обработки сообщений
    #и ждет, пока не будет вызвана exit() или не
    #будет разрушен главный виджет, и возвращает значение установленное в exit().
    #Здесь sys.exit обеспечивает чистый выход из приложения.

main()