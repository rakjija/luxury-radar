from crawler.save_to_db import save_to_db

sample_product = {
    "brand": "Rolex",
    "name": "Cosmograph Daytona",
    "model_number": "M126518LN-0014",
    "official_url_kr": "https://www.rolex.com/watches/cosmograph-daytona/m126518ln-0014",
    "image_url": "https://www.rolex.com/watches/cosmograph-daytona/image.jpg",
    "case_type": "오이스터",
    "case_material": "18캐럿 옐로우 골드",
    "bezel": "타키미터 눈금이 몰딩된 블랙 세라믹 베젤",
    "diameter": "40mm",
    "waterproof": "수심 100미터 / 330피트 방수",
    "movement_type": "퍼페츄얼, 메케니컬 크로노그래프, 셀프 와인딩",
    "caliber": "4131, 롤렉스 매뉴팩처",
    "power_reserve": "약 72시간",
    "bracelet_type": "오이스터플렉스",
    "bracelet_material": "고성능 엘라스토머로 오버몰딩된 유연한 메탈 블레이드",
    "clasp": "롤렉스 글라이드록 익스텐션 시스템",
    "dial": "터콰이즈 블루 및 블랙",
    "dial_detail": "푸른색 야광이 오랫동안 지속되는 크로마라이트 디스플레이",
    "price_kr": "53870000",
    "price_jp": "Price on Request",
    "price_us": "Price on Request",
    "price_hk": "Price on Request",
    "price_ch": "Price on Request",
}

if __name__ == "__main__":
    save_to_db(sample_product)
    print("✅ 저장 완료!")
