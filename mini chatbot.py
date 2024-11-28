
responses = {
    "Hi!": "Hello, how can I assist you today?",
    "How are you?": "I'm just a program, but I'm doing fine, thank you!",
    "Are you working?": "Yes, I am working and ready to chat!",
    "What is your name?": "I am a chatbot created to help you!",
    "What did you do yesterday?": "As a bot, I don't have a past, but I'm always here for you!",
    "Quit.": "Goodbye! It was nice chatting with you. Have a great day!"
}


def chat():
    print("Welcome to the simple chatbot! Type 'Quit.' to exit the conversation.")
    while True:
        user_input = input("You: ").strip()  
        

        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "Quit.":
                break
        else:
            print("Bot: Sorry, I didn't understand that. Please ask something else.")


chat()
