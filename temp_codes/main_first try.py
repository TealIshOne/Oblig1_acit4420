"""
explain
"""

### classes ###

class observations:
    """
    validates collected observation data
    seperates data into data containers
    """
    def __init__(self, data_set1=None,data_set2=None):
        self.baselines =data_set1
        self.data=data_set2


        self.heart_rate= list()
        self.skin_response=list()
        self.temperature=list()
        self.activity_level=list()
        self.signal_quality=list()

        
    def observation_aquisition_validation(self):
        try:
            if self.baselines is None or self.data is None :
                print("missing data set")
                return None, None
            else:
                return self.baselines, self.data
        except:
            print("something went wrong")


    
    def data_container_seperation(self):
        ###this does not acount for non dict types!!!!!!! fix!!!!!!!!!###
        try:
            ## although data is stored as int, 
            # the loop appends the values as float  as a security measure to ensure no values are lost
            # and protects against formating issues, such as number type values being stored as str
            for x in self.data:
                self.heart_rate.append(float(x.get("heart_rate")))
                self.skin_response.append(float(x.get("skin_response")))
                self.temperature.append(float(x.get("temperature")))
                self.activity_level.append(float(x.get("activity_level")))
                self.signal_quality.append(float(x.get("signal_quality")))
        except ValueError:
            print("the value could not be converted to integer")

        ##add data missing except !!!!!!!!!!!!!!!!!!!!!!!##
        
        except:
            print("something else went wrong!")
        return self.heart_rate, self.skin_response, self.temperature, self.activity_level, self.signal_quality

    def data_type_validation(self):
        _check_heart = all(type(x) in (int,float) for x in self.heart_rate)
        _check_skin = all(type(x) in (int,float) for x in self.skin_response)
        _check_temp = all(type(x) in (int,float) for x in self.temperature)
        _check_activity = all(type(x) in (int,float) for x in self.activity_level)
        _check_signal = all(type(x) in (int,float) for x in self.signal_quality)
        try:
            if _check_heart and _check_skin and _check_temp and _check_activity and _check_signal:
                return "all is good"
            
            else:
                return f"check_heart: {_check_heart}, check_skin: {_check_skin}, check_temp: {_check_temp}, check_activity: {_check_activity}, check_signal: {_check_signal}"
        except:
            print("something went wrong in data_type_validation")





class participant(observations):
    """
    accsessing participant baseline data
    averaging values
    """
    def __init__(self, data_set1, data_set2, participant_id):
        super().__init__(data_set1, data_set2)
        self.participant_id= participant_id
        
    @property
    def Personal_information(self):
        return self.baselines

    @property
    def heart_rate_B(self):
        return self.baseline.get("baseline_heart_rate")

    @property
    def skin_respons_B(self):
        return self.baseline.get("baseline_skin_response")

    @property
    def temp_B(self):
        return self.baseline.get("baseline_temperature")

    

class session (participant, observations):
    """
    maybe use decorator here?
    compare calculations to baseline data

    """
    
    def __init__(self):
        super().__init__()

    @property
    def heart_rate_avg(self):
        temp_hr_avg=0
        for x in self.heart_rate:
            temp+=x
        return temp_hr_avg/len(self.heart_rate)

    @property
    def skin_resp_avg(self):
        temp_sr_avg=0
        for x in self.skin_response:
            temp+=x
        return temp_sr_avg/len(self.skin_response)

    @property
    def temperatur_avg(self):
        temp_temp_avg=0
        for x in self.temperature:
            temp+=x
        return temp_temp_avg/len(self.temperature)
    
    @property
    def activety_level_avg(self):
        temp_al_avg=0
        for x in self.activity_level:
            temp+=x
        return temp_al_avg/len(self.activity_level)
    @property
    def signal_Q_avg(self):
        temp_sq_avg=0
        for x in self.signal_quality:
            temp+=x
        return temp_sq_avg/len(self.signal_quality)   

    def maximum_values():
        max_hr=max(self.heart_rate)
        max_skin_resp=max(self.skin_response)
        max_temp=max(self.temperature)
        max_activity_l=max(self.activity_level)
        max_signal_q=max(self.signal_quality)
        return max_hr, max_skin_resp, max_temp, max_activity_l, max_signal_q

    def excessive_values():
        
        pass

class session_analysis(session):
    """
    explain
    compares measurments against baseline values
    nice printout
    """
    def __init__(self):
        pass
    pass