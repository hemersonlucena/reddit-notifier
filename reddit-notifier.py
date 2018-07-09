import praw
import time

# SETTINGS ----------------------------------------------------
USER_AGENT = "Passive bot by /u/hemersonlucena"
CLIENT_ID = "INSERT YOUR CLIENT ID HERE!"
CLIENT_SECRET = "INSERT YOUR CLIENT SECRET HERE!"

SUBREDDIT = "AskReddit+AskScience+aww"



# SETUP -------------------------------------------------------
reddit = praw.Reddit(user_agent = USER_AGENT, client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
cache = []

def run_bot():
    subreddit = reddit.subreddit(SUBREDDIT)
    while True:
        try:
            for submission in subreddit.stream.submissions():
                if submission.id not in cache:
                    print(str(submission.subreddit), "|", str(submission.title))
                    cache.append(submission.id)
        except:
            print("Error while retrieving data")
            pass
        
        time.sleep(5)

run_bot()
