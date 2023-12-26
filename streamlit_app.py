import streamlit

streamlit.title("My new healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
#import table
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set Friuit as list index
my_fruit_list = my_fruit_list.set_index('Fruit')

#adding a pick list
streamlit.multiselect("Pick some fruits:", list(fruit_list.index))

#displaying the table
streamlit.dataframe(my_fruit_list)


#new section to display fruitvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
