words=['canada','russia','norway','germany','sweden','scotland','england']
chances=6
count=0
total=0
chosen_letters=[]  #chosen letters are appended to the empty list
from random import choice
word=choice(words)   #randomly picks words
display=['_']*len(word)  # this represents the randomly chosen word with underscores
for i in range(len(word)):
    guess=input('Enter a letter:')
    if guess in word:
        chosen_letters.append(guess)
        displays=word.index(guess)  #an index of the guessed letter in the randomly picked word is returned
        display[displays]=guess   #the underscores are replaced by the correctly guessed letters
        count+=1                 #this counts the numbers of rightly guessed letters
        total=count
        print(f'{display},you have {chances-i} chance(s) left,you have guessed {count}letters correctly')
    else:
        chosen_letters.append(guess)
        print(f'incorrect guess,you have {chances-i} chances left')

if total == len(word):
        print(f'You win,you have guessed {total} letters of the word correctly')
else:
        print(f'You lose,you have guessed {total} letters')    
print(word)
    

