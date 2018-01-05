import ConfigParser #import library

parse = ConfigParser.ConfigParser()
parse.read('config.ini')

print parse.get('info','test') #make a section in brackets