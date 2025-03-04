# Future Developments for the Project

1. Improve the **model** and trying to implement a gridsearch technique to find a model that predicts better than the logicitic regression currently deployed.

2. **Feature Selection Refinement**: Remove **ADR** and **Booking Changes** being generated in the prototype as they are **not available at the time of booking**.

3. **Review and Fix Column Handling**: Check why **Company** and **Agent** columns are **not included** in `app.py`’s processing lists and ensure they are **properly handled**.  

4. **Improving New Booking Data Generation**: Enhance the **randomized booking simulation** to generate **more realistic data**, maybe leveraging the distribution of each feature in the original dataset. 

5. **Enhancing Booking Data**: Include **guest details** that are typically received with a booking but not used for model prediction: **Name, Email, Phone Number, Gender**, etc.  

6. **UI/UX Enhancements for the Streamlit App**  
   - Improve the **interface design** for a **cleaner and more intuitive layout**.  
   - Ensure that **multiple spinners do not appear** when toggling elements like the recent predictions table.