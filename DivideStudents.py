import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtCore import Qt


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


ICON_FILE = resource_path('icon.png')
UI_FILE = resource_path('main.ui')


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi(UI_FILE, self)
        self.setWindowTitle("Divide students!")
        self.setWindowIcon(QIcon(ICON_FILE))
        self.setFixedWidth(724)
        self.setFixedHeight(461)

        # TeamCount
        self.teamCount.setValidator(QIntValidator())
        self.teamCount.setMaxLength(2)
        self.teamCount.setAlignment(Qt.AlignRight)
        self.teamCount.setText("0")

        # MemberCount
        self.memberCount.setValidator(QIntValidator())
        self.memberCount.setMaxLength(2)
        self.memberCount.setAlignment(Qt.AlignRight)
        self.memberCount.setText("2")
        self.studentsCount.setText("1")

        self.results.setReadOnly(True)
        self.studentsCount.setReadOnly(True)

        self.processButton.clicked.connect(self.DoTheThing)
        self.studentsList.textChanged.connect(self.studentsListChanged)

    def studentsListChanged(self):
        people = self.studentsList.toPlainText()
        people = people.split('\n')
        number_people = len(people)
        self.studentsCount.setText(str(number_people))

    def DoTheThing(self):
        self.results.clear()
        people = self.studentsList.toPlainText()
        people = people.split('\n')
        number_people = len(people)
        number_of_members = int(self.memberCount.text())
        number_of_teams = int(self.teamCount.text())
        if number_of_teams == 0:
            number_of_teams = int(number_people/number_of_members)
            while number_people > 0 and number_of_members > 0:
                if number_people < number_of_members:
                    team = random.sample(people, number_people)
                    self.results.appendPlainText(
                        ' - '.join([str(elem) for elem in team]))
                    for x in team:
                        people.remove(x)
                else:
                    team = random.sample(people, number_of_members)
                    self.results.appendPlainText(
                        ' - '.join([str(elem) for elem in team]))
                    for x in team:
                        people.remove(x)
                number_people -= int(number_of_members)
                number_of_teams -= 1
        elif number_of_members == 0:
            number_of_members = int(number_people/number_of_teams)
            while number_people > 0:
                if number_people < number_of_members:
                    team = random.sample(people, number_people)
                    self.results.appendPlainText(
                        ' - '.join([str(elem) for elem in team]))
                    for x in team:
                        people.remove(x)
                else:
                    team = random.sample(people, number_of_members)
                    self.results.appendPlainText(
                        ' - '.join([str(elem) for elem in team]))
                    for x in team:
                        people.remove(x)
                number_people -= int(number_of_members)
                number_of_teams -= 1
        else:
            while number_people > 0 and number_of_teams > 0:
                if number_people < number_of_members:
                    team = random.sample(people, number_people)
                    self.results.appendPlainText(
                        ' - '.join([str(elem) for elem in team]))
                    for x in team:
                        people.remove(x)
                else:
                    team = random.sample(people, number_of_members)
                    self.results.appendPlainText(
                        ' - '.join([str(elem) for elem in team]))
                    for x in team:
                        people.remove(x)
                number_people -= int(number_of_members)
                number_of_teams -= 1


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(ICON_FILE))
mainwidnow = Main()
mainwidnow.show()
sys.exit(app.exec_())
