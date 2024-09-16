import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",  # Regular expression for greeting patterns
        ["Hello!", "Hi there!", "Hey!"]  # Possible responses to greetings
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot.", "I'm Chatbot, nice to meet you!"]
    ],
    [
        r"i want to ask a question",
        ["Yeah sure"]  # Response for asking a question
    ],
    [
        r"(.*) your name(.*)",
        ["My name is Chatbot.", "I go by the name Chatbot."]  # Pattern for asking the chatbot's name
    ],
    [
        r"(.*) (sorry|apologies)(.*)",
        ["No need to apologize.", "It's alright."]  # Pattern for apologies
    ],
    [
        r"quit|bye|exit",
        ["Goodbye!", "Bye, take care!"]  # Response for exit commands
    ],
    [
        r"how old are you?",
        ["I am just a computer program, so I don't have an age."]  # Pattern for asking age
    ],
    [
        r"what can you do?",
        ["I'm here to chat with you and answer your questions!"]  # Pattern for capabilities
    ],
    [
        r"(.*) (hate|dislike) you(.*)",
        ["I'm sorry to hear that."]  # Pattern for negative sentiments
    ],
    [
        r"what is the weather today?",
        ["I'm just a chatbot and I can't check the weather. You can use a weather app or website to find out!"]  # Pattern for weather inquiries
    ],
    [
        r"what is your favorite color?",
        ["I don't have a favorite color, as I am just a program."]  # Pattern for favorite color
    ],
    [
        r"how can I help you?",
        ["You can ask me anything you'd like to know!"]  # Pattern for offering help
    ],
    [
        r"How can I improve my time management skills??",
        ["Use a planner to organize tasks and set short-term goals. Prioritize tasks and break them into smaller steps.!"]  # Time management tips
    ],
    [
        r"What are some tips for a successful job interview?",
        ["Research the company and role beforehand. Dress appropriately, answer questions clearly, and ask insightful questions."]  # Interview tips
    ],
    [
        r"how do you learn?",  # Pattern for asking how the chatbot learns
        ["I learn from the data I was trained on and from interactions with users like you. My developers continuously improve my abilities.", "I improve through machine learning techniques and updates from my developers. How can I assist you today?"]
    ],
    [
        r"what are your hobbies?",  # Pattern for asking about hobbies
        ["I don't have hobbies, but I enjoy engaging conversations. Do you have any hobbies?", "I don't have personal hobbies, but I'd love to hear about yours!"]
    ],
    [
        r"who created you?",  # Pattern for asking about the creator
        ["I was created by a developer PUJA...", "I was developed by PUJA. How can I assist you today?"]
    ],
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    """
    Function to get response from the chatbot.
    """
    return chatbot.respond(user_input)  # Get the chatbot's response based on user input

def send_message():
    """
    Function to send user message and display chatbot response.
    """
    message = entry.get()  # Get the message from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget after sending the message
    if message.lower() == 'quit':  # Check if the user wants to quit
        chat_area.insert(tk.END, "You: " + message + "\n")  # Display user message
        chat_area.insert(tk.END, "Chatbot: " + chatbot_response(message) + "\n")  # Display chatbot response
        chat_area.insert(tk.END, "Chatbot: Bye! Take care.\n")  # Goodbye message
        entry.config(state=tk.DISABLED)  # Disable the entry widget
        send_button.config(state=tk.DISABLED)  # Disable the send button
    else:
        chat_area.insert(tk.END, "You: " + message + "\n")  # Display user message
        chat_area.insert(tk.END, "Chatbot: " + chatbot_response(message) + "\n")  # Display chatbot response
        chat_area.see(tk.END)  # Scroll to the end of the chat area

# Create the main window
root = tk.Tk()
root.title("Chatbot")  # Set the title of the window

# Create a frame to hold the chat area
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Create a scrolled text widget to display the chat
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20)
chat_area.pack(expand=True, fill=tk.BOTH)

# Create a frame to hold the message entry field and send button
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10, fill=tk.BOTH)

# Create an entry widget to type messages
entry = tk.Entry(entry_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

# Create a button to send messages
send_button = tk.Button(entry_frame, text="Send", width=10, command=send_message)
send_button.pack(side=tk.LEFT)

# Bind the Enter key to send messages
root.bind('<Return>', lambda event=None: send_message())

# Focus on the entry field by default
entry.focus()

# Run the main event loop
root.mainloop()
