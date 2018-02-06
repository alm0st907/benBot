import random #using this for random post choices later on
import tweepy #twitter api
import reddit #my reddit praw code file
import credential_config #parsing a ini for the credentials info to keep the code "safe"
#this program uses python 2.7 and the "uses print statement" error can be ignored for now


#need to figure out this code as compared to the get_api code
tokensNkeys = credential_config.get_cfg_info()
consumer_key = tokensNkeys[0]
consumer_secret = tokensNkeys[1]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

#this is code ripped from a stackex post, no idea if it works yet
def get_followers(user_id):
    users = []
    page_count = 0
    for user in tweepy.Cursor(api.followers, id=user_id, count=200).pages():
        page_count += 1
        #im gunna try commenting out the print to see if that speeds up anythong
        #print 'Getting page {} for followers'.format(page_count)
        users.extend(user)
    return users

#this should return a list of people the bot follows
def get_following(user_id):
    users = []
    page_count = 0
    for user in tweepy.Cursor(api.friends, id=user_id, count=200).pages():
        page_count += 1
        #im gunna try commenting out the print to see if that speeds up anythong
        #print 'Getting page {} for followers'.format(page_count)
        users.extend(user)
    return users

def main():
  #we're pulling this info from the cfg.ini using my config parser code
  #this is the memebot account credentials
    cfg = {
        "consumer_key"        : tokensNkeys[0],
        "consumer_secret"     : tokensNkeys[1],
        "access_token"        : tokensNkeys[2],
        "access_token_secret" : tokensNkeys[3]
    }
    
  #calls to get the reddit info using praw, see reddit.py for the code
  
  #this stuff works now
    posts = reddit.fill_posts() #posts is a 'array' of posts pulled from the reddit code
    temp = posts[2]
  
  #this test code works and can be ignored now
  #print(temp.titles+'\n'+temp.links)
  #this dont work yet
  
  #once I get the list call working i can remove this
    link = reddit.get_link()
    title = reddit.get_title()
  
    #api config call?
    bot = get_api(cfg)

    #WIP code
    myUser = bot.me()
    #user = myUser.id
    user = myUser.id



    follower_list=[]
    following_list=[]
    #gets a list of users
    follower_list = get_followers(user)
    following_list = get_following(user)

    #this chunk of code goes through our list of followers, rips their usernames
    #and then adds it to a list of just usernames to make it more easily usable
    #if this bot actually catches on this might be pretty slow
    name_list = []
    for i in range(len(follower_list)):
        name_list.append(follower_list[i].screen_name)

    friend_list=[]
    for i in range(len(following_list)):
        friend_list.append(following_list[i].screen_name)

 #MEME FLING CHOICE SELECTOR
    handle = "blank_string"
    status = False
    if status == False:
        print "Here's your follower list:\n"

    for i in range(len(name_list)):
        print name_list[i]
    
    print '\n'

    for i in range(len(friend_list)):
        print friend_list[i]
        

    print "Shortcut names: ian or ben"
    print '\n'

    handle = raw_input("who you tweetin' at: ")
    if handle == "ben":
        handle = "realBenKuttner"
        status = True
    elif handle == "ian":
        handle = "IanStacks543"
        status = True
    elif handle in name_list or friend_list:#handling other names
        handle = handle
        status = True
    else:
        pass
    #MEME FLING CHOICE SELECTOR
    print '\n'
    #Formats the tweet with the pulled title, pulled link, identifies the bot, then throws the @
    tweet = title + '\n' + link + "\nBy Memebot 9000 (wip)\n"+'@'+handle

    #just a debug line of code, see what the tweet is
    print tweet

    #DROP A TRAIN ON EM EDGAR
    if status == True:
        status = bot.update_status(status=tweet)
    else:
        print "No tweet, you're just api testing"
    # Yes, tweet is called 'status' rather confusing
    redo_choice = raw_input("Do you want to tweet again? (y or n) : ")
    if redo_choice.upper() == "Y":
        main()


    

if __name__ == "__main__":
    main()
