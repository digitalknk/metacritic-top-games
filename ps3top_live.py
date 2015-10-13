"""This script allows a user to retrieve the top games listed on the PS3 metacritic page."""

# Please install Python 3, pip install beautifulsoup4 flask

import urllib.request
import json
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)

# URL that you want to grab the top games from. You could also change the url to playstation-4 as well.
url = "http://www.metacritic.com/game/playstation-3/"

# Must assign a user agent otherwise metacritic just gives you the hand.
# We combine both the URL and the user agent.
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 \
                                            (Macintosh; Intel Mac OS X 10_10_3) \
                                            AppleWebKit/537.36 (KHTML, like Gecko) \
                                            Chrome/42.0.2311.90 Safari/537.36'})

# Let's go ahead and open that url
page = urllib.request.urlopen(req)

# Let BeautifulSoup eat and digest the url that was just requested.
soup = BeautifulSoup(page.read())

#
# above is required
#

# Selectively grab the sections of the site that we want to scrap.
game_titles = soup.select('h3.product_title')
game_scores = soup.select('.basic_stat.product_score span')

# Prepare for the arrays by creating empty arrays.
titles = []  # for Game Titles
scores = []  # for Game Scores
jsondata = []  # for the json array

# A loop block so we can add the titles only into the array
for title in game_titles:
    for t in title:
        titles.append(t.string)

# A loop block so we can add the scores only into the array
for score in game_scores:
    for s in score:
        scores.append(s.string)

# Combine (zip) and append titles along with scores into a json friendly format that can be encoded.
for a, b in zip(titles, scores):
    datazip = {'title': a, 'score': b}
    jsondata.append(datazip)

# Lets set a path/route for index
@app.route('/')
def api_root():
    return 'Hi!'

# Did someone say games? This will grab the json data that we created above and spit it on the browser in a json format.
@app.route('/games', methods = ['GET'])
def api_games():
    resp = jsonify(results=jsondata)

    return resp

# This allows you to display a game title's json data specifically. If a game title is not found it just displays a black json array.
@app.route('/games/<game_title>', methods = ['GET'])
def api_game_title(game_title):
    jd = json.dumps(jsondata)
    dict = json.loads(jd)
    gt = ([o for j in dict if(j['title'] == game_title)])

    return jsonify(results=gt)

# flask do you stuff
if __name__ == '__main__':
    app.run()