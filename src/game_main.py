#-*- coding : utf-8-*-
from pandas import read_csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QWidget

from classes.Campus import Campus
from classes.Cat import Cat
from classes.Game import Game
from ui import main_window


class myWindow(main_window.Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.set_Food.clicked.connect(lambda :self.update_Food())
        self.next_Day.clicked.connect(lambda :self.next_Day_Process())
        #self.save_Record.clicked.connect(lambda :self.save_Data())

    def update_Food(self):
        food, ok = QInputDialog.getInt(QWidget(), "猫粮投放量", "会长，从今以后每天投放多少猫粮呢？")
        if food and ok:
            self.food_Display.setText("今天要喂的猫粮量 "+ str(food))
            game.m_daily_consumption = food

    def next_Day_Process(self):
        game.food_Decrease(game.m_daily_consumption)
        appear_list = game.get_Appeared_Cats(cats)
        self.food_Display_Past.setText("昨天实际喂了的猫粮量 " + str(game.m_daily_consumption))
        self.food_Display_Remain.setText("协会还剩的猫粮量 " + str(campus.m_food))
        appear_name = ""
        for name in appear_list:
            appear_name = appear_name + " " + name
        self.appeared_Cat_List.setText(appear_name)

        game.m_time+=1
        time_Display=[int(game.m_time/7)+1,game.m_time%7+1]
        self.time.setText("这是本学期第"+str(time_Display[0])+"周第"+str(time_Display[1])+"天")

    #def save_Data(self):
        #cats.to_csv(path + "cat_data.csv", sep=",", engine="python")


def load_cats_data(path):
    cats = []
    data = read_csv(path + "cat_data.csv", sep=",", engine="python")
    for i in range(1, data.shape[0] + 1):
        cats.append(Cat(data["Name"][i], data["Friendly_const"][i], data["Consumption"][i]))
    return cats


if __name__ == "__main__":
    import sys

    path = "savings/"
    cats = load_cats_data(path)
    campus = Campus(cats)
    game = Game(campus, cats)
    app = QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    win = myWindow(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())
