import praw
from src.reddit_client import reddit
from src.conversation_manager import get_user_by_thread_id, get_full_conversation, update_last_message
from src.ai_responder import generate_followup_reply

def monitor_replies():
    for message in reddit.inbox.unread(limit=None):
        if isinstance(message, praw.models.Message):
            # It's a private message
            continue
        elif isinstance(message, praw.models.Comment):
            parent_id = message.parent_id
            original_author = get_user_by_thread_id(parent_id)
            if original_author:
                # Generate reply with full conversation context
                conversation = get_full_conversation(message)
                reply = generate_followup_reply(conversation)
                message.reply(reply)
                update_last_message(original_author, message.body)
        message.mark_read() 