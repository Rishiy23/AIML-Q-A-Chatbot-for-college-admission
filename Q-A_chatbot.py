import random

# Define responses for the chatbot
responses = {
    "greeting": ["Hello! Welcome to our college admission chatbot.", "Hi there! How can I assist you with your admission questions?"],
    "admission_procedure": ["To apply for admission, you need to fill out the online application form on our website.", 
                            "The admission procedure involves submitting an application form along with relevant documents."],
    "admission_requirements": ["Admission requirements typically include high school transcripts, standardized test scores, letters of recommendation, and a personal statement or essay.",
                               "You may need to provide transcripts, test scores, recommendation letters, and a personal statement for admission."],
    "admission_deadlines": ["The admission deadlines vary depending on the program and semester. Please check our website or contact the admissions office for specific deadlines.",
                            "Be sure to check the admission deadlines on our website as they may vary for different programs."],
    "farewell": ["Thank you for using our chatbot! Good luck with your college admission!", "Goodbye! Have a great day!"],
    "error": ["I'm sorry, I didn't understand that. Could you please repeat or ask another question?", 
              "Apologies, I'm not sure how to respond to that. Please ask another question."],
}

# Previous context variables
previous_context = {}

# Function to get a response from the chatbot
def get_response(message):
    global previous_question, previous_answer
    message = message.lower()
    
    if message in previous_context:
        response = "You previously asked '"+message+"' and answered '"+previous_context[message]+"'. Is there anything else I can help with?"
        return response
    if "hello" in message or "hi" in message or "hey" in message:
        return random.choice(responses["greeting"])
    elif "bye" in message or "goodbye" in message:
        return random.choice(responses["farewell"])
    elif "procedure" in message or "apply" in message or "application" in message:
        response = random.choice(responses["admission_procedure"]) 
        previous_context[message] = response
        return response
    elif "requirements" in message or "requirement" in message:
        response = random.choice(responses["admission_requirements"]) 
        previous_context[message] = response
        return response
    elif "deadline" in message or "deadlines" in message:
        response = random.choice(responses["admission_deadlines"]) 
        previous_context[message] = response
        return response
    
    else:
        return random.choice(responses["error"])

# Main function to run the chatbot
def main():
    print("Chatbot: Hello! Welcome to the college admission chatbot.")
    print("Chatbot: You can ask about admission procedures, requirements, deadlines, etc.")
    print("Chatbot: Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot:", random.choice(responses["farewell"]))
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
