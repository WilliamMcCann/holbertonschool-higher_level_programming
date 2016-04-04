import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 7787fe0886a53bdf16c980bb319fb09a93e2b59d'
}

import urllib2
content = urllib2.urlopen('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc').read()
print content
