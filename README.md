
# Shopify Brand Insights Scraper
An AI-Powered web scraping and insights extraction tool for Shopify-based e-commerce stores. It
gathers brand information such as about sections, contact emails, social handles, privacy policies,
refund policies, FAQs, product details, and competitors.
## Features
- Scrapes brand details from Shopify store URLs
- Extracts about info, contact emails, phone numbers, social handles, products, policies, FAQs,
links, and competitors
- FastAPI-based API
- MySQL persistence with SQLAlchemy
## Tech Stack
- FastAPI
- SQLAlchemy
- MySQL
- BeautifulSoup, Requests
- Python
## Folder Structure
shopify_insights/
??? app/
? ??? __init__.py
? ??? main.py
? ??? models.py
? ??? scraper.py
? ??? utils.py
? ??? database.py
??? requirements.txt
## Setup Instructions
1. Clone the repo & install dependencies
```
git clone <repo-url>
cd shopify_insights
pip install -r requirements.txt
```
2. Setup MySQL
```
CREATE DATABASE shopify_insights;
```
User | Password
3. Run API
```
uvicorn app.main:app --reload
```
4. Access Endpoint
```
GET http://127.0.0.1:8000/fetch_brand_insights?website_url=<shopify_store_url>
Example: http://127.0.0.1:8000/fetch_brand_insights?website_url=gymshark.myshopify.com
```
## Future Enhancements
- Support for non-Shopify platforms
- Frontend dashboard via Streamlit
- Scheduled scraping
> Built with FastAPI, SQLAlchemy, MySQL, BeautifulSoup.
