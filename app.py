import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# Load the trained model
model_filename = "logistic_regression_pipeline.pkl"
loaded_pipe = joblib.load(model_filename)

# Define numerical and categorical features used during training
numerical_features = [
    "lead_time", "adr", "previous_cancellations", "previous_bookings_not_canceled",
    "booking_changes", "days_in_waiting_list", "adults", "required_car_parking_spaces",
    "total_of_special_requests"
]

categorical_features = [
    "hotel", "customer_type", "market_segment", "distribution_channel",
    "deposit_type", "meal", "reserved_room_type", "assigned_room_type", "is_repeated_guest"
]

# Streamlit UI
st.title("📊 Hotel Booking Cancellation Predictor")

st.write("🔄 This app simulates real-time incoming bookings and predicts the cancellation probability.")
st.write("📌 When a new booking comes into the system, a prediction is made and shown. The most recent predictions are displayed.")

# Initialize session state for storing recent predictions
if "recent_predictions" not in st.session_state:
    st.session_state.recent_predictions = pd.DataFrame(columns=["lead_time", "adr", "cancellation_probability"])

# Function to generate random booking data
def generate_random_booking():
    return pd.DataFrame({
        "lead_time": [np.random.randint(0, 365)],
        "adr": [np.random.uniform(50, 200)],
        "previous_cancellations": [np.random.randint(0, 5)],
        "previous_bookings_not_canceled": [np.random.randint(0, 10)],
        "booking_changes": [np.random.randint(0, 5)],
        "days_in_waiting_list": [np.random.randint(0, 30)],
        "adults": [np.random.randint(1, 3)],
        "required_car_parking_spaces": [np.random.randint(0, 2)],
        "total_of_special_requests": [np.random.randint(0, 5)],
        "hotel": [np.random.choice(["Resort Hotel", "City Hotel"])],
        "customer_type": [np.random.choice(["Contract", "Transient", "Group", "Transient-Party"])],
        "market_segment": [np.random.choice(["Direct", "Corporate", "Online TA", "Offline TA/TO", "Complementary"])],
        "distribution_channel": [np.random.choice(["Direct", "TA/TO", "Corporate", "GDS"])],
        "deposit_type": [np.random.choice(["No Deposit", "Non Refund", "Refundable"])],
        "meal": [np.random.choice(["BB", "HB", "FB", "SC"])],
        "reserved_room_type": [np.random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "P"])],
        "assigned_room_type": [np.random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "P"])],
        "is_repeated_guest": [np.random.choice([0, 1])],
        "company": [float(np.random.randint(0, 500)) if np.random.rand() > 0.2 else float(0)],
        "agent": [float(np.random.randint(0, 500)) if np.random.rand() > 0.2 else float(0)]
    })

# Create an empty placeholder for displaying predictions
recent_predictions_placeholder = st.empty()

# Simulate real-time updates
while True:
    # Generate a new booking
    new_booking = generate_random_booking()
    new_booking["adr"] = new_booking["adr"].astype(int)

    # Predict cancellation probability
    pred_proba = loaded_pipe.predict_proba(new_booking)[:, 1][0]  # Probability of cancellation

    # Create a new row for the table
    new_row = {"lead_time": new_booking["lead_time"].values[0], "adr": new_booking["adr"].values[0], 
               "cancellation_probability": round(pred_proba, 4)}

    # Update session state with the new prediction
    st.session_state.recent_predictions = pd.concat(
        [st.session_state.recent_predictions, pd.DataFrame([new_row])], ignore_index=True
    ).tail(10)  # Keep only the last 10 predictions

    # Display updated table
    with recent_predictions_placeholder.container():
        st.subheader("📈 Recent Predictions")
        st.dataframe(st.session_state.recent_predictions)

    # Wait before generating new data
    time.sleep(np.random.randint(5, 37))


