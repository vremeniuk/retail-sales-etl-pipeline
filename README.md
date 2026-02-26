# Retail Sales ETL Pipeline

Production-style modular ETL pipeline built in Python to simulate data processing for a retail business.

---

## Project Overview

This project demonstrates a structured ETL process:

Raw Data → Cleaning → Validation → Transformation → Business Metrics → Analytics Dataset

The pipeline simulates how transactional retail data could be processed before loading into a Data Warehouse.

---

## Architecture

```
data/
 ├── raw/          # Source data
 ├── cleaned/      # Cleaned dataset
 └── analytics/    # Final transformed dataset

src/
 ├── extract.py
 ├── transform.py
 ├── validate.py
 ├── metrics.py
 └── pipeline.py
```

---

## ETL Process

### Extract
- Load raw CSV data

### Clean
- Remove duplicates
- Parse dates
- Handle missing values
- Remove invalid quantities
- Normalize categorical fields

### Validate
- No null `order_id`
- Quantity > 0
- Price > 0
- Valid payment_status values
- No duplicate order_id

### Transform
- Revenue calculation
- Order month derivation
- Paid flag creation

### Business Metrics
- Total revenue
- Revenue per category
- Average order value
- Paid revenue
- Monthly revenue growth rate

---

## Technologies

- Python
- Pandas
- Git
- Modular architecture principles

---

## How to Run

```bash
pip install -r requirements.txt
python src/pipeline.py
```
