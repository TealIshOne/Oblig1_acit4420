

#testing observations

from main import observations as obs
from main import participant as part
from sample_data import resting




## FETCHING DATA ###
profile, data=resting()
# test1=obs(profile, data)
# validated_prof, vlaidated_data=test1.observation_aquisition_validation()
# #print(validated_prof)
# #print(vlaidated_data)
# x1, x2, x3, x4, x5 =test1.data_container_seperation()

# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
# print(test1.data_type_validation())

from main import participant as part
from sample_data import resting



# 2. Instantiate participant directly (it inherits all methods from observations!)
p1 = part(profile, data, "P001")

# 3. Use all parent methods directly on the child instance
p1.observation_aquisition_validation()
x1, x2, x3, x4, x5 = p1.data_container_seperation()

# 4. Access parent & child attributes directly
print("Heart Rates:", x1)
print("Type Validation:", p1.data_type_validation())
print("Personal Information:", p1.Personal_information)
