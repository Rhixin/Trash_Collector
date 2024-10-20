import pygame
import math
from entity import Entity

class Trash(Entity):
    
    def __init__(self, x, y, width, height, color):
        super().__init__(0, x, y, width, height, color)  
        self.isCollected = False
        
    def update_state(self, entities):
        
        if self.isCollected == False:
            self.current_state = 1
        else:
            self.current_state = 2
            
        if self.current_state == 1:
            self.idle_state()
        else:
            self.dead_state()

        
    #STATES
    def spawn_state(self):
        print(f"A Trash appeared at x {self.x} and y {self.y}")
        
    def idle_state(self):
        print("Trash idle state...")
        
    def dead_state(self):
        self.isCollected = True
        print("Trash has been picked up")
        
        
    