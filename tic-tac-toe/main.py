from tictactoe import *

def main():
	jugador1, jugador2 = get_players()

	mainplayer, secondplayer =chose_starting_player(jugador1,jugador2)


	TABLE= create_table()

	while is_playable(TABLE):
			

		print_table(TABLE)

		positionMainPlayer = get_position(mainplayer , TABLE)

		update_table(TABLE, mainplayer, positionMainPlayer)

		print_table(TABLE)

		if is_winner(mainplayer, TABLE):

			break

		positionSecondPlayer = get_position(secondplayer , TABLE)

		update_table(TABLE, secondplayer, positionSecondPlayer)

		print_table(TABLE)

		if is_winner(secondplayer, TABLE):

			break





























if __name__ == '__main__':
	
	main()