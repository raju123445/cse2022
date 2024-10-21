# from flask import Flask, render_template, request
# import nltk
# from nltk.chat.util import Chat, reflections

# # Initialize Flask app
# app = Flask(__name__)

# # Define the chatbot response pairs
# pairs = [
#     [r"(.*) your name ?", ["My name is HealthBot. I am here to assist you with health-related queries."]],
#     [r"how are you ?", ["I am doing well, thank you! How about you?"]],
#     [r"(.*) help (.*)", ["I can assist you with common health issues like headaches, fevers, or suggest when you might need to see a doctor."]],
#     [r"(.*) headache(.*)", ["For headaches, make sure you're hydrated and try resting in a dark room. If the headache persists, consult a doctor."]],
#     [r"(.*) fever(.*)", ["For fever, stay hydrated and rest. If it’s over 102°F or lasts more than a few days, see a doctor."]],
#     [r"(.*) covid(.*)", ["If you think you have COVID-19, monitor symptoms, isolate, and test. If severe, seek medical attention immediately."]],
#     [r"(.*) tired(.*)", ["Feeling tired could be due to stress, poor diet, or lack of sleep. Consider a balanced diet, exercise, and good sleep."]],
#     [r"quit", ["Thank you for using HealthBot. Take care!"]],
#     [r"(.*)", ["I'm sorry, I don't understand that yet. Please ask something else or contact a healthcare professional."]]
# ]

# # Initialize chatbot
# chatbot = Chat(pairs, reflections)

# # Define Flask routes
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/get_response", methods=["POST"])
# def get_response():
#     user_input = request.form["user_input"]
#     response = chatbot.respond(user_input)
#     return response

# if __name__ == "__main__":
#     app.run(debug=True)


from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load pre-trained GPT model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Input prompt
input_text = "The future of artificial intelligence is"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate text continuation
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
