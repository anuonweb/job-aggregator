from flask import Flask, render_template, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time
import re

app = Flask(__name__)
CORS(app)

# Initialize database
def init_db():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jobs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  company TEXT,
                  location TEXT,
                  job_site TEXT,
                  job_url TEXT UNIQUE,
                  posted_date TEXT,
                  scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# Job scraping functions
def scrape_indeed_ca():
    """Scrape Indeed Canada for warehouse, security, and part-time jobs"""
    jobs = []
    keywords = ['warehouse associate', 'security', 'part time']
    
    for keyword in keywords:
        try:
            url = f"https://ca.indeed.com/jobs?q={keyword.replace(' ', '+')}&l=Canada"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Indeed's job cards
                job_cards = soup.find_all('div', class_='job_seen_beacon')
                
                for card in job_cards[:10]:  # Limit to 10 jobs per keyword
                    try:
                        title_elem = card.find('h2', class_='jobTitle')
                        title = title_elem.get_text(strip=True) if title_elem else 'N/A'
                        
                        company_elem = card.find('span', {'data-testid': 'company-name'})
                        company = company_elem.get_text(strip=True) if company_elem else 'N/A'
                        
                        location_elem = card.find('div', {'data-testid': 'text-location'})
                        location = location_elem.get_text(strip=True) if location_elem else 'Canada'
                        
                        link_elem = title_elem.find('a') if title_elem else None
                        job_url = f"https://ca.indeed.com{link_elem['href']}" if link_elem and 'href' in link_elem.attrs else ''
                        
                        date_elem = card.find('span', class_='date')
                        posted_date = date_elem.get_text(strip=True) if date_elem else 'Recently'
                        
                        if title != 'N/A' and job_url:
                            jobs.append({
                                'title': title,
                                'company': company,
                                'location': location,
                                'job_site': 'Indeed',
                                'job_url': job_url,
                                'posted_date': posted_date
                            })
                    except Exception as e:
                        continue
                
                time.sleep(2)  # Rate limiting
                
        except Exception as e:
            print(f"Error scraping Indeed for '{keyword}': {e}")
    
    return jobs

def scrape_jobbank_ca():
    """Scrape Job Bank Canada"""
    jobs = []
    keywords = ['warehouse', 'security', 'part-time']
    
    for keyword in keywords:
        try:
            url = f"https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring={keyword.replace(' ', '+')}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                job_cards = soup.find_all('article', class_='resultJobItem')
                
                for card in job_cards[:10]:
                    try:
                        title_elem = card.find('a', class_='resultJobItem-title')
                        title = title_elem.get_text(strip=True) if title_elem else 'N/A'
                        
                        company_elem = card.find('span', class_='resultJobItem-employer')
                        company = company_elem.get_text(strip=True) if company_elem else 'N/A'
                        
                        location_elem = card.find('span', class_='resultJobItem-location')
                        location = location_elem.get_text(strip=True) if location_elem else 'Canada'
                        
                        job_url = f"https://www.jobbank.gc.ca{title_elem['href']}" if title_elem and 'href' in title_elem.attrs else ''
                        
                        posted_date = 'Recently'
                        
                        if title != 'N/A' and job_url:
                            jobs.append({
                                'title': title,
                                'company': company,
                                'location': location,
                                'job_site': 'Job Bank Canada',
                                'job_url': job_url,
                                'posted_date': posted_date
                            })
                    except Exception as e:
                        continue
                
                time.sleep(2)
                
        except Exception as e:
            print(f"Error scraping Job Bank for '{keyword}': {e}")
    
    return jobs

def scrape_eluta_ca():
    """Scrape Eluta.ca"""
    jobs = []
    keywords = ['warehouse', 'security']
    
    for keyword in keywords:
        try:
            url = f"https://www.eluta.ca/search?q={keyword.replace(' ', '+')}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                job_listings = soup.find_all('div', class_='job-item')
                
                for listing in job_listings[:10]:
                    try:
                        title_elem = listing.find('a', class_='job-title')
                        title = title_elem.get_text(strip=True) if title_elem else 'N/A'
                        
                        company_elem = listing.find('span', class_='company')
                        company = company_elem.get_text(strip=True) if company_elem else 'N/A'
                        
                        location = 'Canada'
                        
                        job_url = title_elem['href'] if title_elem and 'href' in title_elem.attrs else ''
                        if job_url and not job_url.startswith('http'):
                            job_url = f"https://www.eluta.ca{job_url}"
                        
                        posted_date = 'Recently'
                        
                        if title != 'N/A' and job_url:
                            jobs.append({
                                'title': title,
                                'company': company,
                                'location': location,
                                'job_site': 'Eluta',
                                'job_url': job_url,
                                'posted_date': posted_date
                            })
                    except Exception as e:
                        continue
                
                time.sleep(2)
                
        except Exception as e:
            print(f"Error scraping Eluta for '{keyword}': {e}")
    
    return jobs

