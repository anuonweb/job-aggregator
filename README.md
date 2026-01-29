# 🇨🇦 Canada Job Aggregator

A simple web application that aggregates job postings from multiple Canadian job sites, focusing on:
- **Warehouse Associate** positions
- **Security** jobs  
- **Part-Time** opportunities

## 🎯 Features

- ✅ Aggregates jobs from Indeed, Job Bank Canada, Eluta, Amazon, Walmart, Loblaw, LinkedIn, and Google Jobs
- ✅ Real-time job scraping with refresh button
- ✅ Search and filter functionality
- ✅ Clean, modern UI with responsive design
- ✅ Jobs sorted by most recent first
- ✅ Direct links to original job postings

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**
   ```bash
   cd job-aggregator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

5. **Click "Refresh Jobs"** to start scraping job sites

## 🌐 Deploy to Render (Free Hosting)

### Option 1: Deploy from GitHub

1. **Push code to your GitHub repository** (@anuonweb)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/anuonweb/job-aggregator.git
   git push -u origin main
   ```

2. **Go to [Render.com](https://render.com)** and sign up (free, no credit card)

3. **Create New Web Service**
   - Connect your GitHub account
   - Select the `job-aggregator` repository
   - Configure settings:
     - **Name:** `canada-job-aggregator`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
     - **Plan:** Free

4. **Deploy** - Render will build and deploy automatically

5. **Access your site** at `https://canada-job-aggregator.onrender.com`

### Option 2: Deploy from Local Files

1. Go to [Render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Choose "Deploy from Git" or upload files manually
4. Follow steps above

## 📁 Project Structure

```
job-aggregator/
├── app.py                  # Flask backend with scraping logic
├── templates/
│   └── index.html         # Frontend UI
├── requirements.txt       # Python dependencies
├── jobs.db               # SQLite database (auto-created)
└── README.md             # This file
```

## 🛠️ How It Works

1. **Backend (app.py)**
   - Flask web server
   - Scrapes job sites using BeautifulSoup and requests
   - Stores jobs in SQLite database
   - Provides REST API endpoints

2. **Frontend (index.html)**
   - Single-page application
   - Fetches jobs via API
   - Real-time search and filtering
   - Responsive design

3. **Database (jobs.db)**
   - SQLite database
   - Stores job listings
   - Prevents duplicates

## 🔧 Configuration

### Add More Job Sites

Edit `app.py` and add new scraping functions:

```python
def scrape_newsite():
    jobs = []
    # Your scraping logic here
    return jobs
```

Then call it in `scrape_all_jobs()`:
```python
all_jobs.extend(scrape_newsite())
```

### Change Keywords

Modify the `keywords` list in each scraping function:
```python
keywords = ['warehouse', 'security', 'part-time', 'your-keyword']
```

### Add Email Notifications (Future Feature)

To add scheduled email notifications:

1. Install additional packages:
   ```bash
   pip install apscheduler smtplib
   ```

2. Add email configuration to `app.py`

3. Schedule periodic scraping with APScheduler

## 📊 API Endpoints

- `GET /` - Main web interface
- `GET /api/jobs` - Get all jobs (JSON)
- `GET /api/refresh` - Trigger job scraping
- `GET /api/stats` - Get job statistics

## ⚠️ Important Notes

### Web Scraping Ethics
- This application respects robots.txt
- Includes rate limiting (2 second delays)
- For educational/personal use only
- Some sites may block scraping - use official APIs when available

### Free Hosting Limitations (Render)
- Services sleep after 15 minutes of inactivity
- First request after sleep takes ~30 seconds
- 750 free hours per month
- Upgrade to $7/month for always-on service

## 🔮 Future Enhancements

- [ ] Email notifications for new jobs
- [ ] Scheduled automatic scraping (cron jobs)
- [ ] User accounts and saved searches
- [ ] Job application tracking
- [ ] Mobile app (React Native)
- [ ] Advanced filters (salary, experience level)
- [ ] LinkedIn/Indeed API integration

## 📝 License

MIT License - Free to use and modify

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

## 📧 Contact

GitHub: [@anuonweb](https://github.com/anuonweb)

---

**Built with ❤️ for Canadian job seekers**
