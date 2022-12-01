import praw

reddit = praw.Reddit('backpagebot')

import time
import datetime

subvar = "https://old.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/"
submission = reddit.submission(url=subvar)

for i in range(2):
    print(datetime.datetime.now(), ': made a comment, i=',i)
    try:
        submission.comments[0].reply('this is a reply to a comment')
    except praw.exceptions.APIException:
        print('sleeping for 5 seconds')
        time.sleep(5)
