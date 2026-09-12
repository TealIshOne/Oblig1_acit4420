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
        
    def observation_validation(self):
        try:
            if self.baselines is None or self.data is None :
                print("missing data set")
                return None, None
            else:
                return self.baselines, self.data
        except:
            print("something went wrong")


    
    def seperate(self):
        pass 


class participant(observations):
    """
    accsessing participant baseline data
    averaging values
    """
    def __init__(self):
        pass

    def ID(self):
        pass

    def heart_rate_B(self):
        pass

    def skin_respons_B(self):
        pass

    def temp_B(self):
        pass
    def heart_rate_avg(self):
        pass

    def skin_resp_avg(self):
        pass
    
    def temperatur_avg(self):
        pass
    
    def activety_level_avg(self):
        pass
    
    def signal_Q_avg(self):
        pass

    pass

class session (participant):
    """
    maybe use decorator here?

    """
    def __init__(self):
        pass

    def maximum_values():
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