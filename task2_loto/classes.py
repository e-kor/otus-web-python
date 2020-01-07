from random import choice, randint, shuffle
from typing import NoReturn, Set
from settings import NUMBERS_IN_CARD_COUNT


class Card:
    def __init__(self, numbers):
        self.numbers = set(numbers)
        self.checked_numbers = set()

    def check(self, number: int) -> None:
        if number in self.numbers:
            self.checked_numbers.add(number)

    def __hash__(self):
        res = 0
        for num in self.numbers:
            res += hash(num)
        return res

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError
        for num in self.numbers:
            if num not in other.numbers:
                return False
        return True

    def __repr__(self):
        symbols = [
            f'{"X " if num in self.checked_numbers else "  "}{num}' for num in self.numbers]
        return '|'.join(symbols)


class Player:
    def __init__(self, number: int, card: Card):
        self.number = number
        self.card = card

    def __repr__(self):
        return f"Player {self.number}: {repr(self.card)}"

    @property
    def has_won(self):
        return len(self.card.checked_numbers) == NUMBERS_IN_CARD_COUNT


class Master:
    def __init__(self):
        self.numbers_queue = list(range(10, 100))
        shuffle(self.numbers_queue)
        self.numbers_shown = set()
        self.cards_given = set()

    def show_number(self) -> int:
        number = self.numbers_queue.pop()
        self.numbers_shown.add(number)
        return number

    def get_card(self) -> Card:
        numbers = set()
        while len(numbers) < NUMBERS_IN_CARD_COUNT:
            numbers.add(choice(self.numbers_queue))
        card = Card(numbers)
        if card in self.cards_given:
            card = self.get_card()
        self.cards_given.add(card)
        return card

    def is_checked_right(self, card: Card) -> bool:
        for num in card.checked_numbers:
            if num not in card.numbers or num not in self.numbers_shown:
                return False
            return True
