import pymysql.cursors
import security

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
        sql = "DELETE FROM users WHERE stuid=%s;"
        cursor.execute(sql, (str(ID),))
    conn.commit()

def createPerson(conn, stuid, fname, lname, ccid, rank):
    with conn.cursor() as cursor:
        sql = "INSERT INTO users (stuid, fname, lname, ccid, rank) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (str(stuid), fname, lname, ccid, rank))

        salt = security.getSalt()
        hsh = security.getHash(str(stuid), salt)
        sql = "INSERT INTO passwords (ccid, hash, salt) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ccid, hsh, salt))
    conn.commit()

def editPerson(conn, stuid, fname, lname, ccid, rank):
    with conn.cursor() as cursor:
        sql = "REPLACE INTO users (stuid, fname, lname, ccid, rank) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (str(stuid), fname, lname, ccid, rank))
    conn.commit()

def getFriends(conn, stuid):
    rank = getPersonByID(conn, stuid)["rank"][:-1]
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE rank LIKE'"+rank+"%' AND rank != '"+rank+"';"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def getSubordinates(conn, stuid):
    rank = getPersonByID(conn, stuid)["rank"]
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE rank LIKE'"+rank+"%' AND rank != '"+rank+"';"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def getHash(conn, ccid):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM passwords WHERE ccid=%s;"
        cursor.execute(sql, (ccid,))
        result = cursor.fetchone()
        return result


def clearDatabase(conn):
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("DROP TABLE IF EXISTS passwords;")
    conn.commit()

def setupDatabase(conn):
    clearDatabase(conn)
    with conn.cursor() as cursor:
        sql = """
         CREATE TABLE users (
          stuid INT NOT NULL,
          fname VARCHAR(50) NOT NULL,
          lname VARCHAR(50) NOT NULL,
          ccid VARCHAR(32) NOT NULL,
          rank VARCHAR(100) NOT NULL,
          PRIMARY KEY (stuid)
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
    conn.commit()


"""
# Example usage:
if __name__ == "__main__":
    conn = getConnection()
    setupDatabase(conn)
    createPerson(conn, 1234567, 'Testa', 'McTester', 'mctest', '12')
    createPerson(conn, 7654321, 'Tester', 'McTestface', 'mcface', '234')
    editPerson(conn, 1234567, 'Testa', 'McTester', 'mctest', '1')
    createPerson(conn, 2374943, 'Test3', 'McTester', 'mctest1', '11')
    createPerson(conn, 2493529, 'Test4', 'McTester', 'mctest2', '12')
    createPerson(conn, 9093272, 'Test5', 'McTester', 'mctest3', '13')
    createPerson(conn, 1497646, 'Jacob', 'Reckhard', 'reckhard', '')

    print(getPersonByID(conn, 1234567))
    print(getPersonByID(conn, 7654321))
    print(getSubordinates(conn, 1234567))
    print(getFriends(conn, 2374943))
    print(getSubordinates(conn, 1497646))
    print(getFriends(conn, 1497646))

    conn.close()
"""


