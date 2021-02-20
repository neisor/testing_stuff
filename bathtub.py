import time
class Bathtub():
    def __init__(self, color: str, water_capacity: int, shape: str):
        self.color = color
        self.water_capacity = water_capacity
        self.shape = shape
    
    def fill_up(self):
        print(f'Your bathtub is filling up. {self.water_capacity} liters of water are being poured in...', end='\r')
        time.sleep(5)
        print('Congratulations! Your bathtub has been filled up. You can take your bath now.')
        return "Filled up"