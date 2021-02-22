import time
import sys
class Bathtub():
    
    # Initiate Bathtub class instance
    def __init__(self):
        self.status = "empty"
        print("\nWhat should the color of the bathtub be?:")
        self.color = input()
        if self.color not in ["white", "yellow", "blue", "purple", "black", "red", "green", "mahagon"]:
            print('You did not use a traditional color of a bathtub! Try again...')
            sys.exit()
        print("What should the capacity of the bathtub be (in litres)?:")
        try:
            self.water_capacity = int(input())
        except ValueError:
            print('You can only input an integer! Try again...')
            sys.exit()
        if self.water_capacity < 25:
            print('Water capacity has to be at least 25 litres! Try again...')
            sys.exit()
        print("What should the shape of the bathtub be?:")
        self.shape = input()
        if self.shape not in ["oval", "round", "square"]:
            print("You did not use a traditional shape of a bathtub! Try again...")
            sys.exit()
        self.cleanliness = "clean"
    
    # Fill bathtub all the way up with water
    def fill_up(self):
        print(f'\nYour bathtub is filling up. {self.water_capacity} litres of water are being poured in. Wait...', end='\r')
        time.sleep(5)
        print('Congratulations! Your bathtub has been filled up. You can take your bath now. The water is clean.')
        self.status = "filled"
        return "Filled up"
    
    def fill_up_to_a_certain_level(self, level: int):
        try:
            int(level)
        except ValueError:
            print('You have to pass an integer for filling up the bathtub to a certain level! Try again...')
            sys.exit()
        if level <= 10 and level >= 1:
            for i in range(1, level):
                print()
                print(f'Wait... Filling up the water to level {level}. Water is on level {i}')
                time.sleep(1)
            print(f'Water has been filled up to your desired level: {level}')
            self.status = f"filled to level {level}"
            return "filled to a certain level"
        else:
            print('Bathtub has a maximum of 10 levels to be filled up to! Use a number between 1 and 10. Try again...')
            sys.exit()
            
    # Empty bathub
    def empty(self):
        print('\nEmptying your bathtub. Wait...', end='\r')
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