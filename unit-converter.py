# virtual enviorment is a specific area of computer in
#  which packaegs and other things of our projecr are installed/ available


import streamlit as st # streamlit  is a library that allows us to create web apps

# function to convert  the units based on predefined conversion faction or formulas 
def convert_unit ( value , unit_from , unit_to ): #

    conversions = {

       "meters_Kilometers": 0.001,
       "kilometers_meters": 1000,
       "grams_kilograms": 0.001,
       "kilograms_grams": 1000,
    }


    key = f"{unit_from}_{unit_to}"  # generate a key besd on input and output units.
# logic of unit conversion
    if key in conversions: 
        conversion = conversions[key]
        return value * conversion
    
    else:
        return "conversions not supported" #retun the message if conversion is not supported

st.title("Unit Converter") # title of the web app


value = st.number_input("Enter the value:", min_value=1.0, step=1.0) # user input : numerical value to convert

#dropdown to select the unit to convert from
unit_from = st.selectbox("convert from :", ["meters" , "kilometers", "grams" , "kilograms"]  ) 

#dropdown to select the unit to convert to
unit_to = st.selectbox("convert to :", ["meters" , "kilometers", "grams" , "kilograms"]  )

# button to trigger the value 
if st.button("convert"):
    result = convert_unit(value , unit_from , unit_to) # call the function to convert the value
    st.write(f"converted value : {result}") # display the result
