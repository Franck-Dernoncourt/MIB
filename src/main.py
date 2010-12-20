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

import os

try:
    # Ask the subject's name
    subject_name = raw_input("Nom du sujet (lettres seulement, pas d'espaces): ")
    
    # Create a new result file and write it to disk. We could have also append.
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
    
    # Write result file's headers
    result_file.write('SUBJ' + experiment_env["separator"] + 'EXP#' + experiment_env["separator"] +'ANSWER' + experiment_env["separator"] + 'TIMESTAMP' + '\n')
        
    # Call experiments
    full_screen = False    
    exp1.exp1(full_screen, experiment_env)
    exp2.exp2(full_screen, experiment_env)
    
finally:
    a = 1
