import simple_random_guesser as srg
import basic_strategy_player as bsp


def play_game(verbose=True):
    p1 = srg.SimpleRandomGuesser()
    p2 = bsp.BasicStrategyPlayer()
    game_over = False
    winner = None
    turn_count = 0
    p1_turns = p2_turns = 0
    while not game_over:
        if turn_count % 2 == 0:
            guess = p1.make_guess()
            if verbose:
                print("Player 1 guesses", guess)
            result = p2.check_opponent_guess(guess)
            if verbose:
                print(result)
            p1.process_result(result)
            p1_turns += 1
            if len(p2.ships) == 0:
                game_over = True
                winner = 1
                if verbose:
                    print("Player 1 wins in %d turns" % p1_turns)
        else:
            guess = p2.make_guess()
            if verbose:
                print("Player 2 guesses", guess)
            result = p1.check_opponent_guess(guess)
            if verbose:
                print(result)
            p2.process_result(result)
            p2_turns += 1
            if len(p1.ships) == 0:
                game_over = True
                if verbose:
                    print("Player 2 wins in %d turns" % p2_turns)
                winner = 2
        turn_count += 1
    return winner, p1_turns

if __name__ == "__main__":
    winners, turns = play_game()
