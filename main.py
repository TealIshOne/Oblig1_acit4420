"""
code
"""

#functions
def three_or_more(l1,target):
    if l1.count(target)>=3:
        return True
    else:
        return False


def majority(l1, target):
    if l1.count(target)>len(l1)/2:
        return True
    else:
        return False


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

def suportive_messages(assign1):
    messages=["rest is important!",
              "Good job!",
              "great!",
              "a good rest is good for the soul!",
              "recorded data is insufficient :("
              ]
    possible_assign=["resting", "moderate activity", "high activity", "recovery", "poor_quality"]
    if assign1 in possible_assign:
        if assign1==possible_assign[0]:
            return messages[0]
        elif assign1==possible_assign[1]:
            return messages[1]
        elif assign1==possible_assign[2]:
            return messages[2]
        elif assign1==possible_assign[3]:
            return messages[3]
        elif assign1==possible_assign[4]:
            return messages[4]
    else:
        return "hello, your activety class has eluded me"

def more_or_less(val):
    if val < 1:
        return "less"
    elif val> 1:
        return "more"
    else: 
        return "ERROR"


#classes

class Participant:
    """
    this class acsesses and stores Personal information from the user
    """
    def __init__(self,profile_data=None):
            
        self.personal_data=profile_data

        self._participant_id = None
        self._baseline_hr = None
        self._baseline_skin = None
        self._baseline_temp = None
    
#            baseline_data = ["baseline_heart_rate", "baseline_skin_response", "baseline_temperature"]
    def SetProfileData(self):
            try:
                if isinstance(self.personal_data,dict):
                    self._participant_id = self.personal_data.get("participant_id")
                    self._baseline_hr = self.personal_data.get("baseline_heart_rate")
                    self._baseline_skin = self.personal_data.get("baseline_skin_response")
                    self._baseline_temp = self.personal_data.get("baseline_temperature")
                else:
                    print( "your personal data is not formated correctly")
            except:
                return "something went wrong in Participant, SetProfileData (line 23)"
    @property
    def ID(self):
        return self._participant_id


    @property
    def Baseline_HR(self):
        return self._baseline_hr



    @property
    def Baseline_Skin(self):
        return self._baseline_skin



    @property
    def Baseline_Temp(self):

        return self._baseline_temp



class Observation:

    def __init__(self, raw_data = None):
        self.raw_data=raw_data

        self.inValid=list()
        self.Valid=list()


        self.heart_rate = list()
        self.skin_response = list()
        self.temperature = list()
        self.activity_level = list()
        self.signal_quality=list()

    def isValid(self, Signal_threshold=0.8):
        """ check if the raw data is valid, within realistic limits and meets quality standards"""

        try:
            if isinstance(self.raw_data,list):
                for x in self.raw_data:
                    if isinstance(x,dict):
                        if x.get("signal_quality") < Signal_threshold:
                            self.inValid.append(x)
                        elif None in x.values():
                            self.inValid.append(x)
                        else:
                            self.Valid.append(x)
                    else:
                        return " the contnet of your raw_data list is not dictionaries (line 71)", " the contnet of your raw_data list is not dictionaries (line 71)"
            else:
                return "the raw data you provided is not formated correctly (line 69)", "the raw data you provided is not formated correctly (line 69)"
            return self.inValid, self.Valid
        
        except:
            return "something went wrong in Observation, isValid (line 64)"


    @property
    def ValidValues(self):
        return self.Valid


    def ValidDataContainerAllocation(self):
        try:
            if self.Valid:
                self.heart_rate = [x.get("heart_rate") for x in self.Valid]
                self.skin_response = [x.get("skin_response") for x in self.Valid]
                self.temperature = [x.get("temperature") for x in self.Valid]
                self.activity_level = [x.get("activity_level") for x in self.Valid]
                self.signal_quality = [x.get("signal_quality") for x in self.Valid]
                return self.heart_rate, self.skin_response, self.temperature, self.activity_level, self.signal_quality
            else:
                return "the data container is empty","the data container is empty", "the data container is empty","the data container is empty","the data container is empty"
        except:
            return "something went wrong on Observation, ValidDataContainerAllocation (line 98)"
  
    def ValidateType(self):
            try:

                _check_heart = all(type(x) in (int,float) for x in self.heart_rate)
                _check_skin = all(type(x) in (int,float) for x in self.skin_response)
                _check_temp = all(type(x) in (int,float) for x in self.temperature)
                _check_activity = all(type(x) in (int,float) for x in self.activity_level)
                _check_signal = all(type(x) in (int,float) for x in self.signal_quality)
                if all([_check_heart, _check_skin, _check_temp, _check_activity, _check_signal]) and all([self.heart_rate, self.skin_response, self.temperature, self.activity_level, self.signal_quality]):
                    return True #, [_check_heart,_check_skin,_check_temp,_check_activity,_check_signal],[self.heart_rate, self.skin_response, self.temperature, self.activity_level, self.signal_quality]
                else:
                    return False #, [_check_heart,_check_skin,_check_temp,_check_activity,_check_signal], [self.heart_rate, self.skin_response, self.temperature, self.activity_level, self.signal_quality]
            except:
                return "something went wrong on Observation, ValidateType (line 116)"

