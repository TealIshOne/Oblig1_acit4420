"""
explain

"""


class Observations:
    def __init__(self, profile_data=None, data_set=None):
        ### data sets ###
        self.profile_data = profile_data
        self.data_set = data_set

        #### data containers ###
        self.available_readings = ["heart_rate", "skin_response", "temperature", "activity_level", "signal_quality"]

        self.heart_rate = list()
        self.skin_response = list()
        self.temperature = list()
        self.activity_level = list()

    @property
    def aquisition_validation(self):
        "returns True, if a data set is collected"
        try: 
            if self.profile_data is None or self.data_set is None:
                print("missing data set")
                return False
            else:
                return True
        except:
            print("something went wrong")


    # def data_sepperation():
    #     "sepperates the two components of the data set"
    #     pass
    
    def container_allocation(self):
        "allocates all data into data containers for further use"
        try:

            self.heart_rate = [x.get("heart_rate") for x in self.data_set]
            self.skin_response = [x.get("skin_response") for x in self.data_set]
            self.temperature = [x.get("temperature") for x in self.data_set]
            self.activity_level = [x.get("activity_level") for x in self.data_set]
            self.signal_quality = [x.get("signal_quality") for x in self.data_set]
            return (self.heart_rate, self.skin_response, self.temperature, self.activity_level, self.signal_quality)
        except AttributeError:
                raise ValueError("the data set is not a list, please check the data set (function,line 36)")    
 

    @property
    def isAllReadings(self):
        "returns True if all required readings are in the data set"
        check_list = list()
        for x in self.available_readings: #loops accross the self.available_readings
            for y in self.data_set: #loops
                if x in y.keys():
                    check_list.append(True)
                else:
                    check_list.append(False)
        
        return all(check_list)
                
    @property
    def isNumReadings(self):
        "returns true if number of readings in all categories meets requirement"
        check_list = list()
        for x in self.data_set:
            if len(x) > 6:
                check_list.append(False)
            else:
                check_list.append(True)

        return all(check_list)

    @property
    def CheckType(self):
        "checks if all numeric values are int, or float this function simply double checks incase of formating errors"
        try:
            _check_heart = all(type(x) in (int,float) for x in self.heart_rate)
            _check_skin = all(type(x) in (int,float) for x in self.skin_response)
            _check_temp = all(type(x) in (int,float) for x in self.temperature)
            _check_activity = all(type(x) in (int,float) for x in self.activity_level)
            _check_signal = all(type(x) in (int,float) for x in self.signal_quality)
            if all([_check_heart, _check_skin, _check_temp, _check_activity, _check_signal]):
                return True
            else:
                return False
        except:
            raise TypeError("data type error, please check the data set (function,line 80)")



    # def ErrorHandling(self):
    #     "this class is used to catch data errors before being passed on"

    #     pass




class Participant(Observations):
    def __init__(self,profile_data=None):
        super().__init__(profile_data)

        self._participant_id = None
        self._baseline_hr = None
        self._baseline_skin = None
        self._baseline_temp = None

        baseline_data = ["baseline_heart_rate", "baseline_skin_response", "baseline_temperature"]

        
    def SetProfileData(self):
        try:
            for x in self.profile_data:
                if self.profile_data is None:
                    return "missing participant personal data"
                elif x == "participant_id":
                    self._participant_id = self.profile_data.get("participant_id")
                elif x == "baseline_heart_rate":
                    self._baseline_hr = self.profile_data.get("baseline_heart_rate")
                elif x == "baseline_skin_response":
                    self._baseline_skin = self.profile_data.get("baseline_skin_response")
                elif x == "baseline_temperature":
                    self._baseline_temp = self.profile_data.get("baseline_temperature")
        except:
            return "something went wrong in the SetProfileData function (line 115)"
    @property
    def ID(self):
        try:
            return self._participant_id

        except:
            return "something went wrong in the _id function (line 131)"


    @property
    def Baseline_HR(self):
        try:
            if self._baseline_hr is None:
                return "missing baseline heart rate data"
            else:
                return self._baseline_hr
        except:
            return "something went wrong in the _baseline_hr function (line 140)"


    @property
    def Baseline_Skin(self):
        try:
            if self._baseline_skin is None:
                return "missing baseline skin data"
            else:
                return self._baseline_skin
        except:
            return "something went wrong in the _baseline_skin function (line 148)"


    @property
    def Baseline_Temp(self):
        try:
            return self._baseline_temp
        except:
            return "something went wrong in the _baseline_temp function (line 156)"



