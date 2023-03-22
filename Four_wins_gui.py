
from Four_wins import Game


class Gui:

    def __init__(self, model):
        self.game = model


    def show_field(self):
        game_field = self.game.get_game_field()

        print(game_field[0:7])
        print(game_field[7:14])
        print(game_field[14:21])
        print(game_field[21:28])
        print(game_field[28:35])
        print(game_field[35:42])


    def get__input(self, player):
        """
        """
        i = 0
        
        while i < 1:

            player_input = input("Please enter an index: ")

            if self.game.check__input(player_input):
                player_position = int(player_input)

                empty_field_position = self.game.check__ifFull(player_position)
                if  empty_field_position != False:
                    player_position = self.game.calculate_position(player_position, empty_field_position)
                    self.game.put__player(player, player_position)
                    return True

    
    def show_winner_popup(self, player):
        print(f'Player: {player} won!')
            

    def run(self):
        """
        """
        print("Welcome to Four wins!")

        i = 0
        round_number = 1
        while i < 1:
            print("="*20)
            print(f'Round{round_number}')
            self.show_field()
            for player in self.game.players:
                print(f'Player: {player} turn')

                if self.get__input(player):
                    self.show_field()
                    if self.game.check__all():
                        self.show_winner_popup(player)
                        i += 1
                        break

        print("Game is over!", f'Total rounds: {round_number}')




        