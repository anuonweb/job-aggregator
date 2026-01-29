# 🚀 Quick Start Guide

## Test Locally (5 Minutes)

### 1. Prerequisites
- Python 3.8+ installed
- Internet connection

### 2. Setup
Open terminal/command prompt and run:

```bash
# Navigate to the project folder
cd job-aggregator

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### 3. Open Browser
Go to: http://localhost:5000

### 4. Test It
1. Click the "🔄 Refresh Jobs" button
2. Wait 10-20 seconds for jobs to load
3. Use search and filters to explore jobs
4. Click "View Job →" to see the original posting

### 5. What You Should See
- Job cards with title, company, location
- Jobs from Indeed, Job Bank, Eluta, and sample jobs from Amazon/Walmart/Loblaw
- Filter buttons to sort by job site
- Search box to find specific jobs

---

## Deploy Online (10 Minutes)

### Option A: Render (Easiest)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/anuonweb/canada-job-aggregator.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to https://render.com
   - Sign up (free, no credit card)
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Use these settings:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
   - Click "Create Web Service"
   - Wait 2-3 minutes
   - Done! You get a URL like: `yourapp.onrender.com`

### Option B: Railway

1. Push to GitHub (same as above)
2. Go to https://railway.app
3. Sign up with GitHub
4. Click "New Project" → "Deploy from GitHub"
5. Select your repo
6. Click "Generate Domain"
7. Done!

---

## Troubleshooting

**Q: Jobs not showing?**
A: Click "Refresh Jobs" button - database starts empty.

**Q: "Module not found" error?**
A: Run `pip install -r requirements.txt` again.

**Q: Slow to load?**
A: Normal for free hosting - first request wakes the server.

**Q: Want to add more job sites?**
A: Edit `app.py` and add new scraping functions. See README.md for details.

---

## What's Next?

✅ Local version working
✅ Deployed online
🔜 Add email notifications
🔜 Schedule automatic updates
🔜 Add more job sites
🔜 Improve scraping accuracy

---

## Files Overview

- `app.py` - Backend server with scraping logic
- `templates/index.html` - Frontend UI
- `requirements.txt` - Python packages needed
- `jobs.db` - Database (auto-created)
- `README.md` - Full documentation
- `DEPLOYMENT.md` - Detailed deployment steps

---

## Need Help?

1. Check README.md for detailed docs
2. Check DEPLOYMENT.md for deployment issues
3. Review error logs on hosting platform
4. GitHub: @anuonweb

**Happy job hunting! 🎯**
