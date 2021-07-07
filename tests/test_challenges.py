from daily_exercises.fibonacci_exercise import fibonacci
from daily_exercises.function_qa_exercise import ict_avarege
from daily_exercises.word_splitting_0606 import alphasort
from daily_exercises.dice import dice_roll

def test_dice_roll():
    assert dice_roll() > 0 and dice_roll() <= 6


def test_alphasort():
    assert alphasort("hello world and hello again") == "again and hello world"

def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_ict_average():
    assert ict_avarege(25, 50, 100) == 'Your average is 100.0 % and your grade is A'