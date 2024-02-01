# Import the modules
import requests
from bs4 import BeautifulSoup
import random

# Define a function to get the horoscope from the website
def get_horoscope(sign):
    # Construct the url with the sign parameter
    url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx"
    params = {"sign": sign}
    # Send a request and get the response
    response = requests.get(url, params=params)
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the div element that contains the horoscope text
    # This line has changed to match the new HTML structure
    div = soup.find("div", id="daily-horoscope")
    # Return the text of the paragraph element inside the div
    return div.p.text

# Define a list of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein",
    "Don't let the fear of striking out keep you from playing the game. - Babe Ruth",
    "The journey of a thousand miles begins with a single step. - Lao Tzu",
    "The most difficult thing is the decision to act, the rest is merely tenacity. - Amelia Earhart",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "Whether you think you can or you think you can't, you're right. - Henry Ford"
]

# Define a function to get a random quote from the list
def get_quote():
    # Return a random element from the list
    return random.choice(quotes)

# Ask the user to enter their zodiac sign
sign = input("Enter your zodiac sign: ")

# Get the horoscope for the sign
horoscope = get_horoscope(sign)

# Print the horoscope
print(f"Your horoscope for today is:\n{horoscope}")

# Get a random quote
quote = get_quote()

# Print the quote
print(f"Here is an inspirational quote for you:\n{quote}")

