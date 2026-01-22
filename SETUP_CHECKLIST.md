# ⚡ QUICK ACTION ITEMS

## 🎯 DO THIS RIGHT NOW (5 minutes)

### Step 1: Get Free API Key
```
1. Open browser
2. Go to: https://console.groq.com/
3. Click "Sign Up"
4. Enter your email
5. Verify email & login
6. Click "API Keys" (left sidebar)
7. Click "Create API Key"
8. COPY the key (it looks like: gsk_xxxxxxxxxxxx)
```

### Step 2: Add Key to .env File
```
1. Open file: .env
2. Find line: GROQ_API_KEY=
3. Add your key after = 
   Example: GROQ_API_KEY=gsk_xxxxxxxxxxxx
4. Save file (Ctrl+S)
```

### Step 3: Restart Server
```
1. In terminal, press Ctrl+C (stop current server)
2. Run: uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
3. Wait for: "Application startup complete"
```

### Step 4: Test It
```
1. Open: http://127.0.0.1:8000
2. Type in AI box: "poha"
3. Click: "🚀 Generate Recipe with AI"
4. Wait 5-10 seconds
5. See recipe! ✨
```

---

## 📁 Files You Need

### MUST READ (Before Using)
- **GET_API_KEY.md** ← Read this FIRST!
- **HOW_TO_USE_AI.md** ← Then read this

### Configuration
- **.env** ← Add your API key here

### Server
- Start with: `uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`

---

## ✅ Checklist

- [ ] Created Groq account
- [ ] Got API key
- [ ] Added key to .env
- [ ] Saved .env file
- [ ] Restarted server
- [ ] Opened http://127.0.0.1:8000
- [ ] Typed "poha" in AI box
- [ ] Got recipe back ✨

---

## 🔴 STOP HERE IF:

❌ **API Key is empty in .env**
→ Go do Step 1-2 above

❌ **Server not restarted after adding key**
→ Press Ctrl+C and restart

❌ **Still getting "API Key Not Configured"**
→ Check .env file has your key
→ Restart server again
→ Check browser cache (Ctrl+Shift+Delete)

---

## 📞 Support

If stuck:
1. Check GET_API_KEY.md
2. Check HOW_TO_USE_AI.md  
3. Check QUICK_START.md
4. Check AI_INTEGRATION_GUIDE.md

---

## 🎉 THAT'S IT!

You're all set to use AI recipe suggestions! 🚀

**Just:**
1. Get API key (2 min)
2. Add to .env (1 min)
3. Restart (1 min)
4. Try "poha" or any dish!

Enjoy! 👨‍🍳
