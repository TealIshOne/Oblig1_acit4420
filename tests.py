

#testing observations

from main import observations as obs
from sample_data import resting



profile, data=resting()

test1=obs(profile,data)
validated_prof, vlaidated_data=test1.observation_validation()