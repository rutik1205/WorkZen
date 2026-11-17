# Simple Rule-Based Chatbot using Pattern Matching

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input().lower()

        # Pattern Matching Rules
        if "hello" in user or "hi" in user:
            print("Chatbot: Hello! How can I help you?")

        elif "how are you" in user:
            print("Chatbot: I am fine. Thank you!")

        elif "your name" in user:
            print("Chatbot: I am a simple chatbot.")

        elif "college" in user:
            print("Chatbot: I can provide information about the college.")

        elif "course" in user:
            print("Chatbot: There are many courses available.")

        elif "bye" in user:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Run chatbot
chatbot()

