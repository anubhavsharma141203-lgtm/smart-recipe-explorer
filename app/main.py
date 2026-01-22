from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import List, Optional
import os
from pathlib import Path

from app.models import Recipe, RecipeResponse, AIResponse, SearchFilters
from app.recipes import recipes_db
from app.ai_helper import get_ai_recipe_suggestion

# Initialize FastAPI app
app = FastAPI(
    title="Smart Recipe Explorer API",
    description="A FastAPI-based recipe management application with AI-powered recipe suggestions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
static_dir = Path(__file__).parent.parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# ==================== ROOT ENDPOINT ====================
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    """Serve the main UI."""
    html_path = Path(__file__).parent.parent / "static" / "index.html"
    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Smart Recipe Explorer</h1><p>UI not found. Please check static/index.html</p>"

# ==================== RECIPE ENDPOINTS ====================
@app.get("/api/recipes", response_model=List[RecipeResponse])
def get_all_recipes():
    """Get all recipes from the database."""
    return recipes_db

@app.get("/api/recipes/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int):
    """Get a specific recipe by ID."""
    recipe = next((r for r in recipes_db if r.id == recipe_id), None)
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Recipe with ID {recipe_id} not found")
    return recipe

@app.post("/api/recipes", response_model=RecipeResponse, status_code=201)
def add_recipe(recipe: Recipe):
    """Add a new recipe to the database."""
    # Generate new ID
    new_id = max([r.id for r in recipes_db], default=0) + 1
    recipe.id = new_id
    recipes_db.append(recipe)
    return recipe

@app.put("/api/recipes/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, recipe: Recipe):
    """Update an existing recipe."""
    index = next((i for i, r in enumerate(recipes_db) if r.id == recipe_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail=f"Recipe with ID {recipe_id} not found")
    
    recipe.id = recipe_id
    recipes_db[index] = recipe
    return recipe

@app.delete("/api/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    """Delete a recipe by ID."""
    global recipes_db
    if not any(r.id == recipe_id for r in recipes_db):
        raise HTTPException(status_code=404, detail=f"Recipe with ID {recipe_id} not found")
    
    recipes_db = [r for r in recipes_db if r.id != recipe_id]
    return {"message": f"Recipe with ID {recipe_id} deleted successfully"}

# ==================== SEARCH & FILTERING ENDPOINTS ====================
@app.get("/api/recipes/search/by-cuisine", response_model=List[RecipeResponse])
def search_by_cuisine(cuisine: str = Query(..., min_length=1)):
    """Search recipes by cuisine type."""
    results = [r for r in recipes_db if r.cuisine.lower() == cuisine.lower()]
    if not results:
        raise HTTPException(status_code=404, detail=f"No recipes found for cuisine: {cuisine}")
    return results

@app.get("/api/recipes/search/by-ingredient", response_model=List[RecipeResponse])
def search_by_ingredient(ingredient: str = Query(..., min_length=1)):
    """Search recipes by ingredient."""
    results = [
        r for r in recipes_db 
        if any(ingredient.lower() in ing.lower() for ing in r.ingredients)
    ]
    if not results:
        raise HTTPException(status_code=404, detail=f"No recipes found with ingredient: {ingredient}")
    return results

@app.get("/api/recipes/search/by-time", response_model=List[RecipeResponse])
def search_by_time(max_prep_time: Optional[int] = None, max_cook_time: Optional[int] = None):
    """Search recipes by preparation and cooking time."""
    results = recipes_db
    
    if max_prep_time is not None:
        results = [r for r in results if r.prep_time and r.prep_time <= max_prep_time]
    
    if max_cook_time is not None:
        results = [r for r in results if r.cook_time and r.cook_time <= max_cook_time]
    
    if not results:
        raise HTTPException(status_code=404, detail="No recipes match the specified time criteria")
    
    return results

@app.post("/api/recipes/advanced-search", response_model=List[RecipeResponse])
def advanced_search(filters: SearchFilters):
    """Advanced search with multiple filters."""
    results = recipes_db
    
    if filters.cuisine:
        results = [r for r in results if r.cuisine.lower() == filters.cuisine.lower()]
    
    if filters.ingredient:
        results = [
            r for r in results 
            if any(filters.ingredient.lower() in ing.lower() for ing in r.ingredients)
        ]
    
    if filters.prep_time_max:
        results = [r for r in results if r.prep_time and r.prep_time <= filters.prep_time_max]
    
    if not results:
        raise HTTPException(status_code=404, detail="No recipes match the search criteria")
    
    return results

# ==================== AI ENDPOINTS ====================
@app.get("/api/ai/suggest", response_model=AIResponse)
def ai_suggest(ingredients: str = Query(..., min_length=1)):
    """Get AI-powered recipe suggestion based on ingredients."""
    ingredient_list = [ing.strip() for ing in ingredients.split(",")]
    result = get_ai_recipe_suggestion(ingredient_list)
    return AIResponse(
        suggestion=result["suggestion"],
        ingredients_used=result["ingredients_used"]
    )

@app.post("/api/ai/suggest", response_model=AIResponse)
def ai_suggest_post(ingredient_list: List[str]):
    """Get AI-powered recipe suggestion (POST endpoint)."""
    if not ingredient_list:
        raise HTTPException(status_code=400, detail="At least one ingredient is required")
    
    result = get_ai_recipe_suggestion(ingredient_list)
    return AIResponse(
        suggestion=result["suggestion"],
        ingredients_used=result["ingredients_used"]
    )

# ==================== STATS ENDPOINT ====================
@app.get("/api/stats")
def get_stats():
    """Get statistics about the recipe database."""
    cuisines = list(set(r.cuisine for r in recipes_db))
    all_ingredients = []
    for r in recipes_db:
        all_ingredients.extend(r.ingredients)
    
    return {
        "total_recipes": len(recipes_db),
        "cuisines": cuisines,
        "total_unique_ingredients": len(set(all_ingredients)),
        "avg_prep_time": sum(r.prep_time or 0 for r in recipes_db) / len(recipes_db) if recipes_db else 0
    }

# ==================== HEALTH CHECK ====================
@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "Smart Recipe Explorer API"}
