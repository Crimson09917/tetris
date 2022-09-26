
import pygame

cellWidth = 40
cellHeight = 40


class Border:
    def __init__(self, window: object, topLeft: int):
        self.window = window
        self.bordersArray = []
        for x in range(0, 10):
            for y in range(0, 20):
                self.bordersArray.append([topLeft + x * cellWidth, topLeft + y * cellHeight])

        self.lWall = topLeft
        self.rWall = topLeft + cellWidth * 10
        self.tWall = topLeft
        self.bWall = topLeft + cellHeight * 20

    def display(self):
        for i in self.bordersArray:
            pygame.draw.rect(self.window, (100, 100, 100), (i[0], i[1], cellWidth, cellHeight), 2)