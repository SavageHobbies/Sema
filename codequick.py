# Import the necessary libraries
import requests

# Make a GET request to the quote API
response = requests.get("https://api.quotable.io/random")

# Check if the request was successful
if response.status_code == 200:
    # Retrieve the quote from the response
    quote = response.json()["content"]
    
    # Print the quote
    print(quote)
else:
    # Print an error message if the request failed
    print("Unable to retrieve a quote at the moment. Please try again later.")