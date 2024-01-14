## packages part of requirements.txt
## should be able to successfully import these
## else install pyodbc, dotenv and pandas
## create a .env that contains database credentials

import pyodbc
from dotenv import dotenv_values
import pandas as pd

# Load environment variables from .env file into a dictionary
environment_variables = dotenv_values("../../.env")

# Get the values for the credentials you set in the '.env' file
server = environment_variables.get("SERVER")
database = environment_variables.get("DATABASE")
username = environment_variables.get("USERNAME")
password = environment_variables.get("PASSWORD")

# Create a connection string
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;"

# create connection object
connection = pyodbc.connect(connection_string)

query = "SELECT * FROM "

# read data from database
oil = pd.read_sql(query + "dbo.oil", connection)
holiday_events = pd.read_sql(query + "dbo.holidays_events", connection)
stores = pd.read_sql(query + "dbo.stores", connection)

# save data to csv files
oil.to_csv("../../data/raw/oil.csv")
holiday_events.to_csv("../../data/raw/holiday_events.csv")
stores.to_csv("../../data/raw/stores.csv")
