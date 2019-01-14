import requests
import sys
import re
from bs4 import BeautifulSoup


def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  #gotta go regular html scraping... come on Genius
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  #remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  #at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
  return lyrics

base_url = "https://api.genius.com"
token = 'x-AYGuvO4bJIogvvm4Ewzqjv5V8biszg_-0TGGLTcDAUVA7xncCu7oj2BiyFfo52'
headers = {'Authorization': 'Bearer {}'.format(token)}
search_url = base_url + "/search"
artist_name = "The Beatles"
genre = "rap"
# song_title = "Smells Like Teen Spirit"
params = {'q': artist_name}

response = requests.get(search_url, params=params, headers=headers)
json = response.json()

# print(json)

# songs_infos = None
songs_infos = []
for hit in json["response"]["hits"]:
    print("hit")
    if hit["result"]["primary_artist"]["name"] == artist_name:
        # songs_infos = hit
        print("artist found")
        songs_infos.append(hit)
        # break

print("no hits")

if songs_infos:
    i = 0
    print("there are song infos")
    for song in songs_infos:
        if i == 6:
            sys.exit()
        song_api_path = song["result"]["api_path"]
        lyrics = lyrics_from_song_api_path(song_api_path)
        # print(lyrics)

        s = lyrics.split('\n')
        s = [line for line in s if not line.startswith('[')]
        print(" ".join(s))
        s = " ".join(s)
        s = s + " "
        # fname = "Kanye"
        fname = "Rihanna"
        # fname = artist_name
        fname = "corpora/" + fname + ".txt"
        # fname = "corpora/" + genre + ".txt"
        # print(fname)

        sentence_1 = re.sub(r'[^a-zA-Z0-9\' ]', '', s) + "."

        with open(fname, "a") as my_file:
            my_file.write(s)
        i += 1

print("no song info")
