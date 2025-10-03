# 📰 AI-Enhanced News Dashboard

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![AI Powered](https://img.shields.io/badge/AI-Hugging%20Face-yellow.svg)](https://huggingface.co/)

> A modern, responsive web dashboard that fetches diverse news from multiple categories, creates AI summaries, and displays them in a beautiful interface with real-time updates.

---

## ✨ Features

✅ **Modern Web Dashboard** - Responsive design with dark/light themes  
✅ **Diverse News Categories**: Technology • Business • Sports • Health • Science  
✅ **AI-Powered Summaries** using free Hugging Face models  
✅ **Real-time Updates** with auto-refresh functionality  
✅ **Search & Filter** - Find articles across all categories  
✅ **Trending Sidebar** - Top news by category  
✅ **Mobile Optimized** - Works perfectly on all devices  
✅ **Free to Deploy** - Ready for Railway, Render, or Fly.io

---

## 🎯 What You Get

A beautiful web dashboard with **multiple articles from each category**:

- 💻 **Technology** - Latest tech news, gadgets, and innovations
- 💼 **Business** - Business news, markets, and finance  
- ⚽ **Sports** - Sports news, scores, and updates
- 🏥 **Health** - Health news, medical breakthroughs, and wellness
- 🔬 **Science** - Scientific discoveries and research

**Plus:** Search functionality, trending sidebar, and responsive design!

---

## 🚀 Quick Start

### 🔧 Requirements

- Python 3.11+
- [NewsAPI key](https://newsapi.org/) (free tier: 1000 requests/day)

### 🛠 Local Setup

1. **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/news-dashboard.git
    cd news-dashboard
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create `.env` file:**
    ```env
    NEWS_API_KEY=your_newsapi_key_here
    ```

4. **Run the web app:**
    ```bash
    python app.py
    ```

5. **Open your browser:**
    ```
    http://localhost:5000
    ```

---

## 🧠 How It Works

1. **Fetches News**: Gets top headlines from 5 categories using NewsAPI
2. **AI Summarization**: Creates concise summaries using Hugging Face BART model (free)
3. **Web Interface**: Displays in a modern, responsive dashboard
4. **Real-time Updates**: Auto-refreshes every 30 minutes with manual refresh option
5. **Search & Filter**: Find specific articles across all categories

---

## 🖥️ Dashboard Preview

**Main Features:**
- **Category Tabs**: Switch between Technology, Business, Sports, Health, Science
- **Search Bar**: Find articles across all categories
- **Trending Sidebar**: Top news ranked by category
- **Dark/Light Theme**: Toggle between themes
- **Responsive Design**: Works on desktop, tablet, and mobile

**Sample Interface:**
```
📰 NewsHub                                    🌙 🔄 Refresh

🏠 Home  💻 Technology  💼 Business  ⚽ Sports  🏥 Health  🔬 Science    🔍 Search...

News Today
Friday, October 3, 2025

💻 Apple Unveils New MacBook Pro with M4 Chip
AI-powered performance improvements and enhanced battery life make this the most 
advanced MacBook yet...
TechCrunch • 2 hours ago • 💻 Technology

💼 Tesla Reports Record Q3 Earnings  
Electric vehicle giant exceeds Wall Street expectations with strong delivery 
numbers and improved margins...
Reuters • 3 hours ago • 💼 Business
```

---

## 🚀 Deployment

### Railway (Recommended - Free)
1. **Connect GitHub**: Link your repository to Railway
2. **Add Environment Variables**: Set `NEWS_API_KEY` in Railway dashboard
3. **Deploy**: Automatic deployment from main branch
4. **Access**: Get your live URL (e.g., `your-app.railway.app`)

### Render (Alternative - Free)
1. **Connect Repository**: Link GitHub repo to Render
2. **Configure**: Set environment variables
3. **Deploy**: Auto-deploy on git push
4. **Note**: Free tier sleeps after 15min inactivity

### Local Development
```bash
# Run with debug mode
python app.py

# Access at http://localhost:5000
```

---

## 🔧 Customization

**Add/modify categories** in `app.py`:

```python
# In get_diverse_news() function
categories = {
    "Technology": "technology",
    "Business": "business", 
    "Sports": "sports",
    "Health": "health",
    "Science": "science",
    # Add more NewsAPI categories
}
```

**Customize the interface** in `templates/index.html`:
- Change colors in `static/style.css`
- Modify category emojis and names
- Adjust auto-refresh interval (default: 30 minutes)

**API Configuration**:
```python
# Change news source country
params['country'] = 'gb'  # UK news

# Adjust articles per category
params['pageSize'] = 20  # More articles
```

---

## 📁 Project Structure

```
news-dashboard/
├── app.py                    # Flask web server (main application)
├── news.py                   # Original CLI version (optional)
├── templates/
│   └── index.html           # Web interface template
├── static/
│   └── style.css            # Modern CSS styling with themes
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your credentials (create this)
├── Procfile                # Deployment configuration
├── railway.json            # Railway hosting config
├── runtime.txt             # Python version specification
├── PROJECT_SUMMARY.md      # Detailed project documentation
└── README.md               # This file
```

---

## 🛠 Tech Stack

### Backend
- **Flask** - Web framework
- **NewsAPI** - News data source (free tier: 1000 requests/day)
- **Hugging Face API** - AI summarization (free)
- **python-dotenv** - Environment variable management
- **requests** - HTTP client

### Frontend
- **HTML5 + CSS3** - Modern responsive design
- **Vanilla JavaScript** - Dynamic functionality
- **Google Fonts (Inter)** - Typography
- **CSS Grid & Flexbox** - Layout system

---

## 🤖 AI Features

- **Hugging Face BART** - Free text summarization (facebook/bart-large-cnn)
- **Smart Fallbacks** - Shows article excerpt if AI fails
- **No API Keys** - Uses public Hugging Face inference endpoints
- **Real-time Processing** - Summaries generated on-demand

---

## 🔒 Security & Performance

### Security
- Environment variables in `.env` file (not committed to git)
- NewsAPI key protection
- No user data storage or tracking
- HTTPS ready for production deployment

### Performance
- **Fast Loading**: 3-5 seconds initial load
- **Auto-refresh**: Every 30 minutes
- **Responsive**: Mobile-first design
- **Lightweight**: ~50MB memory usage

---

## 🌟 Key Features Breakdown

### 🎨 Modern Interface
- **Dark/Light Themes** - Toggle with moon/sun icon
- **Responsive Design** - Perfect on desktop, tablet, mobile
- **Smooth Animations** - Hover effects and transitions
- **Category Navigation** - Easy switching between news types

### 🔍 Smart Search
- **Real-time Search** - Find articles as you type
- **Cross-category** - Search across all news categories
- **Highlighted Results** - Clear search result indicators

### 📱 Mobile Experience
- **Touch-friendly** - Optimized for mobile interaction
- **Fast Loading** - Lightweight and efficient
- **Offline-ready** - Cached content for better performance

## 🚀 Getting Started (3 Steps)

1. **Get NewsAPI Key**: Sign up at [newsapi.org](https://newsapi.org) (free)
2. **Clone & Setup**: `git clone` → `pip install -r requirements.txt` → create `.env`
3. **Run**: `python app.py` → Open `http://localhost:5000`

## 📊 Live Demo

Deploy to Railway for free and get your own live news dashboard!

**Total Cost**: $0 (completely free to run and deploy)

---

## 📝 License

MIT License - feel free to modify and use for your projects!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Enjoy your daily dose of diverse, AI-summarized news! 📰✨**