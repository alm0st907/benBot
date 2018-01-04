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

  api = get_api(cfg)
  tweet = "Working on a twitter bot, ignore this tweet\n"+"#boredcoder"
  link=prawTest.get_link()
  print(link)
  #status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()