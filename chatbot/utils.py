def get_bot_reply(message):
    msg = message.lower()
    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you?"
    elif "price" in msg:
        return "Our prices start from 500 BDT."
    elif "bye" in msg:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."
