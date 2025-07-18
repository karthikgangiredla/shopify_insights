import requests
from bs4 import BeautifulSoup
from app.models import BrandResponse, Product
from app.utils import extract_emails, extract_phone_numbers, find_links
import json

def scrape_shopify_site(url: str) -> BrandResponse:
    if not url.startswith('https://') and not url.startswith('http://'):
        url = 'https://' + url

    try:
        product_res = requests.get(url + '/products.json', timeout=10)
        products_data = product_res.json().get('products', [])
    except:
        products_data = []

    products = [Product(title=p['title'], price=str(p['variants'][0]['price']), url=f"{url}/products/{p['handle']}") for p in products_data]

    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, 'lxml')
    text = soup.get_text()

    brand_name = soup.title.string if soup.title else ""
    emails = extract_emails(text)
    phones = extract_phone_numbers(text)

    social_handles = [a['href'] for a in soup.find_all('a', href=True) if any(x in a['href'] for x in ['instagram', 'facebook', 'twitter', 'tiktok'])]

    privacy_links = find_links(soup, ['privacy'])
    refund_links = find_links(soup, ['refund', 'return'])
    faq_links = find_links(soup, ['faq', 'help'])
    contact_links = find_links(soup, ['contact'])
    important_links = privacy_links + refund_links + faq_links + contact_links

    hero_products = []
    for a in soup.find_all('a', href=True):
        if '/products/' in a['href']:
            title = a.text.strip() or 'Hero Product'
            hero_products.append(Product(title=title, price=None, url=url.rstrip('/') + a['href']))

    about_text = ''
    about_section = soup.find('section', {'id': 'about'})
    if about_section:
        about_text = about_section.get_text(strip=True)
    else:
        about_text = "About section not found"

    faqs = [{'question': a.text.strip(), 'answer': 'Available on ' + a['href']} for a in soup.find_all('a', href=True) if 'faq' in a['href'].lower()]

    return BrandResponse(
        brand_name=brand_name,
        about=about_text,
        contact_emails=emails,
        phone_numbers=phones,
        social_handles=social_handles,
        products=products,
        hero_products=hero_products,
        privacy_policy=privacy_links[0] if privacy_links else "",
        refund_policy=refund_links[0] if refund_links else "",
        faqs=faqs,
        important_links=important_links,
        competitors=[]
    )

from serpapi import GoogleSearch

def fetch_competitors(brand_name: str, serpapi_api_key: str):
    search = GoogleSearch({
        "q": f"{brand_name} competitors",
        "api_key": serpapi_api_key
    })
    results = search.get_dict()
    organic_results = results.get('organic_results', [])
    competitors = [result['link'] for result in organic_results if 'link' in result]
    return competitors
