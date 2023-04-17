import requests
import time 

def lookup(search):
    try:
        api_key = os.environ.get("API_KEY")
        api_id = os.environ.get("API_ID")
        response = requests.get(
            f"https://api.edamam.com/api/recipes/v2?type=public&app_id={api_id}&app_key={api_key}&q={search}")
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        result = response.json()
        outcome_dict = result["outcome"]
        recipes_list = []
        for index in outcome_dict:
            link = index["_links"]["self"]["href"]  
            label = index["recipe"]["label"]
            image = index["recipe"]["image"]
            source = index["recipe"]["source"]
            url = index["recipe"]["url"]  
            dietLabels = list(index["recipe"]["dietLabels"])
            healthLabels = list(index["recipe"]["healthLabels"])
            ingredientLines = list(index["recipe"]["ingredientLines"])
            calories = index["recipe"]["calories"]
            totalTime = index["recipe"]["totalTime"]
            cuisineType = list(index["recipe"]["cuisineType"])
            dishType = list(index["recipe"]["dishType"])
            recipes_list.append(
                {
                    "link": link,
                    "label": label,
                    "image": image,
                    "source": source,
                    "url": url,
                    "dietLabels": dietLabels,
                    "healthLabels": healthLabels,
                    "ingredientLines": ingredientLines,
                    "calories": calories,
                    "totalTime": totalTime,
                    "cuisineType": cuisineType,
                    "dishType": dishType
                })
        return recipes_list  
    except (KeyError, TypeError, ValueError):
        return None