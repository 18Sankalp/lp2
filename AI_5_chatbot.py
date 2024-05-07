import random

def greeting():
    responses = ["Hello!", "Hi there!", "Hey!", "Nice to see you!", "Hi! How can I help you?"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Have a great day!", "Bye!"]
    return random.choice(responses)

def respond(message):
    if any(word in message.lower() for word in ["hello", "hey", "hi"]):
        return greeting()
    elif any(word in message.lower() for word in ["bye", "see you", "tata"]):
        return farewell()
    elif "how are you?" in message.lower():
        return "I'm just a bot, but I'm doing well. Thanks for asking!"
    elif "your name" in message.lower():
        return "My name is Panda The Chatbot. How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Chatbot: " + greeting())
    while True:
        user_input = input("You: ")
        if any(word in user_input.lower() for word in ["bye", "see you", "tata"]):
            print("Chatbot: " + farewell())
            break
        else:
            print("Chatbot: " + respond(user_input))

if __name__ == "__main__":
    main()
