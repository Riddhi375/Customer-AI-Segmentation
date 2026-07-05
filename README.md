# 🧠 Customer AI Segmentation

An AI-powered customer analytics platform built with **FastAPI**, **SQLAlchemy**, and **Scikit-learn** to help businesses manage customer data, automatically group customers into meaningful segments, and predict which customers are at risk of churning.

---

## 🎯 What it does

This platform exposes a REST API that lets you:

1. **Manage customers** — full CRUD (create, read, update, delete) on customer records stored in a database
2. **Segment customers** — group customers into clusters using **K-Means** based on attributes like age, so you can identify distinct customer groups (e.g. young, middle-aged, senior)
3. **Predict churn risk** — use a trained **Random Forest** classifier to flag customers as "High Risk" or "Low Risk" of churning, based on age, income, and order history
4. **View dashboard stats** — quick aggregate metrics like total customer count

---

## 🧠 How it works (architecture)

```
                     ┌─────────────────────────┐
                     │      FastAPI App         │
                     │   (app/main.py)           │
                     └────────────┬─────────────┘
                                  │
        ┌─────────────┬──────────┼──────────────┬─────────────┐
        ▼             ▼          ▼              ▼             
┌───────────────┐ ┌──────────┐ ┌─────────────┐ ┌─────────────┐
│ /customers     │ │/dashboard│ │/segmentation │ │  /churn      │
│ CRUD endpoints │ │  stats   │ │  K-Means      │ │ RandomForest │
└───────┬───────┘ └────┬─────┘ └──────┬───────┘ └──────┬───────┘
        │              │              │                │
        ▼              ▼              ▼                ▼
┌────────────────────────────┐ ┌────────────────────────────────┐
│   SQLAlchemy + Database    │ │   app/ml/segmentation.py        │
│   (app/database.py,        │ │   app/ml/churn.py                │
│    app/models.py)           │ │   (trained model in              │
│                              │ │    trained_models/churn_model.pkl)│
└────────────────────────────┘ └────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Web Framework | `FastAPI` |
| Server | `uvicorn` |
| ORM / Database | `SQLAlchemy` |
| Data Validation | `Pydantic` |
| Clustering | `scikit-learn` — `KMeans` |
| Churn Prediction | `scikit-learn` — `RandomForestClassifier` |
| Data handling | `pandas` |
| Model persistence | `joblib` |
| Config | `python-dotenv` |

---

## 📂 Project Structure

```
Customer-AI-Segmentation/
├── README.md
├── requirements.txt
├── .gitignore
└── app/
    ├── main.py              # FastAPI app entry point, registers all routers
    ├── config.py            # Loads environment variables (.env)
    ├── database.py          # SQLAlchemy engine, session, Base
    ├── models.py             # Customer ORM model
    ├── schemas.py            # Pydantic request/response schemas
    ├── utils.py
    ├── ml/
    │   ├── segmentation.py   # K-Means customer segmentation logic
    │   ├── churn.py           # Loads trained model, predicts churn risk
    │   └── train_churn.py     # Script to train & save the churn model
    ├── routes/
    │   ├── customers.py       # /customers CRUD endpoints
    │   ├── segmentation.py    # /segmentation endpoint
    │   ├── churn.py            # /churn endpoint
    │   └── dashboard.py        # /dashboard stats endpoint
    └── services/
```

---

## 🚀 Getting Started

### 1. Clone the repo & install dependencies

```bash
git clone https://github.com/Riddhi375/Customer-AI-Segmentation.git
cd Customer-AI-Segmentation
pip install -r requirements.txt
```

### 2. Set up environment variables

Create a `.env` file in the project root with:

```
DATABASE_URL=sqlite:///./customers.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Train the churn prediction model (one-time setup)

This trains a small Random Forest model on sample data and saves it so the `/churn` endpoint can use it.

```bash
mkdir trained_models
python -m app.ml.train_churn
```

### 4. Run the API server

```bash
uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000/docs** to explore and test every endpoint interactively via the auto-generated Swagger UI.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Welcome message |
| `POST` | `/customers/` | Create a new customer |
| `GET` | `/customers/` | List all customers |
| `GET` | `/customers/{id}` | Get a single customer |
| `PUT` | `/customers/{id}` | Update a customer |
| `DELETE` | `/customers/{id}` | Delete a customer |
| `GET` | `/segmentation/` | Cluster customers into segments (K-Means) |
| `GET` | `/churn/?age=&income=&orders=` | Predict churn risk for given inputs |
| `GET` | `/dashboard/` | Get aggregate stats (e.g. total customers) |

---

## 💡 Key Design Decisions

- **Why FastAPI?** Automatic request validation via Pydantic, built-in interactive API docs (Swagger/ReDoc), and async-ready performance make it ideal for a lightweight analytics API.
- **Why K-Means for segmentation?** It's a simple, fast, and interpretable way to group customers into distinct clusters without needing labeled data.
- **Why Random Forest for churn?** It handles non-linear relationships between features (age, income, orders) well and is robust to overfitting on small datasets, while still being fast to train and easy to persist with `joblib`.
- **Why cache the trained churn model to disk?** Retraining on every request would be wasteful — `train_churn.py` is run once, and `churn.py` simply loads the saved `.pkl` file at startup.

---

## 🔮 Possible Extensions

- Replace the SQLite default with PostgreSQL for production use
- Add authentication (JWT, using the existing `SECRET_KEY`/`ALGORITHM` config)
- Expand segmentation to use more features (income, order frequency, etc.) instead of just age
- Add a proper train/test split and evaluation metrics for the churn model
- Build a frontend dashboard to visualize segments and churn risk

---

## 🙋 Author

Built by **Riddhi**.
