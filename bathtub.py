import time
import sys
class Bathtub():
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
        
    
    def fill_up(self):
        print(f'Your bathtub is filling up. {self.water_capacity} liters of water are being poured in. Wait...', end='\r')
        time.sleep(5)
        print('Congratulations! Your bathtub has been filled up. You can take your bath now. The water is clean.')
        self.status = "filled"
        return "Filled up"
    
    def empty(self):
        print('Emptying your bathtub. Wait...', end='\r')
        time.sleep(5)
        print('Bathtub emptied successfully!')
        self.status = "empty"
        self.cleanliness = "dirty"
        return "Emptied"
    
    def clog(self):
        self.status_clogged = "clogged"
        return "Clogged"
    
    def unclog(self):
        self.status_clogged = "unclogged"
        return "Unclogged"
    
    def clean(self):
        self.cleanliness = "clean"
        return "Clean"