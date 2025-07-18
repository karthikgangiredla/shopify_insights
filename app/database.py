from app.models import BrandResponse
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/shopify_insights"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    about = Column(Text)
    contact_emails = Column(Text)
    phone_numbers = Column(Text)
    social_handles = Column(Text)
    products = Column(Text)
    hero_products = Column(Text)
    privacy_policy = Column(Text)
    refund_policy = Column(Text)
    faqs = Column(Text)
    important_links = Column(Text)
    competitors = Column(Text)

Base.metadata.create_all(bind=engine)

def save_brand_data(brand_data: BrandResponse):
    db = SessionLocal()
    brand = Brand(
        name=brand_data.brand_name,
        about=brand_data.about,
        contact_emails=json.dumps(brand_data.contact_emails),
        phone_numbers=json.dumps(brand_data.phone_numbers),
        social_handles=json.dumps(brand_data.social_handles),
        products=json.dumps([product.dict() for product in brand_data.products]),
        hero_products=json.dumps([product.dict() for product in brand_data.hero_products]),
        privacy_policy=brand_data.privacy_policy,
        refund_policy=brand_data.refund_policy,
        faqs=json.dumps(brand_data.faqs),
        important_links=json.dumps(brand_data.important_links),
        competitors=json.dumps(brand_data.competitors) if brand_data.competitors else None
    )
    db.add(brand)
    db.commit()
    db.refresh(brand)
    db.close()
