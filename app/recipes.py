from app.models import Recipe

recipes_db = [
    Recipe(
        id=1,
        name="Veg Fried Rice",
        ingredients=["rice", "vegetables", "soy sauce", "egg", "garlic"],
        instructions="Heat oil in a wok, stir fry vegetables until cooked, add rice and soy sauce, mix well.",
        cuisine="Asian",
        servings=4,
        prep_time=15,
        cook_time=20
    ),
    Recipe(
        id=2,
        name="Pasta Alfredo",
        ingredients=["pasta", "cream", "cheese", "butter", "garlic"],
        instructions="Cook pasta, prepare sauce with cream and cheese, mix together and serve hot.",
        cuisine="Italian",
        servings=4,
        prep_time=10,
        cook_time=25
    ),
    Recipe(
        id=3,
        name="Chicken Tikka Masala",
        ingredients=["chicken", "yogurt", "tomato sauce", "cream", "spices"],
        instructions="Marinate chicken in yogurt and spices, grill, then simmer in tomato cream sauce.",
        cuisine="Indian",
        servings=4,
        prep_time=30,
        cook_time=40
    ),
    Recipe(
        id=4,
        name="Caesar Salad",
        ingredients=["lettuce", "croutons", "parmesan cheese", "caesar dressing", "lemon"],
        instructions="Toss lettuce with dressing, add croutons and parmesan cheese, serve fresh.",
        cuisine="American",
        servings=2,
        prep_time=10,
        cook_time=0
    ),
    Recipe(
        id=5,
        name="Tacos Al Pastor",
        ingredients=["pork", "pineapple", "tortillas", "onion", "cilantro"],
        instructions="Season and cook pork with pineapple, serve in tortillas with fresh cilantro and onion.",
        cuisine="Mexican",
        servings=4,
        prep_time=20,
        cook_time=30
    )
]
