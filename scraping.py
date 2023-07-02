import bs4 as bs
import urllib.request as url
import pandas as pd

base_url = 'https://www.yelp.com/biz/nusr-et-steakhouse-istanbul-10?page='
page_number = 1

reviews_list = []

while page_number<2:
    current_url = base_url + str(page_number)
    source = url.urlopen(current_url)
    page_soup = bs.BeautifulSoup(source, 'html.parser')

    mains = page_soup.find_all("div", {"class": "margin-b2__09f24__CEMjT border-color--default__09f24__NPAKY"})

    if not mains:
        break

    for main in mains:
        review = main.find("span", {"class": "raw__09f24__T4Ezm"})
        if review:
            text = review.get_text(strip=True)
            reviews_list.append(text)

    page_number += 1

# Create DataFrame from the reviews list
df = pd.DataFrame(reviews_list, columns=['Review'])

df.to_csv("Nusret.csv", index=False)