# Setup Guide - Smart Recipe Explorer

## Prerequisites
- Python 3.8+
- pip package manager

## Installation Steps

### 1. Clone/Navigate to Project Directory
```bash
cd c:\Users\Anubh\Downloads\smart-recipe-explorer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup AI API Key (Choose One Option)

#### Option A: Groq API (Recommended - Free & Reliable)
1. Go to https://console.groq.com/
2. Sign up with your email (free, no credit card required)
3. Create an API key in the dashboard
4. Copy the key and paste it in `.env`:
```
GROQ_API_KEY=your_groq_api_key_here
```

#### Option B: Hugging Face API (Fallback)
1. Go to https://huggingface.co/settings/tokens
2. Create a new access token (read-only is fine)
3. Copy the token and update `.env`:
```
HF_API_KEY=your_huggingface_token_here
```

### 4. Run the Application
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 5. Access the Web Interface
Open your browser and go to:
```
http://127.0.0.1:8000
```

## API Endpoints

### Recipe Management
- `GET /api/recipes` - Get all recipes
- `GET /api/recipes/{recipe_id}` - Get specific recipe
- `POST /api/recipes` - Add new recipe
- `PUT /api/recipes/{recipe_id}` - Update recipe
- `DELETE /api/recipes/{recipe_id}` - Delete recipe

### Search & Filtering
- `GET /api/recipes/search/by-cuisine?cuisine=Italian` - Search by cuisine
- `GET /api/recipes/search/by-ingredient?ingredient=tomato` - Search by ingredient
- `GET /api/recipes/search/by-time?max_prep_time=30` - Search by time
- `POST /api/recipes/advanced-search` - Advanced search with multiple filters

### AI Features
- `GET /api/ai/suggest?ingredients=rice,tomato,onion` - Get AI recipe suggestion
- `POST /api/ai/suggest` - Post ingredients for AI suggestion

### Utilities
- `GET /api/stats` - Get database statistics
- `GET /api/health` - Health check endpoint

## API Documentation

Once the server is running, visit:
```
http://127.0.0.1:8000/docs
```

This provides an interactive Swagger UI where you can test all endpoints.

## Example Usage

### Get AI Recipe Suggestion
```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=chicken,garlic,tomato"
```

### Add a New Recipe
```bash
curl -X POST "http://127.0.0.1:8000/api/recipes" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Chicken Pasta",
    "cuisine": "Italian",
    "ingredients": ["chicken", "pasta", "tomato sauce"],
    "instructions": "Cook pasta, prepare sauce with chicken, combine",
    "prep_time": 20,
    "cook_time": 30
  }'
```

### Search by Cuisine
```bash
curl "http://127.0.0.1:8000/api/recipes/search/by-cuisine?cuisine=Asian"
```

## Troubleshooting

### AI Suggestion Not Working?
1. Make sure you've set either `GROQ_API_KEY` or `HF_API_KEY` in `.env`
2. Restart the server after updating `.env`
3. Check the browser console (F12) for error messages
4. Verify your API key is valid by visiting the provider's website

### Port Already in Use?
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

### ModuleNotFoundError?
Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

## Features

✅ **Recipe Management** - Create, read, update, delete recipes
✅ **Advanced Search** - Filter by cuisine, ingredients, cooking time
✅ **AI Integration** - Get recipe suggestions powered by AI
✅ **Statistics** - View database statistics
✅ **RESTful API** - Complete REST API with proper HTTP methods
✅ **Interactive UI** - Modern, responsive web interface
✅ **Error Handling** - Comprehensive error messages and validation
✅ **CORS Support** - Cross-origin requests enabled

## Technology Stack

- **Backend**: FastAPI, Python 3.11
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI**: Groq API (primary), Hugging Face (fallback)
- **Database**: In-memory list (can be extended to SQLite/PostgreSQL)
- **Server**: Uvicorn ASGI server

## Environment Variables

```env
# Groq API (Free, recommended)
GROQ_API_KEY=your_key_here

# Hugging Face (Fallback)
HF_API_KEY=your_key_here
```

## Project Structure

```
smart-recipe-explorer/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── models.py         # Pydantic models
│   ├── recipes.py        # Recipe database
│   └── ai_helper.py      # AI integration
├── static/
│   └── index.html        # Web UI
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies
└── README.md            # Documentation
```

## Notes

- The application uses an in-memory database, so recipes are lost on server restart
- For production, integrate with a real database (PostgreSQL, MongoDB, etc.)
- API keys should never be committed to version control
- Always use `.env` file for sensitive information

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the API documentation at `/docs`
3. Ensure all dependencies are installed correctly
4. Verify API keys are valid and not expired
