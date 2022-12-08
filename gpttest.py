from revChatGPT.revChatGPT import Chatbot

def get_response(prompt):

    reply = chatbot.get_chat_response(prompt)

    return(reply['message'])
