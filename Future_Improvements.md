### Future Developments for the Project

- [x] Improve the **model** by implementing a full **GridSearch** to find a better-performing alternative to the currently deployed logistic regression.

- [ ] Refine **feature selection** by removing **ADR** and **Booking Changes** from the prototype inputs, as these values are **not known at the time of booking**.

- [ ] **Review and fix column handling** in `app.py` to ensure that **Company** and **Agent** are included and processed consistently.

- [ ] Improve the **generation of simulated bookings** by making the random values **more realistic**, ideally based on the **feature distributions** in the original dataset.

- [ ] Include **additional guest details** (e.g. **Name, Email, Phone Number, Gender**) in the UI to reflect what a hotel system would actually receive, even if they're not used in model prediction.

- [ ] Enhance the **Streamlit UI/UX**:
  - [ ] Design a **cleaner, more structured layout** for better readability and usability.
  - [ ] Fix toggle behavior to **prevent duplicate or overlapping spinners** when switching visibility of recent predictions.