import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import worldnewsapi
from worldnewsapi.rest import ApiException
from dotenv import load_dotenv

# LOAD ENV FILE
load_dotenv()

# Access environment variables
from_email = os.getenv("EMAIL_ADDRESS")
from_password = os.getenv("EMAIL_PASSWORD")

if not from_email or not from_password:
    raise ValueError("Missing email credentials. Please check your .env file.")

# ========== 1. API Setup ==========
API_KEY = os.getenv("API_KEY")
configuration = worldnewsapi.Configuration(
    host="https://api.worldnewsapi.com"
)
configuration.api_key['apiKey'] = API_KEY
configuration.api_key['headerApiKey'] = API_KEY

# ========== 2. Fetch Today's Top News ==========


def get_today_top_news():
    today = str(date.today())
    with worldnewsapi.ApiClient(configuration) as api_client:
        api_instance = worldnewsapi.NewsApi(api_client)
        try:
            response = api_instance.top_news(
                source_country='us',
                language='en',
                var_date=today,
                headlines_only=False
            )
            response_dict = response.to_dict()

            # Correctly access the nested list
            top_news_items = response_dict.get("top_news", [])
            if top_news_items and isinstance(top_news_items[0], dict):
                return top_news_items[0].get("news", [])

            print("Unexpected response format in 'top_news'")
            return []

        except ApiException as e:
            print(f"Error fetching top news: {e}")
            return []


# ========== 3. Flatten News ==========


def flatten_news(news_list):
    if not news_list:
        print("No news items to flatten.")
        return pd.DataFrame()

    df = pd.json_normalize(news_list)

    # Add static metadata
    df['language'] = 'en'
    df['source_country'] = 'us'

    # Safely extract only available columns
    desired_cols = [
        'language', 'image', 'author', 'id', 'text',
        'title', 'publish_date', 'url', 'authors'
    ]
    existing_cols = [col for col in desired_cols if col in df.columns]
    return df[existing_cols]

# ========== 4. Generate Email HTML ==========


def generate_email_html(news_df):
    html = "<h2>Today's Top World News</h2><br>"
    for i, row in news_df.iterrows():
        html += f"<h3>News {i+1}: {row['title']}</h3>"
        html += f"<p><b>Summary:</b> {row['text']}</p>"
        if row.get('image'):
            html += f"<img src='{row['image']}' alt='news image' width='400'/><br>"
        html += f"<p><b>Author:</b> {row.get('author', 'Unknown')}</p>"
        html += f"<p><a href='{row['url']}'>Read Full Article</a></p>"
        html += "<hr>"
    return html

# ========== 5. Send Email ==========


def send_email(subject, html_content, to_emails):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)

    part = MIMEText(html_content, "html")
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, from_password)
        server.sendmail(from_email, to_emails, msg.as_string())
        print("Email sent successfully!")


# ========== 6. Main Flow ==========
if __name__ == "__main__":
    news_list = get_today_top_news()
    if news_list:
        news_df = flatten_news(news_list)
        email_html = generate_email_html(
            news_df.head(5))  # limit to 5 for brevity
        send_email(
            subject="📰 Today's Top World News",
            html_content=email_html,
            to_emails=["theboldtype236@gmail.com"]
        )
    else:
        print("No news data returned.")
