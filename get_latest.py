import requests
import json
import argparse

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "YOUR_TWITTER_BEARER_TOKEN"

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True, help='The username of the Twitter user')
args = parser.parse_args()

def create_url():
    tweet_fields = "tweet.fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    query = "query=from:" + args.username  # Replace this with the search query you want to use
    max_results = "max_results=10"  # Change this to specify the number of tweets to retrieve
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}&{}".format(query, max_results, tweet_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    title = """
    
  _______ _               _______       _ _   _               _____ _      _____ 
 |__   __(_)             |__   __|     (_) | | |             / ____| |    |_   _|
    | |   _ _ __  _   _     | |_      ___| |_| |_ ___ _ __  | |    | |      | |  
    | |  | | '_ \| | | |    | \ \ /\ / / | __| __/ _ \ '__| | |    | |      | |  
    | |  | | | | | |_| |    | |\ V  V /| | |_| ||  __/ |    | |____| |____ _| |_ 
    |_|  |_|_| |_|\__, |    |_| \_/\_/ |_|\__|\__\___|_|     \_____|______|_____|
                   __/ |                                                         
                  |___/                                                          
                                                                                                                                               
    """
    print(title)
    for object in json_response['data'][::-1]:
        print(args.username + " " + object['text'])
        print("https://twitter.com/" + args.username + "/status/" + object['id'] + '\n')
        


if __name__ == "__main__":
    main()
