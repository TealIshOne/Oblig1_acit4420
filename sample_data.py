
from provided_files.data_generator import generate_fitness_data as GFD
 
def resting():
    profile, obs = GFD(scenario="resting", seed=50)
    return profile, obs

def moderate_activity():
    profile, obs = GFD(scenario="moderate_activity", seed=111)
    return profile, obs

def high_acticity():
    profile, obs = GFD(scenario="high_activity", seed=222)
    return profile, obsS

def recovery():
    profile, obs= GFD(scenario="recovery", seed=333)
    return profile, obs

def poor_quality():
    profile, obs =GFD(scenario="poor_quality", seed=555)
    return profile, obs


### student testing ground ###
