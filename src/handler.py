import json
import os
from plurk_oauth import PlurkAPI
from dotenv import load_dotenv

def hello(event, context):
    load_dotenv()
    plurkAPI = PlurkAPI(os.environ['PLURK_APP_KEY'], os.environ['PLURK_SECRET'])
    plurkAPI.authorize(os.environ['PLURK_ACCESS_TOKEN'], os.environ['PLRUK_ACCESS_SECRET'])

    query = os.environ['QUERY']
    max_size = int(os.environ['MAX_SIZE'])
    offset = 0
    while offset < max_size:
        results = plurkAPI.callAPI('/APP/PlurkSearch/search',
                                   options={'query': query, 'offset' : offset});
        filtered = list(filter(sould_replurk , results['plurks']))
        if not filtered:
            break
        plurk_ids =  list(map(lambda x : x['plurk_id'], filtered))
        #print(plurk_ids)
        plurkAPI.callAPI('/APP/Timeline/replurk',
                         options={'ids': json.dumps(plurk_ids)})
        offset += results['last_offset']


def sould_replurk(data) -> bool:
    return data['replurkable'] and not data['replurked']


if __name__ == "__main__":
    hello('', '')
