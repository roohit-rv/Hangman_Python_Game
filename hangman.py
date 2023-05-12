import hangman_art
import hangman_words
import random
choosen_word=random.choice(hangman_words.word_list)
n=len(choosen_word)
print(choosen_word)
list=[]
for i in range(0,n):
    list.append("_")
print(list)
display=[]
lives=n
for i in range (0,n):
    display.append(choosen_word[i])
print(display)
print("HangMan Game")
print(hangman_art.logo)
print(hangman_art.HANGMANPICS[0])
print("you have", n, "lives\n" "For each wrong word you will guess, the body parts of man will be hanged and if you loose all the lives then you will be lost.\n" "So guess the right word and save the man")
art=1
while list!=display and lives!=0:
    x=0
    y=0
    print("guess a word")
    l=input()
    for i in range(0,n):
        if l==list[i]:
            x=1
    if x==1:
        print("you already have guessed the word")
    for i in range(0,n):
        if l==choosen_word[i]:
            list[i]=l
    for i in range(0,n):
        if l==choosen_word[i]:
            y=1
    if y==0:
        print("wrong guess")
        lives-=1
        print("lives left", lives)
        print(hangman_art.HANGMANPICS[art])
        art+=1
            
if lives==0:
    print("you lost")
else:
    print("you win")
        
