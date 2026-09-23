test1= [{'timestamp': 0, 'heart_rate': 78, 'skin_response': 2.29, 'temperature': 33.23, 'activity_level': 0.53, 'signal_quality': 0.88}, {'timestamp': 1, 'heart_rate': 93, 'skin_response': 1.97, 'temperature': 33.19, 'activity_level': 0.4, 'signal_quality': 0.86}, {'timestamp': 2, 'heart_rate': 82, 'skin_response': 1.95, 'temperature': 33.17, 'activity_level': 0.4, 'signal_quality': 0.93}, {'timestamp': 3, 'heart_rate': 88, 'skin_response': 2.18, 'temperature': 33.17, 'activity_level': 0.39, 'signal_quality': 0.97}, {'timestamp': 4, 'heart_rate': 84, 'skin_response': 2.03, 'temperature': 33.33, 'activity_level': 0.51, 'signal_quality': 0.93}, {'timestamp': 5, 'heart_rate': 81, 'skin_response': 2.14, 'temperature': 33.32, 'activity_level': 0.45, 'signal_quality': 0.91}, {'timestamp': 6, 'heart_rate': 89, 'skin_response': 2.17, 'temperature': 33.34, 'activity_level': 0.6, 'signal_quality': 0.98}, {'timestamp': 7, 'heart_rate': 102, 'skin_response': 2.22, 'temperature': 33.37, 'activity_level': 0.41, 'signal_quality': 0.95}, {'timestamp': 8, 'heart_rate': 90, 'skin_response': 2.04, 'temperature': 33.11, 'activity_level': 0.48, 'signal_quality': 0.88}, {'timestamp': 9, 'heart_rate': 91, 'skin_response': 2.29, 'temperature': 33.2, 'activity_level': 0.52, 'signal_quality': 0.98}, {'timestamp': 10, 'heart_rate': 90, 'skin_response': 2.14, 'temperature': 33.25, 'activity_level': 0.45, 'signal_quality': 0.9}, {'timestamp': 11, 'heart_rate': 87, 'skin_response': 2.16, 'temperature': 33.19, 'activity_level': 0.6, 'signal_quality': 0.85}]

personal_data= None

data_set= None


heartr=[]
skin_rep=[]
for x in test1:
    # k=test1.get("heart_rate")
    heartr.append(int(x.get("heart_rate")))
    skin_rep.append(x.get("skin_response"))


print(heartr)
for x in heartr:
    print(type(x))
print(skin_rep)

test_dict = {
    "participant_id": "P042",
    "baselines": {
        "heart_rate": 68,
        "skin_response": 2.4,
        "temperature": 36.6
    },
    "active": True,
    "readings": [70, 72, 71, 75]
}
print("--------------------")
print(test_dict.get(""))
if test1 is dict():
    print("yes")

# l=[1,2,3,4,5]
# print(max(l))




tf_l=[True, True, True, False, True, True, True, True, True, True, True, True]

if all(tf_l):
    print("all is good")
else:
    print("something is wrong")

for x in test1:
    print(len(x))

L=[1,2,3,4,5,6,7,8,9,10]

dididi=dict()
dididi["heart_rate"] = {
            "max": max(L),
            "avg": sum(L) / len(L),
            "min": min(L)
        }
print(dididi)
print("-----------")
for x in dididi:
   for y in x:
    val= dididi.get(y)
    print(val)


# def majority_check(bool_list):
#     count=bool_list
#     return sum(bool(x) for x in count)> len(count)/2
# tf_l2=["r", "r", "r", "r"]
# print(majority_check(tf_l2))

# def three_or_more(l1,target):
#     if l1.count(target)>=3:
#         return True
#     else:
#         return False
# print(three_or_more(tf_l2,"r"))
# l22=[1,2,3,4,5,6,7,8,9,10,11,12]
# def seperate_list(l2):
#     middle_data=list()
#     last_data=list()
#     total_readings=len(l2)
#     for x in l2:
#         if (total_readings/2)-2<= x <= (total_readings/2)+2:
#             middle_data.append(x)
#         elif (total_readings-5)<= x <= total_readings:
#             last_data.append(x)
#     return middle_data, last_data

