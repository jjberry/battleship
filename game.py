import simple_random_guesser as srg
import basic_strategy_player as bsp


def play_game():
    p1 = srg.SimpleRandomGuesser()
    p2 = bsp.BasicStrategyPlayer()
    print(p1.my_grid.grid)
    game_over = False
    turn_count = 0
    p1_turns = p2_turns = 0
    while not game_over:
        if turn_count % 2 == 0:
            guess = p1.make_guess()
            print("Player 1 guesses", guess)
            result = p2.check_opponent_guess(guess)
            print(result)
            p1.process_result(result)
            p1_turns += 1
            if len(p2.ships) == 0:
                game_over = True
                print("Player 1 wins in %d turns" % p1_turns)
        else:
            guess = p2.make_guess()
            print(p1.my_grid.grid)
            print("Player 2 guesses", guess)
            result = p1.check_opponent_guess(guess)
            print(result)
            p2.process_result(result)
            p2_turns += 1
            print(p2.opponent_grid.grid)
            if len(p1.ships) == 0:
                game_over = True
                print("Player 2 wins in %d turns" % p2_turns)
        turn_count += 1

if __name__ == "__main__":
    play_game()
