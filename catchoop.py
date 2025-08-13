import pygame
import random
import sys

class CatchGame:
    def __init__(self):
        self.runnng = True
        self.display_surf= None
        self.size = self.weight, self.height = 600, 600

    def onInit(self):
        pygame.init()
        self.display_surf= pygame.display.set_mode(self.size,pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
        pygame.display.set_caption("Welcome to Falling Blocks")

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
            sys.exit()
    def onLoop(self):
        pass

    def onRender(self):
        pass
    def onCleanup(self):
        pygame.quit()
        sys.exit()
    
    def onExecute(self):
        if self.onInit() == False:
            self.running = False
        while self.running:
            for event in pygame.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
        self.onCleanup()

    def run(self):
        pass

if __name__=="__main__":
    thisGame = CatchGame()
    thisGame.onExecute()