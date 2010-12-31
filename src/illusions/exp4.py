##############################################################################################################
# -*- coding: cp1252 -*-
# 
# Project MIB
# To:  Mark WEXLER <mark.wexler@gmail.com>
# Date: December 2010
#
# ----
# Franck DERNONCOURT <franck.dernoncourt@gmail.com>
# Xavier RAMPINO <xavier.rampino@mailhec.net>
# ----
# Python: 2.6.6 32bits
# Pygame: 1.9.1
#
##############################################################################################################


import random, pygame
from pygame.locals import *
from math import *

# Parameters definition
window_size = (1024, 768)
n_dots = 300
sphere_radius = 0.5
dot_radius = 2
rotation_speed = pi/2
bg_color = (0, 0, 0)
window_center = (window_size[0]/2.0, window_size[1]/2.0)
window_scale = min(window_size)/2.0

grid_spacing = 0.2
grid_size = (1, 1)
grid_center = (0, 0)
grid_width_points = 50
grid_height_points = grid_width_points
grid_width = 1.2
grid_height = 1.2
grid_color = (0, 0, 255)
grid_lines_width = 2
grid_space_height = 0.002
square_center_color = (255, 0, 0)
square_center_location = (0, 0)
square_center_size = (10, 10)

# Takes real coordinates, returns pixel coordinates
def coord(real):
    return (int(round(real[0] * window_scale + window_center[0])), \
            int(round(-real[1] * window_scale + window_center[1])))

# Sets up rotation
g_cos = []
g_sin = []
g_cos.append(1)
g_sin.append(0)
def set_rotation(angle, rotation_number = 0):
    global g_cos, g_sin
    g_cos[rotation_number], g_sin[rotation_number] = cos(angle), sin(angle)
    
    
# Rotates a 3D point about the Z-axis by given angle set by set_rotation()
def rotate(point, rotation_number = 0):
    return (g_cos[rotation_number] * point[0] + g_sin[rotation_number] * point[1], -g_sin[rotation_number] * point[0] + g_cos[rotation_number] * point[1])

    
def exp4(full_screen, experiment_env, surf, object_type):
    try:
        t0 = pygame.time.get_ticks()
        frames = 0
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
                    done = True 
                  
            surf.fill(bg_color)  
            t = (pygame.time.get_ticks() - t0)/2000.0
            set_rotation(rotation_speed * t)
            
            ## Blue grid            
            for col in range(grid_width_points):
                for row in range(grid_height_points):
                    fr = (float(col) / grid_width_points * grid_width - (float(grid_width)/2) , float(row) / grid_height_points * grid_height - (float(grid_height)/2) )
                    fr2 = rotate(fr)
                    #to = (fr[0] + g_cos[0] / grid_width_points * grid_width , fr[1] + g_sin[0] / grid_height_points * grid_height)
                    to = (fr2[0], fr2[1] + 1 / float(grid_height_points * grid_height) - grid_space_height)
                    pygame.draw.line(surf, grid_color, coord(fr2), coord(to), grid_lines_width)
            
            
            ## Distortion
            
            
            ## Display the center square
            pygame.draw.rect(surf, square_center_color, pygame.Rect(coord(square_center_location), square_center_size))
           
            ## Display everything 
            pygame.display.flip()
            frames += 1
    
    
    finally:
        print "quit"