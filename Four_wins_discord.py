import discord
from discord import member

from Four_wins import Game


class MyClient(discord.Client):

    def __init__(self, intet):
        super().__init__(intents=intet)
        self.players = []
        self.players_icon = []
        self.game = None



    
    
    async def on_ready(self):
        print("I'm ready!")
        

    async def on_message(self, message):
        #print((str(message.author), str(message.content)))
        if str(message.content) == "Play bot":
            await message.channel.send("Lets start!")
            await message.channel.send("Who wants to be Player 1? Write anything inside")

            player1_message = await self.wait_for("message", check=lambda message: message)
            await message.channel.send(f'So Player1 is {str(player1_message.author)} What icon do you want?')
            player1_icon = await self.wait_for("message", check=lambda message: message)

            self.players.append(str(player1_message.author))
            self.players_icon.append(str(player1_icon.content))

            await message.channel.send("Player 2 please write anything in chat.")
            player2_message = await self.wait_for("message", check=lambda message: message)
            await message.channel.send(f'So Player2 is {str(player2_message.author)} What icon do you want?')
            player2_icon = await self.wait_for("message", check=lambda message: message)

            self.players.append(str(player2_message.author))
            self.players_icon.append(str(player2_icon.content))

            await message.channel.send("Debugging:")
            await message.channel.send(self.players)
            await message.channel.send(self.players_icon)

            #create Game instance
            self.game = Game(self.players_icon)


            #actual game starts
            await message.channel.send("Welcome to Four wins!")

            i = 0
            round_number = 0
            while i < 1:
                round_number += 1
                await message.channel.send("="*20)
                await message.channel.send(f'Round{round_number}')

                await self.show_field(message)

                for index, player_icon in enumerate(self.game.players):
                    await message.channel.send(f'Player: {self.players[index]} turn')

                    if await self.get__input(self.players[index], player_icon, message):
                        await self.show_field(message)
                        if self.game.check__all():
                            await self.show_winner_popup(self.players[index], message)
                            i += 1
                            break
        
            await message.channel.send(f'Game is over! Total rounds: {round_number}')


    
    async def show_field(self, message):
        game_field = self.game.get_game_field()

        await message.channel.send(str(game_field[0:7]))
        await message.channel.send(str(game_field[7:14]))
        await message.channel.send(str(game_field[14:21]))
        await message.channel.send(str(game_field[21:28]))
        await message.channel.send(str(game_field[28:35]))
        await message.channel.send(str(game_field[35:42]))




    async def get__input(self, player, player_icon, message):
        i = 0
        
        player_input_message = True
        while i < 1:

            await message.channel.send(f'Where do you want to put your icon {player} What icon do you want?')
            player_input_message = await self.wait_for("message", check=lambda message: message)

            if player == str(player_input_message.author):
                if self.game.check__input(str(player_input_message.content)):
                    player_position = int(str(player_input_message.content))

                    empty_field_position = self.game.check__ifFull(player_position)
                    if  empty_field_position != False:
                        player_position = self.game.calculate_position(player_position, empty_field_position)
                        self.game.put__player(player_icon, player_position)
                        return True
        


    async def show_winner_popup(self, player, message):
        await message.channel.send(f'Player: {player} won!')
        




    def get__player_icon(self):
        print("give name:")


    


m = MyClient(discord.Intents.all())
m.run("")
