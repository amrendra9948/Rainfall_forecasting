import numpy as np
import pickle
import streamlit as st



# Create a function for prediction
def rainfall_prediction(input_data):
    # Convert input data to a numpy array and reshape it
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make the prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'No Rainfall'
    else:
        return 'Rainfall'

def main():
    st.title('🌧️ Insightful Rainfall Forecasting')

    # Add the VBSPU logo at the top
    st.image('vbspu-logo.png', width=200) # Use your logo path here

    # Displaying the project synopsis and details
    st.subheader("Project Synopsis")
    st.write("""
        **Team Members:**
        - Vikash Jaysingh Yadav (2155063)
        - Amrendra Bahadur Singh (2155009)

        **Guide:** Mr. Purnendra Kumar

        **Department:** Computer Science & Engineering

        **Batch:** 2025
    """)

    # Function to validate if input is numeric and not empty
    def validate_input(input_value, field_name):
        if input_value == "":
            st.error(f"Please enter a value for {field_name}.")
            return None
        try:
            return float(input_value)
        except ValueError:
            st.error(f"Invalid value for {field_name}. Please enter a valid number.")
            return None

    # Input fields for the user to fill
    pressure = validate_input(st.text_input('Pressure (hPa)', ''), 'Pressure')
    dewpoint = validate_input(st.text_input('Dewpoint (°C)', ''), 'Dewpoint')
    humidity = validate_input(st.text_input('Humidity (%)', ''), 'Humidity')
    cloud = validate_input(st.text_input('Cloud Coverage (%)', ''), 'Cloud')
    sunshine = validate_input(st.text_input('Sunshine (hours)', ''), 'Sunshine')
    winddirection = validate_input(st.text_input('Wind Direction (°)', ''), 'Wind Direction')
    windspeed = validate_input(st.text_input('Wind Speed (km/h)', ''), 'Wind Speed')

    # Only proceed if all fields are valid
    if None in [pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]:
        return  # If any field is invalid, exit the function

    # Button for prediction
    if st.button("Predict Rainfall"):
        # Create the input array for prediction
        input_data = [pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]
        diagnosis = rainfall_prediction(input_data)

        # Display the result
        st.success(f"Prediction: {diagnosis}")
        if diagnosis == "Rainfall":
            st.warning("Prepare for rain! It’s likely to rain today.")
        else:
            st.info("No rainfall expected today. Enjoy the dry weather!")

    st.subheader("Conclusion")
    st.write("""
        By implementing this rainfall prediction system, we aim to provide timely and accurate forecasts based on real-time weather data. The application offers an accessible way to predict rainfall using an intuitive web interface, leveraging machine learning to provide valuable insights.
        
        This model can be expanded by integrating more complex features like geographical data or real-time weather data APIs to further enhance its predictive accuracy.
    """)

if __name__ == '__main__':
    main()
