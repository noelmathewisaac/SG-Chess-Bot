#telegram bot named "@botfather" will help create a bot and generate the token
token="<Telegram_Bot_Token>" 

#Visit dialogflow.com
apiai_token="<Dialogflow_API_Token>" 

#Create a postgres database hosted online and get the database_url
#Note: You have to create 2 tables in the database with the following commands for the bot to work:
"""CREATE TABLE IF NOT EXISTS Notifications(
   chat_id INTEGER PRIMARY KEY, 
   Tournament_1 TEXT, 
   Days_left_1 INTEGER, 
   Tournament_2 TEXT, 
   Days_left_2 INTEGER,
   Tournament_3 TEXT, 
   Days_left_3 INTEGER,
   Tournament_4 TEXT, 
   Days_left_4 INTEGER,
   Tournament_5 TEXT, 
   Days_left_5 INTEGER,
   Tournament_6 TEXT, 
   Days_left_6 INTEGER);
"""
"""CREATE TABLE IF NOT EXISTS Userdata(
       chat_id INTEGER PRIMARY KEY, 
       first_name TEXT,
       last_name TEXT,
       username TEXT);"""

database_url="<Postgres_Database_Url>"