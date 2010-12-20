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
    # demandons le nom du sujet ; noue l'écrirons dans le fichier de données
    subj = raw_input("nom du sujet (lettres seulement, pas d'espaces): ")
    
    # Create a new result file and write it to disk. We could have also append.
    i = 1
    while True:
        filename = subj + str(i)
        if not os.path.isfile(filename): break
        i += 1
    resultFile = open(filename, "w")
    
    # Call experiments
    full_screen = False
    exp1.exp1(full_screen, resultFile)
    exp2.exp2(full_screen, resultFile)
    
finally:
    a = 1
