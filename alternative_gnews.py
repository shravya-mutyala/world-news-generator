# Alternative implementation using GNews API (no API key needed for basic use)

def get_news_by_category_gnews(category, max_results=1):
    """Get news using GNews API (no API key required for basic use)"""
    try:
        url = "https://gnews.io/api/v4/search"
        params = {
            'q': category,
            'lang': 'en',
            'country': 'us',
            'max': max_results,
            'apikey': 'demo'  # Use 'demo' for testing, get real key for production
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return data.get('articles', [])
        
    except Exception as e:
        print(f"Error fetching {category} news: {e}")
        return []