def add_sample_jobs():
    """Add sample jobs for LinkedIn, Google, Amazon, Walmart, Loblaw (manual entries for now)"""
    sample_jobs = [
        {
            'title': 'Warehouse Associate - Part Time',
            'company': 'Amazon',
            'location': 'Toronto, ON',
            'job_site': 'Amazon Jobs',
            'job_url': 'https://www.amazon.jobs/en/search?base_query=warehouse&loc_query=Canada',
            'posted_date': '1 day ago'
        },
        {
            'title': 'Security Guard - Part Time',
            'company': 'Walmart Canada',
            'location': 'Mississauga, ON',
            'job_site': 'Walmart Careers',
            'job_url': 'https://careers.walmart.ca/search-jobs/security/Canada',
            'posted_date': '2 days ago'
        },
        {
            'title': 'Warehouse Team Member',
            'company': 'Loblaw Companies',
            'location': 'Brampton, ON',
            'job_site': 'Loblaw Careers',
            'job_url': 'https://jobs.loblaw.ca/search-jobs/warehouse/Canada',
            'posted_date': '3 days ago'
        },
        {
            'title': 'Part-Time Warehouse Associate',
            'company': 'Various Employers',
            'location': 'Ontario, Canada',
            'job_site': 'LinkedIn',
            'job_url': 'https://www.linkedin.com/jobs/search/?keywords=warehouse%20associate&location=Canada',
            'posted_date': 'Today'
        },
        {
            'title': 'Security Officer - Part Time',
            'company': 'Various Employers',
            'job_site': 'Google Jobs',
            'location': 'Canada',
            'job_url': 'https://www.google.com/search?q=security+jobs+canada+part+time',
            'posted_date': 'Today'
        }
    ]
    
    return sample_jobs

def scrape_all_jobs():
    """Scrape all job sites and store in database"""
    all_jobs = []
    
    print("Scraping Indeed...")
    all_jobs.extend(scrape_indeed_ca())
    
    print("Scraping Job Bank Canada...")
    all_jobs.extend(scrape_jobbank_ca())
    
    print("Scraping Eluta...")
    all_jobs.extend(scrape_eluta_ca())
    
    print("Adding sample jobs...")
    all_jobs.extend(add_sample_jobs())
    
    # Store in database
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    
    stored_count = 0
    for job in all_jobs:
        try:
            c.execute('''INSERT OR IGNORE INTO jobs 
                        (title, company, location, job_site, job_url, posted_date)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                     (job['title'], job['company'], job['location'], 
                      job['job_site'], job['job_url'], job['posted_date']))
            if c.rowcount > 0:
                stored_count += 1
        except Exception as e:
            print(f"Error storing job: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"Scraped {len(all_jobs)} jobs, stored {stored_count} new jobs")
    return len(all_jobs)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/jobs')
def get_jobs():
    conn = sqlite3.connect('jobs.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Get all jobs ordered by scraped_at (most recent first)
    c.execute('''SELECT * FROM jobs 
                 ORDER BY scraped_at DESC 
                 LIMIT 100''')
    
    jobs = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify(jobs)

@app.route('/api/refresh')
def refresh_jobs():
    count = scrape_all_jobs()
    return jsonify({'status': 'success', 'jobs_scraped': count})

@app.route('/api/stats')
def get_stats():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    
    c.execute('SELECT COUNT(*) FROM jobs')
    total_jobs = c.fetchone()[0]
    
    c.execute('SELECT job_site, COUNT(*) as count FROM jobs GROUP BY job_site')
    by_site = {row[0]: row[1] for row in c.fetchall()}
    
    conn.close()
    
    return jsonify({
        'total_jobs': total_jobs,
        'by_site': by_site
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
