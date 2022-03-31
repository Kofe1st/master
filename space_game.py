from time import time
import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
import time
from scores import Scores


def run():

        pygame.init()
        screen = pygame.display.set_mode((700, 800))
        pygame.display.set_caption("Битва с пришельцами ")
      
        bg_color = (255, 255, 255)
        gun = Gun(screen)
        bullets = Group()
        inos = Group()
        controls.create_army(screen, inos)
        stats = Stats()
        sc = Scores(screen, stats)


        while True:
            controls.events(screen, gun, bullets)
            if stats.run_game:
                gun.update_gun()
                controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
                controls.update_bullets(screen, stats, sc, inos, bullets)
                controls.update_inos(stats, screen,sc, gun, inos, bullets) 
            
            this_round_begin = int(round(time.time() * 1000))
            this_round_end = int(round(time.time() * 1000))
            if this_round_end - this_round_begin <= 4:
                time.sleep(0.001 * (4 - (this_round_end - this_round_begin)))
           

 
run()
            





            