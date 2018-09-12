import json

from api import PocketTornado
import database
import security


app = PocketTornado()
app.default_content = "application/json"


@app.post("/authenticate")
def admin(data):
    usr = security.validateUser(data["ccid"], data["passwd"])
    if usr:
        return json.dumps(usr)
    return PocketTornado.UNAUTHORIZED


