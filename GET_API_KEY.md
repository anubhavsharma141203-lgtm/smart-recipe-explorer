# 🚀 AI Setup - Get Your Free API Key in 2 Minutes

## ⚡ Quick Setup (Just 3 Steps)

### Step 1: Go to Groq Console
**Click here:** https://console.groq.com/

### Step 2: Sign Up (Free - No Credit Card!)
- Click "Sign Up"
- Enter your email
- Verify email
- Done! ✅

### Step 3: Get Your API Key
1. Log in to your Groq account
2. Go to **"API Keys"** section (in left sidebar)
3. Click **"Create API Key"**
4. Copy the key (looks like: `gsk_xxxxxxxxxxxxxxxxxxxxx`)

### Step 4: Add to .env File
Open the file: `.env` (in your project folder)

Find this line:
```
GROQ_API_KEY=
```

Paste your key like this:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
```

**Save the file!** (Ctrl+S)

### Step 5: Restart Server
Kill current server (Ctrl+C) and run:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## ✨ Now You Can Use AI!

Go to http://127.0.0.1:8000 and try:

### Example 1: Recipe by Dish Name
**Type:** `poha`
**Click:** "🚀 Generate Recipe with AI"
**Result:** Full recipe for poha!

### Example 2: Recipe by Ingredients
**Type:** `chicken, garlic, tomato`
**Click:** "🚀 Generate Recipe with AI"
**Result:** Full recipe using those ingredients!

### Example 3: Any Dish
**Type:** `biryani` or `pasta carbonara` or `samosa`
**Result:** Complete AI-generated recipe!

---

## 🆘 Still Not Working?

### Check 1: Is API Key Added?
```
Open .env file
Look for: GROQ_API_KEY=gsk_...
Make sure it's NOT empty
```

### Check 2: Is Server Restarted?
```
Did you restart after adding key?
Press Ctrl+C to stop
Then run: uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Check 3: Check Terminal
Look at terminal for error messages. Share them if stuck.

### Check 4: Wrong Key Format?
- Groq key starts with: `gsk_`
- Hugging Face starts with: `hf_`

If copied wrong, go back to Groq console and get new one.

---

## 🎯 What You Should See

### When Working:
- Type dish name or ingredients
- Click button
- 5-10 seconds loading
- Full recipe appears! ✅

### When NOT Working:
- "AI service not configured" message
- Check Step 1-5 above
- Make sure key is in .env
- Restart server

---

## 📞 Need Help?

**Groq Support:** https://console.groq.com/help
**Check Docs:** See QUICK_START.md or AI_INTEGRATION_GUIDE.md

---

## ✅ Verify It Works

1. Start server
2. Go to http://127.0.0.1:8000
3. Type: `poha`
4. Click: "🚀 Generate Recipe with AI"
5. Wait 5-10 seconds
6. See full recipe! ✨

**That's it! Enjoy! 👨‍🍳**
