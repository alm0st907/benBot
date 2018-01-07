import ConfigParser #import library

parse = ConfigParser.ConfigParser()
parse.read('cfg.ini') #template file will show you how to make your own and then fill in with the actual credentials

#make a section in brackets
#print parse.get('info','test') 

#I could add this data all in to a tuple/structure of some sort, or make multiple functions. I havent decided

print parse.get('info','consumer_key')
print parse.get('info','consumer_secret')
print parse.get('info','access_token')
print parse.get('info','access_token_secret')