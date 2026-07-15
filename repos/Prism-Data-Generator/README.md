# Prism Data Generator

> Synthetic Data Generator for Enterprise Manufacturing

---

## Overview

Generate realistic, **100% synthetic** manufacturing data for testing, benchmarking, and development. No real company data is used or needed.

---

## 🎯 Purpose

- Create realistic test datasets
- Generate benchmark data for AI models
- Populate development environments
- Test edge cases without real data

---

## ✨ Features

- 🏭 **Multi-entity** — Customers, products, suppliers, transactions
- 📈 **Realistic patterns** — Seasonal trends, growth rates, anomalies
- 🔧 **Configurable** — Adjust distributions, volumes, relationships
- 📊 **Multiple formats** — CSV, JSON, SQL, Parquet
- 🎯 **Domain-specific** — Manufacturing, inventory, production

---

## 📊 Generated Entities

| Entity | Count | Relationships |
|--------|-------|---------------|
| Customers | 500 | → Orders, Invoices |
| Products | 50 | → Order Items, Inventory |
| Suppliers | 100 | → Purchase Orders |
| Employees | 200 | → Production, Sales |
| Orders | 50K | → Items, Payments |
| Inventory | 100K | → Products, Warehouses |
| Production | 20K | → Products, Employees |

---

## 🚀 Quick Start

```bash
# Install
pip install -r requirements.txt

# Generate all data
python generate.py --config config/default.yaml

# Generate specific entity
python generate.py --entity customers --count 1000

# Export to specific format
python generate.py --format sql --output data.sql
```

---

## ⚙️ Configuration

```yaml
# config/default.yaml
company:
  name: "Prism Fertilizers"
  industry: "manufacturing"
  
entities:
  customers:
    count: 500
    regions: ["Middle East", "Africa", "Asia"]
  products:
    count: 50
    categories: ["Urea", "DAP", "NPK", "Potash"]
  orders:
    count: 50000
    date_range: "2023-2026"
```

---

## 📂 Structure

```
Prism-Data-Generator/
├── generators/         # Entity generators
├── configs/            # Configuration files
├── data/               # Generated output
├── templates/          # Data templates
└── docs/               # Documentation
```

---

## ⚠️ Important

> **All generated data is 100% synthetic.** It resembles manufacturing data but does not represent any real company.

---

## 📝 License

MIT License
