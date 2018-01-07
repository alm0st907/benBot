import ConfigParser #import library

def get_cfg_info():
    parse = ConfigParser.ConfigParser()
    parse.read('cfg.ini') #template file will show you how to make your own and then fill in with the actual credentials

    #make a section in brackets
    #print parse.get('info','test') 

    #I could add this data all in to a tuple/structure of some sort, or make multiple functions. I havent decided

    ckey = parse.get('info','consumer_key')
    cskey = parse.get('info','consumer_secret')
    atoken = parse.get('info','access_token')
    astoken = parse.get('info','access_token_secret')
    cfg=(ckey,cskey,atoken,astoken)
    return cfg

    #print cfg[0] #prints ckey from the tuple