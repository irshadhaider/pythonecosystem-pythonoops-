class Airport(object):
    
    def __init__(self,runwayrent,flightnumber,flightarrivaltime,flightdeparturetime):
        self.runwayrent=runwayrent
        self.flightnumber=flightnumber
        self.flightarrivaltime=flightarrivaltime
        self.flightdeparturetime=flightdeparturetime
        
        
    def __repr__(self):
        return f'object("{self.runwayrent},{self.flightnumber},{self.flightarrivaltime},{self.flightdeparturetime}")'
    
    
if __name__=="__main__":
    YYZ=Airport(60000,786,13:30,12:30)
    print (YYZ.__repr__())
    print(YYZ)
    
    