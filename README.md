# Smart Recipe Explorer with AI Assistance

A FastAPI-based recipe management application with AI-powered recipe suggestions, comprehensive search and filtering capabilities, and a modern web interface.

## Features

✨ **Core Features:**
- 📚 **Recipe Management**: Create, read, update, and delete recipes
- 🔍 **Advanced Search**: Filter recipes by cuisine, ingredients, and cooking time
- 🤖 **AI Recipe Suggestions**: Get intelligent recipe recommendations based on available ingredients using Hugging Face API
- 📊 **Statistics Dashboard**: View recipe database statistics
- 🎨 **Modern UI**: Responsive web interface with smooth interactions

## Technology Stack

- **Backend**: FastAPI (Python web framework)
- **Server**: Uvicorn (ASGI server)
- **API Documentation**: Automatic Swagger UI & ReDoc
- **Frontend**: Vanilla JavaScript with modern CSS
- **AI Integration**: Hugging Face Inference API (free tier)
- **Environment Management**: python-dotenv

## Project Structure

```
smart-recipe-explorer/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # FastAPI application with all endpoints
│   ├── models.py            # Pydantic models for data validation
│   ├── recipes.py           # Recipe database (in-memory)
│   └── ai_helper.py         # AI integration with Hugging Face
├── static/
│   └── index.html           # Frontend UI
├── .env                     # Environment variables (API keys)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or navigate to the project directory**:
   ```bash
   cd smart-recipe-explorer
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Open `.env` file
   - Add your Hugging Face API key:
     ```
     HF_API_KEY=your_hugging_face_api_key_here
     ```
   - Get a free API key from: https://huggingface.co/settings/tokens

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the application**:
   - Open your browser and navigate to: `http://127.0.0.1:8000`
   - API Documentation (Swagger UI): `http://127.0.0.1:8000/docs`
   - Alternative API Documentation (ReDoc): `http://127.0.0.1:8000/redoc`

## API Endpoints

### Recipe Management

#### Get All Recipes
```
GET /api/recipes
```
Returns all recipes in the database.

#### Get Recipe by ID
```
GET /api/recipes/{recipe_id}
```
Returns a specific recipe.

#### Add New Recipe
```
POST /api/recipes
Content-Type: application/json

{
  "name": "Spaghetti Carbonara",
  "cuisine": "Italian",
  "ingredients": ["pasta", "eggs", "bacon", "cheese"],
  "instructions": "Cook pasta, mix with bacon and eggs...",
  "prep_time": 10,
  "cook_time": 20,
  "servings": 4
}
```

#### Update Recipe
```
PUT /api/recipes/{recipe_id}
Content-Type: application/json
```

#### Delete Recipe
```
DELETE /api/recipes/{recipe_id}
```

### Search & Filtering

#### Search by Cuisine
```
GET /api/recipes/search/by-cuisine?cuisine=Italian
```

#### Search by Ingredient
```
GET /api/recipes/search/by-ingredient?ingredient=tomato
```

#### Search by Cooking Time
```
GET /api/recipes/search/by-time?max_prep_time=30&max_cook_time=45
```

#### Advanced Search
```
POST /api/recipes/advanced-search
Content-Type: application/json

{
  "cuisine": "Italian",
  "ingredient": "pasta",
  "prep_time_max": 30
}
```

### AI Features

#### Get AI Recipe Suggestion (GET)
```
GET /api/ai/suggest?ingredients=rice,tomato,onion
```

#### Get AI Recipe Suggestion (POST)
```
POST /api/ai/suggest
Content-Type: application/json

{
  "ingredient_list": ["rice", "tomato", "onion"]
}
```

### Utility Endpoints

#### Get Statistics
```
GET /api/stats
```
Returns database statistics including total recipes, unique cuisines, ingredients, and average prep time.

#### Health Check
```
GET /api/health
```
Simple endpoint to verify API is running.

## API Response Examples

### Successful Recipe Response
```json
{
  "id": 1,
  "name": "Veg Fried Rice",
  "ingredients": ["rice", "vegetables", "soy sauce", "egg", "garlic"],
  "instructions": "Heat oil in a wok...",
  "cuisine": "Asian",
  "servings": 4,
  "prep_time": 15,
  "cook_time": 20
}
```

