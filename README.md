# chatbot

1. How does the code handle multi-turn conversations and context?
It stores previous user and bot messages in a list and includes the last few when forming a
new query to maintain context.
2. How does the chatbot maintain context throughout the conversation?
It appends each interaction to a history list and uses recent entries when generating the next
response.
3. How would you implement and test the chatbot?
Use Hugging Face for embeddings and a language model for replies; test with different
queries to check if it remembers context.
Use unit tests for parts (like context builder) and simulate full conversations to validate
responses.
4. List of Potential Edge Cases
● Unanswered Questions: Reply with a fallback message like "I don't have that info."
● Ambiguous Queries: Ask follow-up questions to clarify.
● Multiple Questions at Once: Split and answer both parts separately.
● Too Much Context: Use only the last few messages to keep responses focused.
