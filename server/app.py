import json
import time

from api import PocketTornado
import database
import security


#app = PocketTornado(secret=security.getHash("secret", security.getSalt()))
app = PocketTornado(secret="TMP FOR TESTING")
app.default_content = "application/json"

def secure(func):
    def inner(*args, **kwargs):
        token = args[0]["token"]
        if security.validateToken(token, app.secret):
            out = func(*args, **kwargs)
            return out
        return PocketTornado.UNAUTHORIZED
    return inner

def make_secure(func):
    def inner(*args, **kwargs):
        out = func(*args, **kwargs)
        if out != PocketTornado.UNAUTHORIZED:
            data = json.loads(out)
            data["token"] = security.genToken(json.dumps(
                {"timeout": int(time.time() + app.timeout),
                    "ccid": data["ccid"]}
                ), app.secret)
        return data
    return inner


@app.post("/auth_test")
@secure
def test(data):
    return '{"Success": "True"}'

@app.post("/flipMember")
@secure
def flipMember(data):
    usr = security.getUserFromToken(data["token"], app.secret)
    flippie = data["ccid"]

    conn = database.getConnection()
    if database.isSubordinate(conn, usr, flippie):
        database.flipStatus(conn, flippie)

    conn.close()

    return '{"Success": "True"}'

@app.post("/authenticate")
@make_secure
def admin(data):
    usr = security.validateUser(data["ccid"], data["passwd"])
    if usr:
        return json.dumps(usr)
    return PocketTornado.UNAUTHORIZED

@app.get("/teams")
def getTeams():
    return_data = {}
    conn = database.getConnection()
    return_data['teams'] = database.getTeams(conn)
    conn.close()
    return return_data or PocketTornado.UNAUTHORIZED

@app.post("/getallsubordinates")
@secure
def getallsubordinates(data):
    return_data = {}
    conn = database.getConnection()
    return_data["members"] = database.getSubordinates(conn, data["ccid"], data["rank"])
    conn.close()
    return return_data or PocketTornado.UNAUTHORIZED




