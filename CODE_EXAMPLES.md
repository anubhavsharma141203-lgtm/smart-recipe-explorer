# 💻 Code Examples & API Usage Guide

## Table of Contents
1. [Web UI Usage](#web-ui-usage)
2. [Python Examples](#python-examples)
3. [JavaScript Examples](#javascript-examples)
4. [cURL Examples](#curl-examples)
5. [API Response Examples](#api-response-examples)

---

## Web UI Usage

### Accessing the Web Interface

1. **Start the server:**
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

2. **Open your browser:**
   ```
   http://127.0.0.1:8000
   ```

### Using the AI Suggestion Feature

```
1. Look for "🤖 AI Recipe Suggestion" section
2. In the input field, type: "chicken, garlic, tomato"
3. Click "Get AI Suggestion"
4. Wait for response (2-5 seconds)
5. See the AI-generated recipe
```

### Using Search Features

**Search by Cuisine:**
```
1. Go to "🔍 Search Recipes"
2. Click "By Cuisine" tab
3. Select cuisine from dropdown (e.g., "Asian")
4. See all recipes from that cuisine
```

**Search by Ingredient:**
```
1. Go to "🔍 Search Recipes"
2. Click "By Ingredient" tab
3. Type ingredient (e.g., "rice")
4. Click "Search"
5. See recipes with that ingredient
```

**Search by Time:**
```
1. Go to "🔍 Search Recipes"
2. Click "By Time" tab
3. Enter max time in minutes (e.g., "30")
4. Click "Search"
5. See recipes you can make in that time
```

### Adding a New Recipe

```
1. Go to "➕ Add New Recipe" section
2. Fill all fields:
   - Recipe Name: "Spaghetti Carbonara"
   - Cuisine: "Italian"
   - Ingredients: "pasta, eggs, bacon, cheese"
   - Instructions: "Cook pasta, mix with bacon and eggs..."
   - Prep Time: "10"
   - Cook Time: "20"
3. Click "Add Recipe"
4. See success message
5. Recipe is added to database
```

---

## Python Examples

### Basic Setup

```python
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"
HEADERS = {"Content-Type": "application/json"}

def make_request(method, endpoint, data=None, params=None):
    """Make an API request"""
    url = f"{BASE_URL}{endpoint}"
    
    if method == "GET":
        return requests.get(url, params=params)
    elif method == "POST":
        return requests.post(url, json=data, headers=HEADERS)
    elif method == "PUT":
        return requests.put(url, json=data, headers=HEADERS)
    elif method == "DELETE":
        return requests.delete(url)
```

### Get All Recipes

```python
# Get all recipes
response = requests.get(f"{BASE_URL}/recipes")

if response.status_code == 200:
    recipes = response.json()
    for recipe in recipes:
        print(f"Name: {recipe['name']}")
        print(f"Cuisine: {recipe['cuisine']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print("---")
else:
    print(f"Error: {response.status_code}")
```

### Get Specific Recipe

```python
recipe_id = 1

response = requests.get(f"{BASE_URL}/recipes/{recipe_id}")

if response.status_code == 200:
    recipe = response.json()
    print(f"Recipe: {recipe['name']}")
    print(f"Cuisine: {recipe['cuisine']}")
    print(f"Prep Time: {recipe['prep_time']} min")
    print(f"Cook Time: {recipe['cook_time']} min")
elif response.status_code == 404:
    print("Recipe not found")
```

### Add a New Recipe

```python
new_recipe = {
    "name": "Garlic Butter Pasta",
    "cuisine": "Italian",
    "ingredients": ["pasta", "garlic", "butter", "parsley"],
    "instructions": "Cook pasta, melt butter with garlic, toss together",
    "prep_time": 15,
    "cook_time": 20
}

response = requests.post(f"{BASE_URL}/recipes", json=new_recipe)

if response.status_code == 201:
    created_recipe = response.json()
    print(f"Recipe created with ID: {created_recipe['id']}")
else:
    print(f"Error: {response.json()}")
```

### Update a Recipe

```python
recipe_id = 1
updated_recipe = {
    "name": "Updated Recipe Name",
    "cuisine": "Italian",
    "ingredients": ["new", "ingredients"],
    "instructions": "New instructions...",
    "prep_time": 20,
    "cook_time": 30
}

response = requests.put(f"{BASE_URL}/recipes/{recipe_id}", json=updated_recipe)

if response.status_code == 200:
    print("Recipe updated successfully")
else:
    print(f"Error: {response.status_code}")
```

### Delete a Recipe

```python
recipe_id = 1

response = requests.delete(f"{BASE_URL}/recipes/{recipe_id}")

if response.status_code == 200:
    print("Recipe deleted successfully")
elif response.status_code == 404:
    print("Recipe not found")
```

### Search by Cuisine

```python
cuisine = "Asian"

response = requests.get(f"{BASE_URL}/recipes/search/by-cuisine", params={"cuisine": cuisine})

if response.status_code == 200:
    recipes = response.json()
    print(f"Found {len(recipes)} {cuisine} recipes:")
    for recipe in recipes:
        print(f"  - {recipe['name']}")
else:
    print(f"No recipes found for cuisine: {cuisine}")
```

### Search by Ingredient

```python
ingredient = "tomato"

response = requests.get(f"{BASE_URL}/recipes/search/by-ingredient", params={"ingredient": ingredient})

if response.status_code == 200:
    recipes = response.json()
    print(f"Found {len(recipes)} recipes with {ingredient}:")
    for recipe in recipes:
        print(f"  - {recipe['name']}")
```

### Get AI Recipe Suggestion

```python
ingredients = "chicken,garlic,tomato"

response = requests.get(f"{BASE_URL}/ai/suggest", params={"ingredients": ingredients})

if response.status_code == 200:
    data = response.json()
    print("AI Suggestion:")
    print(data['suggestion'])
    print(f"\nUsing ingredients: {', '.join(data['ingredients_used'])}")
else:
    print(f"Error: {response.json()}")
```

### Get Statistics

```python
response = requests.get(f"{BASE_URL}/stats")

if response.status_code == 200:
    stats = response.json()
    print(f"Total Recipes: {stats['total_recipes']}")
    print(f"Cuisines: {', '.join(stats['cuisines'])}")
    print(f"Unique Ingredients: {stats['total_unique_ingredients']}")
    print(f"Avg Prep Time: {stats['avg_prep_time']:.1f} minutes")
```

---

## JavaScript Examples

### Fetch Helper Function

```javascript
const API_BASE = "http://127.0.0.1:8000/api";

async function apiCall(method, endpoint, data = null) {
    try {
        const options = {
            method: method,
            headers: { "Content-Type": "application/json" }
        };
        
        if (data && method !== "GET") {
            options.body = JSON.stringify(data);
        }
        
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
}
```

### Get All Recipes

```javascript
async function getAllRecipes() {
    try {
        const recipes = await apiCall("GET", "/recipes");
        console.log("Recipes:", recipes);
        
        // Display recipes
        recipes.forEach(recipe => {
            console.log(`${recipe.name} (${recipe.cuisine})`);
        });
    } catch (error) {
        console.error("Failed to get recipes:", error);
    }
}

// Usage
getAllRecipes();
```

### Add a New Recipe

```javascript
async function addRecipe(recipe) {
    try {
        const newRecipe = await apiCall("POST", "/recipes", recipe);
        console.log("Recipe created:", newRecipe);
        alert(`Recipe "${newRecipe.name}" added successfully!`);
    } catch (error) {
        console.error("Failed to add recipe:", error);
        alert("Failed to add recipe");
    }
}

// Usage
const recipe = {
    name: "Spaghetti Carbonara",
    cuisine: "Italian",
    ingredients: ["pasta", "eggs", "bacon", "cheese"],
    instructions: "Cook pasta, mix with bacon and eggs sauce",
    prep_time: 10,
    cook_time: 20
};

addRecipe(recipe);
```

### Search by Ingredient

```javascript
async function searchByIngredient(ingredient) {
    try {
        const recipes = await apiCall(
            "GET", 
            `/recipes/search/by-ingredient?ingredient=${encodeURIComponent(ingredient)}`
        );
        console.log(`Found ${recipes.length} recipes with "${ingredient}"`);
        recipes.forEach(r => console.log(`  - ${r.name}`));
        return recipes;
    } catch (error) {
        console.error("Search failed:", error);
    }
}

// Usage
searchByIngredient("tomato");
```

### Get AI Suggestion

```javascript
async function getAISuggestion(ingredients) {
    try {
        const ingredientString = ingredients.join(",");
        const response = await apiCall(
            "GET",
            `/ai/suggest?ingredients=${encodeURIComponent(ingredientString)}`
        );
        console.log("AI Suggestion:");
        console.log(response.suggestion);
        return response;
    } catch (error) {
        console.error("AI suggestion failed:", error);
    }
}

// Usage
getAISuggestion(["chicken", "garlic", "tomato"]);
```

---

## cURL Examples

### Health Check

```bash
curl http://127.0.0.1:8000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Smart Recipe Explorer API"
}
```

### Get All Recipes

```bash
curl http://127.0.0.1:8000/api/recipes
```

### Get Single Recipe

```bash
curl http://127.0.0.1:8000/api/recipes/1
```

### Add Recipe

```bash
curl -X POST http://127.0.0.1:8000/api/recipes \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Chicken Stir Fry",
    "cuisine": "Asian",
    "ingredients": ["chicken", "vegetables", "soy sauce"],
    "instructions": "Fry chicken with vegetables and sauce",
    "prep_time": 15,
    "cook_time": 20
  }'
```

### Update Recipe

```bash
curl -X PUT http://127.0.0.1:8000/api/recipes/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Recipe",
    "cuisine": "Asian",
    "ingredients": ["new", "ingredients"],
    "instructions": "Updated instructions",
    "prep_time": 20,
    "cook_time": 25
  }'
```

### Delete Recipe

```bash
curl -X DELETE http://127.0.0.1:8000/api/recipes/1
```

### Search by Cuisine

```bash
curl "http://127.0.0.1:8000/api/recipes/search/by-cuisine?cuisine=Italian"
```

### Search by Ingredient

```bash
curl "http://127.0.0.1:8000/api/recipes/search/by-ingredient?ingredient=tomato"
```

### Get AI Suggestion

```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=chicken,garlic,tomato"
```

### Get Statistics

```bash
curl http://127.0.0.1:8000/api/stats
```

---

## API Response Examples

### Recipe Response Format

```json
{
  "id": 1,
  "name": "Spaghetti Carbonara",
  "cuisine": "Italian",
  "ingredients": ["pasta", "eggs", "bacon", "cheese"],
  "instructions": "Cook pasta, mix with bacon and eggs sauce",
  "servings": 4,
  "prep_time": 10,
  "cook_time": 20
}
```

### AI Suggestion Response

```json
{
  "suggestion": "Here's a delicious Chicken Tomato Pasta recipe...",
  "ingredients_used": ["chicken", "garlic", "tomato"]
}
```

### Error Response

```json
{
  "detail": "Recipe with ID 999 not found"
}
```

### Stats Response

```json
{
  "total_recipes": 5,
  "cuisines": ["Asian", "Italian", "Indian", "Mexican", "American"],
  "total_unique_ingredients": 28,
  "avg_prep_time": 16.0
}
```

### Search Results

```json
[
  {
    "id": 1,
    "name": "Veg Fried Rice",
    "cuisine": "Asian",
    "ingredients": ["rice", "vegetables", "soy sauce"],
    "instructions": "Stir fry vegetables, add rice and sauce",
    "servings": 4,
    "prep_time": 15,
    "cook_time": 20
  }
]
```

---

## Common Patterns

### Try/Catch Pattern

```python
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for bad status
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
```

### Async/Await Pattern

```javascript
async function getData() {
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}
```

### Validation Pattern

```python
recipe = {
    "name": "Test",
    "cuisine": "Test",
    "ingredients": ["ing1"],
    "instructions": "Cook it"
}

# FastAPI will validate automatically
response = requests.post(url, json=recipe)
# Returns 422 if validation fails
```

---

## Testing Commands

### Test with Python

```python
# Save as test_recipe.py
import requests

BASE = "http://127.0.0.1:8000/api"

# Test all endpoints
print("Testing API...")

# 1. Health check
r = requests.get(f"{BASE}/health")
print(f"✓ Health: {r.status_code}")

# 2. Get recipes
r = requests.get(f"{BASE}/recipes")
print(f"✓ Get Recipes: {r.status_code} ({len(r.json())} recipes)")

# 3. Add recipe
recipe = {
    "name": "Test Recipe",
    "cuisine": "Test",
    "ingredients": ["test"],
    "instructions": "Test"
}
r = requests.post(f"{BASE}/recipes", json=recipe)
print(f"✓ Add Recipe: {r.status_code}")

# 4. Search
r = requests.get(f"{BASE}/recipes/search/by-cuisine?cuisine=Asian")
print(f"✓ Search: {r.status_code}")

# 5. AI Suggest
r = requests.get(f"{BASE}/ai/suggest?ingredients=chicken,rice")
print(f"✓ AI Suggest: {r.status_code}")

print("\n✅ All tests passed!")
```

Run with:
```bash
python test_recipe.py
```

---

**Happy Coding! 🚀**
