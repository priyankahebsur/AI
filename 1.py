import random
#We start with Hangman
text_file = open("words.txt", "r")
mytuple=text_file.readlines()
#mytuple=("ant","cat","dog","sheep","spider")
mylist=[]
#tuple can't be updated
print("Starting the Game: ")
r=random.randint(0,len(mytuple)-1)
secretWord=mytuple[r]
l=len(secretWord)
turns=3
guess=''
for i in range(0,l):
    mylist.append("_ ")
print(secretWord)
print(mylist)

while turns>0:
    flag=0
    for char in secretWord :
        if char in guess :
                print(char)
                flag+=1
        else :
            print("_")
           # flag+=1
    if flag==l:
      print("You won")
      break
    
    letter=input("Guess the letter?" )
    guess+=letter
    #print(str)
    if letter not in secretWord :
        turns-=1
    print ("Turns left : ",+turns)
    if turns==0 :
        print("Lose")

#if str in secretWord:
 #   print("Yay")
#else:
 #   print("Nay")
#print("done finally")
