import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),(self.position),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        velocity = self.velocity 
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else :
            random_angle = random.uniform(20,50)
            new_Ast1= Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_Ast1.velocity = 1.2* velocity.rotate(random_angle)
            new_Ast2= Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_Ast2.velocity = 1.2 *velocity.rotate(-random_angle)
        self.kill()



        
