import game
import numpy as np
import matplotlib.pyplot as plt


def run_games(n=100):
    history = []
    for i in range(n):
        if (i + 1) % 100 == 0:
            print("Played %d of %d games" % (i + 1, n))
        winner, p1_turns = game.play_game(False)
        history.append([winner, p1_turns])
    return np.array(history)


def summary(history):
    p1 = history[history[:, 0] == 1]
    p2 = history[history[:, 0] == 2]
    mn = history[:, 1].min() - 1
    mx = history[:, 1].max() + 1
    bins = np.linspace(mn, mx, 15)
    print("Player 1 won %.2f of games" % (float(p1.shape[0])/history.shape[0]))
    f, axarr = plt.subplots(1, 2)
    axarr[0].bar([1, 2], [p1.shape[0], p2.shape[0]], align='center', alpha=0.5)
    axarr[0].set_xticks([1, 2])
    axarr[0].set_xticklabels(["Player 1", "Player 2"])

    axarr[1].hist(p1[:, 1], bins=bins, alpha=0.5, label="Player 1")
    axarr[1].hist(p2[:, 1], bins=bins, alpha=0.5, label="Player 2")
    axarr[1].legend()

    plt.show()

if __name__ == "__main__":
    games = run_games(5000)
    summary(games)