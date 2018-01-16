import praw
import credential_config

#works and does not need to be modified further to the best of my knowledge
class postData:
    #this is a 'struct' that will hold all the data of possible tweets. I can add post structs into a list to pull from later
    titles = ""
    links = ""
    posted = False

#simple function to return a reddit link. Useable by the twitterbot to @ some fire at @ the homies
#DEPRECIATED, NO LONGER NECESSARY
def get_link():
    credentials = credential_config.get_cfg_info()
    bot = praw.Reddit(user_agent= credentials[4],client_id= credentials[5],client_secret= credentials[6],username=credentials[7],password=credentials)
    subreddit = bot.subreddit('dankmemes')


    #code returns hot 100 posts()
    subreddit = bot.subreddit('dankmemes')

    #this is a list of submissions
    submissions = subreddit.hot()

    #iterates to the next submission; submission is a given data type?
    #starts with the first post,loop ieratres to the 3rd post
    i=0
    for i in range(0,3):
        submission=submissions.next()

    #print the submission title/link
    #print(submission.title)
    #print(submission.shortlink)
    #print("success")
    return submission.shortlink

#gets the title of the post on reddit /r dankmemes
#DEPRECIATED, NO LONGER NECESSARY
def get_title():
    credentials = credential_config.get_cfg_info()
    bot = praw.Reddit(user_agent= credentials[4],client_id= credentials[5],client_secret= credentials[6],username=credentials[7],password=credentials)

    #code returns hot 100 posts()
    subreddit = bot.subreddit('dankmemes')

    #this is a list of submissions
    submissions = subreddit.hot()

    #iterates to the next submission; submission is a given data type?
    #starts with the first post,loop ieratres to the 3rd post
    i=0
    for i in range(0,3):
        submission = submissions.next()

    #print the submission title/link
    #print(submission.title)
    #print(submission.shortlink)
    #print("success2")
    return submission.title
    
def fill_posts():
    #basic initialization, not sure how to change it yet
    credentials = credential_config.get_cfg_info()
    bot = praw.Reddit(user_agent= credentials[4],client_id= credentials[5],client_secret= credentials[6],username=credentials[7],password=credentials)
    subreddit = bot.subreddit('dankmemes')

    submissions_list= subreddit.hot(limit = 100)

    tweets = [] #gunna store all the post data in here

    #just gunna call this twice instead of adding a loop, get to the non sticked posts first
    submission = submissions_list.next()
    submission = submissions_list.next()
    #it is indeed the right ammount of iteration
    
    #loop works as intended
    for i in range(3,100):
        post = postData() #temp holder for the post
        submission = submissions_list.next() #grab first non sticked post by iterating at this point to the third position in dankmemes

        #shove the data
        post.links = submission.shortlink
        post.titles = submission.title

        #append to list
        tweets.append(post)

    #testcode for accessing
    #print(tweets[0].links +'\n'+tweets[0].titles+'\n')
    #it works so its no longer really needed

    return tweets
