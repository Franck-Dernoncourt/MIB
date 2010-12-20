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

import sys, random, pygame
from pygame.locals import *
from math import *

# Parameters definition
window_size = (1024, 768)
circles = ((0, 1),)
circle_scale = 0.3
circle_radius = 8
n_grid = 3
grid_spacing = 0.2
grid_length = 0.05
grid_width = 2
fix_radius = 8
rotation_speed = pi / 2
bg_color = (0, 0, 0)
grid_color = (100, 100, 255)
circle_color = (255, 255, 0)
disapp_frames = 1
window_center = (window_size[0] / 2.0, window_size[1] / 2.0)
window_scale = min(window_size) / 2.0
g_cos = 1
g_sin = 0

# Takes real coordinates, returns pixel coordinates
def coord(real):
    return (int(round(real[0] * window_scale + window_center[0])), \
            int(round(-real[1] * window_scale + window_center[1])))

# Sets up rotation
def set_rotation(angle):
    global g_cos, g_sin
    g_cos, g_sin = cos(angle), sin(angle)
    
# Rotates a 3D point about the Z-axis by given angle set by set_rotation()
def rotate(point):
    return (g_cos * point[0] + g_sin * point[1], -g_sin * point[0] + g_cos * point[1])


# Main function
def exp1(full_screen, resultFile):
    frames, show = 0, True
    try:
        pygame.init()
        
        # Graphics initializations
        if full_screen:
            surf = pygame.display.set_mode(window_size, HWSURFACE | FULLSCREEN | DOUBLEBUF)
        else:
            surf = pygame.display.set_mode(window_size)
    
        # Stimulus display
        t0 = pygame.time.get_ticks()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif event.type == MOUSEBUTTONDOWN:
                    s, show = 0, False
                elif event.type == MOUSEBUTTONUP: 
                    frames, show = 0, True
    
            surf.fill(bg_color)
            t = (pygame.time.get_ticks() - t0) / 1000.0
            set_rotation(rotation_speed * t)
            for i in range(-n_grid, +n_grid + 1):
                for j in range(-n_grid, +n_grid + 1):
                    center = (grid_spacing * i, grid_spacing * j)
                    fr = rotate((center[0] - grid_length, center[1]))
                    to = rotate((center[0] + grid_length, center[1]))
                    pygame.draw.line(surf, grid_color, coord(fr), coord(to), grid_width)
                    fr = rotate((center[0], center[1] - grid_length))
                    to = rotate((center[0], center[1] + grid_length))
                    pygame.draw.line(surf, grid_color, coord(fr), coord(to), grid_width)
            for circ in circles:
                c = (circle_scale * circ[0], circle_scale * circ[1])
                if show:
                    col = (150, 150, 0)
                    pygame.draw.circle(surf, col, coord(c), circle_radius, 0)
                else:
                    step = 150 / disapp_frames
                    lev = max(0, 150 - frames * step)
                    col = (lev, lev, 0)
                    if lev > 0:
                        pygame.draw.circle(surf, col, coord(c), circle_radius, 0)
                        
            pygame.draw.circle(surf, grid_color, coord((0, 0)), fix_radius)
            pygame.display.flip()
            frames += 1
            
            
    finally: 
        pygame.quit()

