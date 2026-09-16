"""
explain
"""


class Observations:
    def __init__(self):
        pass

    def aquisition_validation():
        "returns True, if a data set is collected"
        pass

    def data_sepperation():
        "sepperates the two components of the data set"
        pass
    
    def container_allocation():
        "allocates all data into data containers for further use"
        pass

    def isAllReadings():
        "returns True if all required readings are in the data set"
        pass

    def isNumReadings():
        "returns true if number of readings in all categories meets requirement"
        pass

    def checkType():
        "checks, and fixes data types in data containers, the data _generator returns int values,"
        "this function simply double checks incase of formating errors"
        pass


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
    
