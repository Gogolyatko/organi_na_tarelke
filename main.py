from PyQt5.QtWidgets import QApplication

from random import choice, shuffle
from time import sleep

app = QApplication([])

from m2 import *
from m3 import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask +=1
q1 = Question('В яких одиницях вимірюють вагу?', 'в яблуках','кг','грами','ньютони')
q2 = Question('Температуру вимірюють в...', 'метрах','секундах','кілограмах','градусах Цельсія')
q3 = Question('Зміна положення тіла або його частин у просторі відносно інших тіл з часом - це ...', 'траєкторія','механічний рух','стан спокою','шлях')
q4 = Question('Що таке траєкторія?', 'слід на дорозі','тіло влітку','лінія, яку описує тіло під час механічного руху','це лінія')
q5 = Question('Що таке шлях?', ' це векторна величина','це відстань між двома точками','це пряма лінія','довжина траєкторії, описаної тілом за певний час')
q6 = Question('Комар летів, за пів години він подолав шлях 70 км. З якою швидкістю рухається комар?', '340 км/год','140 км/год','Комарі так швидко не літають','35 км/год')
q7 = Question('Яким приладом вимірюють швидкість автомобіля?', 'термометром','рулеткою','секундоміром','спідометром')
q8 = Question('Автобус за 1 хв пройшов 600 м. З якою швидкістю він рухався?', '10 м/с','371 км/год','100 м/с','41 км/год')
q9 = Question('Все те, що нас оточує - це...', 'поле','фізичне тіло','речовина','матерія')
q10 = Question('Речовина і поле - це ...', 'фізичні явища','фізичне тіло','види матерії','яблуко')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
question = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

def new_question():
    global cur_q
    cur_q = choice(question)
    lb_question.setText(cur_q.question)
    lb_right_answwer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answwer.text():
                lb_result.setText('Правільна!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Неправільне!')
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.text() == 'Отвітить':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Следующій вопрос')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText('Отвітить')
btn_next.clicked.connect(click_ok)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    question.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)



def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)


def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()