import pymysql.cursors
import security

CONFIRMED = 1
UNCONFIRMED = 0

def getConnection():
    usr = ''
    passwd = ''
    database = ''
    with open('.database_info', 'r') as f:
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


def getPersonByX(conn, by, value):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE "+by+"=%s;"
        cursor.execute(sql, (str(value),))
        result = cursor.fetchone()
        return result

def deletePersonByID(conn, ID):
    with conn.cursor() as cursor:
        sql = "DELETE FROM users WHERE ccid=%s;"
        cursor.execute(sql, (str(ID),))
    conn.commit()

def getTeams(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM teams")
        return cursor.fetchall()


def createPerson(conn, fname, lname, ccid, rank, status):
    with conn.cursor() as cursor:
        sql = "INSERT INTO users (fname, lname, ccid, rank, status) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (fname, lname, ccid, rank, str(status)))

        salt = security.getSalt()
        hsh = security.getHash(str(ccid), salt)
        sql = "INSERT INTO passwords (ccid, hash, salt) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ccid, hsh, salt))
    conn.commit()

def editPerson(conn, fname, lname, ccid, rank, status):
    with conn.cursor() as cursor:
        sql = "REPLACE INTO users (fname, lname, ccid, rank, status) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (fname, lname, ccid, rank, str(status)))
    conn.commit()

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
    editPerson(conn, person["ccid"], person["fname"], person["lname"], person["ccid"], person["rank"], (person["status"] + 1) % 2)

def getHash(conn, ccid):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM passwords WHERE ccid=%s;"
        cursor.execute(sql, (ccid,))
        result = cursor.fetchone()
        return result

def createDefaultTeams(cur):
    sql = """INSERT INTO teams (name, id) VALUES
    ('President', '0'),

    ('Project Manager', '00'),
    ('VP Finance', '01'),
    ('VP External Relations', '02'),
    ('VP Interal Affairs', '03'),

    ('Control System Lead', '000'),
    ('Power System Lead', '001'),
    ('Structural Lead', '002'),
    ('Clinical Lead', '003'),
    ('Commercial Lead', '004'),

    ('Control System Member', '0000'),
    ('Power System Member', '0010'),
    ('Structural Member', '0020'),
    ('Clinical Member', '0030'),
    ('Commercial Member', '0040');
    """
    cur.execute(sql)

def clearDatabase(conn):
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("DROP TABLE IF EXISTS passwords;")
        cursor.execute("DROP TABLE IF EXISTS teams;")
    conn.commit()

def setupDatabase(conn):
    clearDatabase(conn)
    with conn.cursor() as cursor:
        sql = """
         CREATE TABLE users (
          fname VARCHAR(50) NOT NULL,
          lname VARCHAR(50) NOT NULL,
          ccid VARCHAR(32) NOT NULL,
          rank VARCHAR(100) NOT NULL,
          status INT NOT NULL,
          PRIMARY KEY (ccid)
        );
        """
        cursor.execute(sql)
        sql = """
         CREATE TABLE passwords (
          ccid VARCHAR(32) NOT NULL,
          hash VARCHAR(256) NOT NULL,
          salt VARCHAR(256) NOT NULL,
          PRIMARY KEY (ccid)
        );
        """
        cursor.execute(sql)
        sql = """
         CREATE TABLE teams (
          name VARCHAR(128) NOT NULL,
          id   VARCHAR(100) NOT NULL,
          PRIMARY KEY (id)
        );
        """
        cursor.execute(sql)
        createDefaultTeams(cursor)
    conn.commit()


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


