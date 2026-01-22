# 🤖 AI Integration Guide

## Overview

The Smart Recipe Explorer integrates with AI APIs to generate intelligent recipe suggestions based on available ingredients.

## Supported AI Services

### 1. Groq API (Recommended)

**Best For**: Production use, fast responses, reliability

**Advantages:**
- ✅ Free tier with generous limits (no credit card required)
- ✅ Super fast responses (mixtral-8x7b model)
- ✅ No rate limiting concerns for normal use
- ✅ Reliable and battle-tested
- ✅ Easy signup and setup

**Setup:**
1. Go to https://console.groq.com/
2. Sign up with your email
3. Go to API keys section
4. Create a new key
5. Add to `.env`:
   ```
   GROQ_API_KEY=gsk_your_key_here
   ```

**Model Used:** Mixtral-8x7b-32768
- 8 expert mixture model
- 32K context window
- Excellent for cooking recipes

### 2. Hugging Face API (Fallback)

**Best For**: Backup when Groq is unavailable

**Advantages:**
- ✅ Free tier available
- ✅ Many model options
- ✅ Good for experimental use

**Setup:**
1. Go to https://huggingface.co/settings/tokens
2. Create a new access token
3. Add to `.env`:
   ```
   HF_API_KEY=hf_your_token_here
   ```

## How It Works

### Request Flow

```
User Input (Ingredients)
    ↓
API Endpoint (/api/ai/suggest)
    ↓
Check Groq API → Try Groq First
    ↓
If Groq fails → Fall back to Hugging Face
    ↓
Return suggestion to user
```

### Example Request

**GET Request:**
```
/api/ai/suggest?ingredients=chicken,tomato,garlic
```

**POST Request:**
```
POST /api/ai/suggest
Content-Type: application/json

{
  "ingredient_list": ["chicken", "tomato", "garlic"]
}
```

### Example Response

```json
{
  "suggestion": "Chicken Tomato Basil Pasta

Here's a delicious recipe using your ingredients:

**Recipe:** Quick Chicken Tomato Garlic Pasta
**Cuisine:** Italian-Asian Fusion
**Prep Time:** 10 minutes
**Cook Time:** 20 minutes

**Ingredients:**
- 500g chicken breast, diced
- 3 medium tomatoes, chopped (or 1 can crushed tomatoes)
- 4 cloves garlic, minced
- 350g pasta (spaghetti or penne)
- 2 tbsp olive oil
- Salt and pepper to taste
- Fresh basil (optional)

**Instructions:**
1. Cook pasta according to package directions. Drain and set aside.
2. Heat olive oil in a large pan over medium-high heat.
3. Add minced garlic and cook for 1 minute until fragrant.
4. Add diced chicken and cook until golden, about 5-7 minutes.
5. Add chopped tomatoes and simmer for 10 minutes.
6. Season with salt and pepper to taste.
7. Toss the cooked pasta with the chicken tomato sauce.
8. Garnish with fresh basil if available.
9. Serve hot!

**Tips:**
- For a creamier sauce, add a splash of heavy cream
- You can add other vegetables like bell peppers or zucchini
- Fresh basil makes a huge difference in flavor",
  "ingredients_used": ["chicken", "tomato", "garlic"]
}
```

## Configuration Details

### Environment Variables

```env
# Primary AI service (Groq)
GROQ_API_KEY=gsk_your_groq_key_here

# Fallback AI service (Hugging Face)
HF_API_KEY=hf_your_huggingface_token_here
```

### API Configuration

**File:** `app/ai_helper.py`

```python
# Primary: Groq API
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
Model: "mixtral-8x7b-32768"
Temperature: 0.7
Max tokens: 500

# Fallback: Hugging Face
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
```

## Code Implementation

### How to Use the AI Helper

```python
from app.ai_helper import get_ai_recipe_suggestion

# Call the function
ingredients = ["chicken", "rice", "soy sauce"]
result = get_ai_recipe_suggestion(ingredients)

# Result
print(result["suggestion"])      # The recipe suggestion
print(result["ingredients_used"]) # List of ingredients used
```

### Internal Implementation

The `ai_helper.py` module:

1. **Checks for API keys** on startup
2. **Tries Groq first** (if `GROQ_API_KEY` is set)
3. **Falls back to Hugging Face** (if `HF_API_KEY` is set)
4. **Returns error message** if neither is available
5. **Handles timeouts and errors** gracefully

