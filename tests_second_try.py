

#testing observations

from main_second_try import Observations as obs
from main_second_try import Participant as part
from main_second_try import Session as ses
from main_second_try import Analyzer as ana
from sample_data import resting, moderate_activity ,high_activity, recovery, poor_quality


test_data_set= [{'timestamp': 0, 'heart_rate': 95, 'skin_response': 2.29, 'temperature': 33.23, 'activity_level': 0.53, 'signal_quality': 0.88}, {'timestamp': 1, 'heart_rate': 93, 'skin_response': 1.97, 'temperature': 33.19, 'activity_level': 0.4, 'signal_quality': 0.86}, {'timestamp': 2, 'heart_rate': 82, 'skin_response': 1.95, 'temperature': 33.17, 'activity_level': 0.4, 'signal_quality': 0.93}, {'timestamp': 3, 'heart_rate': 88, 'skin_response': 2.18, 'temperature': 33.17, 'activity_level': 0.39, 'signal_quality': 0.97}, {'timestamp': 4, 'heart_rate': 84, 'skin_response': 2.03, 'temperature': 33.33, 'activity_level': 0.51, 'signal_quality': 0.93}, {'timestamp': 5, 'heart_rate': 81, 'skin_response': 2.14, 'temperature': 33.32, 'activity_level': 0.45, 'signal_quality': 0.91}, {'timestamp': 6, 'heart_rate': 89, 'skin_response': 2.17, 'temperature': 33.34, 'activity_level': 0.6, 'signal_quality': 0.98}, {'timestamp': 7, 'heart_rate': 102, 'skin_response': 2.22, 'temperature': 33.37, 'activity_level': 0.41, 'signal_quality': 0.95}, {'timestamp': 8, 'heart_rate': 90, 'skin_response': 2.04, 'temperature': 33.11, 'activity_level': 0.48, 'signal_quality': 0.88}, {'timestamp': 9, 'heart_rate': 91, 'skin_response': 2.29, 'temperature': 33.2, 'activity_level': 0.52, 'signal_quality': 0.98}, {'timestamp': 10, 'heart_rate': 90, 'skin_response': 2.14, 'temperature': 33.25, 'activity_level': 0.45, 'signal_quality': 0.9}, {'timestamp': 11, 'heart_rate': 87, 'skin_response': 2.16, 'temperature': 33.19, 'activity_level': 0.6, 'signal_quality': 0.85}]


## FETCHING DATA ###
#profile, data=resting()
#profile, data=moderate_activity()
#profile, data=high_activity()
profile, data=poor_quality()
#profile, data=recovery()
test1=obs(profile, data)
#test1=obs(profile, profile)
#test1=obs(profile, test_data_set)
print(test1.aquisition_validation)

print("---------container allocation------------")

containers = test1.container_allocation()
print(containers)

print("--------isAllReadings-----------")

print(test1.isAllReadings)
#
print("--------isNumReadings-----------")
print(test1.isNumReadings)

print("--------CheckType-----------")
print(test1.CheckType)

#test2=part(profile)
test2=part(test1.profile_data)
test2.SetProfileData()
print("personal ID:",test2.ID)
print("Baseline Heart Rate:", test2.Baseline_HR)
print("Baseline Skin Response:", test2.Baseline_Skin)
print("Baseline Temperature:", test2.Baseline_Temp)


test3=ses(test1.profile_data, test1.data_set)
print("--------sorted data containers-----------")
print(test3.sort_observations())

print("--------number of valid readings-----------")
print(test3.numValidRead)


test4=ana(test3.profile_data, test3.data_set)

print("--------summary data-----------")
hr=test4.summary_hr()
#print(test4.summary_hr())
print(hr)

sr=test4.summary_sr()
#print(test4.summary_sr())
print(sr)

temp=test4.summary_temp()
#print(test4.summary_temp())
print(temp)

al=test4.summary_al()
#print(test4.summary_al())
print(al)

print("--------total summaries-----------")
print(test4.all_calculated_data)

print("----cassification -----")
classify_s=test4.classify_session()
#print(test4.classify_session())
print(classify_s)

rec=test4.recovery_tracker()
#print(test4.recovery_tracker())
print(rec)

print("***************************")
print_list=test4.data_summary(hr,sr,temp,al,classify_s,rec )
if isinstance(print_list,list):
    print(*print_list, sep='\n', end="\n")
else:
    print("printing data summary failed")

