#!/usr/bin/env python3
"""
Quick test script for the Smart Recipe Explorer API
Run this to test all endpoints and verify the setup
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"
API_URL = f"{BASE_URL}/api"

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def test_endpoint(method, endpoint, data=None, params=None, title=None):
    """Test an API endpoint"""
    url = f"{API_URL}{endpoint}"
    
    if title:
        print(f"📌 {title}")
    print(f"   {method} {endpoint}")
    
    try:
        if method == "GET":
            response = requests.get(url, params=params, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=5)
        elif method == "PUT":
            response = requests.put(url, json=data, timeout=5)
        elif method == "DELETE":
            response = requests.delete(url, timeout=5)
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code < 300:
            print(f"   ✅ Success")
        else:
            print(f"   ❌ Error: {response.text[:100]}")
        
        return response
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return None

def main():
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + "  Smart Recipe Explorer - API Test Suite".center(58) + "║")
    print("╚" + "="*58 + "╝")
    
    # Health check
    print_section("1. Health Check")
    response = test_endpoint("GET", "/health", title="Check API Health")
    if response and response.status_code == 200:
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    # Get all recipes
    print_section("2. Get All Recipes")
    response = test_endpoint("GET", "/recipes", title="Fetch all recipes")
    if response and response.status_code == 200:
        data = response.json()
        print(f"   Found {len(data)} recipes")
        if data:
            print(f"   First recipe: {data[0]['name']}")
    
    # Search by cuisine
    print_section("3. Search by Cuisine")
    response = test_endpoint("GET", "/recipes/search/by-cuisine", 
                            params={"cuisine": "Asian"},
                            title="Search for Asian cuisine")
    if response and response.status_code == 200:
        data = response.json()
        print(f"   Found {len(data)} recipes")
    
    # Search by ingredient
    print_section("4. Search by Ingredient")
    response = test_endpoint("GET", "/recipes/search/by-ingredient",
                            params={"ingredient": "rice"},
                            title="Search for recipes with rice")
    if response and response.status_code == 200:
        data = response.json()
        print(f"   Found {len(data)} recipes")
    
    # AI Suggestion
    print_section("5. AI Recipe Suggestion")
    response = test_endpoint("GET", "/ai/suggest",
                            params={"ingredients": "chicken,garlic,tomato"},
                            title="Get AI suggestion for: chicken, garlic, tomato")
    if response and response.status_code == 200:
        data = response.json()
        print(f"   Suggestion: {data.get('suggestion', 'N/A')[:150]}...")
    
    # Get statistics
    print_section("6. Database Statistics")
    response = test_endpoint("GET", "/stats", title="Get database stats")
    if response and response.status_code == 200:
        data = response.json()
        print(f"   Total recipes: {data.get('total_recipes', 0)}")
        print(f"   Total cuisines: {data.get('cuisines', [])}")
        print(f"   Unique ingredients: {data.get('total_unique_ingredients', 0)}")
    
    # Add new recipe
    print_section("7. Add New Recipe")
    new_recipe = {
        "name": "Test Stir Fry",
        "cuisine": "Asian",
        "ingredients": ["noodles", "vegetables", "soy sauce"],
        "instructions": "Cook noodles, stir fry vegetables, mix with sauce",
        "prep_time": 15,
        "cook_time": 20
    }
    response = test_endpoint("POST", "/recipes", data=new_recipe,
                            title="Add a new test recipe")
    if response and response.status_code == 201:
        data = response.json()
        print(f"   Recipe added with ID: {data.get('id', 'N/A')}")
        recipe_id = data.get('id')
        
        # Update recipe
        print_section("8. Update Recipe")
        updated_recipe = new_recipe.copy()
        updated_recipe["name"] = "Updated Stir Fry"
        response = test_endpoint("PUT", f"/recipes/{recipe_id}", data=updated_recipe,
                                title=f"Update recipe {recipe_id}")
        
        # Delete recipe
        print_section("9. Delete Recipe")
        test_endpoint("DELETE", f"/recipes/{recipe_id}",
                     title=f"Delete recipe {recipe_id}")
    
    # API Documentation
    print_section("10. API Documentation")
    print(f"   📚 Interactive API docs available at:")
    print(f"   🔗 {BASE_URL}/docs")
    print(f"   🔗 {BASE_URL}/redoc")
    
    print_section("Summary")
    print("   ✅ All basic tests completed!")
    print("   📱 Web UI: http://127.0.0.1:8000")
    print("   📚 API Docs: http://127.0.0.1:8000/docs")
    print("   💡 To use AI features, set GROQ_API_KEY in .env")
    print("\n")

if __name__ == "__main__":
    main()
