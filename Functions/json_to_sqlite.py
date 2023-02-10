import sqlite3
import json
import pandas as pd


# function to create geos sql table
def geos_json_to_sql(filename):
# Open JSON data
    with open(filename) as f:
        data = json.load(f)
# scrape json file to collect the meta_data
    list_df = []
    years = list(data["ABI-L1b-RadC"].keys())

    for year in years[1:]:
        for day in list(data["ABI-L1b-RadC"][year].keys())[1:]:
            for hour in list(data["ABI-L1b-RadC"][year][day].keys())[1:]:
                list_df.append(tuple(("ABI-L1b-RadC",year,day,hour)))

# create dataframe
    geos_df = pd.DataFrame(list_df,columns=["station","year","day","hour"])
# create table in the sqlite databae
    cursor.execute("CREATE TABLE IF NOT EXISTS geos (station TEXT,  year INTEGER, day INTEGER, hour INTEGER, CONSTRAINT PK_geos PRIMARY KEY (station,year,day,hour))")   
# Insert geos_df into sqlite table geos 
    geos_df.to_sql('geos', connection, if_exists='replace', index = False)
    connection.commit()

# function to create nexrad sql table
def nexrad_json_to_sql(filename):
    with open(filename) as f:
        data = json.load(f)


    list_df = []
    for year in data.keys():
        for month in list(data[year].keys())[1:]:
            for day in list(data[year][month].keys())[1:]:
                for station in list(data[year][month][day].keys())[1:]:
                    list_df.append(tuple((year,month,day,station)))

# create dataframe
    nexrad_df = pd.DataFrame(list_df,columns=["year","month","day","station"])

# create table in the sqlite databae
    cursor.execute("CREATE TABLE IF NOT EXISTS nexrad (year INTEGER, month INTEGER, day INTEGER, station TEXT, CONSTRAINT PK_nexrad PRIMARY KEY (year,month,day,station))")   
# Insert geos_df into sqlite table nexrad
    nexrad_df.to_sql('nexrad', connection, if_exists='replace', index = False)
    connection.commit()


# create sqlite database    
connection = sqlite3.connect("../streamlit/meta_data.db")
cursor = connection.cursor()


geos_json_to_sql("../Metadata/GEOS.json")
nexrad_json_to_sql("../Metadata/NexRad.json")

