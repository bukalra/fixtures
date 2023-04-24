from os import close, unlink
from tempfile import mkstemp
from itertools import count
from sqlalchemy import create_engine
import pytest

from tic_tac_toe.database import winner, metadata, history


@pytest.fixture
def create_games(database_connection):

    def game_creator(*games):
        move_id = count(1)
        for game_id, moves in enumerate(games, 1):
            database_connection.execute(history.insert(), [
                {
                    'game_id': game_id,
                    'move_id': next(move_id),
                    'position': int(position),
                    'symbol': symbol
                } for position, symbol in zip(moves[::2], moves[1::2])
            ])

    return game_creator


@pytest.fixture
def database_connection():
    fd, name = mkstemp(prefix='test_winner_', suffix='.sqlite')
    engine = create_engine(f'sqlite:///{name}')
    metadata.create_all(engine)
    with engine.connect() as connection:
        yield connection
    close(fd)
    unlink(name)


def test_3x_in_a_column(database_connection, create_games):
    create_games('4X1O5X3O2X6O8X')
    assert winner(database_connection, 1) == 'X'