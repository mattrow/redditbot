from src.conversation_manager import user_has_been_contacted, save_conversation
from src.ai_responder import generate_reply

def process_submission(submission):
    author = submission.author.name
    if not user_has_been_contacted(author):
        reply = generate_reply(submission.title, submission.selftext)
        reply_instance = submission.reply(reply)
        save_conversation(author, reply_instance)

def process_comment(comment):
    author = comment.author.name
    if not user_has_been_contacted(author):
        reply = generate_reply(comment.link_title, comment.body)
        reply_instance = comment.reply(reply)
        save_conversation(author, reply_instance) 