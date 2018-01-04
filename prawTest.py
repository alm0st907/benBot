import praw

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
print(submission.title)
print(submission.shortlink)

# for submission in submissions:
#     print(submission.title)
#     print(submission.url)
#     break
