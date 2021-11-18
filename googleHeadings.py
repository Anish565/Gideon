import bs4, requests
# default = "https://google.com/search?q="
default = "https://www.youtube.com/results?search_query="

searchKey = input("Search : ")
searchURL = default + searchKey
request_result = requests.get(searchURL)
resultText = request_result.text
soup = bs4.BeautifulSoup(resultText,"html.parser")
# print(soup)

headingObject = soup.find_all("h3,div")

# for info in headingObject:
#     print(info.getText())
#     print("-------")
    # break

# print(headingObject[1].getText())

# import urllib
# import simplejson

# id = 'KQEOBZLx-Z8'
# url = "https://www.youtube.com/results?search_query=baby+pull+me+closer" % id

# json = simplejson.load(urllib.urlopen(url))

# title = json['entry']['title']['$t']
# author = json['entry']['author'][0]['name']

# print("id:%s\nauthor:%s\ntitle:%s" % (id, author, title))
