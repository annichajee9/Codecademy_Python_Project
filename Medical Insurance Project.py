## Medical Insurance Project
# Add your code here
# Create empty dictionary
medical_costs = {}
# Add two values into the dictionary
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
# Add multiple keys and values into the dictionary
medical_costs.update({"Connie":8886.0, "Isaace":16444.0, "Valentina":6420.0})
print(medical_costs)
#Update the correct value to Vinay
medical_costs["Vinay"] = 3325.0
print(medical_costs)
#Calculate the average medical cost of each patient
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
print(total_cost)
# Calculate the average cost
average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")
# List Comprehension
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]
# map two lists together
zipped_ages = list(zip(names, ages))
names_to_ages = {}
print(zipped_ages)
# loop through the merged list and add each valuee to new dictionary
for name, age in zipped_ages:
  names_to_ages[name] = age
print(names_to_ages)
# Collect the Marina's age and store it in new variable
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}")
# Create a medical database
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
print(medical_records)
medical_records.update({"Vinay":{"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}, "Connie":{"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}, "Isaac":{"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}, "Valentina":{"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})
print(medical_records)
# Access to a specific data
X = medical_records["Connie"].get("Insurance_cost")
print(f"Connie's insurance cost is {X} dollars.")
# Romove Vinay from medical_records
medical_records.pop("Vinay")
print(medical_records)
# Iterate through items in medical_records
for Name, record in medical_records.items():
  print(f"{Name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}\n")
# Extra Practice
# Create a function for update the medical records
def updated_medical_records(name, medical_data):
  medical_records[name] = medical_data
  return medical_records
# If you want to enter the medical data, so please input the dictionary of medical dat include age, sex, BMI, childre, smoker_status, Insurance_cost
# Testing function 
print(updated_medical_records("Annicha", {"Age": 22, "Sex": "Female", "BMI": 32.3, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3500.0}))