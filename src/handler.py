import json
import os
from plurk_oauth import PlurkAPI
from dotenv import load_dotenv

def hello(event, context):
    load_dotenv()
    plurk = PlurkAPI(os.environ['PLURK_APP_KEY'], os.environ['PLURK_SECRET'])
    plurk.authorize(os.environ['PLURK_ACCESS_TOKEN'], os.environ['PLRUK_ACCESS_SECRET'])
    print(plurk.callAPI('/APP/Users/me'))

if __name__ == "__main__":
    hello('', '')
