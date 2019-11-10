import random
import pygame
from War_sprites import *

pygame.init()


class PlaneWar(object):

    def __init__(self):

        # create screen
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create clock
        self.clock = pygame.time.Clock()
        # create sprites
        self.__create_sprites()
        # set timer
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 1000)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(is_alt=True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = HeroPlane()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # refresh frequency
            self.clock.tick(REFRESH)

            self.__event_monitor()

            self.__update_sprites()

            self.__check_collide()

            pygame.display.update()

    def __event_monitor(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneWar.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # create enemy sprite
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("go right")

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # bullets collide with enemy
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # hero collide with enemy
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, False)
        if len(enemies) > 0:
            PlaneWar.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneWar()
    game.start_game()
