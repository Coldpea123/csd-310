import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "C01D&y18",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)


    print("\n   Database user   {}  connected to MySQL on host {}   with database   {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()
    for team in teams:
        print ("-- DISPLAYING TEAM RECORDS --\nTeam ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))


    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
    for player in players:
        print("--DISPLAYING PLAYER RECORDS --\nPlayer ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}".format(player[0], player[1], player[2], player[3]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)
    
finally:
    db.close()
