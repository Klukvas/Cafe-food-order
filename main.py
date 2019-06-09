import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qwe import Ui_MainWindow
from garph import Ui_MainWindows
from PyQt5.QtWidgets import QMessageBox
import bd_logging as wbd
from sqlite3 import IntegrityError as IntegErr


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow, QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.login.clicked.connect(self.login2)
        self.ui.login_2.clicked.connect(self.create_new)
        self.graph = Graph()
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon("ww.png"))

    def login2(self):
        self.login = self.ui.username.text()
        self.password = self.ui.password.text()

        try:
            sql = wbd.work_db(str(self.login), str(self.password))

            if len(sql) > 0:
                self.graph.show()
                #MyWin().exec_()
               #self.ui.hide()
                self.close()
                print("sad")

        except ValueError:
            self.ui.label_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.label_3.setText("Логин или пароль неверны")

    def create_new(self):
        if len(self.ui.username.text()) >= 5 and len(self.ui.password.text()) >= 5:
            self.login = self.ui.username.text()
            self.password = self.ui.password.text()
            try:
                wbd.create_new_db(str(self.login), str(self.password))
                msgd = QMessageBox(QMessageBox.Information, "Accept", "Успешно!")
                msgd.exec_()
                self.graph.show()
                self.close()
            except IntegErr:
                self.ui.label_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                self.ui.label_3.setText("Username занят")
        elif len(self.ui.username.text()) < 5:
            self.ui.label_3.setText("Username слишком короткий")
        elif len(self.ui.password.text()) < 5:
            self.ui.label_3.setText("Пароль слишком короткий")

