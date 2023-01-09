# tiny-twitter-cli

A simple, lightweight Twitter CLI client written in Python.

`tiny-twitter-cli` was created as a lightweight alternative to using a web browser or a full-featured Twitter client to view a specific user's tweets. By using the command line interface, you can quickly retrieve and view the latest tweets from a user without having to worry about the distractions and overhead of a GUI. This can be especially useful for developers or power users who spend a lot of time in the terminal and want a fast, efficient way to stay updated on the tweets of a particular user.

![demo](https://user-images.githubusercontent.com/102765426/211244304-9280683a-d3d4-4257-aed6-23c60f3b6e53.png)


Description: tiny-twitter-cli is a responsive command line interface designed to retrieve and display the latest tweets from a specific Twitter user. As a developer or power user, you may find yourself spending a significant amount of time in the terminal and require a fast and efficient way to stay updated on the tweets of a particular user without the distractions and overhead of a GUI. This is where tiny-twitter-cli comes in. With tiny-twitter-cli, you can retrieve and view the latest tweets from a user simply by running a command and specifying the username as an argument. The tweets are displayed directly in the terminal, allowing you to quickly scan and stay informed without having to switch contexts or open a web browser. In addition to its speed and convenience, tiny-twitter-cli also offers a high degree of customization. The tweet_fields parameter allows you to specify which fields of the tweet object to include in the response, and the max_results parameter lets you control the number of tweets to retrieve. This allows you to tailor the output to your specific needs and preferences. tiny-twitter-cli is a powerful tool that can greatly enhance your Twitter experience by allowing you to stay up-to-date on the tweets of a specific user while working in the terminal. Its advanced features and customizable nature make it a valuable addition to any developer's toolkit.

## Requirements
- Python 3
- `requests` library
- A valid Twitter API key with the `tweet.search` permission (See details: https://developer.twitter.com/en/docs/twitter-api)

## Setup
1. Clone this repository to your local machine:
```
git clone https://github.com/user/tiny-twitter-cli.git
```
2. Navigate to the cloned repository:
```
cd tiny-twitter-cli
```
3. Set your Twitter API key as an environment variable. In your terminal, run the following command, replacing <your_bearer_token> with your actual API key:
```
export BEARER_TOKEN='<your_bearer_token>'
```
4.Run the get_latest.py script, specifying the username of the Twitter user whose tweets you want to retrieve as an argument:
```
python get_latest.py --username <username>
```

## Technical Details
The get_latest.py script uses the Recent search tweets endpoint of the Twitter API to retrieve recent tweets from a specific user. The requests library is used to make a GET request to the API, and the argparse library is used to parse the --username command line argument.

The bearer_oauth() function is used to authenticate the request using the Bearer Token authentication method, which requires setting the Authorization and User-Agent headers of the request.

The create_url() function constructs the API endpoint URL using the query and tweet_fields parameters, which allow you to specify the search query and which fields of the tweet object to include in the response, respectively. The max_results parameter can be used to specify the maximum number of tweets to retrieve.

The connect_to_endpoint() function makes the GET request to the API and returns the JSON response. The main() function loops through the tweets in the response and prints the username, tweet text, and tweet URL to the console.


## Customization
- Changing the number of tweets retrieved
By default, the max_results parameter is set to 10, which means that tiny-twitter-cli will retrieve and display the 10 most recent tweets from the specified user. You can change this value to retrieve a different number of tweets by modifying the max_results parameter in the create_url() function:

```
max_results = "max_results=20"  # Change this to specify the number of tweets to retrieve
```

- Modifying the tweet fields included in the response
The tweet_fields parameter allows you to specify which fields of the tweet object to include in the response from the Twitter API. By default, only the lang and author_id fields are included. To modify the fields included, you can modify the tweet_fields parameter in the create_url() function:

```
tweet_fields = "tweet.fields=lang,author_id,created_at,text"  # Change this to specify the tweet fields to include
```

- Changing the search query
By default, the query parameter is set to search for tweets from the specified user. You can modify the search query to specify different search criteria by modifying the query parameter in the create_url() function:

```
query = "query=from:" + args.username + " lang:en"  # Replace this with the search query you want to use
```
These are just a few examples of the customizations you can make to tiny-twitter-cli. By experimenting with different parameter values and search queries, you can tailor the output to your specific needs and preferences.

## Testing
To run the tests for the tiny-twitter-cli project, you will need to have the necessary dependencies installed. You can install these dependencies by running the following command:

```
pip install -r requirements.txt
```
This will install the Python libraries listed in the requirements.txt file, which are required to run the tests.

Once the dependencies are installed, you can run the tests using the unittest command-line interface:

```
python -m unittest discover
```
This will discover and run all the test functions in the tests/ directory and report on their results.

You can also use a tool like pytest to run the tests. To do this, you will need to install pytest and any additional plugins that you want to use:

```
pip install pytest pytest-cov
```
Then, you can run the tests using the pytest command:

```
pytest
```
This will run all the test functions in the tests/ directory and report on their results. You can also use the --cov flag to generate a test coverage report:

```
pytest --cov=get_latest
```
This will show you which lines of code in the get_latest.py script are covered by the tests and which ones are not.

I hope this gives you an idea of how to run the tests for the tiny-twitter-cli project. Let me know if you have any questions or need further assistance!


## License
This project is licensed under the MIT License - see the LICENSE.md file for details




