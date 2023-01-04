import pygame as pg
import sys 
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *



class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES) #Crear pantalla con res de settings
        self.clock = pg.time.Clock() #Reloj?
        self.delta_time = 1 #Delta time
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game() #Instancia de nuevo juego

    def new_game(self):
        self.map = Map(self) #Crear nuevo mapa en nuevo juego
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        #pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip() #Actualizar pantalla
        self.delta_time = self.clock.tick(FPS) #Reloj con fps delta time
        pg.display.set_caption(f'{self.clock.get_fps():.1f}') #Titulo con los fps

    def draw(self):
        #self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        self.map.draw()
        self.player.draw()

    def check_events(self):
        """Salir del juego con escape o cerrando"""
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()


