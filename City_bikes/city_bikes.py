"""In this exercise I will write some functions 
for working on a file containing location data from 
the stations for city bikes in Helsinki.
"""
import math

def get_station_data(filename):
    stations = {}

    with open(filename) as file:
        for row in file:
            parts = row.strip().split(";")

            #Skip the first row
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    
    return stations

def distance(stations,stat1,stat2):
    x_km = (stations[stat1][0] - stations[stat2][0]) * 55.26
    y_km = (stations[stat1][1] - stations[stat2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations):
    stat1 =""
    stat2 = ""
    greatest = 0.0

    cities = []

    for x in stations:
        cities.append(x)
    
    for x in cities:
        for y in cities:
            if greatest < distance(stations, x ,y):
                stat1 = x
                stat2 = y
                greatest = distance(stations, x ,y)

    return (stat1, stat2, greatest)

if __name__ == "__main__":
    stations = get_station_data("stations1.csv")

    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
