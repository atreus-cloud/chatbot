import openai
from embeddingRAG import embeddings
import os


from dotenv import load_dotenv
load_dotenv()
#openai.api_key = os.getenv("OpenAI key")

class chatbot:
    def __init__(self, embeddings):
        self.embed = embeddings
        self.history = []
        self.prompt = "You are a helpful, patient support assistant for an company that sells electronic gadgets, including smartphones, laptops, accessories, etc"

    def saving(self, inp, out):
        self.history.append({"role": "user", "content": inp})
        self.history.append({"role": "assistant", "content": out})
        self.history = self.history[-8]
        #keeping only last 4 turns/8 messages

    def ask(self, inp):
        rag = self.embed.query(inp)
        context = "\n".join(rag)

        messages = ({"role": "system", "content": self.prompt})
        messages += self.history
        messages.append({"role": "user", "content": "Context:\n{context}\n\nQuestion: {inp}"})

        response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature = 0.6
        )

        bot_response = response['choices'][0]['message']['content']

        self.histoty(inp, bot_response)
        return bot_response




