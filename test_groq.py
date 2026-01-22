from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

try:
    client = Groq(api_key=api_key)
    print("Testing Groq API with recipe request...\n")
    
    prompt = """You are an expert chef. Create a recipe for poha.

Format:
**Recipe Name:** Poha
**Cuisine:** Indian
**Prep Time:** 5 min
**Cook Time:** 5 min
**Servings:** 2

**Ingredients:**
- List all needed ingredients with quantities

**Instructions:**
1. First step
2. Second step
(etc)

**Tips:** Any helpful tips"""
    
    message = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
        max_tokens=1000
    )
    
    print("✓ API working!\n")
    print(message.choices[0].message.content)
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
