import json

def get_trending_products():
    # Placeholder for scraping Amazon, TikTok, Etsy
    trends = [
        {"product": "LED Galaxy Projector", "link": "https://amazon.com/led-galaxy"},
        {"product": "Fitness Tracker", "link": "https://tiktok.com/trending-fitness"},
        {"product": "Minimalist Jewelry", "link": "https://etsy.com/minimalist"}
    ]
    with open("resources/trending_products.json", "w") as f:
        json.dump(trends, f)
    print("Top trends saved.")
