import tweepy
import reddit #my reddit praw code file

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

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
  

  api = get_api(cfg)

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
      handle="@alm0st907"
      status=True
      pass
 #MEME FLING CHOICE SELECTOR

  #Formats the tweet with the pulled title, pulled link, identifies the bot, then throws the @
  tweet = title + '\n' + link + "\nBy Memebot 9000 (wip)\n"+handle
  print(tweet)
  
  #DROP A TRAIN ON EM EDGAR
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()