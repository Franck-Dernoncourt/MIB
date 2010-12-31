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
from utils import *

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
grid_size = (1.4, 1.4)
grid_center = (0, 0)
grid_width_points = 50
grid_height_points = grid_width_points
grid_width = 1.4
grid_height = 1.4
grid_color = (0, 0, 255)
grid_lines_width = 2
grid_space_height = 0.002
square_center_color = (255, 0, 0)
square_center_location = (0, 0)
square_center_size = (10, 10)
distortion_center = (-0.3, 0.3)
distortion_radius = 0.09

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


# Compute distance between two 2D points
def distance(x, y):
    return sqrt((x[0]-y[0])*(x[0]-y[0])+(x[1]-y[1])*(x[1]-y[1]))


def exp4(full_screen, experiment_env, surf, distortion_type):
    try:
        t0 = pygame.time.get_ticks()
        frames = 0
        start_key_down = 0
        initial_id_answer = experiment_env["id_answer"]
        done = False
        t = 0
        while (not done) and t < float(experiment_env["exp_duration"]):
            
            done, start_key_down = exp_events_handle(experiment_env, distortion_type, start_key_down, t0)   
           
            surf.fill(bg_color)  
            t = (pygame.time.get_ticks() - t0)/2000.0
            set_rotation(rotation_speed * t)
            
            ## Blue grid + distortion          
            for col in range(grid_width_points):
                for row in range(grid_height_points):
                    fr = (float(col) / grid_width_points * grid_width - (float(grid_width)/2) , float(row) / grid_height_points * grid_height - (float(grid_height)/2) )
                    fr2 = rotate(fr)
                    to = (fr2[0], fr2[1] + 1 / float(grid_height_points * grid_height) - grid_space_height)
                    
                    ## Distortion type
                    grid_color = (0, 0, 255)   
                    grid_lines_width = 2    
                    if distance(to, distortion_center) < distortion_radius:      
                        ratio = float(distance(to, distortion_center))/distortion_radius
                        if distortion_type == 'luminance_distortion':
                            grid_color = (0, 0, ratio*255)
                        elif distortion_type == 'contraction_distortion':
                            to = (fr2[0], fr2[1] + (1 / float(grid_height_points * grid_height) - grid_space_height) * ratio / 2 )
                        elif distortion_type == 'expansion_distortion':
                            grid_lines_width = min([round(1/(ratio/2.5+0.02)), 7])
                            print grid_lines_width
                        elif distortion_type == 'curvature_distortion':
                            a = 1
                        elif distortion_type == 'color_distortion':
                            grid_color = ((255-ratio*255)/1.3, (255-ratio*255)/1.3, ratio*255)     
                    pygame.draw.line(surf, grid_color, coord(fr2), coord(to), grid_lines_width)
                        
            
            ## Display the center square
            pygame.draw.rect(surf, square_center_color, pygame.Rect(coord(square_center_location), square_center_size))
           
            ## Display everything 
            pygame.display.flip()
            frames += 1
            
        ## Ending experiment
        experiment_end(experiment_env, distortion_type, initial_id_answer)
    
    
    finally:
        print "quit"