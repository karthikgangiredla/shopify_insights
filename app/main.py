from fastapi import FastAPI, HTTPException
from app.scraper import scrape_shopify_site, fetch_competitors
from app.models import BrandResponse
from app.database import save_brand_data

app = FastAPI()
import os
from dotenv import load_dotenv
load_dotenv()
@app.get("/")
def read_root():
    return {"message": "Shopify Insights API is running"}

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

@app.get("/fetch_brand_insights", response_model=BrandResponse)
def fetch_brand_insights(website_url: str):
    try:
        data = scrape_shopify_site(website_url)
        if data:
            # Fetch competitors
            competitors = fetch_competitors(data.brand_name, SERPAPI_API_KEY)
            data.competitors = competitors
            # Persist to DB
            save_brand_data(data)
            return data
        else:
            raise HTTPException(status_code=401, detail="Website not found or not a Shopify store")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
