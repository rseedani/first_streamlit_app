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
fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set Friuit as list index
fruit_list = fruit_list.set_index('Fruit')

#adding a pick list
streamlit.multiselect("Pick some fruits:", list(fruit_list.index))

#displaying the table
streamlit.dataframe(fruit_list)