### AI Suggestion Response
```json
{
  "suggestion": "You can make a delicious stir-fried rice with the ingredients you have...",
  "ingredients_used": ["rice", "tomato", "onion"]
}
```

### Statistics Response
```json
{
  "total_recipes": 5,
  "cuisines": ["Asian", "Italian", "Indian", "Mexican", "American"],
  "total_unique_ingredients": 25,
  "avg_prep_time": 18.0
}
```

## Frontend Features

The web UI provides:

1. **🤖 AI Recipe Suggestion**: Input ingredients and get recipe suggestions
2. **🔍 Recipe Search**: Three search modes
   - By Cuisine (dropdown selection)
   - By Ingredient (text search)
   - By Cooking Time (time range filter)
3. **➕ Add New Recipe**: Create new recipes with full details
4. **📚 View All Recipes**: Browse all available recipes
5. **📊 Statistics Dashboard**: Real-time stats about the recipe database

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input or missing required fields
- **404 Not Found**: Recipe or resource not found
- **500 Internal Server Error**: Server-side errors

All error responses include descriptive messages.

## Responsible AI Usage

This application uses the **Hugging Face Inference API** (free tier):

- **Free to use**: No credit card required
- **Model**: Google's FLAN-T5-Small for text generation
- **Rate limits**: Typical free tier includes reasonable limits
- **Privacy**: Review Hugging Face privacy policy for data handling

### Best Practices for AI Integration

✅ **Do's:**
- Use meaningful ingredient combinations
- Monitor API usage for rate limits
- Cache results when possible
- Validate AI responses before displaying

❌ **Don'ts:**
- Don't expose API keys in code repositories
- Don't spam the AI endpoint with requests
- Don't rely solely on AI-generated content

## Example Workflows

### Creating a Recipe
1. Click "Add New Recipe"
2. Fill in recipe details (name, cuisine, ingredients, instructions, times)
3. Click "Add Recipe"
4. Recipe appears in the database

### Getting AI Suggestions
1. Enter ingredients separated by commas
2. Click "Get AI Suggestion"
3. Receive AI-powered recipe suggestion
4. Use as inspiration for new recipes

### Searching Recipes
1. Choose search method (cuisine, ingredient, or time)
2. Enter search criteria
3. View matching recipes
4. Click recipe cards to see full details

## Future Enhancements

- Database persistence (SQLite/PostgreSQL)
- User authentication and personal recipe collections
- Recipe ratings and reviews
- Nutritional information integration
- Image upload for recipes
- Recipe scaling (adjust servings)
- Export recipes to PDF
- Shopping list generation

## Troubleshooting

### API Not Starting
- Ensure Python 3.8+ is installed
- Check all dependencies: `pip list`
- Verify no port conflicts on 8000

### AI Suggestions Not Working
- Verify HF_API_KEY in .env file
- Check Hugging Face API status
- Ensure internet connection is active

### Frontend Not Loading
- Verify server is running: `http://127.0.0.1:8000`
- Check browser console for errors
- Clear browser cache if needed

## Environment Variables

Create a `.env` file in the project root:

```env
# Hugging Face API Configuration
HF_API_KEY=your_api_key_here

# Optional: FastAPI Configuration
API_TITLE=Smart Recipe Explorer API
DEBUG=True
```

## Security Notes

⚠️ **Important:**
- Never commit `.env` file to version control
- Use environment variables for all sensitive data
- Validate all user inputs
- Use HTTPS in production
- Implement rate limiting for production deployment

## Learning Outcomes

This project demonstrates:

✅ **Python Web Development**
- FastAPI framework usage
- RESTful API design
- Request/response handling
- Error management

✅ **Frontend Integration**
- Async JavaScript (Fetch API)
- DOM manipulation
- Form handling and validation
- CSS styling and responsiveness

✅ **AI Integration**
- External API consumption
- Prompt engineering
- Error handling for AI responses

✅ **Full-Stack Development**
- Backend-frontend communication
- CORS configuration
- API documentation
- Responsive web design

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Check `.env` configuration
4. Verify all dependencies are installed

## API Documentation

Once the server is running, access:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

These provide interactive API documentation with the ability to test endpoints directly.
