# open_txt.py
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


class Question:
    def __init__(self, question: str):
        self.question = question
        self.answers = []
        self.right = None

    def add_answer(self, answer: str):
        self.answers.append(answer.replace('+', ''))
        if answer.find('+') != -1:
            self.right = len(self.answers) - 1

    def get_right(self):
        return self.answers[self.right]


def get_questions():
    with open('../resources/questions.txt') as f:
        data = f.read()

    data = data.split('\t')
    data = data[0].split('\n')
    data_clean = []
    for i in data:
        if not i == '':
            data_clean.append(i)

    questions = []

    k = 0
    index = 0
    while k < len(data_clean):
        if data_clean[k][0].isdigit():
            temp = Question(data_clean[k])
            index = k + 1
            while True:
                if index < len(data_clean):
                    if not data_clean[index][0].isdigit():
                        temp.add_answer(data_clean[index])
                    else:
                        break
                    index += 1
                else:
                    break
            questions.append(temp)
            del temp
        k = index
    return questions


if __name__ == '__main__':
    q = get_questions()
    print(len(q))
    print(q[0].question)
    print(q[0].answers)
    print(q[0].right)
