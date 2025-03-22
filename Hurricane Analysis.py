## Hurricane Analysis
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
# Define the function to replace 'M' and 'B' with the values in conversion variable
def unit_conversion(damages):
    updated_damages = []
    for item in damages:
        if 'M' in item:
            value = float(item.replace('M', '')) * conversion['M']
            updated_damages.append(value)
        elif 'B' in item:
            value = float(item.replace('B', '')) * conversion['B']
            updated_damages.append(value)
        else:
            updated_damages.append(item)
    return updated_damages

# Convert damages
damage = unit_conversion(damages)

# 2 
# Create a title list
def combined_list():
    titles = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Damage", "Deaths"]
    element = list(zip(names, months, years, max_sustained_winds, areas_affected, damage, deaths))
    hurricanes_list = []
    for j in element:
        hurricane_dict = dict(zip(titles, j))
        hurricanes_list.append(hurricane_dict)
    return hurricanes_list

# 3
# Organizing by Year
def generate_by_year():
  # create a new dictionary of hurricanes with year and key
  new_dict = {}
  for values in combined_list():
    year = values["Year"]
    if year not in new_dict:
      new_dict[year] = []
    new_dict[year].append(values)
  return new_dict
#print(generate_by_year())

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
hurricanes_list = combined_list()
def count_affected_areas(hurricanes_list):
    # Initialize an empty dictionary to store area counts
    area_count = {}
    
    # Iterate through each hurricane
    for hurricane in hurricanes_list:
        # Iterate through each affected area for the hurricane
        for area in hurricane['Areas Affected']:
            # Check if the area is already in the dictionary
            if area not in area_count:
                area_count[area] = 1  # Initialize count
            else:
                area_count[area] += 1  # Increment count
    
    return area_count
#print(count_affected_areas(hurricanes_list))

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def most_affected_areas():
  max_count = float("-inf")
  for value in count_affected_areas(hurricanes_list).values():
    if value > max_count:
      max_count = value
    most_affected_city = count_affected_areas(hurricanes_list).get(max_count)
  return (f"The most affected city is {most_affected_city} which has {max_count} hurricanes.")
#print(most_affected_areas())

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def find_deadliest_hurricane(hurricanes):
    # Initialize variables to track the deadliest hurricane
    max_mortality_cane = None
    max_mortality = 0
    
    # Iterate through each hurricane
    for hurricane in hurricanes:
        # Get the number of deaths for the current hurricane
        deaths = hurricane['Deaths']
        
        # Check if this hurricane has more deaths than the current maximum
        if deaths > max_mortality:
            max_mortality = deaths
            max_mortality_cane = hurricane['Name']
    
    return max_mortality_cane, max_mortality

# Assuming hurricanes_list is the list of hurricane dictionaries
deadliest_hurricane, death_count = find_deadliest_hurricane(combined_list())
print(f"The deadliest hurricane is {deadliest_hurricane} with {death_count} deaths.")

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# categorize hurricanes in new dictionary with mortality severity as key
def mortality_scale_hurricane_rate():
    hurricane_rate = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in combined_list():
        deaths = hurricane["Deaths"]
        for scale, upper_bound in mortality_scale.items():
            if deaths > upper_bound:
                continue
            hurricane_rate[scale].append(hurricane)
            break
    return hurricane_rate

# Test the function
print(mortality_scale_hurricane_rate())

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def find_most_damaging_hurricane(hurricanes):
    max_damage_cane = None
    max_damage = 0
    for hurricane in hurricanes:
        damage = hurricane['Damage']
        if damage != "Damages not recorded" and damage > max_damage:
            max_damage = damage
            max_damage_cane = hurricane['Name']
    return max_damage_cane, max_damage

# Test the function
most_damaging_hurricane, damage_amount = find_most_damaging_hurricane(combined_list())
print(f"The most damaging hurricane is {most_damaging_hurricane} with a damage cost of ${damage_amount}.")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def rate_hurricanes_by_damage(hurricanes):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes:
        damage = hurricane['Damage']
        if damage == "Damages not recorded":
            continue
        for scale, upper_bound in damage_scale.items():
            if damage > upper_bound:
                continue
            hurricanes_by_damage[scale].append(hurricane)
            break
    return hurricanes_by_damage
# Testing function
hurricanes_by_damage = rate_hurricanes_by_damage(combined_list())
print(hurricanes_by_damage)