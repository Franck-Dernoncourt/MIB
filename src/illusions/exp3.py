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

window_size = (1024, 768)
circles = ((0, 1), (sqrt(3)/2, -0.5), (-sqrt(3)/2, -0.5))
circle_scale = 0.3
circle_radius = 6
n_dots = 300
sphere_radius = 0.5
dot_radius = 2
rotation_speed = pi/2
bg_color = (0, 0, 0)
sph_color = (0, 0, 255)
circle_color = (255, 0, 0)
circle_center_color = (255, 255, 255)
window_center = (window_size[0]/2.0, window_size[1]/2.0)
window_scale = min(window_size)/2.0
grid_spacing = 0.2
grid_length = 0.05
grid_lines_width = 1
grid_color = circle_color


# Takes real coordinates, returns pixel coordinates
def coord(real):
    return (int(round(real[0] * window_scale + window_center[0])), \
            int(round(-real[1] * window_scale + window_center[1])))

# Sets up rotation
g_cos = []
g_sin = []
g_cos.append(1)
g_cos.append(1)
g_sin.append(0)
g_sin.append(0)
def set_rotation(angle, rotation_number = 0):
    global g_cos, g_sin
    g_cos[rotation_number], g_sin[rotation_number] = cos(angle), sin(angle)
    
# Rotates a 3D point about the Z-axis by given angle set by set_rotation()
def rotate(point, rotation_number = 0):
    return (g_cos[rotation_number] * point[0] + g_sin[rotation_number] * point[1], -g_sin[rotation_number] * point[0] + g_cos[rotation_number] * point[1])
    
    
def exp3(full_screen, experiment_env, surf, object_type):
    try:
        t0 = pygame.time.get_ticks()
        frames = 0
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
                    done = True 
                    
            surf.fill(bg_color)
            t = (pygame.time.get_ticks() - t0)/1000.0
            
            # Draw center point
            c = (0, 0)
            pygame.draw.circle(surf, circle_center_color, coord(c), circle_radius, 1)
            pygame.draw.circle(surf, circle_center_color, coord(c), circle_radius/2, 1)
            
            # Draw lines of points
            set_rotation(rotation_speed * t, 1)
            number_of_lines = 18            
            for line_number in range(number_of_lines):
                set_rotation(2*pi*line_number/number_of_lines)
                space_between_circles = 0.1
                count = 0
                c = (0, 0)
                while c[1] <= 3:
                    count += 1
                    c = (0, count * space_between_circles) 
                    pygame.draw.circle(surf, circle_color, coord(rotate(rotate(c), 1)), circle_radius, 0)            
            
            # Display grid
            set_rotation(0)
            
            if object_type == "object":
                grid_width = 0.05
                grid_height = 0.05
                grid_width_in_lines = 3
                grid_height_in_lines = 3
                grid_center = (-0.5, 0.5)
                
            else:
                grid_width = 2
                grid_height = 2
                grid_width_in_lines = 200
                grid_height_in_lines = 200
                grid_center = (-1, 1)
            
            grid_space_width = float(grid_width) / (grid_width_in_lines - 1)
            grid_space_height = float(grid_height) / (grid_height_in_lines - 1)
            for line_x in range(grid_width_in_lines):                
                fr = (grid_center[0] - grid_width / 2.0 + line_x * grid_space_width, grid_center[1] - grid_height / 2.0)
                to = (grid_center[0] - grid_width / 2.0 + line_x * grid_space_width, grid_center[1] + grid_height / 2.0)
                pygame.draw.line(surf, grid_color, coord(fr), coord(to), grid_lines_width)
            for line_y in range(grid_height_in_lines):
                fr = (grid_center[0] - grid_width / 2.0, grid_center[1] - grid_height / 2.0 + line_y * grid_space_height)
                to = (grid_center[0] + grid_width / 2.0, grid_center[1] - grid_height / 2.0 + line_y * grid_space_height)
                pygame.draw.line(surf, grid_color, coord(fr), coord(to), grid_lines_width)
            
            if object_type == "hole":
                hole_radius = 10
                hole_color = (0, 0, 0)
                hole_center = (-0.5, 0.5)
                pygame.draw.circle(surf, hole_color, coord(hole_center), hole_radius, 0)
                
            # Display everything
            pygame.display.flip()
            frames += 1
    
    
    finally:
        print "quit"