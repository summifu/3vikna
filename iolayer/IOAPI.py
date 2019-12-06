import csv
import os


class IOAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_past_flights_from_file(self):
        fileStream_past_flights = open("PastFlights.csv", "r")
        return fileStream_past_flights

    def store_past_flights_to_file(self, new_past_flight=''):
        c = VoyagesIO().write_in_file_past_flights(new_past_flight)

    def load_upcoming_flights_from_file(self):
        fileStream_upcoming_flights = open("UpcomingFlights.csv", "r")
        return fileStream_upcoming_flights

    def store_upcoming_flights_to_file(self, new_upcoming_flight=''):
        d = VoyagesIO().write_in_file_upcoming_flights(new_upcoming_flight)

    def update_upcoming_flights_and_overwrite(self, updated_upcoming_flights_str=''):
        b = VoyagesIO().overwrite_upcoming_flights_file(updated_upcoming_flights_str)

    def load_destination_from_file(self):
        with open('./data_files/Destinations.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['id'], row['destination'], row['country'], row['distance'], row['contactname'],
                      row['emergencynumber'], row['flighttime'], row['destinationnumber'])

    def store_destination_to_file(self, new_destination=''):
        d = DestinationsIO().write_in_destination_file(new_destination)

    def update_destination_and_overwrite(self, updated_destination_str=''):
        b = DestinationsIO().overwrite_destination_file(updated_destination_str)

    def load_airplanes_from_file(self, planeID):
        fileStream_aircraft = open("Aircraft.csv", "r")
        return fileStream_aircraft

    def store_airplanes_to_file(self, new_airplane=''):
        g = AirplanesIO().write_in_airplanes_file(new_airplane)

    def load_airplanesinfo_from_file(self):
        fileStream_airplanesinfo = open("AirplanesInfoFile.csv", "r")
        return fileStream_airplanesinfo

    def store_airplanesinfo_to_file(self, new_airplane_type=''):
        s = AirplanesIO().write_in_airplanesinfo_file(new_airplane_type)

    def load_crew_from_file(self):
        with open('./data_files/CrewFile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'],
                      row['address'], row['phonenumber'], row['email'], row['id'])

    def store_crew_to_file(self, new_employee=''):
        b = CrewIO().write_in_file(new_employee)

    def update_employee_and_overwrite(self, updated_employees_str=''):
        b = CrewIO().overwrite_crew_file(updated_employees_str)


<<<<<<< HEAD
x = IOAPI().load_destination_from_file()
print('')
b = IOAPI().load_crew_from_file()


=======
x = IOAPI().load_crew_from_file()
>>>>>>> dc8d69ac04cd3fa98a35c97312c69ef01eb2193c