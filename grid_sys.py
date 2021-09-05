import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Box class for each pixel
class Box:
    def __init__(self, x_pos, y_pos, color):

        # Top left pos
        self.x = x_pos
        self.y = y_pos

        # Same width and height
        self.side = 12

        # Create a rectangle for the Box
        self.rect = pygame.Rect((self.x, self.y), (self.side, self.side))

        # Color can change
        self.color = color

    def draw_border(self, screen):

        # Draw all lines around the box edge to edge
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + self.side, self.y))
        pygame.draw.line(
            screen,
            BLACK,
            (self.x + self.side, self.y),
            (self.x + self.side, self.y + self.side),
        )
        pygame.draw.line(
            screen,
            BLACK,
            (self.x + self.side, self.y + self.side),
            (self.x, self.y + self.side),
        )
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.side), (self.x, self.y))


# Grid to sort all the boxes together
class Grid:
    def __init__(self):

        # Grid list to hold all the boxes to make the grid
        self.boxes = []

        # box size
        self.side = 12

        for y in range(0, 600, self.side):
            for x in range(0, 600, self.side):

                # Create a Box
                box = Box(x, y, WHITE)  # Default white colour
                self.boxes.append(box)

    # Draw all the boxes and lines inbetween them
    def draw(self, screen):

        for box in self.boxes:  # Draw all the boxes in the grid
            pygame.draw.rect(screen, box.color, box.rect)
            box.draw_border(screen)
