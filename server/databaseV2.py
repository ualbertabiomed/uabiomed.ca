import pymysql.cursors
import security
from datetime import datetime

CONFIRMED = 1
UNCONFIRMED = 0

def getConnection():
    usr = ''
    passwd = ''
    database = ''
    with open('C:\\UAB\\uabiomed.ca\\server\\.database_info', 'r') as f:
        database = f.readline().strip()
        usr = f.readline().strip()
        passwd = f.readline().strip()
    try:
        connection = pymysql.connect(host='localhost',
                                 user=usr,
                                 password=passwd,
                                 db=database,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        return connection
    except pymysql.err.OperationalError as e:
        print("Could not connect to database")

# Base

def getByX(conn, table, col, val):
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM {table} WHERE {col} = %s;"
        cursor.execute(sql, (str(val)))
        result = cursor.fetchone() # Is this getting only the first result? what happens if col=val matches multiple
        return result

def createX(conn, table, vals: dict):
    with conn.cursor() as cursor:
        sql = f"INSERT INTO {table} {', '.join(vals.keys())} VALUES {', '.join(['%s']*len(vals))}"
        cursor.execute(sql, tuple(vals.values()))

def editByX(conn, table, col, val, changeCol, newVal):
    with conn.cursor() as cursor:
        sql = f""

def deleteByX(conn, table, col, val):
    pass

# People

def getPersonByX(conn, col, val):
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM users WHERE {col} = %s;"
        cursor.execute(sql, (str(val)))
        result = cursor.fetchone()
        return result

def createPerson(conn, ccid, first_name, last_name, team_ids, role_ids, active=True, admin=False, notes="NotesTest"):
    with conn.cursor() as cursor:
        pic = ""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO users (ccid, first_name, last_name, team_ids, role_ids, active, admin, notes, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (ccid, first_name, last_name, team_ids, role_ids, int(active), int(admin), notes, timestamp))
        # salt = security.getSalt()
        # hsh = security.getHash(str(ccid), salt)
        # sql = "INSERT INTO passwords (ccid, hash, salt) VALUES (%s, %s, %s)"
        # cursor.execute(sql, (ccid, hsh, salt))
    conn.commit()

def editPerson(conn, fname, lname, ccid, rank, status):
    with conn.cursor() as cursor:
        sql = "REPLACE INTO users (fname, lname, ccid, rank, status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (fname, lname, ccid, rank, str(status)))
    conn.commit()

def deletePersonByID(conn, ID):
    with conn.cursor() as cursor:
        sql = "DELETE FROM users WHERE ccid=%s;"
        cursor.execute(sql, (str(ID),))
    conn.commit()

# Teams

def getTeamByX(conn, col, val):
    pass

def getTeams(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM teams")
        return cursor.fetchall()

def createTeam(conn, name, contact_email):
    pass

def editTeam(conn, col, val, changeCol, newVal):
    pass

def deleateTeamByX(conn, col, val):
    pass

# Roles

def getRoleByX(conn, col, val):
    pass

def createRole(conn, name):
    pass

def editRoleByX(conn, col, val, changeCol, newVal):
    pass

def deleteRoleByX(conn, col, val):
    pass

# Projects

def getProjectByX(conn, col, val):
    pass

def createProject(conn, name):
    pass

def editProjectBX(conn, col, val, changeCol, newVal):
    pass

def deleteProjectByX(conn, col, val):
    pass

def getFriends(conn, ccid):
    rank = getPersonByX(conn, "ccid", ccid)["rank"][:-1]
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE rank LIKE'"+rank+"%' AND rank != '"+rank+"';"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def isSubordinate(conn, lead, member):
    p_lead = getPersonByX(conn, "ccid", lead)
    p_member = getPersonByX(conn, "ccid", member)
    return p_member["rank"].startswith(p_lead["rank"])

def getSubordinates(conn, ccid, desired_rank):
    rank = getPersonByX(conn, "ccid", ccid)["rank"]
    if desired_rank.startswith(rank):
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE rank LIKE'"+desired_rank+"%' AND rank != '"+desired_rank+"';"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    return None

def flipStatus(conn, flippie):
    person = getPersonByX(conn, "ccid", flippie)
    editPerson(conn, person["fname"], person["lname"], person["ccid"], person["rank"], (person["status"] + 1) % 2)

def getHash(conn, ccid):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM passwords WHERE ccid=%s;"
        cursor.execute(sql, (ccid,))
        result = cursor.fetchone()
        return result

def createDefaultTeams(conn):
    with conn.cursor() as cursor:
        sql = """INSERT INTO teams (name, contact_email) VALUES (%s, %s)
        """
        teams = [
            ('Mechanical Team - Arm', ''),
            ('Mechanical Team - Backpack', ''),
            ('Software Team', ''),
            ('Electrical Team', ''),
            ('Commerical Team', ''),
        ]
        cursor.executemany(sql, teams)
        conn.commit()

def clearDatabase(conn):
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("DROP TABLE IF EXISTS passwords;")
        cursor.execute("DROP TABLE IF EXISTS teams;")
        cursor.execute("DROP TABLE IF EXISTS roles;")
        cursor.execute("DROP TABLE IF EXISTS projects;")
        cursor.execute("DROP TABLE IF EXISTS project_blocks;")
    conn.commit()

def setupDatabase(conn):
    clearDatabase(conn)
    with conn.cursor() as cursor:
        sql = """
        CREATE TABLE `users` (
        `ccid` varchar(255) PRIMARY KEY,
        `first_name` varchar(255),
        `last_name` varchar(255),
        `team_ids` varchar(255),
        `role_ids` varchar(255),
        `profile_pic` blob,
        `active` boolean,
        `admin` boolean,
        `notes` varchar(255),
        `created_at` timestamp
        );
        """
        cursor.execute(sql)
        sql = """
        CREATE TABLE `passwords` (
        `ccid` varchar(255) PRIMARY KEY,
        `hash` varchar(255),
        `salt` varchar(255)
        );
        """
        cursor.execute(sql)
        sql = """
        CREATE TABLE `teams` (
        `id` int PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(255),
        `contact_email` varchar(255)
        );
        """
        cursor.execute(sql)
        sql = """
        CREATE TABLE `roles` (
        `id` int PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(255)
        );
        """
        cursor.execute(sql)
        sql = """
        CREATE TABLE `projects` (
        `id` int PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(255),
        `block_ids` varchar(255),
        `main_project` boolean,
        `priority` int
        );
        """
        cursor.execute(sql)
        sql = """
        CREATE TABLE `project_blocks` (
        `id` int PRIMARY KEY AUTO_INCREMENT,
        `text` varchar(255),
        `image` blob
        );
        """
        cursor.execute(sql)
        #createDefaultTeams(cursor)
    conn.commit()

if __name__ == "__main__":
    conn = getConnection()
    # setupDatabase(conn)
    #createPerson(conn, ccid='jboileau2', first_name='Justin', last_name='Boileau', team_ids='1', role_ids='1')
    createDefaultTeams(conn)
    
"""
# Example usage:
if __name__ == "__main__":
    conn = getConnection()
    setupDatabase(conn)
    createPerson(conn, 'Jacob', 'Reckhard', 'reckhard', '', CONFIRMED)
    createPerson(conn, 'Ben', 'Hallworth', 'hallwort', '0', CONFIRMED)

    createPerson(conn, 'Alicia', 'MacDonald', 'ammacdon', '00', CONFIRMED)
    #createPerson(conn, '', '', '', '01', CONFIRMED) # commercial lead
    createPerson(conn, 'Mohamed', 'Wadood', 'wadood', '02', CONFIRMED)
    createPerson(conn, 'Soumya', 'Thpliyal', 'thapliya', '03', CONFIRMED)

    createPerson(conn, 'Adil', 'Younus', 'younus1', '000', CONFIRMED)
    createPerson(conn, 'Wafa', 'Hossain', 'wafa', '001', CONFIRMED)
    createPerson(conn, 'Adullah', 'Iftikahar', 'aiftijha', '002', CONFIRMED)
    createPerson(conn, 'Clayton', 'Molter', 'molter', '003', CONFIRMED)
    createPerson(conn, 'George', 'Felobes', 'felobes', '003', CONFIRMED)
    #createPerson(conn, '', '', '', '004', CONFIRMED) # commercial lead



    print(getPersonByX(conn, 'ccid', 'reckhard'))
    print(getPersonByX(conn, 'ccid',  'hallwort'))
    print(getSubordinates(conn, 'ammacdon', '12'))
    print(getFriends(conn, 'ammacdon'))
    print(getSubordinates(conn, 'hallwort', ''))
    print(getFriends(conn, 'hallwort'))

    conn.close()
#"""


