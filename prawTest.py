import praw

bot = praw.Reddit(user_agent='ben_bot',client_id='GJQk28rd1Bp-DA',client_secret='rjofYTFzwpodjztC0PJU0-TRipI',username='',password='')

subreddit = bot.subreddit('space')
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'mars' in text.lower():
        # Generate a message
       print("test message")
       break