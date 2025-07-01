🌍 #World News Email Notifier
This Python script fetches the top news headlines of the day using the World News API, flattens and formats them, and sends an HTML email summary to your inbox. Great for staying up to date with global events — hands-free!

📦 Features
🕓 Automatically pulls today’s top news

📊 Uses pandas to flatten complex API responses

📨 Sends news in a clean, responsive HTML email format

🔐 Securely loads credentials from a .env file

✅ Easily customizable for daily automation

🚀 Quick Start
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/yourusername/world-news-generator.git
cd world-news-generator
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create your .env file
env
Copy
Edit
# .env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
API_KEY=your_worldnewsapi_key
🔐 Use a Gmail App Password — not your regular password

4. Run the script
bash
Copy
Edit
python news.py
🧠 How It Works
Authenticates with the World News API

Fetches top news for the current date

Normalizes and flattens nested JSON using pandas

Renders a clean HTML email (with title, summary, image, author, and URL)

Sends the email using Gmail SMTP

🛠 Tech Stack
Python 3

pandas

smtplib, email.mime

python-dotenv

worldnewsapi SDK

📅 Optional: Schedule Daily Emails
On Windows: use Task Scheduler

On macOS/Linux: use cron
