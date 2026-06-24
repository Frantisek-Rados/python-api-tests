# Python API Tests

Pokročilé API testy v Pythone s použitím `pytest`, `requests` a výkonnostných testov s `k6`.

---

## 🎯 Obsah

- ✅ API testy (GET, POST, PUT, DELETE)
- ✅ Parametrizované testy (`@pytest.mark.parametrize`)
- ✅ Výkonnostné testy (k6)
- ✅ CI/CD (GitHub Actions)
- ✅ Reporty (pytest-html)

---

## 🚀 Spustenie testov

### 1. Nainštaluj závislosti
```bash
pip install -r requirements.txt
```

### 2. Spusti API testy
```bash
pytest tests/test_api.py -v
```

### 3. Spusti výkonnostný test (k6)
```bash
k6 run load-test.js
```

---

## 📂 Štruktúra projektu

```
python-api-tests/
├── tests/
│   └── test_api.py          # API testy (GET, POST, PUT, DELETE)
├── load-test.js             # k6 – GET test
├── load-test-post.js        # k6 – POST test
├── conftest.py              # Fixtures pre pytest
├── requirements.txt         # Závislosti
└── .github/workflows/ci.yml # CI/CD pipeline
```

---

## 📊 Výsledky

- **API testy:** 10/10 prešlo ✅
- **k6 – GET:** 100% úspešnosť (3733 požiadaviek)
- **k6 – POST:** 100% úspešnosť (723 požiadaviek)

---

## 🛠️ Technológie

- Python + pytest
- requests
- k6
- GitHub Actions

---

## 📬 Autor

[František Radoš](https://github.com/Frantisek-Rados)
