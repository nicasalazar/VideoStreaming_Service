import yaml
import mysql.connector

def get_vids():

    with open('db_config.yaml', 'r') as f:
        db_config = yaml.safe_load(f.read())

    hostname = db_config['datastore']['hostname']
    username = db_config['datastore']['user']
    current_database = db_config['datastore']['db']
    portnumber = db_config['datastore']['port']
    pw = db_config['datastore']['password']

    db = mysql.connector.connect(host=hostname, user=username, database=current_database, port=portnumber, password=pw)

    mycursor = db.cursor()

    videos_list = []

    sql = "SELECT path FROM videos;"

    mycursor.execute(sql)

    videos = mycursor.fetchall()

    for video in videos:
        videos_list.append(video)

    return videos_list