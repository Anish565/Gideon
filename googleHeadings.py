import bs4, requests
from requests.api import head
default = "https://www.youtube.com/results?search_query="
searchKey = input("Search : ")
searchURL = default + searchKey
request_result = requests.get(searchURL)
resultText = request_result.text
soup = bs4.BeautifulSoup(resultText,"html.parser")
# print(soup)

headingObject = soup.find_all("yt-formatted-string")

# for info in headingObject:
#     print(info.getText())
#     print("-------")
    # break
print(headingObject[0].getText())
# print(headingObject[1].getText())