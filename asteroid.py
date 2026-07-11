import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            newVel = random.uniform(20, 50)
            newRad = self.radius - ASTEROID_MIN_RADIUS

            new1 = Asteroid(self.position[0], self.position[1], newRad)
            new2 = Asteroid(self.position[0], self.position[1], newRad)
            new1.velocity = self.velocity.rotate(newVel)
            new2.velocity = self.velocity.rotate(newVel * -1)