# print(seperate_list(l22))



def format_text(string, value, width=55):
    if isinstance(value, (float)):
        value=round(value, 2)
    return f"{string.ljust(width, ".")} {value}"

summary_lines= ["test1", "test2", "twst3"]

print(format_tect(summary_lines[0],42), format_tect(summary_lines[1],7, width=7),format_tect(summary_lines[2],16))
summary_lines= [f"you just finished a session of {activety_type}", 
    f"{sup_msg}",
    f"your heart rate reached {hr_data.get('max')}",
    f"this is {round(hr_data.get('max')-hr_data.get("reference"),1)} {more_or_less(hr_data.get('max')-hr_data.get("reference"))} than your refference of {hr_data.get('reference')} BPM",
    "________________________________________",
    f"your skin response reached {sr_data.get('max')}",
    f"this is {round(sr_data.get("max")-sr_data.get('reference'),2)} {more_or_less(sr_data.get('max')-sr_data.get("reference"))} than your refference of {sr_data.get('reference')}",
    "________________________________________",

    f"your temperature reached {temp_data.get("max")}",
    f"this is {round(temp_data.get("max")-temp_data.get("reference"),2)} {more_or_less(temp_data.get('max')-temp_data.get("reference"))} than your refference of {temp_data.get("reference")} degrees",
    "________________________________________",
    f"your activety level reached {al_data.get("max")}",
    f"your minimum activety level was {al_data.get("min")}, your maximum activety level was {al_data.get("max")}, this is a span of {al_data.get("max")-al_data.get("min")} across the session",
    "________________________________________",
    "your average values were as follows",
    f"average heart rate across the session {round(hr_data.get("avg"), 1)}",
    f"average skin response across the session {round(sr_data.get("avg"), 2)}",
    f"average temperature across the session {round(temp_data.get("avg"),2)}",
    f"average activety level across the session {round(al_data.get("avg"), 2)}",
    f"recovery period? {recovery_check}"
    ]

sum_lines=[
    f"you just finished a session of {activety_type}",
    f"{sup_msg}",
    "_"*60,
    "your maximum values across the sessions were:",
    f"{format_text("your heart rate reached", hr_data.get("max"))} BPM",

    f"{format_text("your skin respone reached", sr_data.get("max"))}",

    f"{format_text("your temperature rate reached", temp_data.get("max"))} C",

    f"{format_text("your activety level reached", al_data.get("max"))}",
    "_"*60,
    "your average values across the sessions were:",
    f"{format_text("your heart rate reached", hr_data.get("avg"))} BPM",

    f"{format_text("your skin respone reached", sr_data.get("avg"))}",

    f"{format_text("your temperature reached", temp_data.get("avg"))} C",

    f"{format_text("your acticity level reached", al_data.get("avg"))}",
    "_"*60,
    "your minimum values across the sessions were:",
    f"{format_text("your heart rate reached", hr_data.get("min"))} BPM",

    f"{format_text("your skin respone reached", sr_data.get("min"))}",

    f"{format_text("your temperature reached", temp_data.get("min"))} C",

    f"{format_text("your activity level reached", al_data.get("min"))}",
    "_"*60,
    "your ranges were as follows",
    f"{format_text("your heart rate spanned", (hr_data.get("max")-hr_data.get("min")))} BPM",

    f"{format_text("your skin respone spanned", (sr_data.get("max")-sr_data("min")))}",

    f"{format_text("your temperature spanned", (temp_data.get("avg")-temp_data.get("min")))} C",

    f"{format_text("your acticety level spanned", (al_data.get("max")-al_data.get("min")))}",
    "_"*60,
    f"{format_text("recovery period?", recovery_check)}"

]
