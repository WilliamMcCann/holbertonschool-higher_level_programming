# function puts Github API data into a file
require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 4c9a275f29ec4a763748d8d77668c90f7dea7680'
}

clnt = HTTPClient.new
x = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')

begin
  file = File.open("/tmp/45", "w")
  file.write(x) 
rescue IOError => e
  #some error occur, dir not writable etc.
ensure
  file.close unless file.nil?
end
