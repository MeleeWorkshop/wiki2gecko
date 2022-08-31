import requests_cache
import wikitextparser
from deep_get import deep_get
from parse_wiki import parse_wiki

endpoint = "https://wiki.supercombo.gg/api.php"
params = {'action': 'query',
          'format': 'json',
          'prop': 'revisions',
          'pageids': 60960,
          'utf8': 1,
          'formatversion': 2,
          'rvprop': 'content',
          'rvslots': '*'}


def main():
    session = requests_cache.CachedSession()
    response = session.get(endpoint, params=params)
    body = deep_get(response.json(), 'query', 'pages', 0, 'revisions', 0, 'slots', 'main', 'content')
    wiki = wikitextparser.parse(body)
    result = parse_wiki(wiki)


if __name__ == '__main__':
    main()
