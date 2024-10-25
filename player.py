import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PROJECTILE_SPEED, PROJECTILE_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shooting_cooldown = 0.0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta
    
    def move(self, delta):
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * PLAYER_SPEED * delta
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PROJECTILE_SPEED

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, delta):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(delta * -1)
        if keys[pygame.K_d]:
            self.rotate(delta)
        
        if keys[pygame.K_w]:
            self.move(delta)
        
        if keys[pygame.K_SPACE] and self.shooting_cooldown <= 0.0:
            self.shoot()
            self.shooting_cooldown = PLAYER_SHOOT_COOLDOWN
        
        if self.shooting_cooldown > 0.0:
            self.shooting_cooldown -= delta

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PROJECTILE_RADIUS)
    
    def update(self, delta):
        self.position += self.velocity * delta

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
