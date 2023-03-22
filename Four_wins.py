
from enum import Enum
from turtle import left

lor = Enum("lor", "LEFT RIGHT")


class Game:
    """
    Class for four wins
    """

    def __init__(self, players = ["x", "o"]):
        self.players = players
        self.empty_field = "-"
    
        self.__game_field = [[self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field],  
                            [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field],
                            [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field],
                            [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field],
                            [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field],
                            [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field], [self.empty_field]]
        
        

    def get_game_field(self):
        """
        A Getter function for self.__game_field
        """
        return self.__game_field
        

    def show_field(self):
        """
        A function to show the game field.
        """
        print(self.__game_field[0:7])
        print(self.__game_field[7:14])
        print(self.__game_field[14:21])
        print(self.__game_field[21:28])
        print(self.__game_field[28:35])
        print(self.__game_field[35:42])



    def check__input(self, player_input):
        """
        A function to check player input.

        :param player_input: Player Input
        :type player_input: str

        :return: Return True if space is in row
        :rtype: Bool
        """

        if player_input in ["0", "1", "2", "3", "4", "5", "6"]:
            return True

        return False




    def check__ifFull(self, input_index):
        """
        A function to calculate how much space is left in a row.

        :param input_index: The input index of the player
        :type input_index: int

        :return: Return False if there is no space or the index if space is available
        :rtype: Bool or int

        """

        column = [self.__game_field[0+input_index][0], self.__game_field[7+input_index][0], self.__game_field[14+input_index][0], self.__game_field[21+input_index][0], self.__game_field[28+input_index][0], 
                  self.__game_field[35+input_index][0]]


        empty_fields_count = column.count(self.empty_field)

        if empty_fields_count == 0:
            return False

        return empty_fields_count


        #calculate the index to place player icon to the field



    def calculate_position(self, input_index, empty_fields):
        """
        A function to calculate the position which player will land in.

        :param input_index: The input index of the player
        :type input_index: int

        :param empty_fields: The number of fields which are empty.
        :type empty_fields: int


        :return: Returns the proper index of player.
        :rtype: int

        """

        field_index = (((empty_fields - 1) * 7) + input_index)


        return field_index


    
    def put__player(self, player, field_index):
        """"
        A function to put player icon into game field.

        :param player: The players icon
        :type player: str

        :param field_index: the index of the player postition
        :type field_index: int
        """

        self.__game_field[field_index].pop() 
        self.__game_field[field_index].append(player)







    def check__rows(self):
        """"
        A function which checks the rows.

        :return True or False
        :rtype: Bool
        """


        for player in self.players:
            for index in range(0, 36, 7):
                count_score = 0
                row = [self.__game_field[0+index][0], self.__game_field[1+index][0], self.__game_field[2+index][0], self.__game_field[3+index][0], self.__game_field[4+index][0], 
                       self.__game_field[5+index][0], self.__game_field[6+index][0]]

                for element in row:
                    if count_score == 4:
                        return True 

                    elif element == player:
                        count_score += 1

                    elif element != player:
                        count_score = 0


                if count_score == 4:
                    return True 

        return False


    def check__columns(self):
        """"
        A function which checks the columns.

        :return True or False
        :rtype: Bool
        """


        for player in self.players:
            for index in range(0, 7):
                count_score = 0
                column = [self.__game_field[0+index][0], self.__game_field[7+index][0], self.__game_field[14+index][0], self.__game_field[21+index][0], self.__game_field[28+index][0], 
                       self.__game_field[35+index][0]]

                for element in column:
                    if count_score == 4:
                        return True 

                    elif element == player:
                        count_score += 1

                    elif element != player:
                        count_score = 0


                if count_score == 4:
                    return True 

        return False




            





    
    def check__small_diagonals(self, left_or_right):
        """
        A function to check the "small" diagonals. 

        Row count to win: 4

        Diagonal Left in Index: 3, 11, 19, 27 
        Diagonal Left in Index: 14, 22, 30, 38

        Diagonal Right in Index: 3, 9, 15, 21 
        Diagonal Right in Index: 20, 26, 32, 40

        param left_or_right: Decides which "middle" diagonal will be checked.
        type left_or_right: Enum(lors)

        return: True if player managed to score a row consisting of 4 or False if uptil now nobody scored a row.
        rtype: Bool
        """
        

        if left_or_right == lor.LEFT:
            diagonals = [[self.__game_field[3], self.__game_field[11], self.__game_field[19], self.__game_field[27]],
                         [self.__game_field[14], self.__game_field[22], self.__game_field[30], self.__game_field[38]]]
            

        if left_or_right == lor.RIGHT:
            diagonals = [[self.__game_field[3], self.__game_field[9], self.__game_field[15], self.__game_field[21]],
                         [self.__game_field[20], self.__game_field[26], self.__game_field[32], self.__game_field[38]]]

        for diagonal in diagonals:
            for player in self.players:
                count_score = 0
                for element in diagonal:
                    

                    if count_score == 4:
                        return True 

                    elif element[0] == player:
                        count_score += 1

                    elif element[0] != player:
                        count_score = 0


                if count_score == 4:
                    return True 
                        
            return False


    
    def check__middel_diagonals(self, left_or_right):
        """
        A function to check the "middle" diagonals. 

        Row count to win: 5

        Diagonal Left in Index: 2, 10, 18, 26, 34 
        Diagonal Left in Index: 7, 15, 23, 31, 39

        Diagonal Right in Index: 4, 10, 16, 22, 28 
        Diagonal Right in Index: 13, 19, 25, 31, 37

        param left_or_right: Decides which "middle" diagonal will be checked.
        type left_or_right: Enum(lors)

        return: True if player managed to score a row consisting of 4 or False if uptil now nobody scored a row.
        rtype: Bool
        """

        

        if left_or_right == lor.LEFT:
            diagonals = [[self.__game_field[2], self.__game_field[10], self.__game_field[18], self.__game_field[26], self.__game_field[34]],
                         [self.__game_field[7], self.__game_field[15], self.__game_field[23], self.__game_field[31], self.__game_field[39]]]
            


        if left_or_right == lor.RIGHT:
            diagonals =  [[self.__game_field[4], self.__game_field[10], self.__game_field[16], self.__game_field[22], self.__game_field[28]],
                                [self.__game_field[13], self.__game_field[19], self.__game_field[25], self.__game_field[31], self.__game_field[37]]]


        for diagonal in diagonals:
            for player in self.players:
                count_score = 0
                for element in diagonal:
                    

                    if count_score == 4:
                        return True 

                    elif element[0] == player:
                        count_score += 1

                    elif element[0] != player:
                        count_score = 0


                if count_score == 4:
                    return True 
                    
        return False

        



    def check__big_diagonals(self, left_or_right):
        """
        A function to check the "big" diagonals. 

        Row count to win: 6

        Diagonal Left in Index: 0, 8, 16, 24, 32, 40 
        Diagonal Left in Index: 1, 9, 17, 25, 33, 41

        Diagonal Right in Index: 5, 11, 17, 23, 29, 35 
        Diagonal Right in Index: 6, 12, 18, 24, 30, 36

        param left_or_right: Decides which "big" diagonal will be checked.
        type left_or_right: Enum(lors)

        return: True if player managed to score a row consisting of 4 or False if uptil now nobody scored a row.
        rtype: Bool
        """

        if left_or_right == lor.LEFT:
            diagonals = [[self.__game_field[0], self.__game_field[8], self.__game_field[16], self.__game_field[24], self.__game_field[32], self.__game_field[40]],
                         [self.__game_field[1], self.__game_field[9], self.__game_field[17], self.__game_field[25], self.__game_field[33], self.__game_field[41]]]
            


        if left_or_right == lor.RIGHT:
            diagonals =  [[self.__game_field[5], self.__game_field[11], self.__game_field[17], self.__game_field[23], self.__game_field[29], self.__game_field[35]],
                                [self.__game_field[6], self.__game_field[12], self.__game_field[18], self.__game_field[24], self.__game_field[30], self.__game_field[36]]]


        for diagonal in diagonals:
            for player in self.players:
                count_score = 0
                for element in diagonal:
                    

                    if count_score == 4:
                        return True 

                    elif element[0] == player:
                        count_score += 1

                    elif element[0] != player:
                        count_score = 0


                if count_score == 4:
                    return True 
                    
        return False



    def check__all(self):
        """

        """
        
        if self.check__rows() == True or self.check__columns() == True or  self.check__small_diagonals(lor.LEFT) == True or self.check__middel_diagonals(lor.LEFT) == True or self.check__big_diagonals(lor.LEFT) == True or self.check__small_diagonals(lor.RIGHT) == True or self.check__middel_diagonals(lor.RIGHT) == True or self.check__big_diagonals(lor.RIGHT) == True:
            
            return True

        return False








                    
