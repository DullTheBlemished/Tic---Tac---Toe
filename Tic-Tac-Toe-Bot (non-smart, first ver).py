import os
import time
import random

print("Hello World")
print("Note that I am still too stoopid to code smart tic-tac-toe bot, the bot movement is completely random!")

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0

player_input = 0
bot_input = 0
bot_move = 0

a1 ="?"
a2 ="?"
a3 ="?"
b1 ="?"
b2 ="?"
b3 ="?"
c1 ="?"
c2 ="?"
c3 ="?"

turn = 0

print("player's turn!")
print("Turn:", turn)
print(a1 + " | " + a2 + " | " + a3)
print("--+---+--")
print(b1 + " | " + b2 + " | " + b3)
print("--+---+--")
print(c1 + " | " + c2 + " | " + c3)

while True:
	
	player_input=input("input a1-c3 (first row is a, and collums follow 1, 2, and 3):")
	os.system("cls")
	turn = turn + 1
	
	
	if (player_input)=="a1" and s1 == 0:
		s1 = 1
	elif (player_input)=="a2" and s2 == 0:
		s2 = 1
	elif (player_input)=="a3" and s3 == 0:
		s3 = 1
	elif (player_input)=="b1" and s4 == 0:
		s4 = 1
	elif (player_input)=="b2" and s5 == 0:
		s5 = 1
	elif (player_input)=="b3" and s6 == 0:
		s6 = 1
	elif (player_input)=="c1" and s7 == 0:
		s7 = 1
	elif (player_input)=="c2" and s8 == 0:
		s8 = 1
	elif (player_input)=="c3" and s9 == 0:
		s9 = 1
	else:
		os.system("cls")
		print("Invalid input/Occupied square selected!")
		time.sleep(2)
		print(a1 + " | " + a2 + " | " + a3)
		print("--+---+--")
		print(b1 + " | " + b2 + " | " + b3)
		print("--+---+--")
		print(c1 + " | " + c2 + " | " + c3)
		continue
	
	if ((s1 == 1 and s2 == 1 and s3 == 1) or (s4 == 1 and s5 == 1 and s6 == 1) or
	(s7 == 1 and s8 == 1 and s9 == 1) or (s1 == 1 and s4 == 1 and s7 == 1) or
	(s2 == 1 and s5 == 1 and s8 == 1) or (s3 == 1 and s6 == 1 and s9 == 1) or
	(s1 == 1 and s5 == 1 and s9 == 1) or (s3 == 1 and s5 == 1 and s7 == 1)):
		time.sleep(1)
		os.system("cls")
		print("PLAYER WINS!")
		time.sleep(3)
		input("press ENTER to restart!")
		os.system("cls")
		s1 = 0
		s2 = 0
		s3 = 0
		s4 = 0
		s5 = 0
		s6 = 0
		s7 = 0
		s8 = 0
		s9 = 0
	
		player_input = 0
		bot_input = 0

		a1 ="?"
		a2 ="?"
		a3 ="?"
		b1 ="?"
		b2 ="?"
		b3 ="?"
		c1 ="?"
		c2 ="?"
		c3 ="?"
		turn = 0
		continue

	os.system("cls")
	print("bot choosing.")
	time.sleep(0.2)
	os.system("cls")
	print("bot choosing..")
	time.sleep(0.2)
	os.system("cls")
	print("bot choosing...")
	time.sleep(0.2)
	os.system("cls")
	
	if turn > 9:
		time.sleep(1)
		os.system("cls")
		print("DRAW!")
		time.sleep(3)
		input("press ENTER to restart!")
		os.system("cls")
		s1 = 0
		s2 = 0
		s3 = 0
		s4 = 0
		s5 = 0
		s6 = 0
		s7 = 0
		s8 = 0
		s9 = 0
	
		player_input = 0
		bot_input = 0

		a1 ="?"
		a2 ="?"
		a3 ="?"
		b1 ="?"
		b2 ="?"
		b3 ="?"
		c1 ="?"
		c2 ="?"
		c3 ="?"
		turn = 0
		continue

	bot_move = 0
	while bot_move == 0:
		bot_input = random.randint(1,9)
	
		if (bot_input)==1 and s1 == 0:
			s1 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==2 and s2 == 0:
			s2 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==3 and s3 == 0:
			s3 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==4 and s4 == 0:
			s4 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==5 and s5 == 0:
			s5 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==6 and s6 == 0:
			s6 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==7 and s7 == 0:
			s7 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==8 and s8 == 0:
			s8 = 2
			bot_move = 1
			turn = turn + 1
		elif (bot_input)==9 and s9 == 0:
			s9 = 2
			bot_move = 1
			turn = turn + 1

	if s1 == 1:
		a1 = "o"
	elif s1 == 2:
		a1 = "x"
	elif s1 == 0:
		a1 = "?"

	if s2 == 1:
		a2 = "o"
	elif s2 == 2:
		a2 = "x"
	elif s2 ==0:
		a2 = "?"

	if s3 == 1:
		a3 = "o"
	elif s3 == 2:
		a3 = "x"
	elif s3 == 0:
		a3 = "?"

	if s4 == 1:
		b1 = "o"
	elif s4 == 2:
		b1 = "x"
	elif s4 ==0:
		b1 = "?"

	if s5 == 1:
		b2 = "o"
	elif s5 == 2:
		b2 = "x"
	elif s5 == 0:
		b2 = "?"

	if s6 == 1:
		b3 = "o"
	elif s6 == 2:
		b3 = "x"
	elif s6 ==0:
		b3 = "?"

	if s7 == 1:
		c1 = "o"
	elif s7 == 2:
		c1 = "x"
	elif s7 == 0:
		c1 = "?"

	if s8 == 1:
		c2 = "o"
	elif s8 == 2:
		c2 = "x"
	elif s8 ==0:
		c2 = "?"

	if s9 == 1:
		c3 = "o"
	elif s9 == 2:
		c3 = "x"
	elif s9 == 0:
		c3 = "?"
	
	print(a1 + " | " + a2 + " | " + a3)
	print("--+---+--")
	print(b1 + " | " + b2 + " | " + b3)
	print("--+---+--")
	print(c1 + " | " + c2 + " | " + c3)

	if ((s1 == 2 and s2 == 2 and s3 == 2) or (s4 == 2 and s5 == 2 and s6 == 2) or
	(s7 == 2 and s8 == 2 and s9 == 2) or (s1 == 2 and s4 == 2 and s7 == 2) or
	(s2 == 2 and s5 == 2 and s8 == 2) or (s3 == 2 and s6 == 2 and s9 == 2) or
	(s1 == 2 and s5 == 2 and s9 == 2) or (s3 == 2 and s5 == 2 and s7 == 2)):
		time.sleep(1)
		os.system("cls")
		print("BOT WINS (how the helly did you lose to pure odds buddy)!")
		time.sleep(3)
		input("press ENTER to restart!")
		os.system("cls")
		s1 = 0
		s2 = 0
		s3 = 0
		s4 = 0
		s5 = 0
		s6 = 0
		s7 = 0
		s8 = 0
		s9 = 0
	
		player_input = 0
		bot_input = 0

		a1 ="?"
		a2 ="?"
		a3 ="?"
		b1 ="?"
		b2 ="?"
		b3 ="?"
		c1 ="?"
		c2 ="?"
		c3 ="?"
		turn = 0
		continue