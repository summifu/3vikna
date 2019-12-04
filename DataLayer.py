import csv


class IOAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_past_flights_from_file(self):
        fileStream_past_flights = open("PastFlightsFile.csv", "r")
        return fileStream_past_flights

    def store_past_flights_to_file(self, new_past_flight):
        c = VoyagesIO().write_in_file_past_flights(new_past_flight)

    def load_upcoming_flights_from_file(self):
        fileStream_upcoming_flights = open("UpcomingFlightsFile.csv", "r")
        return fileStream_upcoming_flights

    def store_upcoming_flights_to_file(self, new_upcoming_flight):
        d = VoyagesIO().write_in_file_upcoming_flights(new_upcoming_flight)

    def load_destination_from_file(self, destination):
        fileStream_destinations = open("DestinationsFile.csv", "r")
        return fileStream_destinations

    def store_destination_to_file(self, new_destination=''):
        d = DestinationsIO().write_in_destination_file(new_destination)

    def load_airplanes_from_file(self, planeID):
        fileStream_aircraft = open("Aircraft.csv", "r")
        return fileStream_aircraft

    def store_airplanes_to_file(self, new_airplane):
        g = AirplanesIO().write_in_airplanes_file(new_airplane)

    def load_airplanesinfo_from_file(self):
        fileStream_airplanesinfo = open("AirplanesInfoFile.csv", "r")
        return fileStream_airinfo

    def store_airplanesinfo_to_file(self, new_airplane_type=''):
        s = AirplanesIO().write_in_airplanesinfo_file(new_airplane_type)

    def load_crew_from_file(self):
        fileStream_crew = open("Crew.csv", "r")
        # ef empty hvað þá?
        return fileStream_crew

    def store_crew_to_file(self, new_employee=''):
        b = CrewIO().write_in_file(new_employee)


class CrewIO(IOAPI):
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_file(self, new_crew_member=''):
        f = open("CrewFile.csv", "a")
        f.write(new_crew_member)
        f.close()


class AirplanesIO(IOAPI):
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_airplanes_file(self, new_airplane):
        f = open("AirplanesFile.csv", "a")
        f.write(new_airplane)
        f.close()

    def write_in_airplanesinfo_file(self, new_airplane_type):
        f = open("AirplanesInfoFile.csv", "a")
        f.write(new_airplane_type)
        f.close()


class DestinationsIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_destination_file(self, new_destination):
        f = open("DestinationsFile.csv", "a")
        f.write(new_destination)
        f.close()


class VoyagesIO():
    def __init__(self, a_str):
        self.a_str = a_str

    def write_in_file_past_flights(self, new_past_flight):
        f = open("PastFlightsFile.csv", "a")
        f.write(new_past_flight)
        f.close()

    def write_in_file_upcoming_flights(self, new_upcoming_flight):
        f = open("UpcomingFlightsFile.csv", "a")
        f.write(new_upcoming_flight)
        f.close()


def main():
    newEmployee = 'New employee \n'
    a = IOAPI().store_crew_to_file(new_employee)

    pastFlight = "i am a past flight \n"
    b = IOAPI().store_past_flights_to_file(new_past_flight)

    UpcomingFlight = "i am a upcoming flight \n"
    y = IOAPI().store_upcoming_flights_to_file(new_upcoming_flight)

    airplaneinfo = "i am info \n"
    y = IOAPI().store_airplanesinfo_to_file(new_airplane_type)

    airplane = "i am airplane \n"
    j = IOAPI().store_airplanes_to_file(new_airplane)

    newDestination = "i am a destination \n"
    j = IOAPI().store_destination_to_file(newDestination)


main()
