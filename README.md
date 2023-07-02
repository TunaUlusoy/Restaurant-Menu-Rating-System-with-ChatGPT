# Restaurant Menu Rating System with ChatGPT

This project aims to develop a rating system that evaluates the taste performance of different menus in restaurants. While restaurant reviews often aggregate ratings under a single "taste" score, this system provides a separate taste score for each menu, making it easier to assess the taste quality of specific menu items.

## Getting Started
To use the Restaurant Menu Rating System, follow these steps:

Clone the repository:
```bash
git clone https://github.com/TunaUlusoy/Restaurant-Menu-Rating-System-with-ChatGPT.git
```

Install the required dependencies:
```bash
cd restaurant-menu-rating-system-with-chatgpt
pip install -r requirements.txt
```

Scrap comments and create csv file:
```bash
python scraping.py
```

Rate comments with Chatgpt:
```bash
python main.py
```

Result:
```bash
{'Beef carpaccio': 5, 'Burger': 2, 'Lamb': 4, 'Dessert': 2}
```

## Contact
For any questions or inquiries, please contact us at tunaeem@gmail.com