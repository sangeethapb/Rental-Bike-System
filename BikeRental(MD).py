
import pandas as pd
import pickle
import streamlit as st

model=pickle.load(open('bike_model.pkl','rb'))

def welcome():
    return "Welcome All"


def main():
    st.title('BIKE RENTAL SYSTEM')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bike Rental Count Prediction Model using Random Forest Regression</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write();

    # Mappings for display
    season_mapping={0:'fall',1:'summer',2:'winter',3:'spring'}
    month_mapping={0:'Jan',1:'Feb',2:'Mar',3:'Apr',4:'May',5:'Jun',6:'Jul',7:'Aug',8:'Sep',9:'Oct',10:'Nov',11:'Dec'}
    holiday_mapping={0:'No',1:'Yes'}
    weekday_mapping={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    workingday_mapping={0:'No',1:'Yes'}
    weather_mapping={0:'Clear',1:'Mist',2:'Light Snow',3:'Heavy Rain'}

    # input form for feature
    with st.form('Prediction_form'):
        season = st.selectbox('Season', options=season_mapping.keys(),format_func=lambda x:season_mapping[x])
        year=st.selectbox('Year',options=range(2011,2027))
        month=st.selectbox('Month', options=month_mapping.keys(),format_func=lambda x:month_mapping[x])
        hour=st.selectbox('Hour',options=range(24))
        holiday=st.selectbox('Holiday', options=holiday_mapping.keys(),format_func=lambda x:holiday_mapping[x])
        weekday= st.selectbox('Weekday', options=weekday_mapping.keys(),format_func=lambda x:weekday_mapping[x])
        workingday=st.selectbox('Workingday', options=workingday_mapping.keys(),format_func=lambda x:workingday_mapping[x])
        weather= st.selectbox('Weather', options=weather_mapping.keys(),format_func=lambda x:weather_mapping[x])
       # min_temp = st.number_input("Minimum Temperature", value=-20)
        #max_temp = st.number_input("Maximum Temperature", value=100)
        min_temp = 0.0
        max_temp = 1.0
        temp = st.slider("Temperature", min_value=min_temp, max_value=max_temp, value=float((min_temp + max_temp) / 2))
        min_atemp = 0.0 
        max_atemp = 1.0  
        initial_atemp = 0.5 
        temp_feel = st.slider("Temperature feels like", min_value=min_atemp, max_value=max_atemp, value=initial_atemp)
        min_hum = 0.0 
        max_hum = 1.0
        initial_hum = 0.5  
        humidity = st.slider("Humidity", min_value=min_hum, max_value=max_hum, value=initial_hum)
        min_windspeed = 0.0  
        max_windspeed = 1.0 
        initial_windspeed = 0.5 
        windspeed = st.slider("Windspeed", min_value=min_windspeed, max_value=max_windspeed, value=initial_windspeed)
        
        submitted=submitted = st.form_submit_button("Submit")
          
        if submitted:
            #prepare input data
            input_data= pd.DataFrame({'season':[season],'year':[year],'month':[month],'hour':[hour],'holiday':[holiday],'weekday':[weekday],'workingday':[workingday],'weather':[weather],'temp':[temp],'temp_feel':[temp_feel],'humidity':[humidity],'windspeed':[windspeed]})
                       
            #predict using the model
            prediction=model.predict(input_data)
            
            #Displaying prediction
            st.write('Predicted Bike Rental Count')
            st.write(int(prediction)) 
            #st.write('Bike High Demand' if prediction[0] > 0.5 else 'Bike Low Demand')
            if prediction[0] > 50:
                st.write(prediction) 
                st.write('Bike High Demand')
            else:
                st.write(prediction) 
                st.write('Bike Low Demand')
                     
        
if __name__=='__main__':
    main()          
