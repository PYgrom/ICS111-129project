'''\
riot_gameVersion.py

This version:
    0. Load JSON
    1. Find "gameversion" and create Dataframe
'''\

import json

import pandas as pd

import sqlite3

JSON_EXTRACT_FILE = 'test.json'

with open(JSON_EXTRACT_FILE, 'r') as json_read:
    jsd = json.load(json_read)
    
#type(jsd)
#print(jsd.keys())

gameVER = jsd['gameVersion']
#print(gameVER)

dict_gameVER = {'Game Version':[gameVER]}
#print(df_gameVER)

df_gameVER = pd.DataFrame(data=dict_gameVER)
#print(df_gameVER)

conn = sqlite3.connect('etlproject.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS gameVersion (gameVersion)")
conn.commit()

df_gameVER.to_sql('gameVersion', conn, if_exists='replace', index=False)

c.execute('''
SELECT * FROM gameVersion
        ''')

for row in c.fetchall():
    print(row)
