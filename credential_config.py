#import ConfigParser #import library
import configparser #import library

def get_cfg_info():
    parse = configparser.ConfigParser()
    parse.read('config.ini')
    #template file will show you how to make your own and then fill in with the actual credentials

    #make a section in brackets
    #print parse.get('info','test')

    #I could add this data all in to a tuple/structure of some sort, or make multiple functions. I havent decided

    #twitter info parse
    ckey = parse.get('info', 'consumer_key')
    cskey = parse.get('info', 'consumer_secret')
    atoken = parse.get('info', 'access_token')
    astoken = parse.get('info', 'access_token_secret')

    #reddit info parse
    r_agent = parse.get('reddit', 'u_agent')
    cl_id = parse.get('reddit', 'cl_id')
    cl_sec = parse.get('reddit', 'cl_sec')
    usr_name = parse.get('reddit', 'usr_name')
    password = parse.get('reddit', 'password')


    cfg=(ckey, cskey, atoken, astoken, r_agent, cl_id, cl_sec, usr_name, password)
    return cfg

#print cfg[0] #prints ckey from the tuple