import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
         # if the image has been loaded already return it
         # otherwise load it
        if image == None:
                canonicalized_path = os.path.join("_img", path)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
        
