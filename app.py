from flask import Flask, render_template, jsonify
import os
import worldnewsapi
from worldnewsapi.rest import ApiException
from dotenv import load_dotenv
import requests
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Setup World News API
API_KEY = os.getenv("API_KEY")
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

def get_diverse_news():
    """Get one article from each category"""
    categories = {
        "Business": "business finance economy",
        "Technology": "technology tech software",
        "AI": "artificial intelligence AI machine learning",
        "Stocks": "stock market trading investment",
        "Movies": "movies cinema film entertainment"
    }
    
    category_emojis = {
        "Business": "💼",
        "Technology": "💻", 
        "AI": "🤖",
        "Stocks": "📈",
        "Movies": "🎬"
    }
    
    all_news = []
    
    for category_name, search_terms in categories.items():
        print(f"🔍 Fetching {category_name} news...")
        news = get_news_by_category(search_terms, 1)
        if news:
            article = news[0]
            
            # Get AI summary
            text = article.text if hasattr(article, 'text') else ''
            title = article.title if hasattr(article, 'title') else 'No title'
            summary = summarize_text(text, title) if text else "No summary available"
            
            news_item = {
                'category': category_name,
                'emoji': category_emojis.get(category_name, "📰"),
                'title': title,
                'summary': summary,
                'author': article.author if hasattr(article, 'author') else 'Unknown',
                'url': article.url if hasattr(article, 'url') else '#',
                'image': article.image if hasattr(article, 'image') else '',
                'publish_date': article.publish_date if hasattr(article, 'publish_date') else ''
            }
            all_news.append(news_item)
        else:
            # Add placeholder if no news found
            all_news.append({
                'category': category_name,
                'emoji': category_emojis.get(category_name, "📰"),
                'title': f'No {category_name} news available',
                'summary': 'Please try refreshing later.',
                'author': 'N/A',
                'url': '#',
                'image': '',
                'publish_date': ''
            })
    
    return all_news

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/news')
def api_news():
    """API endpoint to get latest news"""
    try:
        news = get_diverse_news()
        return jsonify({
            'success': True,
            'news': news,
            'last_updated': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))