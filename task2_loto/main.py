from classes import Card, Player, Master


def run_game():
    players_count = int(input('How many players will play?\n'))
    master = Master()
    players = [Player(i, master.get_card()) for i in range(players_count)]

    n = 0

    while True:
        n += 1
        number = master.show_number()
        print(f"Round {n}. And the number is {number}")
        [p.card.check(number) for p in players]
        winners = list(filter(lambda p: p.has_won, players))
        true_winners = list(
            filter(lambda w: master.is_checked_right(w.card), winners))

        if true_winners:
            print(f"We've got a winner:")
            print('\n'.join([repr(p) for p in winners]))

            break
        print('\n'.join([repr(p) for p in players]))
        print()


if __name__ == '__main__':
    run_game()
