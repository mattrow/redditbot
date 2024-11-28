from src.reddit_client import reddit
from src.processor import process_submission, process_comment
import time

subreddits_to_monitor = ['subreddit1', 'subreddit2']

for subreddit_name in subreddits_to_monitor:
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.new(limit=10):
        # Process new submissions
        process_submission(submission)
    for comment in subreddit.comments(limit=10):
        # Process new comments
        process_comment(comment)
    time.sleep(2)  # Adjust as needed based on Reddit's rate limits 