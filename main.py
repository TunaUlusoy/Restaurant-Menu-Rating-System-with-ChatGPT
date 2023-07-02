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

review = reviews["Review"].values[8]

prompt = f"""
        Rate just the comments made about foods between 0-5

        Desired Format:
        key:rate

        Example:
        Review:
        T-Bone was excellent but the dessert was weak.

        Output:
        T-Bone:5, dessert:2

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
    key_rate_dict[key] = value

print(key_rate_dict)