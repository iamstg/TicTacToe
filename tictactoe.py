#!/usr/bin/python
import os
import sys
from ctypes import *
from sys import stdin
os.system('clear')
print "\n"
print "WELCOME TO THE TIC-TAC-TOE GAME\n"
print "1.Create new user"
print "2:Login"
print "3:Exit"
match = 0
ct = 0
var = int(stdin.readline())
def ask():
	print "\n"
	print "What do you want to do next?"
	print "1: Create new user"
	print "2: Login & Play new game"
	print "3: Exit"

def getVariable(variable):
	variable = int(stdin.readline())
	return variable

def SaveFullGame():
	print "\nDo you want to save the game?\n"
	print "If Yes:Press 4"
	print "If No:Press any other key except 4"
	a = int(stdin.readline())
	if a == 4:
		with open("saved_games.csv","ab") as f:
			f.write("\n\n"+mat[0].value+"\n"+mat[1].value+"\n"+mat[2].value+"\n")
		print "\nYour Game has been Saved!!"
		print "You can check it out by 'vi saved_games.csv'\n"
	else:
		return

class CreateNewUser:
	def __init__(self,uname,passw):
		self.username=uname
		self.password=passw
	def saveinfile(self):
		with open("users.csv","ab") as myfile:
			myfile.write(self.username+","+self.password)
	def saveinfilemodified(self):
		with open("users.csv","ab") as myfile:
			myfile.write("\n"+self.username+","+self.password)

class PlayGame:
	def __init__(self,playername1,playername2,mat):
		self.player1=playername1
		self.player2=playername2
		self.matrix=mat

	def rules(self):
		print "\n"
		print "Rules are as follows:"
		print "When it is "+self.player1+"'s turn he has to enter two integers one by one both on a new line"
		print "The first integer denotes the row i.e either 1,2,3"
		print "The second integer denotes the column i.e 1,2,3"
		print "The corresponding position shall have the X in it"
		print "Same applies for "+self.player2
		print self.player2+"'s position shall be marked by a O"

	def player1turn(self):
		print self.player1+"'s turn"
		while True:
			print "Enter your positions"
			row1,column1 = map(int,sys.stdin.readline().split())
			if row1>=1 and row1<=3 and column1>=1 and column1<=3:
				if mat[row1-1][column1-1] == ' ':
					mat[row1-1][column1-1] = 'X'
					break
				else:
					print "This position is already occupied!!Try again."
			else:
				print "The entries are out of range!!Please enter again"

	def player2turn(self):
		print self.player2+"'s turn"
		while True:
			print "Enter your positions"
			row2,column2 = map(int,sys.stdin.readline().split())
			if row2>=1 and row2<=3 and column2>=1 and column2<=3:
				if mat[row2-1][column2-1] == ' ':
					mat[row2-1][column2-1] = 'O'
					break
				else:
					print "This position is already occupied!!Try again."
			else:
				print "The entries are out of range!!Please enter again"
	
	#0 if nothing ,1 if 1 wins , 2 if p2 wins
	def checkwinner(self):			
		if mat[0][0] == 'X' and mat[0][1] == 'X' and mat[0][2] == 'X':
			return 1			
		if mat[1][0] == 'X' and mat[1][1] == 'X' and mat[1][2] == 'X':
			return 1			
		if mat[2][0] == 'X' and mat[2][1] == 'X' and mat[2][2] == 'X':
			return 1			
		if mat[0][0] == 'X' and mat[1][0] == 'X' and mat[2][0] == 'X':
			return 1			
		if mat[0][1] == 'X' and mat[1][1] == 'X' and mat[2][1] == 'X':
			return 1			
		if mat[0][2] == 'X' and mat[1][2] == 'X' and mat[2][2] == 'X':
			return 1			
		if mat[0][0] == 'X' and mat[1][1] == 'X' and mat[2][2] == 'X':
			return 1			
		if mat[0][2] == 'X' and mat[1][1] == 'X' and mat[2][0] == 'X':
			return 1			
		if mat[0][0] == 'O' and mat[0][1] == 'O' and mat[0][2] == 'O':
			return 2			
		if mat[1][0] == 'O' and mat[1][1] == 'O' and mat[1][2] == 'O':
			return 2			
		if mat[2][0] == 'O' and mat[2][1] == 'O' and mat[2][2] == 'O':
			return 2			
		if mat[0][0] == 'O' and mat[1][0] == 'O' and mat[2][0] == 'O':
			return 2			
		if mat[0][1] == 'O' and mat[1][1] == 'O' and mat[2][1] == 'O':
			return 2			
		if mat[0][2] == 'O' and mat[1][2] == 'O' and mat[2][2] == 'O':
			return 2			
		if mat[0][0] == 'O' and mat[1][1] == 'O' and mat[2][2] == 'O':
			return 2			
		if mat[0][2] == 'O' and mat[1][1] == 'O' and mat[2][0] == 'O':
			return 2
		return 0
	
	#prints the matrix out in a board fashion
	def printboard(self):
		print " "+"\t"+" "+"1"+" "+"2"+" "+"3"
		print "\t"+"________"
		print " "+"1"+"\t"+"|"+mat[0][0]+"|"+mat[0][1]+"|"+mat[0][2]+"|"
		print "\t"+"________"
		print " "+"2"+"\t"+"|"+mat[1][0]+"|"+mat[1][1]+"|"+mat[1][2]+"|"
		print "\t"+"________"
		print " "+"3"+"\t"+"|"+mat[2][0]+"|"+mat[2][1]+"|"+mat[2][2]+"|"
		print "\t"+"________"


