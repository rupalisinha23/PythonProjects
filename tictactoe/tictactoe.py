class tictactoe(object):
    def __init__(self):
        self.__board = {'top_left': [1,' '],
                 'top_center': [2,' '],
                 'top_right': [3, ' '],
                 'middle_left': [4, ' '],
                 'middle_center':[5, ' '],
                 'middle_right': [6, ' '],
                 'bottom_left': [7, ' '],
                 'bottom_center':[8, ' '],
                 'bottom_right': [9, ' ']}

    def print_board(self):
        print(self.__board['top_left'][1] + ' | ' + self.__board['top_center'][1] + ' | ' + self.__board['top_right'][1])
        print(self.__board['middle_left'][1] + ' | ' + self.__board['middle_center'][1] + ' | ' + self.__board['middle_right'][1])
        print(self.__board['bottom_left'][1] + ' | ' + self.__board['bottom_center'][1] + ' | ' + self.__board['bottom_right'][1])

    def check_rules(self, sym):

        if self.__board['top_left'][1] == sym and  \
            self.__board['middle_center'][1] == sym and \
            self.__board['bottom_right'][1] == sym:
            return 'Game Over!'
        elif self.__board['top_right'][1] == sym and \
            self.__board['middle_center'][1] == sym and \
            self.__board['bottom_left'][1] == sym:
            return 'Game Over!'
        elif self.__board['top_left'][1] == sym and \
            self.__board['middle_left'][1] == sym and \
            self.__board['bottom_left'][1] == sym:
            return 'Game Over!'
        elif self.__board['top_right'][1] == sym and \
            self.__board['middle_right'][1] == sym and \
            self.__board['bottom_right'][1] == sym:
            return 'Game Over!'
        elif self.__board['top_left'][1] == sym and \
            self.__board['top_center'][1] == sym and \
            self.__board['top_right'][1] == sym:
            return 'Game Over!'
        elif self.__board['bottom_left'][1] == sym and \
            self.__board['bottom_center'][1] == sym and \
            self.__board['bottom_right'][1] == sym:
            return 'Game Over!'
        elif self.__board['middle_left'][1] == sym and \
            self.__board['middle_center'][1] == sym and \
            self.__board['middle_right'][1] == sym:
            return 'Game Over!'
        else:
            return 'Game not over!'


    def update_board(self, move):

        for key, value in self.__board.items():
            if value[0] ==int(move[1]):
                if self.__board[key][1] == ' ':
                    self.__board[key][1] = move[0]

                    return self.check_rules(move[0]), self.__board
                else:
                    return self.check_rules(move[0]),'You cannot mark! It has already been marked or is a tie!'


    def play(self,player):
        if player:
            move = input('Enter your move symbol with location number separated with white space: ').strip('\n').strip().split(' ')
            status, updated_board = obj.update_board(move)
            obj.print_board()
            return status


if __name__ == '__main__':
    obj = tictactoe()
    player1= True
    player2= False

    if player1:
        print('Location options on the board: ')
        print('1. Top Left')
        print('2. Top Center')
        print('3. Top Right')
        print('4. Middle Left')
        print('5. Middle Center')
        print('6. Middle Right')
        print('7. Bottom Left')
        print('8. Bottom Center')
        print('9, Bottom Right')


        status = 'Game not over!'
        player1 = True
        player2 = False
        while status == 'Game not over!':
            if player1:
                status = obj.play(player1)
                print('Status: ', status)
                if status == 'Game Over!':
                    print('You won player 1')
                player1 = not player1
                player2 = not player2

            elif player2:
                status = obj.play(player2)
                print('status: ', status)
                if status == 'Game Over!':
                    print('You won player 1')
                player1 = not player1
                player2 = not player2
