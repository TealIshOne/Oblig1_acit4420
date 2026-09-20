
data_set= [{'timestamp': 0, 'heart_rate': 95, 'skin_response': 2.29, 'temperature': 33.23, 'activity_level': 0.53, 'signal_quality': 0.88}, {'timestamp': 1, 'heart_rate': 93, 'skin_response': 1.97, 'temperature': 33.19, 'activity_level': 0.4, 'signal_quality': 0.86}, {'timestamp': 2, 'heart_rate': 82, 'skin_response': 1.95, 'temperature': 33.17, 'activity_level': 0.4, 'signal_quality': 0.93}, {'timestamp': 3, 'heart_rate': 88, 'skin_response': 2.18, 'temperature': 33.17, 'activity_level': 0.39, 'signal_quality': 0.97}, {'timestamp': 4, 'heart_rate': 84, 'skin_response': 2.03, 'temperature': 33.33, 'activity_level': 0.51, 'signal_quality': 0.93}, {'timestamp': 5, 'heart_rate': 81, 'skin_response': 2.14, 'temperature': 33.32, 'activity_level': 0.45, 'signal_quality': 0.91}, {'timestamp': 6, 'heart_rate': 89, 'skin_response': 2.17, 'temperature': 33.34, 'activity_level': 0.6, 'signal_quality': 0.98}, {'timestamp': 7, 'heart_rate': 102, 'skin_response': 2.22, 'temperature': 33.37, 'activity_level': 0.41, 'signal_quality': 0.95}, {'timestamp': 8, 'heart_rate': 90, 'skin_response': 2.04, 'temperature': 33.11, 'activity_level': 0.48, 'signal_quality': 0.88}, {'timestamp': 9, 'heart_rate': 91, 'skin_response': 2.29, 'temperature': 33.2, 'activity_level': 0.52, 'signal_quality': 0.98}, {'timestamp': 10, 'heart_rate': 90, 'skin_response': 2.14, 'temperature': 33.25, 'activity_level': 0.45, 'signal_quality': 0.9}, {'timestamp': 11, 'heart_rate': 87, 'skin_response': 2.16, 'temperature': 33.19, 'activity_level': 0.6, 'signal_quality': 0.85}]



def seperate_list(l2, count_condition):
    middle_data=list()
    last_data=list()
    total_readings=len(l2)
    for x in l2:
        ts=x[count_condition]
        if int((total_readings/2))-2 <= ts <= int((total_readings/2))+2:
            middle_data.append(x)
        elif (total_readings-5)<= ts <= total_readings:
            last_data.append(x)
    return middle_data, last_data




middle, end =seperate_list(data_set, "timestamp")

check_list=list()
temp_val=0

for x in middle:
    if "heart_rate" in x:
        print(x["heart_rate"])

x=9
y=5
test_øost=[f"banana{temp_val}", "hello"]
print(f"hello {x - y}")
print([f"you just finished a session of {activety_type}", 
                        "good job!",
                        f"your heart rate reached {hr_data.get("max")}",
                        f"this is {hr_data.get("max")-hr_data.get("refference")}",
                        ])