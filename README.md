# luxury-radar
luxury-radar

```text
luxury-radar/
├── airflow/
│   ├── dags/             ← DAG Python 파일 위치
│   ├── requirements.txt  ← Airflow에서 쓸 패키지
├── crawler/              ← 크롤러 코드
├── db/                   ← RDB 초기 설정, schema 등
└── docker-compose.yml   ← Airflow + DB 실행
```