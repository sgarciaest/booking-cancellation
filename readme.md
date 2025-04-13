# 🏨 Booking Cancellation Predictor

This interactive prototype simulates real-time hotel bookings and predicts the likelihood of a reservation being canceled. It uses a trained machine learning model built from historical hotel booking data and displays live predictions in an intuitive dashboard.

The project includes both a complete **model training notebook** and a **Streamlit application** that visualizes and simulates live booking flows. It’s designed to reflect how front-desk staff or revenue managers could anticipate cancellations in real time.



## 🚀 Features

- Real-time booking simulation with synthetic guest details.
- Predicts *cancellation probability* for each new booking.
- Displays recent booking predictions with rich booking context.
- Live digital clock and booking events.
- Interactive UI using Streamlit.
- Machine learning pipeline using Scikit-learn and best practices (including outlier handling and ordinal/one-hot encoding).
- Fully reproducible training process in Jupyter Notebook.



## 🧠 Model Overview

The model is trained on the [Hotel Booking Demand Dataset](https://www.sciencedirect.com/science/article/pii/S2352340918315191). It has been extended here with feature engineering, outlier handling via `RobustScaler`, and model selection using `GridSearchCV`.

### Model Pipeline:

- Feature selection with domain knowledge and assumptions for this case.
- Preprocessing with `ColumnTransformer` and `Pipeline`
- Encoding strategies:
  - One-hot for nominal features
  - Ordinal for ordered room and meal types
- RobustScaler for outlier resistance
- Logistic Regression and Random Forest evaluated
- Final model selected using grid search (with `recall` as scoring metric)

> We optimize for **recall** because in this business context, **missing actual cancellations (false negatives)** can lead to *significant revenue loss*.  
>  
> If a booking is wrongly predicted as safe and the guest cancels, the room may remain unsold, especially in high-demand periods — a scenario that directly impacts hotel profitability. On the other hand, predicting a cancellation that doesn’t happen (false positive) may cause only minor operational overhead (e.g., overbooking mitigation or follow-up emails).  
>  
> By maximizing recall, the model ensures we *capture as many true cancellations as possible*, enabling proactive actions like:
>
> - **Reallocating inventory** in advance  
> - **Targeted retention efforts** (e.g., incentives to confirm stay)  
> - **More accurate demand forecasting**
>
> This decision aligns with *key hotel operations goals*: **protecting revenue**, improving **inventory management**, and enhancing **customer engagement** based on risk of cancellation.


## 🛠️ Setup Instructions

The project can be checked [here](https://booking-cancellation.streamlit.app/) in a Streamlit Cloud instance.

To run this project locally:

### 1. Clone the repository

```bash
git clone https://github.com/sgarciaest/booking-cancellation.git
cd booking-cancellation
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

This will launch the interactive dashboard in your browser. It will generate bookings every few seconds and display cancellation predictions in real time.



## 📁 Project Structure

```
booking_cancellation/
├── app.py                       # Streamlit prototype app
├── best_model_pipeline.pkl     # Trained ML pipeline (stored via Git LFS)
├── hotel_bookings_model.ipynb  # Main notebook for model training & tuning
├── hotel_bookings_exploration.ipynb  # Initial EDA (optional)
├── hotel_bookings.csv          # Dataset
├── requirements.txt            # Python dependencies
├── readme.md                   # This file
└── _assets/                    # UI assets (e.g., banner image)
```



## ✅ Built With

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for analysis
- [Faker](https://faker.readthedocs.io/) for fake guest details
