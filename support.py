# generates file names in dir tree by walking the tree either top-down or bottom-up. For each dir it yields a 3-tuple (dirpath, dirnames, filenames).
# this helps in making the animations for everything in the game
from os import walk
import pygame

def import_folder(path):
    surface_list = []
    
    for _,__,img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list
