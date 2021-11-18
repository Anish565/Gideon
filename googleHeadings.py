import bs4, requests
default = "https://google.com/search?q="
searchKey = input("Search : ")
searchURL = default + searchKey + "song name"
request_result = requests.get(searchURL)
resultText = request_result.text
soup = bs4.BeautifulSoup(resultText,"html.parser")
# print(soup)

headingObject = soup.find_all("h3")

for info in headingObject:
    print(info.getText())
    print("-------")
    # break

# print(headingObject[1].getText())