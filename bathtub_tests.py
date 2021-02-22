from bathtub import Bathtub

bathtub = Bathtub()

# Tests for checking if bathtub was initiated correctly
def test_check_variable_types():
    assert type(bathtub.color) == str
    assert type(bathtub.water_capacity) == int
    assert type(bathtub.shape) == str
    assert bathtub.status == "empty"
    assert bathtub.cleanliness == "clean"

# Test for checking if bathtub was filled up correctly
def test_fill_up():
    assert bathtub.fill_up() == "Filled up"

# Test for checking if bathtub is filled
def test_check_fill():
    assert bathtub.status == "filled"

# Test for checking if bathtub has been emptied correctly
def test_empty():
    assert bathtub.empty() == "Emptied"

# Test if bathtub is empty and dirty after being used
def test_check_fill_empty():
    assert bathtub.status == "empty"
    assert bathtub.cleanliness == "dirty"

# Test if bathtub has been clogged
def test_check_clogged():
    assert bathtub.clog() == "Clogged"
    assert bathtub.status_clogged == "clogged"

# Test if bathtub has been unclogged
def test_check_unclogged():
    assert bathtub.unclog() == "Unclogged"
    assert bathtub.status_clogged == "unclogged"

# Test if bathtub has been cleaned
def test_clean():
    assert bathtub.clean() == "Clean"
    assert bathtub.cleanliness == "clean"
    
# Test for adding bathing salt and checking if it was added correctly
def test_salt():
    assert bathtub.add_salt() == "Bathing salt added"
    assert bathtub.status == "filled up and with bathing salt added"

# Test for filling up the bathtub to a certain level
def test_fill_to_certain_level():
    assert bathtub.status == "empty"
    assert bathtub.fill_up_to_a_certain_level(5) == "filled to a certain level"
    assert bathtub.status == "filled"
