from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()

lb_quest = QLabel('Вопрос: ')
lb_right_ans = QLabel('Правільний ответ: ')
lb_wrong_ans1 = QLabel('Перший не правільний: ')
lb_wrong_ans2 = QLabel('Другий не правільний: ')
lb_wrong_ans3 = QLabel('Третій не правільний: ')

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()
lb_header_stat = QLabel('Статістіка: ')
lb_statistic = QLabel()

v1_labels = QVBoxLayout()
v1_labels.addWidget(lb_quest)
v1_labels.addWidget(lb_right_ans)
v1_labels.addWidget(lb_wrong_ans1)
v1_labels.addWidget(lb_wrong_ans2)
v1_labels.addWidget(lb_wrong_ans3)

v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(le_question)
v1_lineEdits.addWidget(le_right_ans)
v1_lineEdits.addWidget(le_wrong_ans1)
v1_lineEdits.addWidget(le_wrong_ans2)
v1_lineEdits.addWidget(le_wrong_ans3)

h1_question = QHBoxLayout()
h1_question.addLayout(v1_labels)
h1_question.addLayout(v1_lineEdits)
btn_back = QPushButton('Назад')
btn_add = QPushButton('Добавить вопрос')
btn_clear = QPushButton('Очистить')

h1_button = QHBoxLayout()
h1_button.addWidget(btn_add)
h1_button.addWidget(btn_clear)

v1_res = QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_button)
v1_res.addWidget(lb_header_stat)
v1_res.addWidget(lb_statistic)
v1_res.addWidget(btn_back)
menu_win.setLayout(v1_res)
menu_win.resize(400, 300)

