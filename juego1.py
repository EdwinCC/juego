#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
import numpy as np
from pygame.locals import *
 
# Constantes
WIDTH = 1600
HEIGHT = 900

posicionx=200
posiciony=500

speedsalto=[0.0, 0.5]
speedshurikens=[-0.7, 0.0]
 
# Clases
# ---------------------------------------------------------------------

#class decorador(pygame.sprite.Sprite):

	#def __init__(self):
	#	pygame.sprite.Sprite.__init__(self)

	#def actualizar(self,time)


class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("./imagenes/dinoruto.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = posicionx
        self.rect.centery = posiciony
        self.speed = [0.0, 0.0]
    def actualizar(self,time):
	#self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        #if self.rect.left <= 0 or self.rect.right >= WIDTH:
        #    self.speed[0] = -self.speed[0]
        #    self.rect.centerx += self.speed[0] * time
        #if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
	if self.rect.top >= HEIGHT-posiciony:
            #self.speed[1] = -self.speed[1]
            #self.rect.centery += self.speed[1] * time
	    self.speed[1]=0.0
	if self.rect.top <= 0.0:
	    #self.speed[1]=0.0
	    self.speed[1] = speedsalto[1]
            self.rect.centery += self.speed[1] * time

    def mover(self, time, keys):
        #self.rect.centerx += self.speed[0] * time
        #self.rect.centery += self.speed[1] * time
        #if self.rect.left <= 0 or self.rect.right >= WIDTH:
        #    self.speed[0] = -self.speed[0]
        #    self.rect.centerx += self.speed[0] * time
        #if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
        #    self.speed[1] = -self.speed[1]
        #    self.rect.centery += self.speed[1] * time
	#if keys[K_SPACE]:
	self.speed=[0.0, -0.5]
	self.rect.centery += self.speed[1]*time

class Shurikens(pygame.sprite.Sprite):
	def __init__(self,pos):
        	pygame.sprite.Sprite.__init__(self)
	        self.image = load_image("./imagenes/shurikens.png", True)
	        self.rect = self.image.get_rect()
	        self.rect.centerx = WIDTH
	        self.rect.centery = pos
	        self.speed = speedshurikens
    	def actualizar(self,time,bola):
	        self.rect.centerx += self.speed[0] * time
		#if self.rect.top >= HEIGHT-posiciony:
		#    self.speed[1]=0.0
		if self.rect.x <= 0:
			self.reingresar(time)
		    #self.speed[1] = speedsalto[1]
	            #self.rect.centery += self.speed[1] * time
			print("shuriken salio")
		if pygame.sprite.collide_rect(self,bola):
			print("colision")
			sys.exit(0)
	def reingresar(self,time):
		rnd=np.random.uniform(100,HEIGHT,1)
		self.rect.centerx=WIDTH
		self.rect.centery=rnd
		self.speed=speedshurikens
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dinoruto running")
 
    background_image = load_image('./imagenes/fondo.png')
    bola = Bola()
    shurikens=Shurikens(posiciony)
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
	keys=pygame.key.get_pressed()
        
	if keys[K_SPACE]:
		#print("apreto espacio")
        	bola.mover(time,keys)
	
	for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
	bola.actualizar(time)
	shurikens.actualizar(time,bola)
	
	#shurikens.reingresar(time)


	screen.blit(background_image, (0, 0))
        screen.blit(bola.image, bola.rect)
	screen.blit(shurikens.image,shurikens.rect)
        pygame.display.flip()
	#pygame.display.update()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
