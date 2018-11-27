# game.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from hangman import Hangman
from guess import Guess
from word import Word


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database        
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
# 가로길이를 300까지 크기를 키워주면 13글자 이상도 들어 갈 수 있다.
        self.currentWord.setFixedWidth(300)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.hangman = Hangman()
        #randFromDB() 괄호 사이에 숫자 입력하여 랜덤 길이 넣어준다. !!
        word = self.word.randFromDB(15)
        
        self.guess = Guess(self.word.randFromDB())
        self.gameOver = False
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
        # 메시지 출력하고 - message.setText() - 리턴
            self.message.setText("Game Over")
        # return 추가
            return "Finished"

        

        if len(guessedChar) != 1:
        # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
            self.charInput.setText("1글자만 입력하세요.")
            return "Finished"

        # 먼저 guessedChar를 소문자로 변형
        guessedChar = guessedChar.lower()
        
        if guessedChar in guess.guessedChars:
            self.message.setText("이미 추측한 글자입니다.")
            return "Finished"
        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴

        success = self.guess.guess(guessedChar)
        
        if success == False:
            # 남아 있는 목숨을 1 만큼 감소
            hangman.decreaseLife()
            # 메시지 출력
            self.message.setText("not " + '"' + guessedChar + '"' + "in the word")


        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력        
        self.guessedChars.setText(self.guess.displayGuessed())

        if self.guess.finished():
            # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로            
            self.message.setText("Success!")
            self.gmaeOver == True

        elif self.hangman.getRemainingLives() == 0:
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로
            self.message.setText("Fail!" + guess.secretWord)
            self.gameOver == True


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())

===============================================================================================================
word.py

import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        self.A = 0 # 가장큰 길이 수 구하기.
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
            if len.word > 0:
                A = len.word

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self, minLength):
        #word에서 가장 긴 단어의 길이 찾기

        length = 0
        for i in self.words:
            if length < len(i):
                length = len(i)

        if num > length:
            num = length

        #사용자가 입력한 최소 길이가 word.txt에 있는 가장 긴 단어보다 길면, 최소 길이를 수정    
        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) < num:
                pass
            else:
                break

        return self.words[r]
    # 접근법 2사용
