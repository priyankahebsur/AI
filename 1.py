import random
#We start with Hangman
hang='HANGMAN'
HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   0   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   0   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   0   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   0   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
 =========''']
lines = [line.rstrip('\n') for line in open('words.txt')]
print("Starting the Game, computer chooses secret word.")
print("You have only 7 turns since this is HANGMAN")
def getRandomWord(myt):
    r=random.randint(0,len(myt)-1)
    return myt[r]
mylist=[]
secretWord=getRandomWord(lines)
l=len(secretWord)
turns=len(hang)
guess=''
p=0
for i in range(0,l):
    mylist.append("_ ")
print(mylist)
has={}
was={}
flag1=0
pest=1
for char in secretWord:
    was[char]=secretWord.count(char)
while turns>0:
    flag=0
    letter=input("Guess the letter?" )
    if secretWord.count(letter)>1:
        has[letter]=1
    guess+=letter
    if letter not in secretWord :
        turns-=1
        print(HANGMANPICS[7-turns-1])
    print ("Turns left : ",+turns)
    if turns==0 :
        print("Lose")
    for char in secretWord :
        if was[char]==1:
            if char in guess:
                x=secretWord.count(letter)
                flag=flag+1
        elif char in guess and was[char]>1:
                was[char]=0
                pest=0
                flag1=secretWord.count(letter)
    if pest==0:
        flag+=flag1      
    if flag==l:
      print("You won")
      break
print("The secret word was",secretWord)
    
    


