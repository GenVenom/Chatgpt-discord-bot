from revChatGPT.revChatGPT import Chatbot

def get_response(prompt):

    reply = chatbot.get_chat_response("How do u make turkish coffee")

    return(reply['message'])