class Person:
	def __init__(self,uname):
		self.username=uname
	def welcome(self):
		print "Welcome", self.username

class checkcredentials:
	def __init__(self,player,password):
		self.name1=player
		self.pass1=password
	def chk(self):
		fl=0
		s=self.name1+","+self.pass1
		with open("users.csv","r") as f:
			for x in f:
				x=x.rstrip()
				if s == x:
					fl=1
					break
				if not x:
					continue
		return fl

class PostWin:
	def __init__(self,name,match):
		self.winner=name
		self.match=match
	def winningceremony(self):
		print "\n"
		print "The winner of the match is "+self.winner
		print self.winner+" will be added to Hall of Fame!!"
		print "type vi hall_of_fame.csv to check the list of users in hall of fame"
		if self.match == 1:
			with open("hall_of_fame.csv","ab") as f:
				f.write(self.winner)
		if self.match > 1:
			with open("hall_of_fame.csv","ab") as f:
				f.write("\n"+self.winner)

while var != 3:
	match = match + 1
	attempt=0
	while (var != 1 and var != 2) and attempt<5:
		attempt = attempt + 1
		print "Invalid entry"
		print "Please Enter again"
		var=getVariable(var)
		if var == 3:
			os._exit(1)
	if attempt == 5:
		print "Sorry!! Your limit of trying has exceeded!!Restart the game to play again!!"
		os._exit(1)
	
	while var == 1:
		print "\nCREATE USER\n"
		print "Enter User:"
		User=raw_input('->')
		print "Enter Password:"
		Password=raw_input('->')
		newuser=CreateNewUser(User,Password)
		if ct == 0:
			newuser.saveinfile()
		else:
			newuser.saveinfilemodified()
		ct=1
		print "\n"+"New User "+User+" created!!"
		print "\nTo again create new user,press 1"
		print "To login and start the game,press 2"
		var=getVariable(var)
		if var == 3:
			os._exit(1)

	attempt=0
	while (var != 2) and attempt<5:
		attempt = attempt + 1
		print "Invalid entry"
		print "Please Enter 2 to play the game or Enter 3 to quit the game"
		var=getVariable(var)
		if var == 3:
			os._exit(1)
	if attempt == 5:
		print "Sorry!! Your limit of trying has exceeded!!Restart the game to play again!!"
		os._exit(1)

	if var == 2:
		print "\n"
		print"LOGIN\n"
		print "\n"
		attempt=0
		flag=0
		while flag == 0 and attempt < 5:
			print "Enter User 1:"
			name1=raw_input('->')
			print "Enter password"
			pass1=raw_input('->')
			user1=checkcredentials(name1,pass1)
			flag=user1.chk()
			print "\n"
			if flag == 1:
				p1=Person(name1)
				p1.welcome()
			else: 
				print "Unsuccessful Login!!Try Again"
				attempt = attempt + 1
		if attempt == 5:
			print "Your login chances exceeded!!Restart and try again"
			os._exit(1)
		flag=0
		attempt=0
		print "\n"
		while flag == 0 and attempt<5:
			print "Enter User2:"
			name2=raw_input('->')
			print "Enter password:"
			pass2=raw_input('->')
			user2=checkcredentials(name2,pass2)
			flag=user2.chk()
			print "\n"
			if flag == 1:
				p2=Person(name2)
				p2.welcome()
			else:
				print "Unsuccessful Login!!Try again"
				attempt = attempt + 1
		if attempt == 5:
			print "Your login chances exceeded!!Restart and try again"
			os._exit(1)
		print "\n"
	
	print "Lets start the game"
	print name1+" is X"
	print name2+" is O"
	mat=((c_char * 3) * 3)()
	for i in range(0,3):
		for j in range(0,3):
			mat[i][j] = ' '
	Game=PlayGame(name1,name2,mat)
	Game.rules()
	Game.printboard()
	Game.player1turn()
	Game.printboard()
	Game.player2turn()
	Game.printboard()
	Game.player1turn()
	Game.printboard()
	Game.player2turn()
	Game.printboard()
	Game.player1turn()
	Game.printboard()
	g=Game.checkwinner()
	if g == 1:
		P1=PostWin(name1,match)
		P1.winningceremony()
		SaveFullGame()
		ask()
		var=getVariable(var)
		continue
	if g == 0:
		Game.player2turn()
		Game.printboard()
		g=Game.checkwinner()
	if g == 2:
		P2=PostWin(name2,match)
		P2.winningceremony()
		SaveFullGame()
		ask()
		var=getVariable(var)
		continue
	if g == 0:
		Game.player1turn()
		Game.printboard()
		g=Game.checkwinner()
	if g == 1:
		P1=PostWin(name1,match)
		P1.winningceremony()
		SaveFullGame()
		ask()
		var=getVariable(var)
		continue
	if g == 0:
		Game.player2turn()
		Game.printboard()
		g=Game.checkwinner()
	if g == 2:
		P2=PostWin(name2,match)
		P2.winningceremony()
		SaveFullGame()
		ask()
		var=getVariable(var)
		continue
	if g == 0:
		Game.player1turn()
		Game.printboard()
		g=Game.checkwinner()
	if g == 1:
		P1=PostWin(name1,match)
		P1.winningceremony()
		SaveFullGame()
		ask()
		var=getVariable(var)
		continue
	if g == 0:
		print "Match Tied"
	SaveFullGame()
	ask()
	var=getVariable(var)

if var == 3:
	os._exit(1)
