from configparser import ConfigParser
import praw
import threading
import time
from win10toast import ToastNotifier


if __name__ == "__main__":
    cfg = ConfigParser()

    cfg.read('config.ini')
    USER_AGENT = cfg.get('auth', 'user_agent')
    CLIENT_ID = cfg.get('auth', 'client_id')
    CLIENT_SECRET = cfg.get('auth', 'client_secret')

    SUBREDDIT = cfg.get('preferences', 'subreddit')
    SLEEP_TIME = int(cfg.get('preferences', 'sleep_time'))


reddit = praw.Reddit(user_agent = USER_AGENT, client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
cache = []
toaster = ToastNotifier()
toasterFree = True
def request_toast(title, desc):
    global toasterFree
    if toasterFree:
                toasterFree = False
                toaster.show_toast(title, desc)
                toasterFree = True
    else:
    	return

def run_bot():
    subreddit = reddit.subreddit(SUBREDDIT)
    for submission in subreddit.stream.submissions():
        if submission.id not in cache:
            print(str(submission.subreddit), "|", str(submission.title))
            t1 = threading.Thread(target=request_toast, args=("New post on " + str(submission.subreddit), str(submission.title)))
            t1.start()
            cache.append(submission.id)


run_bot()
