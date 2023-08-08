import pandas as pd
import streamlit as st
import pickle
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-photo/indian-dhal-spicy-curry-bowl-spices-herbs-rustic-black-wooden-background_2829-4751.jpg?w=900");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# [theme]
# backgroundColor="#e0c869"
# secondaryBackgroundColor="#e0c869"
# textColor="#f1eded"
# font="serif"


st.title('INDIAN NIBBLES\n'
         'Food Reccomendation System Based On Indian Cuisine')
foodl= pickle.load(open('meal.pkl','rb'))
foodn = pd.DataFrame(foodl)
similarity = pickle.load(open('similarity.pkl','rb'))
def reccomend(food):
    food_index = foodn[foodn['name']== food].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    rec_food = []
    for i in food_list:
        rec_food.append(foodn.iloc[i[0]].name)
        st.image(foodn.iloc[i[0]].img_url, caption= foodn.iloc[i[0]]['name'], width= 200)

    return rec_food
foodsel = st.selectbox('Select Your Delicacy! ',foodn['name'].values)
if st.button('Reccomend'):
    suggestions = reccomend(foodsel)
    for i in suggestions:
        st.write(i)
