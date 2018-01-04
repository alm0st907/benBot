import tweepy
import prawTest

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "yjnGr1oTv8VmQVmf8Mxw4kbwc",
    "consumer_secret"     : "X3Gk5ubrslnie6yzwZGD82Hh3jMUioB3O7idFMYNtMBgr8GgGm",
    "access_token"        : "537663050-YhA9O5lNU35ws4NBHHEqWgqSZSg1qRlhQu6NWoHY",
    "access_token_secret" : "XWYxwIxNNiSw4Mr7Hg3h6SXdHk3HvMu55piKLcUeqv3kH" 
    }


  #testcode to get the link returned from my praw code
  link=prawTest.get_link()
  title=prawTest.get_title()
  

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
      pass
 #MEME FLING CHOICE SELECTOR

  #more testing
  tweet = title + '\n' + link + "\nBy Memebot 9000 (wip)\n"+handle
  print(tweet)
  
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()