class Session(Observations):
    def __init__(self, profile_data=None, data_set=None):
        super().__init__(profile_data, data_set)
        self.Sortedheart_rate=list()
        self.Sortedskin_response=list()
        self.Sortedtemperature=list()
        self.Sortedactivity_level=list()

    def sort_observations(self):
        "this function sorts through the data and rejects poor signal quality readings, and stores only *good* readings"
        try:
            if self.data_set is None:
                return "missing data set"   
            else:
                self.Sortedheart_rate=[x.get("heart_rate") for x in self.data_set if x.get("signal_quality") > 0.8]
                self.Sortedskin_response=[x.get("skin_response") for x in self.data_set if x.get("signal_quality") > 0.8]  
                self.Sortedtemperature=[x.get("temperature") for x in self.data_set if x.get("signal_quality") > 0.8]
                self.Sortedactivity_level=[x.get("activity_level") for x in self.data_set if x.get("signal_quality") > 0.8]
                return (self.Sortedheart_rate, self.Sortedskin_response, self.Sortedtemperature, self.Sortedactivity_level)
        except:
            return "something went wrong in the sort_observations function (line 180)"
  



    @property
    def numValidRead(self):
        "returns the number of valid readings in the data set"
        containers = [self.Sortedheart_rate, 
                      self.Sortedskin_response, 
                      self.Sortedtemperature, 
                      self.Sortedactivity_level]
        try:
            valid_readings = (
                all([isinstance(con, list) for con in containers]) and 
                all([len(con) > 0 for con in containers]) and
                len(set(len(con) == len(containers[0]) for con in containers)) == 1)

            if valid_readings:
                numValidRead=[
                    len([item for item in self.Sortedheart_rate if item is not None]),
                    len([item for item in self.Sortedskin_response if item is not None]),
                    len([item for item in self.Sortedtemperature if item is not None]),
                    len([item for item in self.Sortedactivity_level if item is not None])]
                
            if len(set(numValidRead)) == 1:
                return (numValidRead[0], numValidRead[1], numValidRead[2], numValidRead[3])

            else:
                return " data is missing please check the data set"
        except:
            return "something went wrong in the numValidRead function (line 200)"
        



