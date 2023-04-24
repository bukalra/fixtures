import unittest
from tic_tac_toe.tic_tac_toe import tic_tac_toe_winner
import doctest
from tic_tac_toe import tic_tac_toe

class TestFinishedGame(unittest.TestCase):  #➜ 1

    def test_3x_in_a_row(self):  #➜ 2
        for i, board in enumerate(('XXXO  O O','O  XXXO O','O OO  XXX')):
            with self.subTest(row=i+1):
                self.assertEqual(tic_tac_toe_winner(board), 'X')

    # kolejne testy dla planszy opisujących zakończone gry


class TestUnfinishedGame(unittest.TestCase):

    def test_empty_board(self):
        self.assertIsNone(tic_tac_toe_winner(' '*9))  #➜ 4

    # kolejne testy dla niezakończonych gier


class TestInvalidBoard(unittest.TestCase):

    def test_illegal_symbols(self):
        with self.assertRaises(ValueError):  #➜ 5
            tic_tac_toe_winner('    E    ')

    @unittest.skip('not implemented')
    def test_3x_in_a_column(self):
        self.assertEqual(tic_tac_toe_winner('X  XO XOO'), 'X')

    # kolejne testy nieprawidłowego wejścia


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tic_tac_toe))
    return tests



