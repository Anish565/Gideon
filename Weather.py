import bs4, requests

def find_weather(city):
    
    # city = input("City : ")
    searchUrl = "https://google.com/search?q=weather+in+" + city

    request_result = requests.get(searchUrl)
    soup = bs4.BeautifulSoup(request_result.text,"html.parser")

    temp = soup.find("div", class_='BNeawe').text
    # print(temp)
    return temp