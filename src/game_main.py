# coding=utf-8
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QWidget

from classes.Campus import Campus
from classes.Cat import Cat
from classes.Game import Game
from ui import main_window


class myWindow(main_window.Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.set_Food.clicked.connect(lambda: self.update_Food())
        self.next_Day.clicked.connect(lambda: self.next_Round_Process())
        self.title = "昨天见到的猫咪"
        self.save_Record.clicked.connect(lambda: self.save_Game())
        self.load_Record.clicked.connect(lambda: self.load_Game())

    def save_Game(self):
        game.save_Saving()

    def load_Game(self):
        cats = load_cats_data(path)
        campus.load_Saving(cats)
        game.load_Saving(campus, cats)
        self.update_Main_Window_Information()

    def update_Food(self):
        food, ok = QInputDialog.getInt(QWidget(), "猫粮投放量", "会长，从今以后每天投放多少猫粮呢？")
        if food and ok:
            self.food_Display.setText("今天要喂的猫粮量 " + str(food))
            game.m_daily_consumption_expect = food

    def update_Main_Window_Information(self):
        # appear list
        appear_list = game.get_Appeared_Cats()
        self.food_Display_Past.setText("昨天实际喂了的猫粮量 " + ("%.2f" % game.m_daily_consumption))
        self.food_Display_Remain.setText("协会还剩的猫粮量 " + ("%.2f" % game.m_campus.m_food))
        appear_name = "\n"
        for name in appear_list:
            appear_name = appear_name + " " + name
        self.appeared_Cat_List.setText(self.title + appear_name)
        # update time
        time_Display = [int(game.m_time / 7) + 1, game.m_time % 7 + 1]
        self.time.setText("这是本学期第" + str(time_Display[0]) + "周第" + str(time_Display[1]) + "天")

    def next_Round_Process(self):
        # game process
        game.next_Round()
        # update gui
        self.update_Main_Window_Information()


def load_cats_data(path):
    cats = []
    data = pd.read_csv(path + "cat_data.csv", sep=",", engine="python", encoding="utf-8")
    for i in range(0, data.shape[0]):
        cats.append(Cat(data[u"Name"][i], data[u"Is_alive"][i], data[u"Friendly_const"][i], data[u"Consumption"][i]))
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
