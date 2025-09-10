
        
# Simple Chatbox Program in Python

def chatbox():
    print("Welcome to ChatBox! (type 'bye' to exit)\n")
    while True:
        user = input("You: ").lower()

        if user == "hi" or user == "hello":
            print("ChatBox: Hello! How are you?")
        elif user == "i am fine" or user == "fine":
            print("ChatBox: That's great to hear!")
        elif user == "what is your name":
            print("ChatBox: I am your simple Python ChatBox 🤖")
        elif user == "bye":
            print("ChatBox: Goodbye! Have a nice day 😊")
            break
        else:
            print("ChatBox: Sorry, I don't understand that.")

# Run the chatbox
chatbox()

