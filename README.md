
# 🕵️‍♂️ Luxury Radar

**명품 브랜드 웹사이트를 크롤링하여 상품 데이터를 수집, 저장, 검색하는 자동화 시스템**

> 웹 크롤러 + ETL 파이프라인 + API 서버 + Elasticsearch 기반 검색 + 로깅 시스템까지 포함된 종합 데이터 파이프라인 프로젝트입니다.

---

## 🧭 프로젝트 개요

- Rolex 등 명품 브랜드 상품 정보를 **자동 수집**
- 수집 데이터를 **RDB + Elasticsearch**에 저장
- 사용자 요청에 따라 **API 형태로 제공**
- 전체 시스템은 **Docker / Kubernetes 환경에 배포**
- **Airflow DAG**으로 ETL 자동화
- **ELK 스택**을 활용하여 운영 로그 시각화

---

## 🧱 시스템 아키텍처

```
[Airflow DAG]
    ↓
[크롤러 (Selenium)]
    ↓
[MySQL 저장] + [Elasticsearch 인덱싱]
    ↓                    ↓
[API 서버 (Express)] ← [Elasticsearch 검색]
    ↓
[사용자 API 호출]

※ 전체 시스템은 Docker / Kubernetes로 배포 및 관리
※ 로그는 ELK Stack으로 수집, Kibana에서 시각화
```

---

## ⚙️ 기술 스택

| 구분         | 스택 |
|--------------|------|
| Language     | Python, TypeScript |
| Web Crawler  | Selenium, BeautifulSoup, pandas |
| Backend API  | Express.js (TypeScript) |
| Database     | MySQL 8.0 |
| Search Engine| Elasticsearch |
| Scheduler    | Apache Airflow |
| Logging      | Filebeat, Logstash, Kibana |
| Container    | Docker, Kubernetes, Helm |
| Infra as Code| Terraform |

---

## 📦 프로젝트 구성

```
luxury-radar/
├── crawler/             # 크롤러 모듈 (브랜드별 크롤러 포함)
├── airflow/             # DAG 정의 및 스케줄러 설정
├── api-server/          # RESTful API 서버 (Express + TS)
├── db/                  # MySQL 초기 스키마, 쿼리 모듈
├── elk-stack/           # ELK 구성 설정 (filebeat/logstash 등)
├── infra/
│   ├── docker/          # Dockerfile
│   ├── helm/            # Kubernetes Helm Chart
│   └── terraform/       # AWS 인프라 구성 (EKS, RDS, S3 등)
└── README.md
```

---

## 🚀 주요 기능

- ✅ 다중 브랜드 크롤링 (Selenium 기반)
- ✅ Airflow DAG 자동화 (정기 실행)
- ✅ MySQL + Elasticsearch 이중 저장
- ✅ Express 기반 API 제공 (`/products`, `/search` 등)
- ✅ ELK 스택 기반 로그 수집 및 Kibana 시각화
- ✅ Docker + Kubernetes 배포 구성
- ✅ Terraform 기반 인프라 자동화

---

## 🔍 주요 화면 (스크린샷은 추후 추가 예정)

- Kibana 대시보드
- Airflow DAG 실행 화면
- API 응답 예시

---

## ✅ 실행 방법

```bash
# 1. Docker 빌드 및 실행
docker-compose up -d --build

# 2. Airflow UI 접속
http://localhost:8080

# 3. API 호출 예시
curl http://localhost:3000/products
```

---

## 🗂️ 작업 히스토리 (Changelog)

| 날짜 | 작업 내용 |
|------|-----------|
| 2025-04-11 | 프로젝트 구조 설계 완료 및 README 작성 시작 |
| 2025-04-11 | Rolex 크롤러 테스트 기반 TDD 도입 시도 → 기능 우선 전략으로 전환 |
| 2025-04-11 | 크롤링/서버/DB/로깅/인프라 5개 축 구조 확정 |
| 2025-04-11 | Elasticsearch를 통한 인덱싱 + API 연동 설계 추가 결정 |

> ⏳ 계속 업데이트 예정입니다.

---

## 🧪 향후 계획

- 관리자 대시보드 추가 (Next.js or React)
- Slack 알림 기능 (Airflow DAG 실패 시)
- 브랜드별 DAG 동적 생성 방식 도입
- 테스트 코드 작성 및 CI/CD 자동화
