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
from utils import *



# Parameters definition
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
g_cos = 1
g_sin = 0

window_size = (1024, 768)
window_center = (window_size[0]/2.0, window_size[1]/2.0)
stimulus_center = [] # Tuples are immutable, so we create a list instead
stimulus_center.append(window_size[0] / 2.0)
stimulus_center.append(window_size[1] / 2.0)
window_scale = min(window_size) / 2.0


# Takes real coordinates, returns pixel coordinates
def coord(real):
    global window_scale, window_center
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
def exp1(full_screen, experiment_env, surf, shift_type, luminosity = 1, rotation_speed_factor = 1, circle_radius_factor = 1):
    
    try: 
        ## Initialization 
        frames, show = 0, True
        shift = 0
        start_key_down = {}
        start_key_down['K_1'] = 0
        start_key_down['K_2'] = 0
        start_key_down['K_3'] = 0
        direction = 'right'
        initial_id_answer = experiment_env["id_answer"]
        shift_type_param = shift_type + '-' + str(luminosity) + '-' + str(rotation_speed_factor) + '-' + str(circle_radius_factor)       
        t0 = pygame.time.get_ticks()
        t = 0
        done = False
        pygame.mouse.set_visible(experiment_env["mouse_visible"])
        
        
        ## Main loop for stimulus display
        while (not done) and t < float(experiment_env["exp_duration"]):

            # To make the circle disappear during MIB
            pressed_keys = pygame.key.get_pressed()
            mib_duration = pygame.time.get_ticks() - t0 - start_key_down['K_1']
        
            # Handle events
            done, start_key_down = exp_events_handle(experiment_env, shift_type_param, start_key_down, t0)  
               
            # Draw grid
            surf.fill(bg_color)
            t = (pygame.time.get_ticks() - t0) / 1000.0
            set_rotation(rotation_speed * t * rotation_speed_factor)
            for i in range(-n_grid, +n_grid + 1):
                for j in range(-n_grid, +n_grid + 1):
                    center = (grid_spacing * i, grid_spacing * j)
                    fr = rotate((center[0] - grid_length, center[1]))
                    to = rotate((center[0] + grid_length, center[1]))
                    pygame.draw.line(surf, grid_color, coord(fr), coord(to), grid_width)
                    fr = rotate((center[0], center[1] - grid_length))
                    to = rotate((center[0], center[1] + grid_length))
                    pygame.draw.line(surf, grid_color, coord(fr), coord(to), grid_width)
                    
            # Draw circle(s)
            for circ in circles:
                c1 = (circle_scale * circ[0] + shift / 1000.0 - 0.35, circle_scale * circ[1])
                c2 = (circle_scale * circ[0] + shift / 1000.0 + 0.35, circle_scale * circ[1])
                c3 = (0, -circle_scale * circ[1])
                print mib_duration
                if show and not (experiment_env["disappearing_point"] and (0 < mib_duration - experiment_env["disappearing_point_start"] < experiment_env["disappearing_point_duration"]) and (pressed_keys[K_1] or pressed_keys[K_KP1])):
                    col = (150*luminosity, 150*luminosity, 0)
                    pygame.draw.circle(surf, col, coord(c1), int(circle_radius*circle_radius_factor), 0)
                    if shift_type == 'fixed' and experiment_env["max_number_of_points"] == 3:
                        pygame.draw.circle(surf, col, coord(c2), int(circle_radius*circle_radius_factor), 0)
                        pygame.draw.circle(surf, col, coord(c3), int(circle_radius*circle_radius_factor), 0)
                else:
                    step = 150 / disapp_frames
                    lev = max(0, 150 - frames * step)
                    col = (lev, lev, 0)
                    if lev > 0:
                        pygame.draw.circle(surf, col, coord(c1), circle_radius, 0)
                        
            if shift_type == 'same_dir':
                pygame.draw.circle(surf, grid_color, coord((0 + shift/1000.0, 0)), fix_radius)
            else:
                pygame.draw.circle(surf, grid_color, coord((0 - shift/1000.0, 0)), fix_radius)
            pygame.display.flip()
            frames += 1
            
            # Shift
            speed = 2 # The biggest, the slowest. Must be an integer    
            right_max_shift = 100
            left_max_shift = -100
            if shift_type <> 'fixed' and frames % speed == 0:
                # Compute shift
                if direction == 'right':
                    shift += 1
                else:
                    shift += -1
                # Checks bounds
                if shift > right_max_shift:
                    direction = 'left'
                if shift <= left_max_shift:
                    direction = 'right'     
                    
                    
        ## Ending experiment
        experiment_end(experiment_env, shift_type_param, initial_id_answer, surf, start_key_down, t0)
            
    finally: 
        print "quit"