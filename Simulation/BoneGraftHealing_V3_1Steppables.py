from cc3d.cpp.PlayerPython import * 
from cc3d import CompuCellSetup
from cc3d.core.PySteppables import *
import numpy as np, random, math, os
from pathlib import Path

RUN_ID = int(os.getenv("CC3D_RUN_ID", "1"))
random.seed(RUN_ID)
np.random.seed(RUN_ID)

# ____________________________________________________________________________________________________________________________________

# Defining Biomaterial Factors
#________________________________________________________________________________________________________________________________________________
biomaterials = {
    "Autograft"                                 : dict(P=0.85, RR=0.03, OSC=2.2, IFI=0.05, ALP_SR=2.0, init_OB=340, init_MSC=600),
    "Sorrento"                                  : dict(P_macro = 0.70, P_CaP = 0.30, RR = 0.032, OSC = 1.9, IFI=0.28, ALP_SR=2.5, init_OB=360, init_MSC=360),
    "Vitoss"                                    : dict(P_macro = 0.35, P_CaP = 0.70, RR = 0.075, OSC = 0.6, IFI=0.75, ALP_SR=1.6, init_OB=280, init_MSC=280),
    "Empty"                                     : dict(P=1.00, RR=0.00, OSC=0.1, IFI=0.10, ALP_SR=0.6, init_OB=250, init_MSC=250) 
    }

GRAFT_CHOICE            = os.getenv('BONE_GRAFT', 'Sorrento')
mat_par                 = biomaterials[GRAFT_CHOICE]

# Proprietary Steppables logic not included in this repo
