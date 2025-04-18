import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from datetime import datetime
from faker import Faker

st.set_page_config(page_title="Booking Cancellation Predictor", page_icon="🛎️")

# Load the trained model
model_filename = "best_model_pipeline.pkl"
loaded_pipe = joblib.load(model_filename)

# Faker instance
faker = Faker()

# Streamlit UI
st.title("🏨🛎️ Hotel Booking Cancellation Predictor")
st.image("_assets/banner.jpg")
st.write("🔄 This app simulates real-time incoming bookings and predicts the cancellation probability.")
st.write("📌 When a new booking comes into the system, a prediction is made and shown. The most recent predictions are displayed.")

# Toggle to display/hide the recent predictions table
show_recent_predictions = st.toggle("Show Recent Predictions", value=True)

# Initialize session state
if "recent_predictions" not in st.session_state:
    st.session_state.recent_predictions = pd.DataFrame(columns=[
        "Booking Date", "Guest Name", "Gender", "Email", "Phone",
        "Hotel Type", "Customer Type", "Market Segment", "Distribution Channel",
        "Reserved Room Type", "Deposit Type", "Repeated Guest", "Company", "Agent",
        "Adults", "Previous Cancellations", "Cancellation Probability"
    ])

# Placeholders
clock_placeholder = st.empty()
new_booking_placeholder = st.empty()
recent_predictions_placeholder = st.empty()

# Clock updater
def update_clock():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clock_placeholder.markdown(
            f"<h2 style='text-align: center; font-family: monospace;'>{current_time}</h2>",
            unsafe_allow_html=True
        )
        time.sleep(1)

import threading
clock_thread = threading.Thread(target=update_clock, daemon=True)
clock_thread.start()

# Random booking data generator
def generate_random_booking():
    return pd.DataFrame({
        "lead_time": [np.random.randint(0, 365)],
        "previous_cancellations": [np.random.randint(0, 5)],
        "previous_bookings_not_canceled": [np.random.randint(0, 10)],
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

# Main loop
while True:
    new_booking = generate_random_booking()

    # Fake guest details
    guest_name = faker.name()
    guest_email = faker.email()
    guest_phone = faker.phone_number()
    guest_gender = np.random.choice(["Male", "Female", "Other"])

    # Predict
    pred_proba = loaded_pipe.predict_proba(new_booking)[:, 1][0]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # New row for recent predictions
    new_row = {
        "Booking Date": timestamp,
        "Guest Name": guest_name,
        "Gender": guest_gender,
        "Email": guest_email,
        "Phone": guest_phone,
        "Hotel Type": new_booking["hotel"].values[0],
        "Customer Type": new_booking["customer_type"].values[0],
        "Market Segment": new_booking["market_segment"].values[0],
        "Distribution Channel": new_booking["distribution_channel"].values[0],
        "Reserved Room Type": new_booking["reserved_room_type"].values[0],
        "Deposit Type": new_booking["deposit_type"].values[0],
        "Repeated Guest": new_booking["is_repeated_guest"].values[0],
        "Company": int(new_booking["company"].values[0]),
        "Agent": int(new_booking["agent"].values[0]),
        "Adults": new_booking["adults"].values[0],
        "Previous Cancellations": new_booking["previous_cancellations"].values[0],
        "Cancellation Probability": round(pred_proba, 4)
    }

    # Update state
    st.session_state.recent_predictions = pd.concat(
        [st.session_state.recent_predictions, pd.DataFrame([new_row])],
        ignore_index=True
    ).tail(10)

    # Display new booking
    with new_booking_placeholder:
        st.info(f"""
        **🆕 New Booking Came In!**  
        - **📅 Date:** {new_row["Booking Date"]}  
        - **👤 Name:** {new_row["Guest Name"]}  
        - **📩 Email:** {new_row["Email"]}  
        - **📱 Phone:** {new_row["Phone"]}  
        - **⚧ Gender:** {new_row["Gender"]}  
        - **🏨 Hotel Type:** {new_row["Hotel Type"]}  
        - **📢 Market Segment:** {new_row["Market Segment"]}  
        - **📡 Distribution Channel:** {new_row["Distribution Channel"]}  
        - **🛏️ Reserved Room Type:** {new_row["Reserved Room Type"]}  
        > **⚠️ Cancellation Probability:** `{new_row["Cancellation Probability"] * 100:.2f}%`
        """, icon="📢")

    if show_recent_predictions:
        with recent_predictions_placeholder:
            st.subheader("📈 Recent Predictions")
            st.dataframe(st.session_state.recent_predictions)

    with st.spinner("⏳ Waiting for new bookings..."):
        time.sleep(np.random.randint(5, 11))
