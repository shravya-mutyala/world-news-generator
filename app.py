from flask import Flask, render_template, jsonify, request
import os
from dotenv import load_dotenv
import requests
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Setup NewsAPI
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_BASE_URL = "https://newsapi.org/v2"

def get_news_by_category(category, max_results=1):
    """Get today's top news articles for a specific category using NewsAPI"""
    try:
        from datetime import date
        today = date.today().isoformat()
        
        url = f"{NEWS_API_BASE_URL}/everything"
        params = {
            'q': category,
            'language': 'en',
            'pageSize': max_results,
            'sortBy': 'publishedAt',
            'from': today,  # Only today's news
            'to': today,    # Only today's news
            'apiKey': NEWS_API_KEY
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == 'ok' and data.get('articles'):
            return data['articles']
        else:
            print(f"No articles found for {category} today, trying recent news...")
            # Fallback: get recent news if no today's news
            return get_recent_news_fallback(category, max_results)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {category} news: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error for {category}: {e}")
        return []

def get_recent_news_fallback(category, max_results=1):
    """Fallback to get recent news if no today's news available"""
    try:
        url = f"{NEWS_API_BASE_URL}/everything"
        params = {
            'q': category,
            'language': 'en',
            'pageSize': max_results,
            'sortBy': 'publishedAt',
            'apiKey': NEWS_API_KEY
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return data.get('articles', [])
        
    except Exception as e:
        print(f"Fallback error for {category}: {e}")
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

def get_top_headlines_by_category(category_name, max_results=10):
    """Get today's top headlines for a specific category"""
    try:
        url = f"{NEWS_API_BASE_URL}/top-headlines"
        params = {
            'category': category_name,
            'language': 'en',
            'country': 'us',
            'pageSize': max_results,
            'apiKey': NEWS_API_KEY
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return data.get('articles', [])
        
    except Exception as e:
        print(f"Error fetching top headlines for {category_name}: {e}")
        return []

def get_diverse_news():
    """Get today's top news from different categories"""
    # Using NewsAPI's predefined categories for top headlines
    categories = {
        "Technology": "technology",
        "Business": "business", 
        "Sports": "sports",
        "Health": "health",
        "Science": "science"
    }
    
    category_emojis = {
        "Technology": "💻",
        "Business": "💼",
        "Sports": "⚽",
        "Health": "🏥",
        "Science": "🔬"
    }
    
    news_by_category = {}
    
    for category_name, api_category in categories.items():
        print(f"🔍 Fetching today's {category_name} headlines...")
        news = get_top_headlines_by_category(api_category, 10)  # Get 10 articles per category
        
        category_articles = []
        for article in news:
            # Get AI summary
            content = article.get('content') or article.get('description', '')
            title = article.get('title', 'No title')
            summary = summarize_text(content, title) if content else article.get('description', 'No summary available')
            
            news_item = {
                'category': category_name,
                'emoji': category_emojis.get(category_name, "📰"),
                'title': title,
                'summary': summary,
                'author': article.get('source', {}).get('name', 'Unknown'),
                'url': article.get('url', '#'),
                'image': article.get('urlToImage', ''),
                'publish_date': article.get('publishedAt', '')
            }
            category_articles.append(news_item)
        
        # Add placeholder if no news found
        if not category_articles:
            category_articles.append({
                'category': category_name,
                'emoji': category_emojis.get(category_name, "📰"),
                'title': f'No {category_name} news available',
                'summary': 'Please try refreshing later.',
                'author': 'N/A',
                'url': '#',
                'image': '',
                'publish_date': ''
            })
        
        news_by_category[api_category] = category_articles
    
    return news_by_category

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/news')
def api_news():
    """API endpoint to get latest news organized by category"""
    try:
        news_by_category = get_diverse_news()
        return jsonify({
            'success': True,
            'news_by_category': news_by_category,
            'last_updated': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/top-news')
def api_top_news():
    """API endpoint to get top trending news by category"""
    try:
        category = request.args.get('category', 'general')
        print(f"🔍 Fetching trending news for category: {category}")
        
        # Check if API key exists
        if not NEWS_API_KEY:
            print("❌ NEWS_API_KEY not found!")
            return jsonify({
                'success': False,
                'error': 'API key not configured'
            }), 500
        
        # Map our categories to NewsAPI categories
        category_mapping = {
            'all': 'general',
            'technology': 'technology',
            'business': 'business',
            'sports': 'sports',
            'health': 'health',
            'science': 'science'
        }
        
        api_category = category_mapping.get(category, 'general')
        print(f"📊 Using API category: {api_category}")
        
        # Get category-specific top headlines
        url = f"{NEWS_API_BASE_URL}/top-headlines"
        params = {
            'country': 'us',
            'pageSize': 15,  # Get more to have variety
            'apiKey': NEWS_API_KEY
        }
        
        # Add category filter if not 'all'
        if category != 'all' and api_category != 'general':
            params['category'] = api_category
        
        print(f"🌐 Making request to: {url}")
        print(f"📋 Parameters: {params}")
        
        response = requests.get(url, params=params)
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ API Error: {response.text}")
            return jsonify({
                'success': False,
                'error': f'API returned status {response.status_code}'
            }), 500
        
        data = response.json()
        print(f"📄 Response data keys: {list(data.keys())}")
        
        if data.get('status') != 'ok':
            error_msg = data.get('message', 'Unknown API error')
            print(f"❌ API Error: {error_msg}")
            return jsonify({
                'success': False,
                'error': error_msg
            }), 500
        
        articles = []
        if data.get('articles'):
            print(f"📰 Found {len(data['articles'])} articles")
            for article in data['articles']:
                articles.append({
                    'title': article.get('title', 'No title'),
                    'author': article.get('source', {}).get('name', 'Unknown'),
                    'url': article.get('url', '#'),
                    'publish_date': article.get('publishedAt', ''),
                    'category': category
                })
        else:
            print("⚠️ No articles found in response")
        
        return jsonify({
            'success': True,
            'articles': articles,
            'category': category
        })
    except requests.exceptions.RequestException as e:
        print(f"🌐 Network error: {e}")
        return jsonify({
            'success': False,
            'error': f'Network error: {str(e)}'
        }), 500
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))