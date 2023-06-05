import os
import openai
import pandas as pd

from dotenv import dotenv_values
from dataframe import Get_Dataframe
from completion import Completion

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

csv_path = os.path.join(os.getcwd(), "Nusret.csv")

dataframe = Get_Dataframe(csv_path)
reviews = dataframe.get_dataframe()

key_rate_dict = {}

for _, review in reviews.iterrows():
    prompt = f"""
            Write what comments are made in the restaurant, rate 0-5

            Desired Format:
            key:rate

            Rules:
            key must not contain adjectives

            Example:
            Review:
            The ambience is wonderful and there is music playing.
            Output:
            Ambience:5, Music:4

            Review:
            {review}

            Output:
            """
    
    completion = Completion("text-davinci-003", review, prompt, max_tokens=1000)
    response = completion.create_completion()

    text = response["choices"][0]["text"]
    pairs = text.split(",")
    for pair in pairs:
        key, value = pair.split(":")
        key = key.strip()
        value = int(value)
        if key in key_rate_dict:
            key_rate_dict[key] = (key_rate_dict[key] + value) / 2
        else:
            key_rate_dict[key] = value

key_rate_df = pd.DataFrame(key_rate_dict, index=["Nusret"])
print(key_rate_df)
key_rate_df.to_csv("key_rate_df.csv", index=True)