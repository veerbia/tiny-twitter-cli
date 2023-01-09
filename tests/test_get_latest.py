import unittest
import scripts.get_latest as get_latest

class TestGetLatest(unittest.TestCase):

    def test_create_url(self):
        # Test that the create_url() function generates the correct API endpoint URL
        url = get_latest.create_url()
        self.assertEqual(url, "https://api.twitter.com/2/tweets/search/recent?query=from:<username>&max_results=10&tweet.fields=lang,author_id")
    
    def test_connect_to_endpoint(self):
        # Test that the connect_to_endpoint() function returns a valid JSON response
        json_response = get_latest.connect_to_endpoint("https://api.twitter.com/2/tweets/search/recent")
        self.assertIsInstance(json_response, dict)
    
    def test_main(self):
        # Test that the main() function prints the expected output to the console
        with self.assertLogs() as logs:
            get_latest.main()
        self.assertIn("<username> tweet text", logs.output[0])
        self.assertIn("https://twitter.com/<username>/status/tweet_id", logs.output[0])
    
    def test_error_handling(self):
        # Test that the script handles errors and exceptions gracefully
        with self.assertRaises(Exception):
            get_latest.connect_to_endpoint("https://invalid-url")
