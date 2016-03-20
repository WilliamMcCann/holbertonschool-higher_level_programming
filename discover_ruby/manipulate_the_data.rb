# function displays the list of the 30 most popular Ruby projects on Github
require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 4c9a275f29ec4a763748d8d77668c90f7dea7680'
}

clnt = HTTPClient.new
raw_info = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
parsed = JSON.parse(raw_info)
parsed ["items"].map {|e| puts e["full_name"]}.join
