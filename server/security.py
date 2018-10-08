import os
import sha3
import json
import database
import base64

def getSalt():
    """
    Returns the salt
    """
    salt = sha3.sha3_512(str(os.urandom(64)).encode('utf-8'))
    # 64 bytes of randomness, as sha512 produces a length of 64 bytes
    return salt.hexdigest()

def getHash(passwd, salt):
    """
    Returns sha3_512 hash of the passwd concated to the string
    """
    return sha3.sha3_512((passwd + salt).encode('utf-8')).hexdigest()

def genToken(data, secret):
    tok = data + "~" + getHash(data, secret)
    return base64.encodestring(tok.encode('utf-8')).decode('utf-8').strip()

def validateToken(tok, secret):
    inp = base64.decodebytes(tok.encode('utf-8')).decode('utf-8')
    data = inp.split('~')
    hsh = getHash(data[0], secret)
    return hsh == data[1]

def getUserFromToken(tok, secret):
    if validateToken(tok, secret):
        inp = base64.decodebytes(tok.encode('utf-8')).decode('utf-8')
        data = json.loads(inp.split('~')[0])
        return data["ccid"]




def validateUser(ccid, passwd):
    """
    Confirms the user is in the database, and the password is correct

    Returns the user, or null if invalid
    """

    # Inner function is used so there is a single exit point
    # this makes it easy to clean up the datebase connection
    def inner(conn, ccid, passwd):
        usr = database.getHash(conn, ccid)
        if usr is None:
            return

        if getHash(passwd, usr["salt"]) != usr["hash"]:
            return

        return database.getPersonByX(conn, "ccid", usr["ccid"])

    conn = database.getConnection()
    usr = inner(conn, ccid, passwd) # inner is the function defined above
    conn.close()

    return usr


"""
if __name__ == "__main__":
    print(validateUser('reckhard', '1497646'))
    print(validateUser('notreckhard', '1497646'))
    print(validateUser('reckhard', 'badpassword'))
"""
