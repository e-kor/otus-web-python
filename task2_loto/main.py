from classes import Player, Master


def run_game():
    master = Master()
    name = input('What is your name?\n')
    player = Player(name, master.get_card())
    print(f'Cool! Your card is:\n{player.card}')
    opponent = Player('computer', master.get_card())
    print(f'Your opponent is: {opponent}')
    while True:
        print()
        number = master.show_number()
        print(f'The number is {number}')
        to_check_ans = input('Want to check? (y/n)\n')
        if to_check_ans.lower() in ['y', 'yes']:
            try:
                player.card.check(number)
                print(f"You've checked a number! "
                      f"Your card now is:\n{player.card}")
            except ValueError:
                print('Wrong checking. Number was not in card. Game over')
                break
        else:
            if number in player.card.numbers:
                print('Wrong. Should have checked the number. '
                      'It was in the card. Game over')
                break
        try:
            opponent.card.check(number)
            print(f'{opponent.name} has checked a number! '
                  f'His card now is:\n{opponent.card}')
        except ValueError:
            pass
        for p in (player, opponent):
            if p.has_won:
                print(f'And... we have a winner!')
                break


if __name__ == '__main__':
    run_game()
