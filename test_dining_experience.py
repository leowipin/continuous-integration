from dining import DiningExperienceManager
from dining import mock_input

def test_maximum_order_quantity(capsys):
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '101', '50', 'done'])
    manager.select_meals(test_input)
    captured = capsys.readouterr()
    assert 'Maximum order quantity exceeded. Please try again.' in captured.out


def test_display_menu(capsys):
    manager = DiningExperienceManager()
    manager.display_menu()
    captured = capsys.readouterr()
    assert "Chinese:" in captured.out
    assert "chaulafan - $10" in captured.out
    assert "Italian:" in captured.out
    assert "pizza - $30" in captured.out

def test_select_meals():
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '2', 'done'])
    manager.select_meals(test_input)
    assert manager.order == {'chaulafan': 2}

def test_invalid_meal_selection():
    manager = DiningExperienceManager()
    test_input = mock_input(['invalid_meal', 'done'])
    manager.select_meals(test_input)
    assert manager.order == {}

def test_invalid_quantity():
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '-1', '2', 'done'])
    manager.select_meals(test_input)
    assert manager.order == {'chaulafan': 2}

def test_cost_calculation():
    manager = DiningExperienceManager()
    manager.order = {'chaulafan': 2}
    manager.total_quantity = 2
    manager.calculate_cost()
    assert manager.total_cost == 20

def test_discount_more_than_5():
    manager = DiningExperienceManager()
    manager.order = {'chaulafan': 6}
    manager.total_quantity = 6
    manager.calculate_cost()
    assert manager.total_cost == 44

def test_discount_more_than_10():
    manager = DiningExperienceManager()
    manager.order = {'cupcake': 12}
    manager.total_quantity = 12
    manager.calculate_cost()
    assert manager.total_cost == 28.8

def test_special_offer_discount_more_than_50():
    manager = DiningExperienceManager()
    manager.order = {'pizza': 3}
    manager.total_quantity = 3
    manager.calculate_cost()
    assert manager.total_cost == 80

def test_special_offer_discount_more_than_100():
    manager = DiningExperienceManager()
    manager.order = {'pizza': 4}
    manager.total_quantity = 4
    manager.calculate_cost()
    assert manager.total_cost == 95

def test_chefs_specials_surcharge():
    manager = DiningExperienceManager()
    manager.order = {'tomahawk': 1}
    manager.total_quantity = 1
    manager.calculate_cost()
    assert manager.total_cost == 26.25

def test_confirm_order_yes(capsys):
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '2', 'done', 'y'])
    manager.select_meals(test_input)
    manager.calculate_cost()
    result = manager.confirm_order(input_function=test_input)
    assert result == True
    captured = capsys.readouterr()
    assert 'Your order:' in captured.out

def test_confirm_order_no(capsys):
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '2', 'done', 'n'])
    manager.select_meals(test_input)
    manager.calculate_cost()
    result = manager.confirm_order(input_function=test_input)
    assert result == False
    captured = capsys.readouterr()
    assert 'Your order:' in captured.out


def test_run(capsys):
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '2', 'done', 'y'])
    result = manager.run(test_input)
    assert result == 20
    captured = capsys.readouterr()
    assert 'Chinese:' in captured.out
    assert 'chaulafan - $10' in captured.out

def test_run_no_confirm():
    manager = DiningExperienceManager()
    test_input = mock_input(['chaulafan', '2', 'done', 'n'])
    result = manager.run(test_input)
    assert result == -1

def test_run_no_order():
    manager = DiningExperienceManager()
    test_input = mock_input(['done'])
    result = manager.run(test_input)
    assert result == -1
