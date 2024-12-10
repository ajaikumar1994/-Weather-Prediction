import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import webbrowser



#function for predection

def predection(precipitation,temp_max,temp_min,wind,day,month,year):
  with open('weather_model.pkl','rb') as f:
    model=pickle.load(f)
  result=model.predict([[precipitation,temp_max,temp_min,wind,day,month,year]])
  if result==0:
    return 'rain'
  elif result==1:
    return 'sun'
  elif result==2:
    return 'fog'
  elif result==3:
    return 'drizzle'
  elif result==4:
    return 'snow'


#page layout

st.set_page_config(layout='wide')
st.image('/content/ocean-7461792_1280.jpg')
st.title('Weather Prediction')
tab1,tab2,tab3=st.tabs(['Home','Prediction','live'])
with tab1:
    st.header('Home')
    st.write('''
    ### Welcome to the Weather Prediction App!

    **Overview:**
    Our Weather Prediction App leverages advanced machine learning techniques to forecast weather conditions based on historical data. By entering parameters such as precipitation, maximum and minimum temperature, wind speed, and date, our model can accurately predict the likelihood of rain, sunshine, fog, drizzle, or snow.

    **How It Works:**
    - **Data Input:** Users can input key weather variables such as precipitation, temperature, and wind speed.
    - **Model Prediction:** The app uses a pre-trained machine learning model to analyze the input data and predict the weather for the selected date.
    - **Live Weather Map:** You can also explore current weather conditions globally through our integrated live weather map.

    **Features:**
    - **User-Friendly Interface:** A clean, intuitive design that makes it easy to input data and get predictions.
    - **Accurate Predictions:** Our model has been trained on a vast dataset to ensure accurate and reliable weather forecasts.
    - **Live Updates:** Access real-time satellite imagery and weather maps through our live weather tab.
    
    **Future Enhancements:**
    - Integration with more comprehensive weather data sources.
    - Enhanced predictive accuracy with ongoing model training and updates.
    - Additional weather parameters for even more precise forecasting.

    **Explore the App:**
    - Navigate to the 'Prediction' tab to enter your data and get weather forecasts.
    - Visit the 'Live' tab for real-time weather updates and satellite views.
    
    We hope you find this tool helpful and insightful. Enjoy exploring the weather like never before!

    **Developed by:** [Ajai Kumar]
    ''')


with tab2:
  st.header('Prediction')
  col1,col2=st.columns(2)
  with col1:
    
    precipitation=st.number_input('precipitation')
    temp_max=st.number_input('temp_max')
    temp_min=st.number_input('temp_min')
    wind=st.number_input('wind')

  with col2:  
    # Create a date input widget
    selected_date = st.date_input("Select a date")
    day=selected_date.day
    month=selected_date.month
    year=selected_date.year
  if st.button('Predict',use_container_width=True):
    result=predection(precipitation,temp_max,temp_min,wind,day,month,year)
    st.success(result)

with tab3:
  st.header('live')
  
  if st.button("live map view"):
    st.write("Zoom Earth is a fantastic tool for exploring our planet and tracking weather patterns. It provides real-time satellite imagery, weather maps, and hurricane tracking, making it a valuable resource for meteorologists, researchers, and anyone interested in the environment.")
    st.markdown('[ZOOM EARTH](https://zoom.earth/places/india/#map=precipitation/model=icon)')
