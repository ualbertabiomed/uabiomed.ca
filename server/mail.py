import requests

api_key = ""

def use_api_key(func):
    def inner(*args, **kwargs):
        global api_key
        if api_key == "":
            with open(".mailgun_apikey", "r") as f:
                api_key = f.readline().strip()
        return func(*args, **kwargs)
    return inner

@use_api_key
def send_message(subject, text, to):
    return requests.post(
        "https://api.mailgun.net/v3/mg.uabiomed.ca/messages",
        auth=("api", api_key),
        data={"from": "Jacobs Recruitment Service <recruiterator@mg.uabiomed.ca>",
              "to": to, "subject": subject, "text": text})

if __name__ == "__main__":
    print(send_message("Hello", "Peter", ["peter@reckhard.ca", "jacob@reckhard.ca"]))
