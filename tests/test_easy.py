from easy import isbn
from easy.grade_calculator import grade_calculator
from easy.isbn import isbn_func
from easy.times_tables import times_tables

def test_grade_calculator():
    assert grade_calculator(50, 50, 50) == "Your average score is : 50.0%\nYou scored a grade of: C"

def test_isbn():
    assert isbn_func('978-0-306-40615-') == '978-0-306-40615-7'

def test_times_tables():
    assert times_tables(2) == "1\t2\t\n2\t4\t\n"