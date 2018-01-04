import tweepy
import reddit #my reddit praw code file

#need to figure out this code as compared to the get_api code
consumer_key = 'RzjIudiw6pddHytAJDDRDPxlz'
consumer_secret = '3HZNFEvPX1aYgoXYq80GvXTLiAmk3bpiyxKgoIR5IVlAWAJDhA'
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
        print 'Getting page {} for followers'.format(page_count)
        users.extend(user)
    return users

def main():
  # Fill in the values noted in previous step here
  #this is the memebot account credentials
  cfg = { 
    "consumer_key"        : "RzjIudiw6pddHytAJDDRDPxlz",
    "consumer_secret"     : "3HZNFEvPX1aYgoXYq80GvXTLiAmk3bpiyxKgoIR5IVlAWAJDhA",
    "access_token"        : "948791438900322304-rO4oAoli6f1aJE0nSVeRZrvGPiMdENO",
    "access_token_secret" : "sARssRS2gfwAHDQvrzljDeXVtLFkmnYuisux6ZUNStn4S" 
    }


  #calls to get the reddit info using praw, see reddit.py for the code
  link=reddit.get_link()
  title=reddit.get_title()
  

  bot = get_api(cfg)

  #WIP code
  myUser=bot.me()
  #user = myUser.id
  user=myUser.id
  
  #just prints user id
  #print(user)

  follower_list=[]
  #gets a list of users
  follower_list=get_followers(user)

  #pop off a user object 
  temp=follower_list.pop()

  #access the screen name of a user object
  #print(temp.screen_name)
  

 #MEME FLING CHOICE SELECTOR
  handle="blank_string"
  status=False
  while status==False:
    
    handle=raw_input("who you tweetin' at: ")
    if handle == "ben":
      handle = "@realBenKuttner"
      status=True
    elif handle == "ian":
      handle = "@IanStacks543"
      status=True
    else:
      if handle == temp.screen_name: #checking if the name matches the temp
        status=True
      pass
 #MEME FLING CHOICE SELECTOR

  #Formats the tweet with the pulled title, pulled link, identifies the bot, then throws the @
  tweet = title + '\n' + link + "\nBy Memebot 9000 (wip)\n"+'@'+handle

  #just a debug line of code, see what the tweet is
  #print(tweet)
  
  #DROP A TRAIN ON EM EDGAR
  status = bot.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
