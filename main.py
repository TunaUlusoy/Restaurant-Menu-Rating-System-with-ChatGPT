import openai

from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

review = ""

prompt = """
        Extract keywords and it's explanations of the restaurant review, keyword must be one word
        explanation must be min two words, as a result, rate them between 0-10

        Warning: Don't use special names

        Review: 
        f{review}

        Desired Format:
        Positive:
        line by line
        Negative:
        line by line

        Example:
        Positive:
        Hamburger:It's so delicious (8)
        Negative:
        Onions: It's so cold(2)
        Waiter: Rude(1)

        Output:
        """

completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=prompt,
                        max_tokens=100
                    )

print(completion)


