# 🌍 World News Email Notifier

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Made with Pandas](https://img.shields.io/badge/pandas-used-brightgreen.svg)](https://pandas.pydata.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

> A Python script to fetch today’s top world news, format it beautifully, and send it straight to your inbox.

---

## ✨ Features

✅ Fetches real-time **top news** using [World News API](https://worldnewsapi.com/)  
✅ Parses and flattens nested JSON using **Pandas**  
✅ Sends a clean **HTML email** with summaries, authors, images, and links  
✅ Secures credentials via `.env`  
✅ Ideal for **daily automation** with cron/Task Scheduler

---

## 🚀 Quick Start

### 🔧 Requirements

- Python 3.8+
- A Gmail account with [App Password](https://support.google.com/accounts/answer/185833)
- A [World News API key](https://worldnewsapi.com/)

### 🛠 Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/world-news-generator.git
    cd world-news-generator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file:
    ```env
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password_here
    API_KEY=your_worldnewsapi_key
    ```

4. Run the script:
    ```bash
    python news.py
    ```

---

## 🧠 How It Works

- Connects to World News API
- Retrieves today’s top headlines
- Flattens the structure using `pandas.json_normalize`
- Renders a rich HTML email with:
  - ✅ Title  
  - 🖼 Image (if available)  
  - ✍️ Author  
  - 🔗 Link  
  - 📆 Publish date  
- Sends it via **Gmail SMTP**

---

## 🖼 Sample Email Output

**Subject:** 📰 Today’s Top World News

```html
News 1: Canada Resumes Trade Talks
Summary: Canadian PM Carney confirmed negotiations have resumed...
Author: Taegan Goddard
[Read Full Article]

<img src="..." />
<hr>
News 2: Philadelphia Homes Collapse...
