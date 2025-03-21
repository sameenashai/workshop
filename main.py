import streamlit as st

st.title('hello world')
st.write('this is simple streamlit app.')
st.button('Click me')
st.text('hello....!! Streamlit...!!')



st.radio("Gender",["Female","Male"],captions=["is ur a girl","is ur a boy"],index=None)

name=st.text_input('please enter a name')
if name:
	st.write(f'hello , {name}!')
	
if st.file_uploader('upload file',type=['txt','csv']):
	st.write('file is uploaded')
