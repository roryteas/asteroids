from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        for i in range(0,2):
            angle = random.uniform(20,50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, radius)
            new_asteroid.velocity = self.velocity.rotate(angle)*1.2
