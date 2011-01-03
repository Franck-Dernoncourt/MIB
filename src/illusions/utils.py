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


# Handle events during experience
def exp_events_handle(experiment_env, exp_type, start_key_down, t0):
    done = False   
    for event in pygame.event.get():
        if event.type in (QUIT, MOUSEBUTTONDOWN):
            done = True
        elif (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_1):
            # Write result file's headers    
            timestamp = pygame.time.get_ticks() - t0
            start_key_down['K_1'] = timestamp
            #experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + '1' + experiment_env["separator"] + str(timestamp) + '\n')
        elif (event.type == KEYUP and event.key == K_1):
            # Write result file's headers
            duration = pygame.time.get_ticks() - t0 - start_key_down['K_1']
            if duration > 0 and start_key_down['K_1'] > 0:
                experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + exp_type + experiment_env["separator"] + '1' + experiment_env["separator"] + str(start_key_down['K_1']) + experiment_env["separator"] + str(duration) + '\n')
                experiment_env["id_answer"] += 1
        
        elif (event.type == KEYDOWN and event.key == K_2):
            # Write result file's headers    
            timestamp = pygame.time.get_ticks() - t0
            start_key_down['K_2'] = timestamp
            #experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + '2' + experiment_env["separator"] + str(timestamp) + '\n')
        elif (event.type == KEYUP and event.key == K_2):
            # Write result file's headers
            duration = pygame.time.get_ticks() - t0 - start_key_down['K_2']
            if duration > 0 and start_key_down['K_2'] > 0:
                experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + exp_type + experiment_env["separator"] + '2' + experiment_env["separator"] + str(start_key_down['K_2']) + experiment_env["separator"] + str(duration) + '\n')
                experiment_env["id_answer"] += 1
                
        elif (event.type == KEYDOWN and event.key == K_3):
            # Write result file's headers    
            timestamp = pygame.time.get_ticks() - t0
            start_key_down['K_3'] = timestamp
            #experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + '3' + experiment_env["separator"] + str(timestamp) + '\n')
        elif (event.type == KEYUP and event.key == K_3):
            # Write result file's headers
            duration = pygame.time.get_ticks() - t0 - start_key_down['K_3']
            if duration > 0 and start_key_down['K_3'] > 0:
                experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + exp_type + experiment_env["separator"] + '3' + experiment_env["separator"] + str(start_key_down['K_3']) + experiment_env["separator"] + str(duration) + '\n')
                experiment_env["id_answer"] += 1
             
    return done, start_key_down



# Ending experiment
def experiment_end(experiment_env, exp_type, initial_id_answer, surf):
    # Emptying event stack
    for event in pygame.event.get():
        pass
                
    # Adding a -1 line is no MIB was experienced
    if initial_id_answer == experiment_env["id_answer"]:
        experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + exp_type + experiment_env["separator"] + '-1' + experiment_env["separator"] + '-1' + experiment_env["separator"] + '-1' + '\n')
        experiment_env["id_answer"] += 1
        
    # Display black screen
    surf.fill((0, 0, 0))
    pygame.display.flip()
    pygame.time.delay(2000)
         