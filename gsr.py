"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time
import os
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass

class RockPlayer(Player):
    wins = 0

    def __init__(self):
        self.prev = "none"
        self.p1their_move = "none"
        self.name = "RockPlayer"

    def learn(self, my_move, their_move):
        pass

    def callname(self, pr1):
        print('\x1b[4;30;41m' + pr1 + ' RocktPlayer' + '\x1b[0m')

class RandomPlayer(Player):
    wins = 0

    def callname(self, pr1):
        print('\x1b[4;32;44m' + pr1 + ' RandomPlayer' + '\x1b[0m')

    def __init__(self):
        self.prev = "none"
        self.p1their_move = "none"
        self.name = "RandomPlayer"

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.p1my_move = my_move
        self.p1their_move = their_move

class CyclePlayer(Player):
    wins = 0

    def __init__(self):
        self.prev = "none"
        self.p1their_move = "none"
        self.name = "CyclePlayer"

    def callname(self, pr1):
        print('\x1b[4;30;47m' + pr1 + ' CyclePlayer' + '\x1b[0m')
        #print("CyclePlayer")

    def move(self):
        if self.prev == "none":
            self.prev = random.choice(moves)
        else:
            index = moves.index(self.prev)
            if index == 2:
                self.prev = moves[0]
            else:
                self.prev = moves[index+1]
        return self.prev

    def learn(self, my_move, their_move):
        self.p1my_move = my_move
        self.p1their_move = their_move

    def winss(self):
        self.wins += 1

class HumanPlayer(Player):
    wins = 0
    winnings = [0, 0, 0, 0]

    def __init__(self):
        self.name = "HumanPlayer"

    def callname(self, pr1):
        print('\x1b[4;34;42m' + pr1 + ' HumanPlayer' + '\x1b[0m')
        #print(self.name)

    def move(self):
        str1 = '\x1b[6;30;42m' + 'Rock, Paper, Scissors? quit >' + '\x1b[0m'
        human_string = input(str1)
        humanmove = human_string.lower()
        while humanmove not in moves:
            if humanmove == "quit":
                return humanmove
            print("Oops, invalid selection, try again >>")
            human_string = input("Rock, Paper, Scissors? >")
            humanmove = human_string.lower()
        return humanmove

    def learn(self, my_move, their_move):
        self.p1my_move = my_move
        self.p1their_move = their_move