class Graph(QtWidgets.QMainWindow, Ui_MainWindows, QtWidgets.QMessageBox):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindows()
        self.ui.setupUi(self)
        self.setWindowTitle("Oregano")
        self.dialog = Dialog()
        self.dialog.resize(200, 80)
        self.sum = 0
        self.setWindowIcon(QtGui.QIcon("ww.png"))
        self.ui.listWidget.hide()
        self.ui.label_3.hide()
        self.ui.for_pic.setStyleSheet('''
                    #for_pic{
                        border-radius: 4px;
                        background-image: url('./OREGANO.png');
                        })
                        '''
                                    )
        self.ui.pizza.setStyleSheet('''
                    #pizza{
                        border-radius: 4px;
                        background-image: url('./for_but/pizza.jpg');
                        })
                        '''
                                    )
        self.ui.sides.setStyleSheet('''
                            #sides{
                                border-radius: 4px;
                                background-image: url('./for_but/drinks.jpg');
                                })
                                '''
                                    )
        self.ui.desserts.setStyleSheet('''
                                    #desserts{
                                        border-radius: 4px;
                                        background-image: url('./for_but/desserts.jpg');
                                        })
                                        '''
                                     )
        self.ui.drinks.setStyleSheet('''
                                            #drinks{
                                                border-radius: 4px;
                                                background-image: url('./for_but/sides.png');
                                                })
                                                '''
                                       )
        self.ui.del_dish.clicked.connect(self.remove)
        self.ui.make_order.clicked.connect(self.messege)
        self.ui.del_all.clicked.connect(self.delete)
        self.ui.pizza.clicked.connect(self.take_pizza)
        self.ui.drinks.clicked.connect(self.take_drinks)
        self.ui.desserts.clicked.connect(self.take_desserts)
        self.ui.sides.clicked.connect(self.take_siedes)
        self.ui.menuWidg.itemClicked.connect(self.for_pic)
        self.ui.menuWidg.itemDoubleClicked.connect(self.add_to_order)
        self.ui.actionWhite.setIcon(QIcon("white.png"))
        self.ui.actionGreen.setIcon(QIcon("G.jpg"))
        self.setAutoFillBackground(True)
        self.ui.actionGreen.triggered.connect(self.green)
        self.ui.actionWhite.triggered.connect(self.white)
    def green(self):
        self.setStyleSheet('''
                             QMainWindow{      
                                background: 'green';    
                                })
                             ''')
    def white(self):
        self.setStyleSheet('''
                             QMainWindow{      
                                background-color: 'white';
                                })
                             ''')
    def add_to_order(self):
        self.ui.menuWidg_2.clear()
        self.price_for_order = int(self.ui.price_dish.text())
        self.sum += self.price_for_order
        self.ui.menuWidg_2.addItem(str(self.sum))
        self.dish = self.ui.menuWidg.currentItem().text()
        self.ui.order.addItem(self.dish)

    def for_pic(self):
        #Для показа ингредиентов пиццы
        self.selected = self.ui.menuWidg.currentItem().text()
        ing = str(wbd.for_ingedients(self.selected))
        if ing != "('0',)":
            self.ui.listWidget.show()
            self.ui.label_3.show()
            self.ui.listWidget.clear()
            selected = self.ui.menuWidg.currentItem().text()
            ing = str(wbd.for_ingedients(selected))
            ing = ing[2:-3]
            ing = ing.split(r"\n")
            for item in ing:
                self.ui.listWidget.addItem(item)
        else:
            self.ui.listWidget.clear()
            self.ui.listWidget.hide()
            self.ui.label_3.hide()
        #Для пикчи с продуктом
        self.pic = str(wbd.for_picture(self.selected))
        self.dis = str(wbd.for_picture_dis(self.selected))
        self.dis_for_pic = self.dis[2:-3]
        self.item_for_pic = self.pic[2:-3]
        self.picute = "\'pic/" + self.dis_for_pic + '/' + self.item_for_pic
        self.ui.for_pic.setStyleSheet("#for_pic{{background-image: url({});}}".format(self.picute))
        #Для показа цены
        self.price = wbd.for_price(self.selected)
        self.price = self.price[0]
        self.ui.price_dish.setText(str(self.price))

    def take_pizza(self):
        self.ui.menuWidg.clear()
        pizza_name_for_menu = wbd.pizza_name()
        for item in pizza_name_for_menu:
            name = str(item)
            name = name[2:-3]
            self.ui.menuWidg.addItem(name)

    def take_drinks(self):
        self.ui.menuWidg.clear()
        drink_name_for_menu = wbd.drinks_name()
        for item in drink_name_for_menu:
            name = str(item)
            name = name[2:-3]
            self.ui.menuWidg.addItem(name)

    def take_desserts(self):
        self.ui.menuWidg.clear()
        dess_name_for_menu = wbd.desserts_name()
        for item in dess_name_for_menu:
            name = str(item)
            name = name[2:-3]
            self.ui.menuWidg.addItem(name)

    def take_siedes(self):
        self.ui.menuWidg.clear()
        sdie_name_for_menu = wbd.sides_name()
        for item in sdie_name_for_menu:
            name = str(item)
            name = name[2:-3]
            self.ui.menuWidg.addItem(name)

    def remove(self):
        #Удалиние цены из общей суммы
        self.selec_item = self.ui.order.currentItem().text()
        self.price_for_remuve = wbd.remove_from_sum(str(self.selec_item))
        self.price_for_remuve = int(self.price_for_remuve[0])
        self.sum -=self.price_for_remuve
        self.ui.menuWidg_2.clear()
        self.ui.menuWidg_2.addItem(str(self.sum))
        #Удаление из общего заказа
        self.item = self.ui.order.currentRow()
        self.ui.order.takeItem(self.item)

    def messege(self):
        masg = QMessageBox(QMessageBox.Question, "Уведомление о заказе", "Это все ?")
        masg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        masg.setIcon(QMessageBox.Question)
        ret = masg.exec_()
        if ret == QMessageBox.Ok:
            msg = QMessageBox(QMessageBox.Question, "Рассілка", "Хотите ли вы получать рассылку о новых блюдах?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setIcon(QMessageBox.Question)
            reіt = msg.exec_()
            if reіt == QMessageBox.Yes:

                self.dialog.show()
                self.close()
            else:
                self.close()

    def delete(self):
        self.ui.order.clear()
        self.ui.menuWidg_2.clear()
        self.sum = 0

class Dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.Label = QLabel()
        self.setWindowIcon(QtGui.QIcon("ww.png"))
        self.Label.setObjectName("adress")
        self.Label.setText("Введите почту")
        self.E_adress = QLineEdit()
        self.E_adress.setObjectName("e_adress")
        self.But = QPushButton()
        self.But.setObjectName("connect")
        self.But.setText("Готово")
        self.But.clicked.connect(self.add)
        self.lauot = QFormLayout()
        self.setWindowTitle("Notification")
        self.lauot.addWidget(self.Label)
        self.lauot.addWidget(self.E_adress)
        self.lauot.addWidget(self.But)
        self.setLayout(self.lauot)
        self.mass_e_adress = []
        self.But.clicked.connect(self.add)
        self.setFixedSize(250, 110)

    def add(self):
        from re import search
        self.Address = self.E_adress.text()
        self.res = search(r'([@,\.])', str(self.Address))
        if self.res != None:
            wbd.for_e_mail(self.Address)
            msg = QMessageBox()
            msg.setText("Cпасибо. Хорошего дня!")
            msg.setIcon(QMessageBox.Information)
            reіtt = msg.exec_()
            timer = QTimer()
            timer.timeout.connect(self.time)
            self.timer.start(500)
        else:
            print("notok")
            msgg = QMessageBox()
            msgg.setText("Введите корректный e-mail")
            msgg.setIcon(QMessageBox.Critical)
            reіt = msgg.exec_()


    def time(self):
        sys.exit(app.exec_())
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
