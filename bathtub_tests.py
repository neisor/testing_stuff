from bathtub import Bathtub

def test_check_variable_types():
    bathtub = Bathtub('white', 100, 'oval')
    assert type(bathtub.color) == str
    assert type(bathtub.water_capacity) == int
    assert type(bathtub.shape) == str