class ReflectPlayer(Player):
    wins = 0

    def callname(self, pr1):
        print('\x1b[4;30;45m' + pr1 + ' ReflectPlayer' + '\x1b[0m')

    def __init__(self):
        self.prev = "none"
        self.p1their_move = "none"
        self.name = "ReflectPlayer"

    def move(self):
        if self.p1their_move == "none":
            return random.choice(moves)
        else:
            return self.p1their_move

    def learn(self, my_move, their_move):
        self.p1my_move = my_move
        self.p1their_move = their_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    rounds = 0

    def __init__(self, p1, p2, p3, p4, p5):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5

    def get_winner(self, m1, m2, pp1, pp2):
        if m1 == m2:
            self.tie = "Tie"
        elif beats(m1, m2) is True:
            self.tie = "P1 wins"
        else:
            self.tie = "P2 wins"
        return self.tie

    def who_won(self, plyrA, plyrB):
        if self.tie == "Tie":
            print("It is a tie, no points")
        elif self.tie == "P1 wins":
            p1w = plyrA.name
            print(f"{p1w} wins")
        elif self.tie == "P2 wins":
            p2w = plyrB.name
            print(f"{p2w} wins")
        return self.tie

    def announcewinner(self, plr_1, plr_2, pos):
        count1 = plr_1.wins
        count2 = plr_2.winnings[pos]
        name1 = plr_1.name
        name2 = plr_2.name
        if count1 == count2:
            print('\x1b[7;30;42m' + '**IT IS A FINAL TIE**' + '\x1b[0m')
            print(f"Player1 Total: {count1}/Player2 Total: {count2}")
        elif count1 > count2:

            print(f"{name1} ** WINS**")
            print(f"{name1} Total: {count1}/{name2} Total: {count2}")
        else:
            print(f"{name2} ** WINS**")
            print(f"{name1} Total: {count1}/{name2} Total: {count2}")

    def play_round(self):
        self.tie = "No tie"
        move1 = self.p1.move()
        move2 = self.p2.move()
        move3 = self.p3.move()
        move4 = self.p4.move()
        move5 = self.p5.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.p3.learn(move3, move2)
        self.p4.learn(move4, move2)
        self.p5.learn(move5, move2)
        if move2 == "quit":
            self.Playon = False
            return self.Playon
        who = self.get_winner(move1, move2, CyclePlayer(), HumanPlayer())
        if who =="P1 wins":
            self.p1.wins += 1
        elif who == "P2 wins":
            self.p2.winnings[0] += 1
        print(f"\nCyclePlayer : {move1} ")
        print(f"Human   :     {move2} ")
        self.who_won(CyclePlayer(), HumanPlayer())
        print(f"P1 score:{self.p1.wins} P2 Score: {self.p2.winnings[0]} " )
        print()
        #next player results
        who = self.get_winner(move3, move2, RandomPlayer(), HumanPlayer())
        if who =="P1 wins":
            self.p3.wins += 1
        elif who == "P2 wins":
            self.p2.winnings[1] += 1
        print(f"\nRandomPlayer : {move3} ")
        print(f"Human   :     {move2} ")
        self.who_won(RandomPlayer(), HumanPlayer())
        print(f"P3 score:{self.p3.wins} P2 Score: {self.p2.winnings[1]} " )
        print()
        #next player results
        who = self.get_winner(move4, move2, ReflectPlayer(), HumanPlayer())
        if who =="P1 wins":
            self.p4.wins += 1
        elif who == "P2 wins":
            self.p2.winnings[2] += 1
        print(f"\nReflectPlayer : {move4} ")
        print(f"Human   :     {move2} ")
        self.who_won(ReflectPlayer(), HumanPlayer())
        print(f"P4 score:{self.p4.wins} P2 Score: {self.p2.winnings[2]} " )
        print()
        #next player results
        who = self.get_winner(move5, move2, RockPlayer(), HumanPlayer())
        if who =="P1 wins":
            self.p5.wins += 1
        elif who == "P2 wins":
            self.p2.winnings[3] += 1
        print(f"\nRockPlayer : {move5} ")
        print(f"Human   :     {move2} ")
        self.who_won(RockPlayer(), HumanPlayer())
        print(f"P5 score:{self.p4.wins} P2 Score: {self.p2.winnings[3]} " )
        print()
        game.rounds += 1

    def play_game(self):
        round = 0
        self.Playon = True
        print("\nGame start!")
        pyr1 = game.p1.name
        pyr2 = game.p2.name
        pyr3 = game.p3.name
        pyr4 = game.p4.name
        pyr5 = game.p5.name
        game.p1.callname("Player1 is")
        #print(f"Player1 is: {pyr1} ")
        game.p2.callname("Player2 is")
        #print(f"Player2 is: {pyr2} ")
        game.p3.callname("Player3 is")
        #print(f"Player3 is: {pyr3} ")
        game.p4.callname("Player4 is")
        #print(f"Player4 is: {pyr4} ")
        game.p5.callname("Player5 is")
        #print(f"Player5 is: {pyr5} ")
        while self.Playon:
            print("\n")
            print(f"Round {round+1}:")
            self.play_round()
            round += 1
        str2 = '\x1b[2;30;41m' + 'Game Over!!' + '\x1b[0m'
        print("\n" + str2)
        str3 = '\x1b[1;30;43m' + 'Total Rounds Played:' + '\x1b[0m'
        print(f"{str3} {game.rounds} \n")
        if game.rounds != 0:
            print('\x1b[6;30;42m' + 'Final Scores' + '\x1b[0m')
            print("Winner of Cycle vs Human")
            self.announcewinner(self.p1, self.p2, 0)
            print("\n")
            print("Winner of Random vs Human")
            self.announcewinner(self.p3, self.p2, 1)
            print("\n")
            print("Winner of Reflect vs Human")
            self.announcewinner(self.p4, self.p2, 2)
            print("\n")
            print("Winner of Rock vs Human")
            self.announcewinner(self.p5, self.p2, 3)

if __name__ == '__main__':
    os.system("clear")
    game = Game(CyclePlayer(), HumanPlayer(), RandomPlayer(), ReflectPlayer(), RockPlayer())
    game.play_game()
