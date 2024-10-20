import pygame
import math
from entity import Entity

class Obstacle(Entity):
    
    def __init__(self, x, y, width, height, color):
        super().__init__(0, x, y, width, height, color)  
        
    
    def update_state(self, entities):
        self.current_state = 1
      
    #STATES
    def spawn_state(self):
        print(f"A Trash appeared at x {self.x} and y {self.y}")
        
    def idle_state(self):
        print("Trash idle state...")
        
    def dead_state(self):
        self.isCollected = True
        print("Trash has been picked up")
        
        
    