import openai

from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

review = \
        """
        I tried Steal Burger, Kasab Burger, Cheese Burger and Bomba Salad. 
        Bomba is kind of onion rings, fries dipped in ketchup syrup. 
        My advice to avoid Bomba. Burgers come with fries and taste perfect. 
        I visited Marmara Mall branch in Food Court. Very friendly staff and great service.
        """

prompt = \
        f"""
        Summarize the review like keyword:explanation, rate explanations between 0-10
 
        Warning: Don't use custom names
 
        Review: 
        {review}
 
        Desired Format:
        Python dictionary
 
        Example:
        Hamburger: 8
        Onions: 2
        Waiter: 1
 
        Output:
        """

completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=prompt,
                        max_tokens=500
                    )

print(completion)


