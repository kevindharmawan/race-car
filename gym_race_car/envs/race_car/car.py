import pygame

CAR_IMAGE_SIZE = (100, 100)

class Car():
    def __init__(self, car_file, map_file, position):
        self.map = pygame.image.load(map_file)
        self.image = pygame.transform.scale(pygame.image.load(car_file), CAR_IMAGE_SIZE)
        self.rotated_image = self.image
        self.position = position
        self.angle = 0
        self.velocity = 0
        self.curr_checkpoint = 0
        self.curr_distance = 0
        self.total_distance = 0
        self.time = 0
        self.radars = []

    def update(self):
        pass

    def update_radars(self):
        pass

    def update_collision(self):
        pass

    def calculate_velocity(self):
        pass

    def calculate_radar_point(self, degree):
        pass

    def draw(self):
        pass

    def draw_radars(self):
        pass
