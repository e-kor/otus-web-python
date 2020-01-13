import pytest
from loto.classes import Card


class TestCard:
    def test_checking(self, card):
        for num in card.numbers:
            card.check(num)

    def test_misschecking(self, create_new_card):
        card = create_new_card()
        with pytest.raises(ValueError):
            card.check(9)


class TestMaster:
    def test_card_type(self, master):
        assert isinstance(master.get_card(), Card)

    def test_card_uniqness(self, master):
        assert master.get_card() != master.get_card()

    def test_num_uniqness(self, master):
        numbers_shown = set()
        while master.numbers_queue:
            new_number = master.show_number()
            assert new_number not in numbers_shown
            numbers_shown.add(new_number)
        with pytest.raises(IndexError):
            master.show_number()


class TestPlayer:
    def test_new_player(self, create_player):
        p = create_player()
        assert not p.has_won

    def test_won_player(self, create_player):
        p = create_player()
        for number in p.card.numbers:
            p.card.check(number)
        assert p.has_won
