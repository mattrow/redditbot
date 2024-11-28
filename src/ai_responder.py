from openai import OpenAI
from src.openai_client import openai

def generate_reply(post_title, message_content):
    prompt = f"""
    You are a helpful assistant. Read the following post and comment, and compose a personalized reply without including any links.

    Post Title: {post_title}

    Comment: {message_content}

    Reply:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip() 

def generate_followup_reply(conversation):
    conversation_text = "\n".join(
        [f"{msg['author']}: {msg['body']}" for msg in conversation]
    )
    prompt = f"""
    Continue the following conversation in a helpful and engaging way.

    Conversation:
    {conversation_text}

    Reply:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip() 