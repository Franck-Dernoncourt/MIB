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



# Ending experiment
def experiment_end(experiment_env, exp_type, initial_id_answer):
    # Emptying event stack
    for event in pygame.event.get():
        pass
                
    # Adding a -1 line is no MIB was experienced
    if initial_id_answer == experiment_env["id_answer"]:
        experiment_env["result_file"].write(str(experiment_env["id_answer"]) + experiment_env["separator"] + experiment_env["subject_name"] + experiment_env["separator"] + str(experiment_env["experiment_number"]) + experiment_env["separator"] + exp_type + experiment_env["separator"] + '-1' + experiment_env["separator"] + '-1' + experiment_env["separator"] + '-1' + '\n')
        experiment_env["id_answer"] += 1
         