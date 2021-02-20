import time
import sys
class Bathtub():
    
    # Initiate Bathtub class instance
    def __init__(self):
        self.status = "empty"
        print("\nWhat should the color of the bathtub be?:")
        self.color = input()
        print("What should the capacity of the bathtub be (in litres)?:")
        try:
            self.water_capacity = int(input())
        except ValueError:
            print('You can only input an integer! Try again...')
            sys.exit()
        print("What should the shape of the bathtub be?:")
        self.shape = input()
        self.cleanliness = "clean"
    
    # Fill bathtub with water
    def fill_up(self):
        print(f'Your bathtub is filling up. {self.water_capacity} litres of water are being poured in. Wait...', end='\r')
        time.sleep(5)
        print('Congratulations! Your bathtub has been filled up. You can take your bath now. The water is clean.')
        self.status = "filled"
        return "Filled up"
    
    # Empty bathub
    def empty(self):
        print('Emptying your bathtub. Wait...', end='\r')
        time.sleep(5)
        print('Bathtub emptied successfully!')
        self.status = "empty"
        self.cleanliness = "dirty"
        return "Emptied"
    
    # Clog bathtub
    def clog(self):
        self.status_clogged = "clogged"
        return "Clogged"
    
    # Unclog bathtub
    def unclog(self):
        self.status_clogged = "unclogged"
        return "Unclogged"
    
    # Clean bathtub
    def clean(self):
        self.cleanliness = "clean"
        return "Clean"
    
    # Adding bathing salt but do not change the instance's attributes
    def add_salt(self):
        return "Bathing salt added"