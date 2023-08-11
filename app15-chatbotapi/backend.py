import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine= "text-davinci-003",
            prompt = user_input,
            max_tokens = 100, # length of the answer
            temperature = 0.5, # rigidity of the answer
        ).choices[0].text
        return response
    

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me about Emma Watson.")
    print(response)