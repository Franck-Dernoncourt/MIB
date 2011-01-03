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

from illusions import exp1
from illusions import exp2
from illusions import exp3
from illusions import exp4
from userinput import *

import os, pygame, random
from pygame.locals import *


try: 
    # Graphics initializations
    full_screen = True    
    window_size = (1024, 768)
    pygame.init()      
    if full_screen:
        surf = pygame.display.set_mode(window_size, HWSURFACE | FULLSCREEN | DOUBLEBUF)
    else:
        surf = pygame.display.set_mode(window_size)

    
    # Create a new result file and write it to disk. We could have also append.
    subject_name = ask(surf, "Name")
    i = 1
    while True:
        filename = subject_name + str(i)
        if not os.path.isfile(filename): break
        i += 1
    result_file = open(filename, "w")
    
    # Set the experiments' environment
    experiment_env = {}
    experiment_env["subject_name"] = subject_name
    experiment_env["experiment_number"] = 1
    experiment_env["result_file"] = result_file
    experiment_env["separator"] = ','
    experiment_env["variant"] = ''
    experiment_env["exp_duration"] = 30
    experiment_env["id_answer"] = 0
    
    # Write result file's headers
    result_file.write('IDANSWER' + experiment_env["separator"] + 'SUBJ' + experiment_env["separator"] + 'EXP#' + experiment_env["separator"] + 'TYPE' + experiment_env["separator"] + 'ANSWER' + experiment_env["separator"] + 'TIMESTAMP' + experiment_env["separator"] + 'DURATION' + '\n')
    
    
    # Call experiments
    exp_map = {'exp1' : exp1.exp1, 'exp2' : exp2.exp2, 'exp3' : exp3.exp3, 'exp4' : exp4.exp4}
    
    exp_arg_list = [('exp1', [full_screen, experiment_env, surf, "fixed", 1, 0.5, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1, 1, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1, 1.5, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1, 1, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1, 1, 2]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1, 1, 4]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 0.5, 1, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1, 1, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "fixed", 1.5, 1, 1]),
                    ('exp1', [full_screen, experiment_env, surf, "same_dir"]),
                    ('exp1', [full_screen, experiment_env, surf, "opp_dir"]),
                    ('exp2', [full_screen, experiment_env, surf, "normal"]),
                    ('exp3', [full_screen, experiment_env, surf, "object"]),
                    ('exp3', [full_screen, experiment_env, surf, "hole"]),
                    ('exp3', [full_screen, experiment_env, surf, "luminance_cycle"]),
                    ('exp3', [full_screen, experiment_env, surf, "luminance_control"]),
                    ('exp4', [full_screen, experiment_env, surf, "luminance_distortion"]),
                    ('exp4', [full_screen, experiment_env, surf, "contraction_distortion"]),
                    ('exp4', [full_screen, experiment_env, surf, "expansion_distortion"]),
                    ('exp4', [full_screen, experiment_env, surf, "color_distortion"])]
    
    random.shuffle(exp_arg_list)
    
    for exp_arg in exp_arg_list:
        experiment_env["experiment_number"] = int(exp_arg[0][3])
        exp_map[exp_arg[0]](*exp_arg[1])
    
    
finally:
    pygame.quit()
    #result_file.close()