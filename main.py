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



    def ErrorHandling():
        "this class is used to catch data errors before being passed on"
        pass




class Participant:
    def __init__(self):
        pass

    @property
    def _id():
        pass

    @property
    def _baseline_hr():
        pass

    @property
    def _baselime_skin():
        pass

    @property
    def _baseline_temp():
        pass



class Session:
    def __init__(self):
        pass

    def add_observtion(self, data_set):
        "this function sorts through the data and rejects poor signal quality readings, and stores only *good* readings"
        pass
    def container_seperation():
        "this container re-seperates the sorted data into containers"
        pass

    @property
    def numValidRead():
        "returns the number of valid readings in the data set"
        pass




class Analyzer:
    def __init__(self):
        pass

    def summary_hr():
        "returns, max, avg, min readings"
        pass

    def summary_sr():
        "returns, max, avg, min readings"
        pass

    def summary_temp():
        "returns, max, avg, min readings"
        pass

    def summary_sr():
        "returns, max, avg, min readings"
        pass

    def all_avg():
        "returns an average readings dict"
        pass

    def classify_session():
        "analyses if session was resting, moderate, high activity, or recovery"
        pass
        ### COMPARISON ###
    def compare():
        "this function compares max, min and average to paseline values and returns deviations"
        pass
    ### PRESENTATION ###
    def present_data():
        "this function presents the calculated datas, and returns an ecouraging message"
        pass
    
