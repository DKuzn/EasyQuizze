# easy_quizze.py
#
# Copyright 2020 Дмитрий Кузнецов
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt5 import QtWidgets
import mainwindow
from open_txt import get_questions


class EasyQuizzeApp(QtWidgets.QMainWindow, mainwindow.Ui_mainWindow):
    def __init__(self):
        super(EasyQuizzeApp, self).__init__()
        self.setupUi(self)
        self.score_count = 0
        self.question_number = 0
        self.quezze_is_end = False
        self.questions = get_questions()
        self.startButton.clicked.connect(self.start_button_clicked)
        self.nextButton.clicked.connect(self.next_button_clicked)

    def start_button_clicked(self):
        if not self.quezze_is_end:
            self.quizze_status.setText('В процессе')
            self.quizze_status.setStyleSheet('color: blue')
        self.nextButton.setEnabled(True)
        self.answer1Button.setEnabled(True)
        self.answer2Button.setEnabled(True)
        self.answer3Button.setEnabled(True)
        self.answer4Button.setEnabled(True)
        self.place_question(self.question_number)

    def next_button_clicked(self):
        if not self.quezze_is_end:
            if self.answer1Button.isChecked():
                answer = self.answer1Button.text()
            elif self.answer2Button.isChecked():
                answer = self.answer2Button.text()
            elif self.answer3Button.isChecked():
                answer = self.answer3Button.text()
            else:
                answer = self.answer4Button.text()
            right = self.check_answer(self.question_number, answer)
            if right:
                self.score_count += 4
            self.score.setText(str(self.score_count))
            self.question_number += 1
            if self.question_number == len(self.questions) - 1:
                self.quezze_is_end = True
            self.place_question(self.question_number)
        else:
            self.quizze_status.setText('Завершена')
            self.quizze_status.setStyleSheet('color: green')

    def place_question(self, number):
        self.question.setText(self.questions[number].question)
        self.answer1Button.setText(self.questions[number].answers[0])
        self.answer2Button.setText(self.questions[number].answers[1])
        self.answer3Button.setText(self.questions[number].answers[2])
        if len(self.questions[number].answers) > 3:
            self.answer4Button.setText(self.questions[number].answers[3])
            self.answer4Button.setEnabled(True)
        else:
            self.answer4Button.setText('')
            self.answer4Button.setEnabled(False)

    def check_answer(self, number: int, answer: str):
        right_answer = self.questions[number].get_right()
        if right_answer == answer:
            return True
        else:
            return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = EasyQuizzeApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
