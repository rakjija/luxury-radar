from datetime import date

from sqlalchemy.orm import Session

from crawler.db import SessionLocal
from crawler.models import Product, ProductPrice


def save_to_db(product_data: dict):
    db: Session = SessionLocal()

    try:
        existing = (
            db.query(Product)
            .filter_by(model_number=product_data["model_number"])
            .first()
        )

        if not existing:
            product = Product(
                **{k: v for k, v in product_data.items() if hasattr(Product, k)}
            )
            db.add(product)
            db.flush()  # ID 확보
        else:
            product = existing

        price = ProductPrice(
            product_id=product.id,
            price_kr=product_data.get("price_kr"),
            price_jp=product_data.get("price_jp"),
            price_us=product_data.get("price_us"),
            price_hk=product_data.get("price_hk"),
            price_ch=product_data.get("price_ch"),
            collected_at=date.today(),
        )

        db.add(price)
        db.commit()

    except Exception as e:
        db.rollback()
        print("❌ Error:", e)
    finally:
        db.close()
