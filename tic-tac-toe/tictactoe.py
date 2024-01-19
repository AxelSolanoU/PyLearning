import random

def get_players():

	p1 = input("quieres ser X o O? ")

	# el usuario escoje que quiere ser y se hace la condicion
	# si el usuario escoje x P2 se le asigna O si escoje O se le asigna x

	if p1.lower() in ["x","o"]:
		
		if p1.lower() == "x":
			p2 = "O"


		else:
			p2="X"


	else:
		
		print(f"Esta opcion {p1} no está entre las opciones validas")
		get_players()

	return p1, p2

def chose_starting_player(x,o):

	firstplayer= random.choice([x,o])
	if firstplayer == x:
		secondplayer= o

	else:
		secondplayer= x

	print(f"Inicia el jugador {firstplayer}")	

	return firstplayer , secondplayer

def create_table(BLANK=" "):

	return ["#",BLANK,BLANK,BLANK,
				BLANK,BLANK,BLANK,
				BLANK,BLANK,BLANK]

def print_table(table):
	
	print( f" {table[1]} | {table[2]} | {table[3]}")
	print("-----------")
	print( f" {table[4]} | {table[5]} | {table[6]}")
	print("-----------")
	print( f" {table[7]} | {table[8]} | {table[9]}")


def is_available(table,position,BLANK=" "):
	if table[position]==BLANK:
		return True
	else:
		return False 	

def get_position(player,table):

	position= int(input(f"Cual posición elijes del 1 al 9 {player}?"))

	if is_available(table,position):
		return position
	else:
		print("Lo siento la posición está ocupada")
		get_position(player, table)

def update_table(table,player,position):
	table[position]=player


def is_winner(player,table):

	if table[1] == player and table[2] == player and table[3] ==player:

		return True

	elif  table[4] == player and table[5] == player and table[6] ==player:

		return True

	elif table[7] == player and table[8] == player and table[9] ==player:

		return True

	elif table[1] == player and table[4] == player and table[7] ==player:
		return True

	
	elif table[2] == player and table[5] == player and table[8] ==player:
		return True


	elif table[3] == player and table[6] == player and table[9] ==player:
		return True	

	elif table[1] == player and table[5] == player and table[9] ==player:
		return True	

	elif table[3] == player and table[5] == player and table[7] ==player:
		return True	

	else:
		return False


def is_playable(table, BLANK=" "):

	if BLANK in table:
		return True

	else:

		return False
	

