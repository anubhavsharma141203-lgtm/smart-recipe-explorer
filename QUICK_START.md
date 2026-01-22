# 🚀 Quick Start Guide - Smart Recipe Explorer

## Step 1: Get Your AI API Key

### Option A: Groq API (Recommended - Free)
Best option for fast, reliable AI responses. No credit card required.

1. **Visit** https://console.groq.com/
2. **Sign up** with your email (completely free)
3. **Copy your API key** from the dashboard
4. **Update .env file:**
   ```
   GROQ_API_KEY=your_api_key_here
   ```

**Why Groq?**
- ✅ Free tier with generous limits
- ✅ Fastest AI responses
- ✅ No credit card required
- ✅ Easy to set up

### Option B: Hugging Face API (Fallback)
If you prefer using Hugging Face models.

1. **Visit** https://huggingface.co/settings/tokens
2. **Create a new token** (read-only is fine)
3. **Copy the token**
4. **Update .env file:**
   ```
   HF_API_KEY=your_token_here
   ```

## Step 2: Install Dependencies

```bash
cd c:\Users\Anubh\Downloads\smart-recipe-explorer
pip install -r requirements.txt
```

## Step 3: Run the Application

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

## Step 4: Access the Application

Open your browser and go to:
- **Web UI**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **Alternative Docs**: http://127.0.0.1:8000/redoc

## 📱 Using the Web Interface

### 1. Get AI Recipe Suggestions
- Enter ingredients separated by commas (e.g., "chicken, garlic, tomato")
- Click "Get AI Suggestion"
- The AI will suggest a recipe using those ingredients

### 2. Search Recipes
- **By Cuisine**: Select a cuisine type (Asian, Italian, Indian, etc.)
- **By Ingredient**: Enter an ingredient to find recipes containing it
- **By Time**: Enter max cooking time to find quick recipes

### 3. Add New Recipes
- Fill in the recipe details
- Click "Add Recipe"
- Your recipe will be added to the database

### 4. View All Recipes
- Click "Load Recipes" to see all available recipes
- Each recipe card shows name, ingredients, instructions, and times

### 5. Check Statistics
- View total recipes, cuisines, ingredients, and average prep time

## 🧪 Testing the API with curl

### Get Health Status
```bash
curl http://127.0.0.1:8000/api/health
```

### Get All Recipes
```bash
curl http://127.0.0.1:8000/api/recipes
```

### Search by Cuisine
```bash
curl "http://127.0.0.1:8000/api/recipes/search/by-cuisine?cuisine=Asian"
```

### Get AI Suggestion
```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=chicken,garlic,tomato"
```

### Add a Recipe
```bash
curl -X POST http://127.0.0.1:8000/api/recipes \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Garlic Chicken",
    "cuisine": "Asian",
    "ingredients": ["chicken", "garlic", "soy sauce"],
    "instructions": "Fry chicken with garlic and soy sauce",
    "prep_time": 20,
    "cook_time": 30
  }'
```

## 📚 API Documentation

The application includes interactive API documentation via Swagger UI:

**Visit**: http://127.0.0.1:8000/docs

Here you can:
- ✅ See all available endpoints
- ✅ Test endpoints directly from your browser
- ✅ View request/response schemas
- ✅ See example data

## ⚙️ Configuration

Edit the `.env` file to customize:

```env
# Groq API (Primary - Recommended)
GROQ_API_KEY=your_groq_api_key

# Hugging Face (Fallback)
HF_API_KEY=your_huggingface_token
```

## 🆘 Troubleshooting

### "Module not found" error?
```bash
pip install -r requirements.txt --force-reinstall
```

### AI suggestions not working?
1. ✅ Verify API key is in `.env`
2. ✅ Restart the server (Ctrl+C, then run again)
3. ✅ Check if your API key is valid
4. ✅ Look at the terminal for error messages

### Port 8000 already in use?
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

### Still having issues?
1. Check the terminal for error messages
2. Verify your API key is correct
3. Try the health check: `curl http://127.0.0.1:8000/api/health`
4. Check the interactive docs at `/docs`

## 🎯 Key Features Explained

### Recipe Management
Add, update, delete, and view recipes in the database. Each recipe includes:
- Name
- Cuisine type
- Ingredients
- Cooking instructions
- Prep time
- Cook time
- Servings

### Advanced Search
Find recipes using multiple criteria:
- **Cuisine**: Find all recipes of a specific cuisine
- **Ingredient**: Find recipes containing a specific ingredient
- **Time**: Find recipes that can be made in a certain time
- **Combined**: Search with multiple filters at once

### AI Assistance
Get intelligent recipe suggestions based on your available ingredients. The AI will:
- Analyze your ingredients
- Suggest a complete recipe
- Include cooking method and time estimates
- Provide step-by-step instructions

### Statistics
Track your recipe database:
- Total number of recipes
- Available cuisines
- Unique ingredients
- Average preparation time

## 📖 Example Workflows

### Workflow 1: Find a Quick Dinner
1. Go to "Search Recipes" → "By Time" tab
2. Enter 30 minutes
3. See all recipes you can make in 30 minutes
4. Click on one and follow the instructions

### Workflow 2: Use Available Ingredients
1. Go to "AI Recipe Suggestion"
2. Enter your available ingredients
3. Get an AI-suggested recipe
4. Cook and enjoy!

### Workflow 3: Explore a Cuisine
1. Go to "Search Recipes" → "By Cuisine" tab
2. Select a cuisine (e.g., "Italian")
3. Browse all recipes from that cuisine
4. Add your favorites or try new ones

## 🔗 Links

- **Groq Console**: https://console.groq.com/
- **Hugging Face**: https://huggingface.co/settings/tokens
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **API Documentation**: http://127.0.0.1:8000/docs

## ✨ Next Steps

1. ✅ Get your API key (Groq or Hugging Face)
2. ✅ Update the `.env` file
3. ✅ Run the server
4. ✅ Open http://127.0.0.1:8000 in your browser
5. ✅ Try the AI suggestions
6. ✅ Add your own recipes
7. ✅ Explore the advanced search features

## 🎓 Learning Resources

This project teaches:
- Building REST APIs with FastAPI
- Working with external APIs
- Data validation with Pydantic
- Frontend-backend integration
- Error handling and status codes
- Environment variable management
- CORS and middleware configuration

---

**Happy Cooking! 👨‍🍳👩‍🍳**

**Questions?** Check the API documentation at http://127.0.0.1:8000/docs
