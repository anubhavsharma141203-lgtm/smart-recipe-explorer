# 🎯 AI Recipe Feature - How to Use

## The Problem (Current State)
```
User types: "poha"
AI responds: "AI service not configured"
❌ API key is empty in .env
```

## The Solution (3 Simple Steps)

### 1️⃣ GET API KEY
```
Go to: https://console.groq.com/
Sign up for FREE (no credit card!)
Go to API Keys section
Create new API key
Copy it (gsk_xxx...)
```

### 2️⃣ ADD TO .env
```
Open: .env file
Find: GROQ_API_KEY=
Add: GROQ_API_KEY=gsk_xxx...
Save file
```

### 3️⃣ RESTART SERVER
```
Stop: Press Ctrl+C
Run: uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
Start: Wait for "Application startup complete"
```

---

## NOW IT WORKS! ✨

### User wants Poha recipe
```
1. Go to: http://127.0.0.1:8000
2. Type: "poha"
3. Click: "🚀 Generate Recipe with AI"
4. Wait: 5-10 seconds
5. Get: Full recipe with ingredients & instructions
```

### User has ingredients
```
1. Go to: http://127.0.0.1:8000
2. Type: "chicken, garlic, tomato"
3. Click: "🚀 Generate Recipe with AI"
4. Wait: 5-10 seconds
5. Get: Full recipe using those ingredients
```

---

## 🔧 What Changed in Code

### ai_helper.py
✅ **Better error message** - Shows exactly what to do
✅ **Accepts dish names** - "poha", "biryani", "pasta" etc
✅ **Accepts ingredients** - "chicken, garlic, tomato"
✅ **Longer timeout** - 15 seconds (was 10)
✅ **Bigger responses** - Max 1000 tokens (was 500)

### index.html (Frontend)
✅ **Better instructions** - Shows examples
✅ **Better formatting** - Recipe displays nicely
✅ **Longer loading message** - Shows "5-10 seconds"
✅ **Better button text** - "🚀 Generate Recipe with AI"

---

## 📋 Checklist Before Using

- [ ] Opened https://console.groq.com/
- [ ] Signed up with email
- [ ] Got API key (starts with gsk_)
- [ ] Opened .env file
- [ ] Added key to GROQ_API_KEY=
- [ ] Saved .env file
- [ ] Restarted server
- [ ] Waited for "Application startup complete"

---

## 🧪 Test It

1. Start server
2. Open http://127.0.0.1:8000
3. Go to "🤖 AI Recipe Suggestion" section
4. Type: **`poha`**
5. Click: **"🚀 Generate Recipe with AI"**
6. Wait 5-10 seconds
7. See full recipe! ✅

---

## Expected Output

```
✨ AI Generated Recipe

**Recipe Name:** Poha (Flattened Rice Breakfast)
**Cuisine:** Indian
**Prep Time:** 5 min
**Cook Time:** 5 min
**Servings:** 2

**Ingredients:**
- 1 cup flattened rice (poha)
- 1 potato, diced
- 1/2 onion, diced
- 1 tbsp oil
- 1 tsp mustard seeds
- Turmeric, salt, chili powder
- Fresh cilantro
- Lemon juice

**Instructions:**
1. Heat oil in a pan
2. Add mustard seeds, let them crackle
3. Add diced potatoes and onions
4. Fry until potatoes are soft
5. Add flattened rice
6. Season with spices
7. Mix well and cook for 2 minutes
8. Add cilantro and lemon juice
9. Serve hot!

**Tips:** You can add peanuts or cashews for crunch
```

---

## ⚠️ Common Issues & Fixes

### Issue: "API Key Not Configured"
**Fix:**
1. Open .env file
2. Check GROQ_API_KEY line is NOT empty
3. Make sure key is pasted correctly
4. Restart server

### Issue: "Request timeout"
**Fix:**
1. Try again (might be slow first time)
2. Check internet connection
3. Server might be processing

### Issue: "API Key invalid"
**Fix:**
1. Go back to https://console.groq.com/
2. Generate new API key
3. Copy and paste carefully
4. Restart server

### Issue: Server won't start
**Fix:**
1. Check for syntax errors
2. Make sure .env file is valid
3. Try: `pip install -r requirements.txt --force-reinstall`
4. Restart

---

## ✅ Verification

Open browser console (F12) and try:
```javascript
// Check API is responding
fetch('http://127.0.0.1:8000/api/health')
  .then(r => r.json())
  .then(d => console.log(d))
```

Should show:
```json
{
  "status": "healthy",
  "service": "Smart Recipe Explorer API"
}
```

---

## 🎓 How It Works

1. **You type:** "poha"
2. **Frontend sends:** GET request with "poha"
3. **Backend receives:** "poha" in ingredients parameter
4. **AI helper checks:** Is GROQ_API_KEY set?
5. **Groq API:** Creates smart prompt about poha
6. **Groq returns:** Full recipe for poha
7. **Frontend displays:** Nicely formatted recipe
8. **You see:** Complete recipe with steps!

---

## 🎉 You're Ready!

**Just follow the 3 steps above and you're done!**

### Next Steps:
1. Get API key
2. Add to .env
3. Restart server
4. Try "poha" or any dish
5. Enjoy AI-generated recipes! 🚀

---

**Any questions? Check:**
- GET_API_KEY.md (this file)
- QUICK_START.md
- AI_INTEGRATION_GUIDE.md
- INDEX.md (documentation map)
