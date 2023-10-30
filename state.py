import reflex as rx
import os
import together
together.api_key = "53e10b6b65aa0543494d81723f4a3d79a21f25e426ea06b15aa7f61f92027931"
class State(rx.State):
     # The current question being asked.
    question: str
    amount: str

     # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        output = together.Complete.create(
            prompt = f"[INST] Convert {self.amount} dollars to {self.question}. Only Give me the value[INST]", 
            model = "togethercomputer/llama-2-70b-chat", 
            max_tokens = 256,
            temperature = 0.8,
            top_k = 60,
            top_p = 0.6,
            repetition_penalty = 1.1,
            stop = ['[INST]', '</s>']
        )

    

        # print generated text
        # Add to the answer as the chatbot responds.
        answer = output['output']['choices'][0]['text']
        final_answer = f"<Econvert>: {answer}"
        final_question = f"<User>: {self.amount} {self.question}"
        self.chat_history.append((final_question, final_answer))

    
        # Clear the question input.
        self.question = ""
        self.amount = ""
        # Yield here to clear the frontend input before continuing.
        yield
