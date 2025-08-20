import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
        # Filter animals with weight > 100
    filtered = animals[animals['weight'] > 100]

    # Sort by weight in descending order
    sorted_animals = filtered.sort_values(by='weight', ascending=False)

    # Return only the name column
    return sorted_animals[['name']]

data = {"name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
    "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
    "age": [98, 50, 6, 45, 100, 26],
    "weight": [464, 41, 328, 463, 50, 349]
}

animals_df = pd.DataFrame(data)

print(findHeavyAnimals(animals_df))
