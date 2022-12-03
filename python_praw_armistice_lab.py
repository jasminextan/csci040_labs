import praw 

titles=[]
dict={}

reddit = praw.Reddit('bigjbot', user_agent='cs40.0.1')

submission = reddit.submission(url="https://www.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/")
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    try:
        if comment.author == "ArmisticeBot":
            text=comment.body
            split=text.split('\n')
            title=split[1]
            titles.append(title)
    except AttributeError:
        print('not a comment')

for title in titles:
    if title in dict:
        dict[title]+=1
    else:
        dict[title]=1

print(dict)