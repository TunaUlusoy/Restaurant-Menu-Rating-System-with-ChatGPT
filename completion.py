import openai

class Completion:
    def __init__(self, model, review, prompt, max_tokens):
        self.model = model
        self.review = review
        self.prompt = prompt
        self.max_tokens = max_tokens

    def create_completion(self):
        completion = openai.Completion.create(
                        model=self.model,
                        prompt=self.prompt,
                        max_tokens=self.max_tokens
                    )
        return completion