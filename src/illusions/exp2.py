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
circles = ((0, 1), (sqrt(3)/2, -0.5), (-sqrt(3)/2, -0.5))
circle_scale = 0.3
circle_radius = 6
n_dots = 300
sphere_radius = 0.5
dot_radius = 2
rotation_speed = pi/3
bg_color = (0, 0, 0)
sph_color = (0, 0, 255)
circle_color = (255, 255, 0)
window_center = (window_size[0]/2.0, window_size[1]/2.0)
window_scale = min(window_size)/2.0

def coord(real):
    """takes real coordinates, returns pixel coordinates"""
    return (int(round(real[0]*window_scale + window_center[0])),\
            int(round(real[1]*window_scale + window_center[1])))

def random_point():
    """returns random point on surface of sphere"""
    theta = acos(random.uniform(-1.0, +1.0))
    phi = random.uniform(0.0, 2*pi)
    return (sphere_radius*sin(theta)*cos(phi),\
            sphere_radius*sin(theta)*sin(phi),\
            sphere_radius*cos(theta))

g_cos = 1
g_sin = 0
def set_rotation(angle):
    """sets up rotation"""
    global g_cos, g_sin
    g_cos = cos(angle)
    g_sin = sin(angle)
    
def rotate_y(point):
    """rotates a 3D point about the Y-axis by given angle set by set_rotation()"""
    return (g_cos*point[0] + g_sin*point[2],\
            point[1],\
            -g_sin*point[1] + g_cos*point[2])

def exp2(full_screen, experiment_env, surf, exp_type):
    # initialize random points on sphere
    dots = []
    start_key_down = {}
    start_key_down['K_1'] = 0
    start_key_down['K_2'] = 0
    start_key_down['K_3'] = 0
    initial_id_answer = experiment_env["id_answer"]
    for i in range(n_dots):
        dots.append(random_point())
    
    try:
    
        t0 = pygame.time.get_ticks()
        t = 0
        frames = 0
        done = False
        while (not done) and t < float(experiment_env["exp_duration"]):
            
            done, start_key_down = exp_events_handle(experiment_env, exp_type, start_key_down, t0)            
    
            surf.fill(bg_color)
            t = (pygame.time.get_ticks() - t0)/1000.0
            set_rotation(rotation_speed*t)
            for r3 in dots:
                rot = rotate_y(r3)
                r2 = rot[:-1]
                pygame.draw.circle(surf, sph_color, coord(r2), dot_radius, 0)
            for c0 in circles:
                c = (circle_scale*c0[0], circle_scale*c0[1])
                pygame.draw.circle(surf, circle_color, coord(c), circle_radius, 0)
            pygame.display.flip()
            frames += 1
            
        ## Ending experiment
        experiment_end(experiment_env, exp_type, initial_id_answer)
            
    finally:
        t = (pygame.time.get_ticks() - t0)/1000.0
        print "quit"
