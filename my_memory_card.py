from PyQt5.QtCore import Qt
from random import shuffle
from random import randint
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel,QButtonGroup)
question_list = []

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q1 = Question('Госудаственный язык Португалии', 'Португальский', 'Английский', 'Немецкий', 'Русский')
q2 = Question('Столица Швеции','Берн', 'Стогкольм', 'Киев', 'Вашингтон')
q3 = Question('Столица Америки','Берн', 'Стогкольм', 'Киев', 'Вашингтон')
q4 = Question('Столица Украины','Берн', 'Стогкольм', 'Киев', 'Вашингтон')
q5 = Question('Столица Швейцарии','Берн', 'Стогкольм', 'Киев', 'Вашингтон')
question_list.append(q1)


question_list.append(q2)


question_list.append(q3)


question_list.append(q4)

question_list.append(q5)






app = QApplication([])
window = QWidget()
window.total = 0
window.score = 0

window.setWindowTitle('Memo Card')
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Какой национальности не существует?') # текст вопроса
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton("Алеуты")
rbtn_4 = QRadioButton('Смурфы')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым






#создаем панель результата


AnsGroupBox= QGroupBox('Результат теста')
answer = QLabel('Правильно/неправильно')
result = QLabel('тут будет правильній ответ')
layout_result = QVBoxLayout()
layout_result.addWidget(answer ,alignment = Qt.AlignLeft | Qt.AlignTop)
layout_result.addWidget(result,alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layout_result)


lat = QHBoxLayout()
lat2 = QHBoxLayout()
lat3 = QHBoxLayout()

lat.addWidget(lb_Question)
lat2.addWidget(AnsGroupBox)
lat2.addWidget(RadioGroupBox)
lat3.addWidget(btn_OK)

layout_Card = QVBoxLayout()
layout_Card.addLayout(lat, stretch=2)
layout_Card.addLayout(lat2, stretch=8)
layout_Card.addStretch(1)
layout_Card.addLayout(lat3, stretch=1)
layout_Card.addStretch(1)
layout_Card.setSpacing(5)


AnsGroupBox.hide()
window.setLayout(layout_Card)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')



def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    
def start_test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_question()


q = Question('Какой материк самый большой?','Евразия', 'Лондон', 'Австралия', 'Киев')
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    result.setText(q.right_answer)
    show_question()

def show_correct(res):
    answer.setText(res)
    show_result()
'''
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print("Статистика\n-Всего вопросов:', window.total , '\nПравильных ответов:' , window.score)
        print('Рейтинг:',window.score/window.total * 100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:',window.score/window.total * 100)
ask(q)'''
'''
def next_question():
    window.cur_question  += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    window_cur_question = randint(0, len(question_list) - 1)
    q = question_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_OK.text == 'Следующий вопрос':
        next_question()
    else:
        check_answer()'''

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:' , window.total , '\nПравильных ответов:' , window.score)
        print('Рейтинг:' , window.score / window.total * 100)

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:' , window.score / window.total * 100)

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:' , window.total , '\nПравильных ответов:' , window.score)
    window.car_question = window.car_question + 1
    if window.car_question >= len(question_list):
        window.car_question = 0
    q = question_list[window.car_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Следующий вопрос':
        next_question()
    else:
        check_answer()
btn_OK.clicked.connect(click_ok)

window.car_question = -1
total = 0 
score = 0


next_question()
window.show()
app.exec()