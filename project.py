import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def main():
    print("Welcome to the PIEAS Chatbot!")
    data = load_data()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thanks for using Chatbot, hope you got help from this")
            break
        response = generate_response(user_input, data)
        print(f"Bot: {response}")

def generate_response(user_input, data):
    # Preprocess the input
    tokens = preprocess_input(user_input)

    # Dictionary to map keywords to their corresponding data keys
    keyword_map = {
        "admissions": "admission_info",
        "courses": "courses_info",
        "programs": "courses_info",
        "contact": "contact_info",
        "fee": "fee_info",
        "located": "location_info",
        "situated": "location_info",
        "last": "last_info",
        "sat": "sat_info",
        "famous": "famous_info",
        "ranking": "rank_info",
        "merit": "merit_info",
        "test": "test_info",
        "hostels": "hostel_info",
        "gpa": "gpa_info"
    }

    # Iterate through the tokens and check for a match in keyword_map
    for token in tokens:
        if token in keyword_map:
            return data.get(keyword_map[token], f"Sorry, I don't have information on {token} right now.")

    return "I'm not sure about that. Please visit our website or contact the administration for more information."


def preprocess_input(user_input):
    # Tokenize and remove stopwords
    tokens = word_tokenize(user_input.lower())
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    return filtered_tokens

def load_data():
    # Load university data from a JSON file or database
    with open('pieas_data.json', 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('stopwords')
    main()
