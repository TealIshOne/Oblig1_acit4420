
from sample_data import resting, moderate_activity ,high_activity, recovery, poor_quality
from main import Participant as part
from main import Observation as obs
from main import SessionsStorage as sest
from main import sessionMath as sesMa

test_data_set= [{'timestamp': 0, 'heart_rate': 95, 'skin_response': 2.29, 'temperature': 33.23, 'activity_level': 0.53, 'signal_quality': 0.90}, {'timestamp': 1, 'heart_rate': 93, 'skin_response': 1.97, 'temperature': 33.19, 'activity_level': 0.4, 'signal_quality': 0.86}, {'timestamp': 2, 'heart_rate': 82, 'skin_response': 1.95, 'temperature': 33.17, 'activity_level': 0.4, 'signal_quality': 0.93}, {'timestamp': 3, 'heart_rate': 88, 'skin_response': 2.18, 'temperature': 33.17, 'activity_level': 0.39, 'signal_quality': 0.97}, {'timestamp': 4, 'heart_rate': 84, 'skin_response': 2.03, 'temperature': 33.33, 'activity_level': 0.51, 'signal_quality': 0.93}, {'timestamp': 5, 'heart_rate': 81, 'skin_response': 2.14, 'temperature': 33.32, 'activity_level': 0.45, 'signal_quality': 0.91}, {'timestamp': 6, 'heart_rate': 89, 'skin_response': 2.17, 'temperature': 33.34, 'activity_level': 0.6, 'signal_quality': 0.98}, {'timestamp': 7, 'heart_rate': 102, 'skin_response': 2.22, 'temperature': 33.37, 'activity_level': 0.41, 'signal_quality': 0.95}, {'timestamp': 8, 'heart_rate': 90, 'skin_response': 2.04, 'temperature': 33.11, 'activity_level': 0.48, 'signal_quality': 0.88}, {'timestamp': 9, 'heart_rate': 91, 'skin_response': 2.29, 'temperature': 33.2, 'activity_level': 0.52, 'signal_quality': 0.98}, {'timestamp': 10, 'heart_rate': 90, 'skin_response': 2.14, 'temperature': 33.25, 'activity_level': 0.45, 'signal_quality': 0.9}, {'timestamp': 11, 'heart_rate': 87, 'skin_response': 2.16, 'temperature': 33.19, 'activity_level': 0.6, 'signal_quality': 0.85}]



#profile, data=resting()
profile, data=moderate_activity()
#profile, data=high_activity()
#profile, data=poor_quality()
#profile, data=recovery()

L=[1,2,3,4]
print("-------------test participant class------------------")
# test1=part(profile)
# test1.SetProfileData()
# print("personal ID:",test1.ID)
# print("Baseline Heart Rate:", test1.Baseline_HR)
# print("Baseline Skin Response:", test1.Baseline_Skin)
# print("Baseline Temperature:", test1.Baseline_Temp)


print("-------------test Observation class------------------")
test2=obs(data)
#test2=obs()
#test2=obs(test_data_set)
print("*isValid*")
invalid, valid= test2.isValid()
# print(invalid)
# print()
# print(valid)
print("*ValidValues*")
#print(test2.ValidValues)
print("*ValidDataContainerAllocation*")
hr, sr, temp, al, sig = test2.ValidDataContainerAllocation()
# print(hr)
# print(sr)
# print(temp)
# print(al)
# print(sig)
print("*ValidateType*")
ValidateType=test2.ValidateType()
#print(ValidateType) #true/false --> test with test_data

profile1, data1=resting()
profile2, data2=moderate_activity()
profile3, data3=high_activity()
profile4, data4=poor_quality()
#profile, data=recovery()

print("-------------test Sessions class------------------")
test3=sest(data1,data2,data3,data4)
x,y= test3.ValidateAll()
# print(x)
# print("*******************************")
# print(y)


print("-------------test SessionsMath class------------------")
test4=sesMa(profile1, data4,data4,data4,data4)
hr_i=test4.hr_info()
sr_i=test4.sr_info()
temp_i=test4.temp_info()
al_i=test4.al_info()
sig_i=test4.signal_info()

# print("hr",hr_i)
# print("sr",sr_i)
# print("temp",temp_i)
# print("al", al_i)
# print("sig", sig_i)

print("*classify*")
classify_s=test4.SessionClassification()
#print(test4.classify_session())
print(classify_s)