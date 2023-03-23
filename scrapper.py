import requests as re
from bs4 import BeautifulSoup as bs

YOUTUBE_TRENDING_PAGE_URL = 'https://www.youtube.com/feed/trending'
response = re.get(YOUTUBE_TRENDING_PAGE_URL)
print('The status code of the page : ', response.status_code)

# Now we wil parse the webpage using Beaut8ifulSoup

trending_doc = bs(response.text, 'html.parser')
print('The title of the page is: ', trending_doc.title.text)


