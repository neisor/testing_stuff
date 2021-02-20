import time
class Bathtub():
    def __init__(self):
        self.status = "empty"
        print("What should the color of the bathtub be?:")
        self.color = input()
        print("What should the capacity of the bathtub be?:")
        self.water_capacity = int(input())
        print("What should the shape of the bathtub be?:")
        self.shape = input()
        
    
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
        return "Emptied"