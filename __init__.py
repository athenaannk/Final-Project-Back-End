import os
from flask import Flask, redirect, render_template, request, session
from config import Config
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__) 

app.config.from_object(Config)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")
elif not os.environ.get("API_ID"):
    raise RuntimeError("API_ID not set")

#terms from api docs

dietlabels = {
    "balanced": "Balanced",
    "high-fiber": "High Fiber",
    "high-protein": "High Protein",
    "low-carb": "Low Carb",
    "low-fat": "Low Fat",
    "low-sodium": "Low Sodium",
}

healthlabels = {
    "pescatarian": "Pescatarian",
    "shellfish-free": "Shellfish-Free",
    "alcohol-free": "Alcohol-Free",
    "celery-free": "Celery-Free",
    "soy-free": "Soy-Free",
    "sugar-free": "Sugar-Free",
    "pork-free": "Pork-Free",
    "red-meat-free": "Red-Meat-Free",
    "sesame-free": "Sesame-Free",
    "sulfite-free": "Sulfite-Free",
    "tree-nut-free": "Tree-Nut-Free",
    "vegan": "Vegan",
    "sugar-conscious": "Sugar-Conscious",
    "vegetarian": "Vegetarian",
    "wheat-free": "Wheat-Free",
    "alcohol-cocktail": "Alcohol-Cocktail",
    "crustacean-free": "Crustacean-Free",
    "dairy-free": "Dairy-Free",
    "lupine-free": "Lupine-Free",
    "mediterranean": "Mediterranean",
    "dash": "DASH",
    "kidney-friendly": "Kidney-Friendly",
    "egg-free": "Egg-Free",
    "fish-free": "Fish-Free",
    "fodmap-free": "FODMAP-Free",
    "gluten-free": "Gluten-Free",
    "mollusk-free": "Mollusk-Free",
    "peanut-free": "Peanut-Free",
    "immuno-supportive": "Immuno-Supportive",
    "keto-friendly": "Keto-Friendly",
    "low-sugar": "Low-Sugar",
    "mustard-free": "Mustard-Free",
    "kosher": "Kosher",
    "low-potassium": "Low-Potassium",
    "no-oil-added": "No oil added",
    "paleo": "Paleo",
}

cuisinetype = {
    "chinese": "Chinese",
    "eastern europe": "Eastern Europe",
    "british": "British",
    "caribbean": "Caribbean",
    "asian": "Asian",
    "central europe": "Central Europe",
    "american": "American",
    "french": "French",
    "kosher": "Kosher",
    "indian": "Indian",
    "korean": "Korean",
    "italian": "Italian",
    "greek": "Greek",
    "japanese": "Japanese",
    "mediterranean": "Mediterranean",
    "south east asian": "South East Asian",
    "mexican": "Mexican",
    "south american": "South American",
    "world": "World",
    "nordic": "Nordic",
    "middle eastern": "Middle Eastern",
}

dishtype = {
    "starter": "Starter",
    "main course": "Main Course",
    "side dish": "Side Dish",
    "drinks": "Drinks",
    "desserts": "Desserts",
    'alcohol cocktail': 'Alcohol Cocktail',
    'biscuits and cookies': 'Biscuit and Cookies',
    'bread': 'Bread',
    'cereals': 'Cereals',
    'condiments and sauces': 'Condiments and Sauces',
    'desserts': 'Desserts',
    'drinks': 'Drinks',
    'egg': 'Egg',
    'ice cream and custard': 'Ice Cream and Custard',
    'main course': 'Main Course',
    'pancake': 'Pancake',
    'pasta': 'Pasta',
    'pastry': 'Pastry',
    'pies and tarts': 'Pies and Tarts',
    'pizza': 'Pizza',
    'preps': 'Preps',
    'preserve': 'Preserve',
    'salad': 'Salad',
    'sandwiches': 'Sandwiches',
    'seafood': 'Seafood',
    'side dish': 'Side Dish',
    'soup': 'Soup',
    'special occasions': 'Special Occasions',
    'starter': 'Starter',
    'sweets': 'Sweets'
}