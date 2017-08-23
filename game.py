import player


def play_game():
    p1 = player.Player()
    p2 = player.Player()
    game_over = False
    turn_count = 0
    while not game_over:
        if turn_count % 2 == 0:
            guess = p1.make_guess()
            print "Player 1 guesses", guess
            result = p2.check_opponent_guess(guess)
            print result
            p1.process_result(result)
            if len(p2.ships) == 0:
                game_over = True
                print "Player 1 wins in %d turns" % turn_count
        else:
            guess = p2.make_guess()
            print "Player 2 guesses", guess
            result = p1.check_opponent_guess(guess)
            print result
            p2.process_result(result)
            if len(p1.ships) == 0:
                game_over = True
                print "Player 2 wins in %d turns" % turn_count
        turn_count += 1

if __name__ == "__main__":
    play_game()
