from bathtub import Bathtub

bathtub = Bathtub('white', 100, 'oval')

def test_check_variable_types():
    assert type(bathtub.color) == str
    assert type(bathtub.water_capacity) == int
    assert type(bathtub.shape) == str

def test_fill_up():
    assert bathtub.fill_up() == "Filled up"