## Testing AI Integration

### Test 1: Verify API Key

```bash
# Check if your Groq API key is valid
curl -H "Authorization: Bearer YOUR_KEY" \
  https://api.groq.com/openai/v1/models
```

### Test 2: Get a Recipe Suggestion

```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=chicken,rice,onion"
```

### Test 3: Test with Multiple Ingredients

```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=pasta,tomato,basil,garlic,olive oil"
```

## Troubleshooting AI Features

### Issue: "AI service not configured"

**Solution:**
1. Make sure `.env` file exists in the project root
2. Check that `GROQ_API_KEY` or `HF_API_KEY` is set
3. Restart the server after adding the key
4. Verify the key has no extra spaces

### Issue: "Request timeout"

**Possible Causes:**
- Groq API is slow to respond
- Network connectivity issue
- API key rate limit exceeded

**Solution:**
1. Try again in a few seconds
2. Check your internet connection
3. Try the fallback API (Hugging Face)

### Issue: "Invalid API key"

**Solution:**
1. Visit the API provider's website
2. Generate a new API key
3. Copy the complete key without spaces
4. Update `.env` and restart server

### Issue: Groq returns error 401

**Solution:**
- Your API key is invalid or expired
- Go to https://console.groq.com/ and generate a new key
- Update `.env` with the new key

## Performance Considerations

### Groq API
- **Response Time**: ~2-5 seconds
- **Free Tier Rate Limit**: 30 requests per minute
- **Quality**: Excellent
- **Cost**: Free (up to limits)

### Hugging Face API
- **Response Time**: ~10-30 seconds (model warm-up time)
- **Free Tier Rate Limit**: Varies by model
- **Quality**: Good
- **Cost**: Free (limited)

## Best Practices

### 1. API Key Security
```
✅ DO: Use environment variables
✅ DO: Add .env to .gitignore
❌ DON'T: Hardcode API keys in source code
❌ DON'T: Commit .env file to git
```

### 2. Error Handling
```
✅ DO: Handle timeouts
✅ DO: Provide fallback options
✅ DO: Log errors for debugging
❌ DON'T: Expose API keys in error messages
```

### 3. Rate Limiting
```
✅ DO: Implement request caching
✅ DO: Monitor API usage
✅ DO: Use reasonable timeouts
```

## Example Usage Scenarios

### Scenario 1: Quick Dinner

User has: chicken, rice, soy sauce

```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=chicken,rice,soy sauce"
```

AI suggests: Chicken Fried Rice

### Scenario 2: Leftover Ingredients

User has: pasta, tomato, garlic, basil, olive oil

```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=pasta,tomato,garlic,basil,olive oil"
```

AI suggests: Pasta al Pomodoro

### Scenario 3: Dietary Experiment

User has: tofu, broccoli, ginger, sesame oil

```bash
curl "http://127.0.0.1:8000/api/ai/suggest?ingredients=tofu,broccoli,ginger,sesame oil"
```

AI suggests: Ginger Sesame Tofu Stir Fry

## Advanced Configuration

### Custom Prompts

Edit `app/ai_helper.py` to customize the prompt:

```python
prompt = f"""You are a professional chef. Based on these ingredients: {', '.join(ingredients)}, 
suggest a simple, delicious recipe. Include:
1. Recipe name
2. Main cooking method
3. Estimated cooking time
4. 3-4 simple steps

Be concise and practical."""
```

### Temperature Settings

```python
# Lower = more consistent (0.3-0.5)
# Higher = more creative (0.8-1.0)
"temperature": 0.7,  # Balanced
```

### Token Limits

```python
# Longer = more detailed response
# Shorter = concise response
"max_tokens": 500,  # Current setting
```

## FAQ

**Q: Which API should I use?**
A: Start with Groq. It's faster, free, and more reliable.

**Q: Can I use both APIs?**
A: Yes! Groq is the primary, and Hugging Face is the automatic fallback.

**Q: What if both APIs fail?**
A: The app returns a helpful error message and links to setup guides.

**Q: Is there a cost?**
A: Both Groq and Hugging Face offer free tiers. No credit card required.

**Q: How many requests can I make?**
A: Groq: 30 requests/minute free. Hugging Face varies by model.

**Q: Can I switch APIs without restarting?**
A: No, you need to restart the server after updating `.env`.

---

**Need Help?** Check the quick start guide or visit the API docs at `/docs`
