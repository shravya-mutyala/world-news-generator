# 📰 News 

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![AI Powered](https://img.shields.io/badge/AI-Hugging%20Face-yellow.svg)](https://huggingface.co/)

> A simple Python script that fetches diverse news from 5 different categories, creates AI summaries, and sends a beautifully formatted email to your inbox.

---

## ✨ Features

✅ **Diverse News Categories**: Business • Technology • AI • Stocks • Movies  
✅ **AI-Powered Summaries** using free Hugging Face models  
✅ **Clean HTML Email** with category emojis and formatting  
✅ **Simple & Fast** - just 80 lines of code  
✅ **Free to Run** - no paid APIs required  
✅ **Daily Automation Ready** with cron/Task Scheduler

---

## 🎯 What You Get

Each email contains **one article from each category**:

- 💼 **Business** - Finance, economy news
- 💻 **Technology** - Tech, software updates  
- 🤖 **AI** - Artificial intelligence, machine learning
- � **Stocks** - Market trends, trading news
- 🎬 **Movies** - Cinema, entertainment news

---

## 🚀 Quick Start

### 🔧 Requirements

- Python 3.8+
- Gmail account with [App Password](https://support.google.com/accounts/answer/185833)
- [World News API key](https://worldnewsapi.com/) (free tier available)

### 🛠 Setup

1. **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/world-news-generator.git
    cd world-news-generator
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create `.env` file:**
    ```env
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password_here
    API_KEY=your_worldnewsapi_key
    ```

4. **Run the script:**
    ```bash
    python news.py
    ```

---

## 🧠 How It Works

1. **Fetches News**: Gets one article from each of the 5 categories using World News API
2. **AI Summarization**: Creates concise summaries using Hugging Face BART model (free)
3. **Email Generation**: Formats into clean HTML with category emojis and styling
4. **Email Delivery**: Sends via Gmail SMTP to your inbox

---

## 📧 Sample Email Output

**Subject:** 📰 Today's Diverse News: Business • Tech • AI • Stocks • Movies

```html
📰 Today's Diverse News Briefing
Business • Technology • AI • Stocks • Movies

💼 Business: Tesla Reports Record Q4 Earnings
Summary: Tesla announced record quarterly earnings with revenue exceeding expectations...
Author: Financial Times
📖 Read Full Article

💻 Technology: Apple Launches New MacBook Pro
Summary: Apple unveiled its latest MacBook Pro featuring the new M3 chip...
Author: TechCrunch  
📖 Read Full Article

🤖 AI: OpenAI Releases GPT-5 Preview
Summary: OpenAI demonstrated significant improvements in reasoning capabilities...
Author: AI News
📖 Read Full Article

📈 Stocks: S&P 500 Reaches All-Time High
Summary: Major indices closed at record levels driven by tech sector gains...
Author: Bloomberg
📖 Read Full Article

🎬 Movies: Avatar 3 Release Date Announced
Summary: James Cameron confirms Avatar 3 will premiere in December 2025...
Author: Entertainment Weekly
📖 Read Full Article
```

---

## ⚙️ Automation

**Set up daily emails:**

**Linux/Mac (cron):**
```bash
# Run daily at 8 AM
0 8 * * * /usr/bin/python3 /path/to/news.py
```

**Windows (Task Scheduler):**
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger to "Daily" at your preferred time
4. Set action to start `python.exe` with argument `news.py`

---

## 🔧 Customization

**Change categories** by editing the `categories` dictionary in `get_diverse_news()`:

```python
categories = {
    "Sports": "sports football basketball",
    "Health": "health medical wellness", 
    "Science": "science research discovery",
    # Add your preferred categories
}
```

**Change email recipient** in the `send_email()` function:
```python
msg["To"] = "your_email@example.com"
```

---

## 📁 Project Structure

```
world-news-generator/
├── news.py              # Main script (80 lines)
├── requirements.txt     # Dependencies (3 packages)
├── .env.example        # Environment variables template
├── .env                # Your credentials (create this)
└── README.md           # This file
```

---

## 🛠 Dependencies

- **python-dotenv** - Environment variable management
- **worldnewsapi** - News data fetching
- **requests** - HTTP requests for AI summaries

---

## 🤖 AI Technology

- **Hugging Face BART** - Free text summarization
- **No API keys required** - Uses public inference endpoints
- **Fallback handling** - Works even if AI fails

---

## 🔒 Security

- Credentials stored in `.env` file (not committed to git)
- Gmail App Password recommended over regular password
- No sensitive data logged or stored

---

## 📝 License

MIT License - feel free to modify and use for your projects!

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Enjoy your daily dose of diverse, AI-summarized news! 📰✨**
