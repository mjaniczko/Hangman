from player import Player
from game import Game
import view
import data 


def app():

    view.welcome_screen()
    play = view.new_game()

    while play == 'y':

        game = Game()
        print(game.answer)
        player = Player(game, 5) 
        while not player.move() > 0:
            pass

        print('''\nWyjaśnienie zagadnienia wedłgu SJP, ortograficzny,
wyrazów obcych i słownik do gier w jednym:''')
        data.describe(game.answer)
        play = view.new_game()

app()  