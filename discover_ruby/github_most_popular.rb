# usage
require 'httpclient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 4c9a275f29ec4a763748d8d77668c90f7dea7680'
}

clnt = HTTPClient.new
puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
