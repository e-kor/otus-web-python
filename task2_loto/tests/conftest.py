from pytest import fixture
from loto.classes import Card, Player, Master
from random import randint


@fixture()
def create_new_card():
    def wrap():
        m = Master()
        return m.get_card()
    return wrap


@fixture()
def create_player():
    def wrap():
        m = Master()
        return Player('test player', m.get_card())
    return wrap


@fixture
def card():
    m = Master()
    return m.get_card()


@fixture
def master():
    return Master()
