import requests
import os
from dotenv import load_dotenv
from typing import List

# Import Groq client
try:
    from groq import Groq
except ImportError:
    Groq = None

load_dotenv()

# Try to use Groq API (recommended - free tier available)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

def get_ai_recipe_suggestion(ingredients: List[str]) -> dict:
    """
    Get AI-powered recipe suggestion using Groq API (primary) or Hugging Face (fallback).
    
    Args:
        ingredients: List of available ingredients or dish names
        
    Returns:
        Dictionary with suggestion and ingredients used
    """
    if not ingredients:
        return {
            "suggestion": "Please provide at least one ingredient or dish name.",
            "ingredients_used": []
        }
    
    # Check if API keys are configured
    if not GROQ_API_KEY and not HF_API_KEY:
        return {
            "suggestion": """🚨 AI API Key Not Configured!

To use AI recipe suggestions:

1. Get Free Groq API Key (Recommended):
   - Visit: https://console.groq.com/
   - Sign up (free, no credit card needed)
   - Copy your API key
   
2. Or Get Hugging Face Token:
   - Visit: https://huggingface.co/settings/tokens
   - Create a new token
   
3. Add to .env file:
   GROQ_API_KEY=your_key_here
   OR
   HF_API_KEY=your_token_here
   
4. Restart the server

Need help? See QUICK_START.md or AI_INTEGRATION_GUIDE.md""",
            "ingredients_used": ingredients
        }
    
    # Try Groq API first (if key is available)
    if GROQ_API_KEY:
        result = _get_groq_suggestion(ingredients)
        if result:
            return result
    
    # Fallback to Hugging Face
    if HF_API_KEY:
        result = _get_huggingface_suggestion(ingredients)
        if result:
            return result
    
    # If both fail, return error message with instructions
    return {
        "suggestion": "⚠️ AI services are temporarily unavailable. Please try again in a moment.",
        "ingredients_used": ingredients
    }

def _get_groq_suggestion(ingredients: List[str]) -> dict:
    """Get recipe suggestion using Groq API."""
    try:
        if not Groq:
            print("Groq library not available")
            return None
            
        client = Groq(api_key=GROQ_API_KEY)
        
        # Check if input is a dish name or ingredients
        input_text = ', '.join(ingredients)
        
        # Create a smart prompt that handles both dish names and ingredients
        prompt = f"""You are an expert chef. The user wants a recipe.

They provided: {input_text}

This could be:
- A dish name (like "poha", "biryani", "pasta carbonara")
- Ingredients they have (like "chicken, garlic, tomato")

Please provide a COMPLETE RECIPE that either:
1. Is for the exact dish they named, OR
2. Uses the ingredients they provided

Format your response as:
**Recipe Name:** [name]
**Cuisine:** [type]
**Prep Time:** [minutes] min
**Cook Time:** [minutes] min
**Servings:** [number]

**Ingredients:**
- [ingredient with quantity]
- [ingredient with quantity]
(list all needed ingredients)

**Instructions:**
1. [step 1]
2. [step 2]
3. [step 3]
(continue with clear steps)

**Tips:** [any helpful tips]

Be specific, practical, and delicious!"""

        message = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=1000
        )
        
        suggestion = message.choices[0].message.content
        return {
            "suggestion": suggestion,
            "ingredients_used": ingredients
        }
            
    except Exception as e:
        print(f"Groq API error: {str(e)}")
        return None

def _get_huggingface_suggestion(ingredients: List[str]) -> dict:
    """Get recipe suggestion using Hugging Face API."""
    try:
        prompt = f"Suggest a simple recipe using these ingredients: {', '.join(ingredients)}. Include cooking instructions."
        
        headers = {
            "Authorization": f"Bearer {HF_API_KEY}"
        }
        
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                suggestion = result[0].get("generated_text", "Could not generate suggestion.")
                return {
                    "suggestion": suggestion,
                    "ingredients_used": ingredients
                }
        
        return None
        
    except Exception as e:
        print(f"Hugging Face API error: {str(e)}")
        return None
