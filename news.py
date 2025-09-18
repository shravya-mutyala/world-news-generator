import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import worldnewsapi
from worldnewsapi.rest import ApiException
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Email credentials
from_email = os.getenv("EMAIL_ADDRESS")
from_password = os.getenv("EMAIL_PASSWORD")
API_KEY = os.getenv("API_KEY")

# Setup World News API
configuration = worldnewsapi.Configuration(host="https://api.worldnewsapi.com")
configuration.api_key['apiKey'] = API_KEY
configuration.api_key['headerApiKey'] = API_KEY

def get_news_by_category(category, max_results=1):
    """Get news articles for a specific category"""
    with worldnewsapi.ApiClient(configuration) as api_client:
        api_instance = worldnewsapi.NewsApi(api_client)
        try:
            response = api_instance.search_news(
                text=category,
                language='en',
                number=max_results,
                sort='publish-time',
                sort_direction='DESC'
            )
            return response.news if response.news else []
        except ApiException as e:
            print(f"Error fetching {category} news: {e}")
            return []

def get_diverse_news():
    """Get one article from each category"""
    categories = {
        "Business": "business finance economy",
        "Technology": "technology tech software",
        "AI": "artificial intelligence AI machine learning",
        "Stocks": "stock market trading investment",
        "Movies": "movies cinema film entertainment"
    }
    
    all_news = []
    
    for category_name, search_terms in categories.items():
        print(f"🔍 Fetching {category_name} news...")
        news = get_news_by_category(search_terms, 1)
        if news:
            # Add category label to the article
            news[0].category = category_name
            all_news.extend(news)
        else:
            print(f"⚠️ No {category_name} news found")
    
    return all_news

def summarize_text(text, title):
    """Summarize news article using Hugging Face (free)"""
    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        payload = {
            "inputs": f"{title}. {text[:800]}",
            "parameters": {"max_length": 100, "min_length": 30}
        }
        response = requests.post(API_URL, json=payload)
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0:
            return result[0].get('summary_text', text[:150] + "...")
        return text[:150] + "..."
    except:
        return text[:150] + "..."

def create_email_html(news_list):
    """Create simple HTML email from diverse news categories"""
    html = "<h2>📰 Today's Diverse News Briefing</h2>"
    html += "<p><em>Business • Technology • AI • Stocks • Movies</em></p><br>"
    
    category_emojis = {
        "Business": "💼",
        "Technology": "💻", 
        "AI": "🤖",
        "Stocks": "📈",
        "Movies": "🎬"
    }
    
    for i, article in enumerate(news_list, 1):
        title = article.title if hasattr(article, 'title') else 'No title'
        text = article.text if hasattr(article, 'text') else ''
        author = article.author if hasattr(article, 'author') else 'Unknown'
        url = article.url if hasattr(article, 'url') else '#'
        image = article.image if hasattr(article, 'image') else ''
        category = getattr(article, 'category', 'General')
        
        # Get emoji for category
        emoji = category_emojis.get(category, "📰")
        
        # Get AI summary
        summary = summarize_text(text, title) if text else "No summary available"
        
        html += f"""
        <div style="margin-bottom: 20px; padding: 15px; border-left: 4px solid #007acc;">
            <h3>{emoji} {category}: {title}</h3>
            <p><strong>Summary:</strong> {summary}</p>
        """
        
        if image:
            html += f'<img src="{image}" style="max-width: 300px; height: auto; margin: 10px 0;"><br>'
        
        html += f"""
            <p><strong>Author:</strong> {author}</p>
            <p><a href="{url}" style="color: #007acc;">📖 Read Full Article</a></p>
        </div>
        <hr>
        """
    
    return html

def send_email(html_content):
    """Send email with news content"""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📰 Today's Diverse News: Business • Tech • AI • Stocks • Movies"
    msg["From"] = from_email
    msg["To"] = "theboldtype236@gmail.com"
    
    part = MIMEText(html_content, "html")
    msg.attach(part)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, from_password)
        server.sendmail(from_email, ["theboldtype236@gmail.com"], msg.as_string())
        print("✅ Email sent successfully!")

# Main execution
if __name__ == "__main__":
    print("🚀 Getting diverse news from different categories...")
    
    news_list = get_diverse_news()
    if news_list:
        print(f"📰 Found {len(news_list)} articles from different categories")
        print("🤖 Creating summaries...")
        
        email_html = create_email_html(news_list)
        send_email(email_html)
    else:
        print("❌ No news found")
