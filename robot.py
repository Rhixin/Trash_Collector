from entity import Entity
import pygame
import math

class Robot(Entity):
    
    def __init__(self, speed, x, y, width, height, color):
        super().__init__(speed, x, y, width, height, color)  
        self.collected_trash = 0
        self.move_timer = 0
        self.idle_state_timer = 0
        
        
    def render(self, screen):
        super().render(screen)
    
        font = pygame.font.SysFont('Arial', 12)  
        text_surface = font.render(f'{self.collected_trash}', True, "black") 
        
        text_x = self.x + 6
        text_y = self.y - 15
    
        screen.blit(text_surface, (text_x, text_y))
        
    def update_state(self, trash_list,obstacle_list,trashbin, dt):
        nearest_trash = self.find_nearest_entity(trash_list)
        nearest_obstacle = self.find_nearest_entity(obstacle_list)
        
        trashbin_collided = self.detect_collison(trashbin)
        obstacle_collided = self.detect_collison(nearest_obstacle)
        
        if obstacle_collided:
            self.collected_trash = 0
            self.current_state = 1
            
        if nearest_trash:
            trash_collided = self.detect_collison(nearest_trash)
            
        
            if trash_collided:
                trash_collided.isCollected = True
                self.collected_trash += 1
        
            if self.collected_trash < 2:
                self.current_state = 2
            elif self.collected_trash == 2:
                self.current_state = 3
                
                
        if trashbin_collided and self.collected_trash >= 2:
            print("trash throw")
            trashbin.trash_count += self.collected_trash
            self.collected_trash = 0
            self.x = 140
            self.y = 100
            self.current_state = 1
            
        
        if self.current_state == 0:
            self.spawn_state()
        elif self.current_state == 1:
            self.idle_state()
        elif self.current_state == 2:
            self.finding_trash(trash_list, dt)
        elif self.current_state == 3:
            self.throw_trash(trashbin, dt)
        
    #STATES
    
    #0
    def spawn_state(self):
        print("Robot just spawned")
        
    #1
    def idle_state(self):
        print("Robot is in idle state")
        
    #2
    def finding_trash(self, trash_list, dt):
        print("Finding Trash")
        nearest_trash = self.find_nearest_entity(trash_list)
        
        if nearest_trash is not None:
            self.move_towards_entity(nearest_trash, dt)
            
    #2
    def finding_first_trash(self, trash_list, dt):
        print("Finding trash 1")
    
    #3
    def picked_first_trash(self, trash_list, dt):
        print("Picked trash 1")
        
    #4
    def finding_second_trash(self, trash_list, dt):
        print("Finding trash 1")
    
    #5
    def picked_second_trash(self, trash_list, dt):
        print("Picked trash 1")
        
    #6
    def throw_trash(self, bin,dt):
        self.move_towards_entity(bin,dt)
        
    #7
    def collision_with_obstacle(self):
        print("Collision with obstacle")
    
    #8
    def succesfull_throwing_trashes(self):
        print("Succesfull throwing")
    
    
    
    #HELPERS
    def move_towards_entity(self, entity, dt):
        self.move_timer += dt
        
        if self.move_timer >= self.speed:
            self.direction = pygame.Vector2(entity.x - self.centerx, entity.y - self.centery)
        
            if self.direction.length() > 0: 
                self.direction.normalize_ip()  
                
            new_position = self.center + (self.direction * self.speed)
            
            if 0 <= new_position.x < 1280 - self.width and 0 <= new_position.y < 720 - self.height:
                self.move_ip(self.direction * 10)  
                self.move_timer = 0
                
    def find_nearest_entity(self, list):
        nearest_entity = None
        nearest_distance = float('inf') 

        for entity in list:

            distance = math.sqrt((self.centerx - entity.x) ** 2 + (self.centery - entity.y) ** 2)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_entity = entity

        if nearest_entity is not None:
            return nearest_entity 
        else:
            return None
        
        
    def detect_collison(self, entity):
       
        distance = math.sqrt((self.centerx - entity.centerx) ** 2 + (self.centery - entity.centery) ** 2)
            
        if distance <= (entity.width):
            return entity
        return None