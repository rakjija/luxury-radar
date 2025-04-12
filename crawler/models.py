from sqlalchemy import TIMESTAMP, Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from crawler.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    model_number = Column(String(50), unique=True)
    official_url_kr = Column(Text)
    image_url = Column(Text)
    case_type = Column(String(100))
    case_material = Column(Text)
    bezel = Column(Text)
    diameter = Column(String(20))
    waterproof = Column(String(20))
    movement_type = Column(String(100))
    caliber = Column(String(100))
    power_reserve = Column(String(50))
    bracelet_type = Column(String(100))
    bracelet_material = Column(String(100))
    clasp = Column(Text)
    dial = Column(String(100))
    dial_detail = Column(Text)
    created_at = Column(TIMESTAMP)

    prices = relationship(
        "ProductPrice", back_populates="product", cascade="all, delete"
    )


class ProductPrice(Base):
    __tablename__ = "product_prices"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    price_kr = Column(String(50))
    price_jp = Column(String(50))
    price_us = Column(String(50))
    price_hk = Column(String(50))
    price_ch = Column(String(50))
    collected_at = Column(Date)
    created_at = Column(TIMESTAMP)

    product = relationship("Product", back_populates="prices")