class SessionsStorage:
    def __init__(self, *raw_datasets: list):
        self.collection_raw_dataset=raw_datasets
        self.raw=list()
        self.all_valid_record=list()
        self.all_invalid_record=list()

    def ValidateAll(self):
        for entry in self.collection_raw_dataset:
            obs_instance=Observation(entry)
            invalid, valid = obs_instance.isValid()
            

            obs_instance.ValidDataContainerAllocation()
            self.raw.append(obs_instance)
            
            if valid:
                self.all_valid_record.append(valid)
            if invalid:
                self.all_invalid_record.append(invalid)
        return self.all_invalid_record, self. all_valid_record



class sessionMath(SessionsStorage):
    def __init__(self, profile_data=None, *raw_datasets):
        SessionsStorage.__init__(self, *raw_datasets)
        self.participant = Participant(profile_data)
        self.participant.SetProfileData()
        self.summary_data = dict()
        
        self.ValidateAll()


    def hr_info(self):
        try:
            all_hr=list()
            for values in self.raw:
                if values.heart_rate and isinstance(values.heart_rate,list):
                    all_hr.extend(values.heart_rate)
            if all_hr:
                self.summary_data["heart_rate"] = {
                    "reference": self.participant.Baseline_HR,
                    "max": max(all_hr),
                    "avg": sum(all_hr) / len(all_hr),
                    "min": min(all_hr)
                }

            elif not all_hr:
                self.summary_data["heart_rate"] = {
                    "reference": self.participant.Baseline_HR,
                    "max": 0,
                    "avg": 0,
                    "min": 0
                }
            else:
                return "something went wrong(line183)"
            return self.summary_data["heart_rate"]
        except Exception as e:
            return f"something went wrong in sessionMath, hr_info: {type(e).__name__} - {e}"


    def sr_info(self):
        try:
            all_sr=list()
            for values in self.raw:
                if values.skin_response and isinstance(values.skin_response,list):
                    all_sr.extend(values.skin_response)
            if all_sr:
                self.summary_data["skin_response"] = {
                    "reference": self.participant.Baseline_Skin,
                    "max": max(all_sr),
                    "avg": sum(all_sr) / len(all_sr),
                    "min": min(all_sr)
                }

            elif not all_sr:
                self.summary_data["skin_response"] = {
                    "reference": self.participant.Baseline_Skin,
                    "max": 0,
                    "avg": 0,
                    "min": 0
                }
            else:
                return "something went wrong(line183)"
            return self.summary_data["skin_response"]
        except Exception as e:
            return f"something went wrong in sessionMath, sr_info: {type(e).__name__} - {e}"


    def temp_info(self):
        try:
            all_temp=list()
            for values in self.raw:
                if values.temperature and isinstance(values.temperature,list):
                    all_temp.extend(values.temperature)
            if all_temp:
                self.summary_data["temperature"] = {
                    "reference": self.participant.Baseline_Temp,
                    "max": max(all_temp),
                    "avg": sum(all_temp) / len(all_temp),
                    "min": min(all_temp)
                }

            elif not all_temp:
                self.summary_data["temperature"] = {
                    "reference": self.participant.Baseline_Temp,
                    "max": 0,
                    "avg": 0,
                    "min": 0
                }
            else:
                return "something went wrong(line183)"
            return self.summary_data["temperature"]
        except Exception as e:
            return f"something went wrong in sessionMath, temp_info: {type(e).__name__} - {e}"


    def al_info(self):
        try:
            all_al=list()
            for values in self.raw:
                if values.activity_level and isinstance(values.activity_level,list):
                    all_al.extend(values.activity_level)
                elif (isinstance(values.activity_level, list)):
                        if not all_al:
                            self.summary_data["activity_level"] = {
                            "reference": "NA",
                            "max": 0,
                            "avg": 0,
                            "min": 0
                            }
                        else:
                            self.summary_data["activity_level"] = {
                                "reference": "NA",
                                "max": max(all_al),
                                "avg": sum(all_al) / len(all_al),
                                "min": min(all_al)
                            }
                        return self.summary_data["activity_level"]
            else:
                return "data set is not valid, please check the data set, summary_al function (line 297)"
        

        except Exception as e:
            return f"something went wrong in sessionMath, al_info: {type(e).__name__} - {e}"
  

    def signal_info(self):
        try:
            all_sig=list()
            for values in self.raw:
                if values.signal_quality and isinstance(values.signal_quality,list):
                    all_sig.extend(values.signal_quality)
                elif (isinstance(values.signal_quality, list)):
                        if not all_sig:
                            self.summary_data["signal_quality"] = {
                            "reference": "NA",
                            "max": 0,
                            "avg": 0,
                            "min": 0
                            }
                        else:
                            self.summary_data["signal_quality"] = {
                                "reference": "NA",
                                "max": max(all_sig),
                                "avg": sum(all_sig) / len(all_sig),
                                "min": min(all_sig)
                            }
                        return self.summary_data["signal_quality"]
            else:
                return "data set is not valid, please check the data set, summary_signal function (line 297)"
        

        except Exception as e:
            return f"something went wrong in sessionMath, temp_info: {type(e).__name__} - {e}"

    @property
    def all_info_dict(self):
        return self.summary_data

    def SessionClassification(self):
        type_data=dict()
        
        self.hr_info()
        self.sr_info()
        self.temp_info()
        self.al_info()

        for x in self.summary_data:
            if x == "heart_rate":
                hr_avg = self.summary_data[x].get("avg")
                if hr_avg < self.participant._baseline_hr +15:
                    type_data["heart_rate"] = "resting"
                elif hr_avg < self.participant._baseline_hr+45:
                    type_data["heart_rate"] = "moderate activity"
                elif self.participant._baseline_hr+45 < hr_avg < 220: # general formulas set 220 as maximum heartrate value before heart damage
                    type_data["heart_rate"] = "high activity"

                else:
                    type_data["heart_rate"] = "inconclusive or unknown session type"

            elif x == "skin_response":
                sr_avg = self.summary_data[x].get("avg")
                if sr_avg < self.participant._baseline_skin + 0.30:
                    type_data["skin_response"] = "resting"
                elif sr_avg < self.participant._baseline_skin + 0.55:
                    type_data["skin_response"] = "moderate activity"
                elif self.participant._baseline_skin + 0.55 < sr_avg <100: # 100 is an arbitrary estimated value
                    type_data["skin_response"] = "high activity"
                else:
                    type_data["skin_response"] = "inconclusive or unknown session type"

            elif x == "temperature":
                temp_avg = self.summary_data[x].get("avg")
                if temp_avg < self.participant._baseline_temp + 0.30:
                    type_data["temperature"] = "resting"
                elif temp_avg < self.participant._baseline_temp + 0.55:
                    type_data["temperature"] = "moderate activity"
                elif temp_avg < 42: # 42 is the temeperature human protein denaturates and is therefore set as max value
                    type_data["temperature"] = "high activity"
                else:
                    type_data["temperature"] = "inconclusive or unknown session type"

            elif x == "activity_level": #bsolute values, no scaling changes needed
                al_avg = self.summary_data[x].get("avg")
                if al_avg <= 0.25:
                    type_data["activity_level"] = "resting"
                elif al_avg <= 0.67:
                    type_data["activity_level"] = "moderate activity"
                elif al_avg <= 1:
                    type_data["activity_level"] = "high activity"
                else:
                    type_data["activity_level"] = "inconclusive or unknown session type"


        values=list(type_data.values())
        #since the data_generator is based on rng and gauss distribution some values may become autliers and reult in,
        # some parameters not linight perfectly up with the others, by checking for majority/ minimum of 3 equals, 
        # I hope to mittigate this issue
        if majority(values,"resting"):
            return "resting"
        elif majority(values, "moderate activity"):
            return "moderate activity"
        elif majority(values, "high activity"):
            return "high activity"
        else:
            return f"inconclusive or unknown session type, {values}"
    