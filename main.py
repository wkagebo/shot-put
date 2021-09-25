import re
import random

games = int(input("Hur många tävlingar? "))


def game():
    player = []  # two column 2D array: Name , Wins
    winner = []  # tracks winner of current game: Name, Score
    # game loop
    for i in range(0, games):
        # corresponds to the line number (minus 1) in the text file.
        player_num = 0
        score = 0
        highscore = 0

        with open('players.txt', encoding='utf8') as f:
            for line in f:
                data = line.split(" ")

                name = data[0] + " " + data[1]
                m = float(data[2])
                s = float(data[3])

                # calculates score for a given player in a given game
                for j in range(0, 6):
                    score += random.normalvariate(m, s)
                score = round(score / 6, 2)

                if score > highscore:
                    highscore = score
                    winner = [player_num, highscore]

                # populates list column zero with player names
                if i == 0:
                    player.append([name])
                    # sets number of wins to 0 initially
                    player[player_num].append(0)

                player_num += 1

            # game is finished and we have a winner!
            player[winner[0]][1] += 1  # increment wins by one

            # prints winner
            print("\n", player[winner[0]][0], winner[1], "\n")

    # prints win statistics
    print(player)


game()
