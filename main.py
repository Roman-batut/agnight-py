import pySBB as sbb
import datetime

# Get all stations
with open('stations.txt', 'r') as f:
    stations = f.read().splitlines()
f.close()

# AG Night Time
start = "19:00"
end_week = "05:00"
end_weekend = "07:00"

# Infos
departure = "Lausanne "

#Lausanne (19:19, Plat. 1) -> Aadorf (22:28, Plat. 1) | 3h 9min

def encrypt_connection(con: str):
    departure_station = str(con).split(" -> ")[0].split(" (")[0]
    if ',' in str(con).split(" -> ")[0].split(" (")[1]:
        departure_time = str(con).split(" -> ")[0].split(" (")[1].split(", Plat. ")[0]
        departure_plat = str(con).split(" -> ")[0].split(" (")[1].split(", Plat. ")[1].split(")")[0]
    else:
        departure_time = str(con).split(" -> ")[0].split(" (")[1].split(")")[0]
        departure_plat = "None"
    arrival_station = str(con).split(" -> ")[1].split(" (")[0]
    if ',' in str(con).split(" -> ")[1].split(" (")[1]:
        arrival_time = str(con).split(" -> ")[1].split(" (")[1].split(", Plat. ")[0]
        arrival_plat = str(con).split(" -> ")[1].split(" (")[1].split(", Plat. ")[1].split(")")[0]
    else:
        arrival_time = str(con).split(" -> ")[1].split(" (")[1].split(")")[0]
        arrival_plat = "None"
    duration = str(con).split(" | ")[1]
    return [departure_station, departure_time, departure_plat, arrival_station, arrival_time, arrival_plat, duration]

def decrypt_connection(connection: list):
    return connection[0] + " (" + str(connection[1]) + ", Plat. " + connection[2] + ") -> " + connection[3] + " (" + str(connection[4]) + ", Plat. " + connection[5] + ") | " + connection[6]

# Get all reachable stations from departure station with AG Night Time
reachable_stations = []
def is_reachable(c):
    def superior_time(t1, t2):
        if t1.split(":")[0] > t2.split(":")[0]:
            return True
        elif t1.split(":")[0] == t2.split(":")[0] and t1.split(":")[1] > t2.split(":")[1]:
            return True
        else:
            return False
    def inferior_time(t1, t2):
        if t1.split(":")[0] < t2.split(":")[0]:
            return True
        elif t1.split(":")[0] == t2.split(":")[0] and t1.split(":")[1] < t2.split(":")[1]:
            return True
        else:
            return False
    
    if superior_time(c[1], start) and inferior_time(c[4], end_weekend):
        return True
    else:
        return False
    
for station in stations:
    conn = encrypt_connection(sbb.get_connections(departure, station, date="2024-01-06", time=start, limit=1)[0])
    if not is_reachable(conn):
        print(station)
        reachable_stations.append(station)