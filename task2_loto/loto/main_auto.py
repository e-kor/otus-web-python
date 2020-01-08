from classes import Player, Master


def run_game(players_count):
    master = Master()
    players = [Player(f'computer #{i}', master.get_card())
               for i in range(players_count)]
    loop_number = 0
    while True:
        loop_number += 1
        number = master.show_number()
        print(f"Round {loop_number}. And the number is {number}")
        for p in players:
            try:
                p.card.check(number)
            except ValueError:
                pass
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
    players_count = int(input('How many players will play?\n'))
    run_game(players_count)
