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

    cursor = db.cursor()
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    teams = cursor.fetchall()
    print ("-- DISPLAYING PLAYERS AFTER INSERT --")
    for team in teams:
        print ("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0], team[1], team[2], team[3]))

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    teams = cursor.fetchall()
    print ("-- DISPLAYING PLAYERS AFTER UPDATE --")
    for team in teams:
        print ("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0], team[1], team[2], team[3]))

    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    teams = cursor.fetchall()
    print ("-- DISPLAYING PLAYERS AFTER DELETE --")
    for team in teams:
        print ("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0], team[1], team[2], team[3]))



    input("\n\n Press any key to continue...")



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)
    
finally:
    db.close()
