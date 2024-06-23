import joblib
read = joblib.load("C:/Users/RTX696969/Desktop/Chatbot With LangChain/Compiled_Model.pkl")
query3 = "When was AIUB found?"
doc3 = read[1].similarity_search(query3)

input_data = {
    'input_documents': doc3,
    'question': query3
}
response = read[0].invoke(input_data)

print(response['output_text'])