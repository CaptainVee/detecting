
#importing libraries
import pandas as pd
import datetime


#importing dataset
dataset = pd.read_csv('C:/Users/CAPTAIN VEE/Desktop/042AI/interview/Data2bots/detecting/data2bots/dataset.csv')

#Initializing some important variables
expired_date = str(datetime.date(2021, 1, 1))
dates = dataset['date']
boolean_field = []

#Check if date is expired
for date in dates:
    if date > expired_date:
        boolean_field.append(False)
    else:
        boolean_field.append(True)

dataset['obsolete'] = boolean_field

#converting to json and storing in local directory
dataset.to_json (r'C:/Users/CAPTAIN VEE/Desktop/042AI/interview/Data2bots/detecting/data2bots/dataset.csv')    
