# Global Variables
stations = []   # List of stations
lines = []      # List of lines
explored = set()

class SubwayStation:
    def __init__(self, name):
        self.name = name        # Name of the SubwayStation
        self.lines = []         # Lines that the SubwayStation is on
        self.coordinates_X = 0  # X coordinates
        self.coordinates_Y = 0  # Y coordinates
        stations.append(self)   # Add SubwayStation to stations list

    def list_available_stations(self):
        # station_set prevents repeating names from being printed
        station_set = set()

        print("Available Stations from", self.name)
        # For each SubwayLine in lines,
        for i in self.lines:
            # add the name of each SubwayStation on that line to station_set
            for j in i.stations:
                if j.name is not self.name:
                    station_set.add(j.name)
        
        # Print the names in station_set
        for i in station_set:
            print(i)
    
    def print_lines(self):
        print("Available Lines from", self.name)
        # Print the name of each SubwayLine in lines
        for i in self.lines:
            print(i.name)

class SubwayLine:
    def __init__(self, name):         
        self.name = name        # Name of the SubwayLine
        self.stations = []      # Stations that are on the SubwayLine
        lines.append(self)      # Add SubwayLine to lines list

    def list_available_lines(self):
        # line_set prevents repeating names from being printed
        line_set = set()

        print("Available Lines from", self.name)
        # For each SubwayStation in stations,
        for i in self.stations:
            # add the name of each SubwayLine on that station to line_set
            for j in i.lines:
                line_set.add(j.name)
        
        # Print the names in line_set
        for i in line_set:
            print(i)

    def print_stations(self):
        print("Available Stations from", self.name)
        # Print the name of each SubwayStation in stations
        for i in self.stations:
            print(i.name)

def create_connection(subway_station, subway_line):
    subway_station.lines.append(subway_line)    # Add subway_line to subway_station's lines list
    subway_line.stations.append(subway_station) # Add subway_station to subway_line's stations list

# This function will take a SubwayStation and return a list of the immediate intersection SubwayStations
# -- ones with 2 or more SubwayLines on them.
def explore_station(current_station):
    intersections = []

    # For each line in current_station
    for i in current_station.lines:
        # For each station in the line
        for j in i.stations:
            present = False
            # If station is an intersection
            if len(j.lines) > 1:
                # and is not current_station
                if j.name is not current_station.name:
                    # Check if station is already in intersections
                    for k in intersections:
                        if k.name is j.name:
                            present = True
                    # If not, add to intersections
                    if present is False:
                        intersections.append(j)
    
    return intersections

# This function will take a SubwayStation and check if it is in the explored set.
def check_if_explored(current_station):
    for i in explored:
        if current_station is i:
            return True
    
    return False

# This function will take two SubwayStations: a start and a goal, and perform a BFS
# search through the subway system in order to find the goal station. 
def bfs_search(start_station, goal_station):
    bfs = []                    # Queue used to store states  
    previous_station = None     # Will keep track of the previously explored station

    bfs.append(start_station)
    # Loop through queue while there are stations to explore 
    while len(bfs) is not 0:
        current_station = bfs.pop(0)
        # Check if the current station is on the same line as the goal station
        if compare_lines(current_station, goal_station):
            print "Target Station Found"
            return

        # If the current station is unexplored,
        if not check_if_explored(current_station):
            # get its neighboring intersections
            intersections = explore_station(current_station)
            for i in intersections:
                if previous_station is None: # this check is only used for the first loop
                    bfs.append(i)
                # Only add stations that the previously explored one couldn't reach
                elif compare_lines(i, previous_station) is False:
                    bfs.append(i)
            # Add current station to explored set
            explored.add(current_station)
        
        previous_station = current_station
    
    print "Target Station Not Found" # reached when bfs is empty and goal hasn't been found

# This function will take two SubwayStations and iterates and compares their lines values
# to see if they share a line
def compare_lines(current_station, other_station):
    # 
    for i in current_station.lines:
        for j in other_station.lines:
            if i is j:
                return True
    return False

# ======= Start of Creating Problem Space =======

# Create Stations
harvard_square = SubwayStation("Harvard Square")
central_square = SubwayStation("Central Square")
kendall_square = SubwayStation("Kendall Square")
park_street = SubwayStation("Park Street")
boston_u = SubwayStation("Boston U")
copley_square = SubwayStation("Copley Square")
washington = SubwayStation("Washington")
south_station = SubwayStation("South Station")
north_station = SubwayStation("North Station")
haymarket = SubwayStation("Haymarket")
government_center = SubwayStation("Government Center")
wood_island = SubwayStation("Wood Island")
airport = SubwayStation("Airport")
aquarium = SubwayStation("Aquarium")
state = SubwayStation("State")

# Create Lines
red_line = SubwayLine("Red Line")
orange_line = SubwayLine("Orange Line")
green_line = SubwayLine("Green Line")
blue_line = SubwayLine("Blue Line")

# Create Connections for Red Line
create_connection(harvard_square, red_line)
create_connection(central_square, red_line)
create_connection(kendall_square, red_line)
create_connection(park_street, red_line)
create_connection(washington, red_line)
create_connection(south_station, red_line)

# Create Connections for Orange Line
create_connection(north_station, orange_line)
create_connection(haymarket, orange_line)
create_connection(state, orange_line)
create_connection(washington, orange_line)

# Create Connections for Green Line
create_connection(north_station, green_line)
create_connection(haymarket, green_line)
create_connection(government_center, green_line)
create_connection(park_street, green_line)
create_connection(copley_square, green_line)
create_connection(boston_u, green_line)

# Create Connections for Blue Line
create_connection(wood_island, blue_line)
create_connection(airport, blue_line)
create_connection(aquarium, blue_line)
create_connection(state, blue_line)
create_connection(government_center, blue_line)

# ======= End of Creating Problem Space =======

bfs_search(harvard_square, wood_island)