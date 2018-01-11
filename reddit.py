import praw

class postData:
    #this is a 'struct' that will hold all the data of possible tweets. I can add post structs into a list to pull from later
    titles = ""
    links = ""
    posted = False

#simple function to return a reddit link. Useable by the twitterbot to @ some fire at @ the homies
def get_link():
    bot = praw.Reddit(user_agent='ben_bot',client_id='GJQk28rd1Bp-DA',client_secret='rjofYTFzwpodjztC0PJU0-TRipI',username='',password='')

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

#gets the title of the post on reddit
def get_title():
    bot = praw.Reddit(user_agent='ben_bot',client_id='GJQk28rd1Bp-DA',client_secret='rjofYTFzwpodjztC0PJU0-TRipI',username='',password='')

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
    bot = praw.Reddit(user_agent='ben_bot',client_id='GJQk28rd1Bp-DA',client_secret='rjofYTFzwpodjztC0PJU0-TRipI',username='',password='')

    subreddit = bot.subreddit('dankmemes')

    submissions_list= subreddit.hot(limit = 100)

    tweets = [] #gunna store all the post data in here

    
    for i in range(3,100):
        post = postData() #temp holder for the post
        submission = submissions_list.next() #grab first sub

        #shove the data
        post.links = submission.shortlink
        post.titles = submission.title

        #append to list
        tweets.append(post)

        #iterate
        

    #testcode for accessing
    print(tweets[0].links +'\n'+tweets[0].titles+'\n')

    return tweets
