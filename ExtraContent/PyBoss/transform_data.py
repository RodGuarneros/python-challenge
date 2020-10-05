print("""
----------------------------------------------------------------------
                            
                    Starting the application...

----------------------------------------------------------------------
""")
# importing modules
import os
import csv

# Oppening the door to know data base
employees=os.path.join("..","DATABASE_TRANSFORMATION", "employee_data.csv")

# Transforming data following a predeterminated format:
#Creating lists for the new structure of the data base
# ¿Antes de abrir la puerta tengo que definir la base?
Emp_ID = []
First_Name = []
Last_Name = []
Date_of_Bird= []
Security_Number = []
States = []
new_DOB = []

countries_dictionary = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
 } 

# Operations with dictionary previous used has an input
with open (employees, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
#x is an observation in the table proof of data base
    # for x in csv_reader:  
    #     print(x)
    for obs in csv_reader:
        
        Emp_ID.append(obs[0]) #add ID to the list created
        
        new_complete_name = obs[1].split(" ") # split the name in a list to get every element
        First_Name.append(new_complete_name[0]) # add first name in the list
        Last_Name.append(new_complete_name[1]) # add last name in the list
        
        new_DOB = obs[2].replace("-","/")  # replace in that row (DOB)
        Date_of_Bird.append(new_DOB) # add DOB in the list
        
        new_SSN = obs[3].rsplit("-") # split the SSN in three parts 
        visual_SSN = new_SSN[2] # the last part of the list (last group of numbers)
        Security_Number.append(f"***-**-{visual_SSN}") #making a tring for the final list First_Name

        country = obs[4] 
        
        # for state, avb in countries_dictionary.items(): # Making a tuple and a conditional iteration 
        #       if state == country: # comparing state of the tuple with country in our dataset
        #         States.append(avb) # ready to finish our new framework!
        
        #List comprenhention alternative:
        [States.append(avb) for state,avb in countries_dictionary.items() if state==country] # it works!
  
  # Closing the door
cleaned_csv = zip(Emp_ID, First_Name, Last_Name, Date_of_Bird, Security_Number, States)

ouput_file = "employee_data_final.csv"

with open(ouput_file, "w", newline="") as datafile:
    csv_writer =  csv.writer(datafile)

    csv_writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]) #writing the correct header

    csv_writer.writerows(cleaned_csv) # write every row 

print("""
__________________________________________________________________________

                         We finish
__________________________________________________________________________
""")




