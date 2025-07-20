"""
Name:Zhenyang Gao

Description: The program which I've written is a game called "Sokoban". The aim for this game is to control
the player-"P" and push crates-"#" into the hole-"o" in a finite space, which some asterisk characters-"*"
are represent walls. Each round player can only move one step, you can press "u" button to undo your
previous step, and "r" button to restart the game. How many steps you have used will also be counted.
You can play this game with your friends and see who can use the least steps to finish the challenge!

"""


class Sokoban:
    def __init__(self, board):
        self.__board = board
        self.__move = []
        self.__new = []
        for row in range(len(self.__board)):
            current = []
            for col in range(len(self.__board[row])):
                current.append(self.__board[row][col])
            self.__new.append(current)
            

    def find_player(self):
        for row in range(len(self.__new)):
            for col in range(len(self.__new[row])):
                if self.__new[row][col] == 'P':
                    return (row, col)

    def complete(self):
        for row in range(len(self.__new)):
            for col in range(len(self.__new[row])):
                if self.__new[row][col] == 'o':
                    return False
        return True
            
    def get_steps(self):
        return len(self.__move)

    def restart(self):
        self.__move = []
        self.__new = []
        for row in range(len(self.__board)):
            current = []
            for col in range(len(self.__board[row])):
                current.append(self.__board[row][col])
            self.__new.append(current)

    def undo(self):
        if len(self.__move) > 0:
            last_move = self.__move.pop()
            for row, col in last_move.items():
                self.__new[row[0]][row[1]] = col
    
    def move(self, direction):
        row, col = self.find_player()
        character = {(row, col): 'P'}
        if direction == 'w':
            if self.__new[row - 1][col] == ' ':
                current = self.__new[row - 1][col]
                character[(row - 1, col)] = current
                self.__new[row - 1][col] = self.__new[row][col]
                self.__new[row][col] = ' '
                self.__move.append(character)
            elif self.__new[row - 1][col] == "#" and self.__new[row-2][col] not in ("#", "*"):
                if self.__new[row - 2][col] == 'o':
                    self.__new[row - 2][col] = ' '
                    character[(row - 2, col)] = 'o'
                    character[(row - 1, col)] = self.__new[row - 1][col]
                    self.__new[row - 1][col] = self.__new[row][col]
                    self.__new[row][col] = ' '
                elif self.__new[row - 2][col] == ' ':
                    self.__new[row - 2][col] = '#'
                    character[(row - 2, col)] = ' '
                    character[(row - 1, col)] = self.__new[row - 1][col]
                    self.__new[row - 1][col] = self.__new[row][col]
                    self.__new[row][col] = ' '
                self.__move.append(character)

        elif direction == 'a':
            if self.__new[row][col - 1] == " ":
                current = self.__new[row][col - 1]
                character[(row, col - 1)] = current
                self.__new[row][col - 1] = self.__new[row][col]
                self.__new[row][col] = ' '
                self.__move.append(character)
            elif self.__new[row][col - 1] == "#" and self.__new[row][col - 2] not in ("#", "*"):
                if self.__new[row][col - 2] == "o":
                    self.__new[row][col - 2] = " "
                    character[(row, col - 2)] = 'o'
                    character[(row, col - 1)] = self.__new[row][col - 1]
                    self.__new[row][col - 1] = self.__new[row][col]
                    self.__new[row][col] = ' '
                elif self.__new[row][col - 2] == ' ':
                    self.__new[row][col - 2] = '#'
                    character[(row, col - 2)] = ' '
                    character[(row, col - 1)] = self.__new[row][col - 1]
                    self.__new[row][col - 1] = self.__new[row][col]
                    self.__new[row][col] = ' '
                self.__move.append(character)

        elif direction == 's':
            length = len(self.__new)
            if self.__new[(row + 1) % length][col] == " ":
                current = self.__new[(row + 1) % length][col]
                character[((row + 1) % length, col)] = current
                self.__new[(row + 1) % length][col] = self.__new[row][col]
                self.__new[row][col] = ' '
                self.__move.append(character)
            elif self.__new[(row + 1) % length][col] == "#" and self.__new[(row + 2) % length][col] not in ("#", "*"):
                if self.__new[(row + 2) % length][col] == "o":
                    self.__new[(row + 2) % length][col] = ' '
                    character[((row + 2) % length, col)] = 'o'
                    character[((row + 1) % length, col)] = self.__new[(row + 1) % length][col]
                    self.__new[(row + 1) % length][col] = self.__new[row][col]
                    self.__new[row][col] = ' '
                elif self.__new[(row + 2) % length][col] == ' ':
                    self.__new[(row + 2) % length][col] = '#'
                    character[((row + 2) % length, col)] = ' '
                    character[((row + 1) % length, col)] = self.__new[(row + 1) % length][col]
                    self.__new[(row + 1) % length][col] = self.__new[row][col]
                    self.__new[row][col] = ' '
                self.__move.append(character)

        elif direction == 'd':
            length = len(self.__new[row])
            if self.__new[row][(col + 1) % length] == " ":
                current = self.__new[row][(col + 1) % length]
                character[(row, (col + 1) % length)] = current
                self.__new[row][(col + 1) % length] = self.__new[row][col]
                self.__new[row][col] = ' '
                self.__move.append(character)
            elif self.__new[row][(col + 1) % length] == "#" and self.__new[row][(col + 2) % length] not in ("#", "*"):
                if self.__new[row][(col + 2) % length] == "o":
                    self.__new[row][(col + 2) % length] = ' '
                    character[(row, (col + 2) % length)] = 'o'
                    character[(row, (col + 1) % length)] = self.__new[row][(col + 1) % length]
                    self.__new[row][(col + 1) % length] = self.__new[row][col]
                    self.__new[row][col] = ' '
                elif self.__new[row][(col + 2) % length] == ' ':
                    self.__new[row][(col + 2) % length] = '#'
                    character[(row, (col + 2) % length)] = ' '
                    character[(row, (col + 1) % length)] = self.__new[row][(col + 1) % length]
                    self.__new[row][(col + 1) % length] = self.__new[row][col]
                    self.__new[row][col] = ' '
                self.__move.append(character)  
                
    def __str__(self):
        return "\n".join(' '.join(row) for row in self.__new)
            

def main(board):
    game = Sokoban(board)
    message = 'Press w/a/s/d to move, r to restart, or u to undo'
    print(message)
    while not game.complete():
        print(game)
        move = input('Move: ').lower()
        while move not in ('w', 'a', 's', 'd', 'r', 'u'):
            print('Invalid move.', message)
            move = input('Move: ').lower()
        if move == 'r':
            game.restart()
        elif move == 'u':
            game.undo()
        else:
            game.move(move)
    print(game)
    print(f'Game won in {game.get_steps()} steps!')


# The map of the game:

board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'], 
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'], 
    ['*', ' ', 'P', '#', ' ', ' ', ' ', '*'], 
    ['*', '*', '*', '*', '*', ' ', '#', '*'], 
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'], 
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'], 
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
main(board)