class Analyzer(Session):
    def __init__(self, profile_data=None, data_set=None):
        super().__init__(profile_data, data_set)
        self.participant= Participant(profile_data)

        self.summary_data = dict()

        self.participant.SetProfileData()
        self.sort_observations()
        

    def summary_hr(self):
        "returns, max, avg, min readings"
        try:
            if self.Sortedheart_rate is None:
                return "missing data set"
            elif (isinstance(self.Sortedheart_rate, list)):
                    self.summary_data["heart_rate"] = {
                        "reference": self.participant._baseline_hr,
                        "max": max(self.Sortedheart_rate),
                        "avg": sum(self.Sortedheart_rate) / len(self.Sortedheart_rate),
                        "min": min(self.Sortedheart_rate)
                    }
                    return self.summary_data["heart_rate"]
            else:
                return "data set is not valid, please check the data set, summary_hr function (line 234)"
        except:
            return "something went wrong in the summary_hr function (line 234)"


    def summary_sr(self):
        "returns, max, avg, min readings"
        try:
            if self.Sortedskin_response is None:
                



    def summary_temp(self):
        "returns, max, avg, min readings"
        try:
            if self.Sortedtemperature is None:
                return "missing data set"
            elif (isinstance(self.Sortedtemperature, list) and 
                  isinstance(self._baseline_temp, dict) and 
                  "temperature" in self._baseline_temp):
                    self.summary_data["temperature"] = {
                        "reference": self._baseline_temp,
                        "max": max(self.Sortedtemperature),
                        "avg": sum(self.Sortedtemperature) / len(self.Sortedtemperature),
                        "min": min(self.Sortedtemperature)
                    }
                    return self.summary_data["temperature"]
            else:
                return "data set is not valid, please check the data set, summary_temp function (line 276)"

        except:
            return "something went wrong in the summary_temp function (line 276)"
   

    def summary_al(self):
        "returns, max, avg, min readings"
        try:
            if self.Sortedactivity_level is None:
                return "missing data set"
            elif isinstance(self.Sortedactivity_level, list):
                    self.summary_data["activity_level"] = {
                        "max": max(self.Sortedactivity_level),
                        "avg": sum(self.Sortedactivity_level) / len(self.Sortedactivity_level),
                        "min": min(self.Sortedactivity_level)
                    }
                    return self.summary_data["activity_level"]
            else:
                return "data set is not valid, please check the data set, summary_al function (line 297)"

        except:
            return "something went wrong in the summary_al function (line 297)"

    @property
    def all_calculated_data(self):
        "returns an average readings dict"
        return self.summary_data
   
    @property
    def classify_session(self):
        "analyses if session was resting, moderate, high activity, or recovery"
        type_data=dict()


        for x in self.summary_data:
            if x == "heart_rate":
                hr_avg = self.summary_data[x].get("avg")
                if hr_avg < 85:
                    type_data["heart_rate"] = "resting"
                elif hr_avg < 115:
                    type_data["heart_rate"] = "moderate activity"
                elif hr_avg < 155:
                    type_data["heart_rate"] = "high activity"

                else:
                    type_data["heart_rate"] = "inconclusive or unknown session type"
            elif x == "skin_response":
                sr_avg = self.summary_data[x].get("avg")
                if sr_avg < 1.9:
                    type_data["skin_response"] = "resting"
                elif sr_avg < 2.3:
                    type_data["skin_response"] = "moderate activity"
                elif sr_avg < 3.2:
                    type_data["skin_response"] = "high activity"
                else:
                    type_data["skin_response"] = "inconclusive or unknown session type"

            elif x == "temperature":
                temp_avg = self.summary_data[x].get("avg")
                if temp_avg < 33.3:
                    type_data["temperature"] = "resting"
                elif temp_avg < 33.6:
                    type_data["temperature"] = "moderate activity"
                elif temp_avg < 34.0:
                    type_data["temperature"] = "high activity"
                else:
                    type_data["temperature"] = "inconclusive or unknown session type"

            elif x == "activity_level":
                al_avg = self.summary_data[x].get("avg")
                if al_avg <= 0.25:
                    type_data["activity_level"] = "resting"
                elif al_avg <= 0.67:
                    type_data["activity_level"] = "moderate activity"
                elif al_avg <= 0.1:
                    type_data["activity_level"] = "high activity"
                else:
                    type_data["activity_level"] = "inconclusive or unknown session type"



                if all(item for item in type_data.values() if item == "resting"):
                    return "resting"
                elif all(item for item in type_data.values() if item == "moderate activity"):
                    return "moderate activity"
                elif all(item for item in type_data.values() if item == "high activity"):
                    return "high activity"
                elif all(item for item in type_data.values() if item == "recovery"):
                    return "recovery"
                else:
                    return "inconclusive or unknown session type"


        
        pass


    def recovery_tracker():
        pass
        ### COMPARISON ###
    def compare():
        "this function compares max, min and average to paseline values and returns deviations"
        pass
    ### PRESENTATION ###
    def present_data():
        "this function presents the calculated datas, and returns an ecouraging message"
        pass
    
