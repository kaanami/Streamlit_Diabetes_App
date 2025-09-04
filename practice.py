import streamlit as st

# Text
st.title('Streamlit application Example')
st.header('The Automaton')
st.markdown('Hololive En Justice')

st.write('She can Yap!')

st.image('cc.jpg', caption="The Automaton")

# Input Widgets
st.button('Predict')

st.radio('Select option:',['GG','CC'])

    ## st.checkbox('Pick your option:'['Yes','Yes'])

st.selectbox('Pick a Gen',['Myth','Promise','Advent','Justice'])

st.multiselect('choose a planet:',['Earth1','Earth2','Earth3'])

st.select_slider('Pick a mark',['Chaotic','Normal','Not-Chaotic'])

st.slider('Pick a JP gen:',0,7)


# Input fields

Age = st.number_input('Enter your age:',1,100,18)

