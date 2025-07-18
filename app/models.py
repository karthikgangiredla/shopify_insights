from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    title: str
    price: Optional[str]
    url: Optional[str]

class BrandResponse(BaseModel):
    brand_name: Optional[str]
    about: Optional[str]
    contact_emails: List[str]
    phone_numbers: List[str]
    social_handles: List[str]
    products: List[Product]
    hero_products: List[Product]
    privacy_policy: Optional[str]
    refund_policy: Optional[str]
    faqs: List[dict]
    important_links: List[str]
    competitors: Optional[List[str]]
