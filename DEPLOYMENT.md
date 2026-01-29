# 🚀 Deployment Guide - Canada Job Aggregator

## Option 1: Deploy to Render (Recommended - FREE)

### Step 1: Prepare Your GitHub Repository

1. **Create a new repository on GitHub:**
   - Go to https://github.com/anuonweb
   - Click "New repository"
   - Name: `canada-job-aggregator`
   - Make it Public
   - Don't initialize with README (we already have one)
   - Click "Create repository"

2. **Push your code to GitHub:**
   ```bash
   cd job-aggregator
   git init
   git add .
   git commit -m "Initial commit - Canada Job Aggregator"
   git branch -M main
   git remote add origin https://github.com/anuonweb/canada-job-aggregator.git
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Sign up for Render:**
   - Go to https://render.com
   - Click "Get Started for Free"
   - Sign up with GitHub (easiest option)
   - No credit card required!

2. **Create a new Web Service:**
   - Click "New +" in the top right
   - Select "Web Service"
   - Click "Connect account" to connect GitHub
   - Select the `canada-job-aggregator` repository
   - Click "Connect"

3. **Configure the service:**
   ```
   Name: canada-job-aggregator
   Region: Oregon (US West) or closest to you
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Instance Type: Free
   ```

4. **Click "Create Web Service"**
   - Render will automatically build and deploy
   - Wait 2-3 minutes for initial deployment
   - You'll get a URL like: `https://canada-job-aggregator.onrender.com`

5. **Test your site:**
   - Open the provided URL
   - Click "Refresh Jobs" to start scraping
   - Your job aggregator is now live! 🎉

### Step 3: Keep It Active

**Important:** Free Render services sleep after 15 minutes of inactivity.

To keep it active, you can:
- Visit the site regularly
- Set up a free uptime monitor (e.g., UptimeRobot.com)
- Upgrade to paid plan ($7/month) for always-on service

---

## Option 2: Deploy to Railway

### Step 1: Prepare Code (Same as Render)
Follow "Step 1" from Render instructions above.

### Step 2: Deploy on Railway

1. **Sign up:**
   - Go to https://railway.app
   - Sign up with GitHub
   - Get $5 free credit (30-day trial)

2. **Create new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `canada-job-aggregator`
   - Railway auto-detects settings

3. **Add domain:**
   - Click "Settings" → "Networking"
   - Click "Generate Domain"
   - Your site is live!

**Cost after trial:** $5/month includes $5 usage credit

---

## Option 3: Deploy to Heroku

### Step 1: Create Procfile
Create a file named `Procfile` (no extension):
```
web: gunicorn app:app
```

### Step 2: Deploy
1. Sign up at https://heroku.com
2. Install Heroku CLI
3. Run:
   ```bash
   heroku login
   heroku create canada-job-aggregator
   git push heroku main
   heroku open
   ```

**Note:** Heroku no longer has a free tier. Starts at $5/month.

---

## Option 4: Deploy to AWS (Advanced)

### Using AWS Elastic Beanstalk

1. **Install AWS CLI and EB CLI:**
   ```bash
   pip install awscli awsebcli
   aws configure
   ```

2. **Initialize EB:**
   ```bash
   eb init -p python-3.9 canada-job-aggregator
   ```

3. **Create environment:**
   ```bash
   eb create canada-job-aggregator-env
   ```

4. **Deploy:**
   ```bash
   eb deploy
   ```

5. **Open app:**
   ```bash
   eb open
   ```

**AWS Free Tier:** 12 months free (limited usage)

---

## Troubleshooting

### Issue: "Module not found"
**Solution:** Make sure `requirements.txt` is in your repository root and all dependencies are listed.

### Issue: "Application error" 
**Solution:** Check logs:
- Render: Dashboard → Logs tab
- Railway: Click service → Logs
- Heroku: `heroku logs --tail`

### Issue: Jobs not loading
**Solution:** Click "Refresh Jobs" button - database starts empty.

### Issue: Site is slow on first load
**Solution:** Normal for free hosting - services sleep when inactive. Paid plans solve this.

---

## Updating Your Deployed Site

After making changes locally:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Most platforms auto-deploy on push. If not:
- Render: Click "Manual Deploy"
- Railway: Automatic on push
- Heroku: `git push heroku main`

---

## Monitoring & Analytics

### Add Google Analytics (Optional)

Add this to `templates/index.html` before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

### Set Up Uptime Monitoring

Use [UptimeRobot](https://uptimerobot.com) (free):
1. Sign up
2. Add new monitor
3. URL: Your deployed site URL
4. Interval: Every 5 minutes
5. Get email alerts if site goes down

---

## Custom Domain (Optional)

### With Render:
1. Buy domain (Namecheap, Google Domains, etc.)
2. In Render: Settings → Custom Domains
3. Add your domain
4. Update DNS records as instructed

### Cost:
- Domain: $10-15/year
- Hosting: Free (or $7/month for always-on)

---

## Next Steps

1. ✅ Deploy your site
2. ✅ Test all features
3. ✅ Share the URL with others
4. 📧 Set up email notifications (future)
5. 🔄 Schedule automatic job scraping (future)
6. 📱 Build mobile app version (future)

---

## Support

If you run into issues:
1. Check the logs on your hosting platform
2. Review error messages carefully
3. Search the issue on Stack Overflow
4. Check hosting platform documentation

**Your job aggregator is ready to deploy! 🚀**
