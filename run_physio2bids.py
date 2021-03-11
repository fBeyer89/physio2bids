
import sys
sys.path.append("/data/u_fbeyer_software/physio2bids")
python physio2bids -d "/data/p_life_raw/patients/LI0300371X/LI0300371X_20201125_080132.VER1/DICOMDIR" \
       -p "/data/p_life_raw/patients/LI0300371X/LI0300371X_20201125_080132.VER1/PHYS_LI0300371X/LI0300371X" \
       -o "/data/gh_gr_agingandobesity_share/life_shared/Analysis/Data_Organization/lifebids/physio2bids/" \
       -l "/data/gh_gr_agingandobesity_share/life_shared/Analysis/Data_Organization/lifebids/physio2bids/log"