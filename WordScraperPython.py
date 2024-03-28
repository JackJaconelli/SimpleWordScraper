import requests
from bs4 import BeautifulSoup

def find_specific_word(url, word):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Search for the specific word in the HTML content
        if soup.find(text=lambda text: text and word in text):
            print(f'The word "{word}" was found on the website.')
        else:
            print(f'The word "{word}" was not found on the website.')
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

# Example usage:
url_to_check = 'https://garudalinux.org/'
specific_word_to_find = 'linux'

find_specific_word(url_to_check, specific_word_to_find)
