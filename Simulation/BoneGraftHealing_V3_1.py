from cc3d import CompuCellSetup

from BoneGraftHealing_V3_1Steppables import *

# --‑‑‑ Steppable registration ‑‑‑--
CompuCellSetup.register_steppable(GeometryInitialiserSteppable(frequency=1))          # once at start
CompuCellSetup.register_steppable(CellAgeUpdateAndOxygenSteppable(frequency=1))       # per‑MCS field update
CompuCellSetup.register_steppable(ICSecretionSteppable(frequency=4))                  # ≈ 6 min – keep fine

# ==== 3‑hour cadence (120 MCS) ======================================
CompuCellSetup.register_steppable(OsteoblastALPSecretionSteppable(frequency=40))
CompuCellSetup.register_steppable(MacrophageICSteppable(frequency=120))
CompuCellSetup.register_steppable(MacToOCLSteppable(frequency=120))
CompuCellSetup.register_steppable(MSCProlifAndDifSteppable(frequency=120))
CompuCellSetup.register_steppable(ResorptionSteppable(frequency=120))
CompuCellSetup.register_steppable(NewBoneFormationSteppable(frequency=120))
CompuCellSetup.register_steppable(BoneMarrowBleedingAdaptiveSteppable(frequency=120))
CompuCellSetup.register_steppable(FibrousRemodelingSteppable(frequency=120))
CompuCellSetup.register_steppable(MacrophageProliferationSteppable(frequency=120))

# ==== 6‑hour cadence (240 MCS) ======================================
CompuCellSetup.register_steppable(CollagenInflamDecaySteppable(frequency=240))
CompuCellSetup.register_steppable(MSCRecruitmentSteppable(frequency=2000))

# Live monitor – every simulated day
CompuCellSetup.register_steppable(AnalysisOutputSteppable(frequency=1000))

#Experimental
CompuCellSetup.register_steppable(OsteoclastHomeostasisSteppable(frequency=1000))  # ~1 simulated day
CompuCellSetup.register_steppable(MarrowOxygenationSteppable(frequency=240))       # every ~6 h



#  Run 
CompuCellSetup.run()

