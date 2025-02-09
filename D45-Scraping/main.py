from bs4 import BeautifulSoup
import lxml


with open('./website.html') as web_file:
    content = web_file.read()

soup = BeautifulSoup(content, 'html.parser' )
soup.find_all(name='a')

# CSS Selector
soup.select(selector="p a li") ## all li elements in anchor tag in p tag
soup.select_one(selector="#title")

form = soup.find('form')
form.ge
# print(soup.li)