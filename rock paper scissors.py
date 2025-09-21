s='Rock-Paper-Scissors project'
print(s.title())
score1=0
score2=0
total1=0
total2=0
hands=['Rock','Paper','Scissors']
from random import choice,shuffle
for i in range(3):
	shuffle(hands)
	player1=choice(hands)
	player2=input('choose your hand:')
	if player1 == 'Rock' and player2 == 'Scissors':
		score1+=10
		print(f'player1 has {score1}points and player2 has {score2}point(s)')
	elif player2 == 'Rock' and player1 == 'Scissors':
		score2+=10
		print(f'player2 has {score2}points and player1 has {score1}point(s)')
	elif player1 == 'Scissors' and player2 == 'Paper':
		score1+=10
		print(f'player1 has {score1}points and player2 has {score2}point(s)')
	elif player2 == 'Scissors' and player1 == 'Paper':
		score2+=10
		print(f'player2 has {score2}points and player1 has {score1}point(s)')
	elif player1 == 'Paper' and player2 == 'Rock':
		score1+=10
		print(f'player1 has {score1}points and player2 has {score2}point(s)')
	elif player2 == 'Paper' and player1 == 'Rock':
		score2+=10
		print(f'player2 has {score2}points and player1 has {score1}point(s)')
	elif player1 == 'Rock' and player2 == 'Rock':
		print(f'player1 has {score1}points and player2 has {score2}point(s)')
	elif player1 == 'Scissors' and player2 == 'Scissors':
		print(f'player1 has {score1}points and player2 has {score2}point(s)')
	elif player1 == 'Paper' and player2 == 'Paper':
		print(f'player1 has {score1}points and player2 has {score2}point(s)')	
	total1=score1
	total2=score2
print(f'player1={total1}, player2={total2}')
if total1 > 10 and total2 < 10:
		print(f'player1 has {total1} point(s) and player2 has {total2} point(s)')
		print('player1 wins')
elif total1 < 10 and total2 > 10:
		print(f'player1 has {total1} points and player2 has {total2} point')
		print('player2 wins')
elif (total1 == 10 or total1 == 0) and (total2 == 10 or total2 == 0):
		print('its a tie')