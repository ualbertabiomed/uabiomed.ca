import json
import time

from api import PocketTornado
import database
import security


app = PocketTornado(secret=security.getHash("secret", security.getSalt()))
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
            data["token"] = security.genToken(json.dumps({"timeout": int(time.time() + app.timeout)}), app.secret)
        return data
    return inner


@app.post("/auth_test")
@secure
def test(data):
    return '{"Success": "True"}'

@app.post("/authenticate")
@make_secure
def admin(data):
    usr = security.validateUser(data["ccid"], data["passwd"])
    if usr:
        return json.dumps(usr)
    return PocketTornado.UNAUTHORIZED

@app.post("/getallsubordinates")
@secure
def getallsubordinates(data):
    return_data = {}
    conn = database.getConnection()
    return_data["members"] = database.getSubordinates(conn, data["ccid"])
    conn.close()
    return return_data




