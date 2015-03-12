import sys
import pygame
import os

working_dir = os.path.dirname(os.path.realpath(__file__))

HEIGHT = 800
WIDTH = 600
IMG_PATH = os.path.join(working_dir, "assets/leftshark.png")

def main():

  pygame.init()
  background_color = (0,0,0)
  screen = pygame.display.set_mode((WIDTH, HEIGHT))

  shark = pygame.image.load(IMG_PATH)
  texr = shark.get_rect()

  screen.fill(background_color)
  screen.blit(shark, ((WIDTH/2) - (shark.get_width()/2),(HEIGHT/2) - (shark.get_height()/2)))
  pygame.display.flip()

  pygame.time.delay(2000)

  sys.exit()

  return 0

if __name__ == "__main__":
    main()
