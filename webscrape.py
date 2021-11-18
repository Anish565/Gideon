import newspaper
 
site = newspaper.build("https://news.ycombinator.com/")  
 
# get list of article URLs
site.article_urls()
site_article = site.articles[0]
 
site_article.download()
site_article.parse()
 
# print(site_article.text)


top_articles = []
for index in range(10):
    article = site.articles[index]
    article.download()
    article.parse()
    top_articles.append(article)
    
print(site[0].text)
 
print(site[3].text)