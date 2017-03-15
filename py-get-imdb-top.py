import urllib.request
from bs4 import BeautifulSoup

#open the IMDb Top films page
url = "http://www.imdb.com/chart/top"
http_req = urllib.request.urlopen(url)

#parse the HTML content, find the HTML container with the table with Top films, extract the titles from the container
parsed_html = BeautifulSoup(http_req, "html.parser")
filmsTable = parsed_html.body.find("tbody", {"class" : "lister-list"})
titles = filmsTable.find_all("td", {"class" : "titleColumn"})

#extract and put into a list of dictionaries holding the position, the name and the year for each film
topFilms = []
for title in titles:
    titleContent = title.get_text().split("\n")
    topFilms.append({'position' : titleContent[1].strip()[:-1],
                     'name' : titleContent[2].strip(),
                     'year' : titleContent[3].strip()[1:-1]})

#print the results   
for film in topFilms:
    print(film['position'] + ". " + film['name'] + " (" + film['year'] + ")")

