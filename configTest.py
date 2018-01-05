import ConfigParser #import library

parse = ConfigParser.ConfigParser()
parse.read('config.ini')

#make a section in brackets
#print parse.get('info','test') 

print parse.get('info','consumer_key')
print parse.get('info','consumer_secret')
print parse.get('info','access_token')
print parse.get('info','access_token_secret')