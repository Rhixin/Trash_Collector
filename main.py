# Example file showing a circle moving on screen
import pygame
from robot import Robot
from trash import Trash
from trashbin import Bin
from obstacle import Obstacle
import random

class Trash_Generator():
    def __init__(self):
        self.cooldown = 2
        self.cooldown_timer = 0
    
    def generate(self, dt):
        self.cooldown_timer += dt
        
        if self.cooldown_timer >= self.cooldown:
            x = random.randint(20, 1260)
            y = random.randint(20, 700)
            
            new_trash = Trash(x, y, 20,20, "black")
            
            self.cooldown_timer = 0
            
            return new_trash
        else:
            return None

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#List to hold all NPCs
trashbin = Bin(100, 100, 40, 40, "red")
trash_list = []
robot_list = []
obstacle_list = [Obstacle(500, 200, 50, 50, "green") , Obstacle(50, 30, 50, 50, "green"), Obstacle(300, 600, 50, 50, "green"), Obstacle(1100, 400, 50, 50, "green"), Obstacle(100, 350, 50, 50, "green"), Obstacle(700, 440, 50, 50, "green")]


trash_generator = Trash_Generator()
    


while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()  
                new_robot = Robot(0.1, mouse_x, mouse_y, 20, 20, "blue")
                robot_list.append(new_robot) 

    screen.fill("white")
    
    
    #obstacles logic
    for obstacle in obstacle_list:
        obstacle.render(screen)
        
    #trashbin logic
    trashbin.render(screen)
        
    #trashes logic
    new_trash = trash_generator.generate(dt)
    
    if new_trash is not None:
        #only 5 trash max sa map
        if len(trash_list) < 5:
            trash_list.append(new_trash)
            
    for trash in trash_list:
        trash.render(screen)
        trash.update_state(robot_list)
        
    trash_list = [trash for trash in trash_list if trash.isCollected == False]
        
        
    #robot logic
    for robot in robot_list:
        robot.render(screen)
        robot.update_state(trash_list,obstacle_list,trashbin,dt)
        
    
        

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
