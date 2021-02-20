from bathtub import Bathtub

bathtub = Bathtub()

def test_check_variable_types():
    assert type(bathtub.color) == str
    assert type(bathtub.water_capacity) == int
    assert type(bathtub.shape) == str
    assert bathtub.status == "empty"
    assert bathtub.cleanliness == "clean"

def test_fill_up():
    assert bathtub.fill_up() == "Filled up"

def test_check_fill():
    assert bathtub.status == "filled"
    
def test_empty():
    assert bathtub.empty() == "Emptied"
    assert bathtub.cleanliness == "dirty"

def test_check_fill_empty():
    assert bathtub.status == "empty"

def test_check_clogged():
    assert bathtub.clog() == "Clogged"
    assert bathtub.status_clogged == "clogged"

def test_check_unclogged():
    assert bathtub.unclog() == "Unclogged"
    assert bathtub.status_clogged == "unclogged"
    
def test_clean():
    assert bathtub.clean() == "Clean"
    assert bathtub.cleanliness == "clean"