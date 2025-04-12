-- products 테이블
CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  brand VARCHAR(50) NOT NULL,
  name VARCHAR(255) NOT NULL,
  model_number VARCHAR(50),
  official_url_kr TEXT,
  image_url TEXT,
  case_type VARCHAR(100),
  case_material TEXT,
  bezel TEXT,
  diameter VARCHAR(20),
  waterproof VARCHAR(20),
  movement_type VARCHAR(100),
  caliber VARCHAR(100),
  power_reserve VARCHAR(50),
  bracelet_type VARCHAR(100),
  bracelet_material VARCHAR(100),
  clasp TEXT,
  dial VARCHAR(100),
  dial_detail TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- product_prices 테이블
CREATE TABLE IF NOT EXISTS product_prices (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  price_kr VARCHAR(50),
  price_jp VARCHAR(50),
  price_us VARCHAR(50),
  price_hk VARCHAR(50),
  price_ch VARCHAR(50),
  collected_at DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);