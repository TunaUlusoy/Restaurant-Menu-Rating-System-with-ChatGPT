import os
import re
import openai
import pandas as pd

from dotenv import dotenv_values
from data_manipulation import DataManipulation
from completion import Completion

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

csv_path = os.path.join(os.getcwd(), "restaurant_reviews.tsv")

manipulation = DataManipulation(csv_path, "\t")
reviews = manipulation.get_reviews()

key_rate_dict = {}

for _, review in reviews[11:21].iterrows():
    prompt = f"Write what is commented about in the restaurant, write rates between 0-5\nDesired Format:key(adjectives should not be):rate\nExample:The ambience is wonderful and there is music playing.\nOutput:Ambience:5, Music:4\nReview:{review}\nOutput:"
    
    completion = Completion("text-davinci-003", review, prompt, max_tokens=500)
    response = completion.create_completion()

    text = response["choices"][0]["text"]
    if re.search(r'\d', text):
        pairs = text.split(",")
        for pair in pairs:
            key, value = pair.split(":")
            key = key.strip()
            value = int(value)
            if key in key_rate_dict:
                key_rate_dict[key] = (key_rate_dict[key] + value) / 2
            else:
                key_rate_dict[key] = value
    else:
        pass

key_rate_df = pd.DataFrame(key_rate_dict, index=["Restaurant_B"])

if not os.path.exists(os.path.join(os.getcwd(), "key_rate_df.csv")):
    key_rate_df.to_csv("key_rate_df.csv", index=True)
else:
    key_rate_csv = pd.read_csv("key_rate_df.csv")
    key_rate_csv = pd.concat([key_rate_csv, key_rate_df])
    key_rate_csv.to_csv("key_rate_df.csv", index=True)