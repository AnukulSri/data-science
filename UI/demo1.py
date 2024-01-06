# command to run streamlit file on terminal
# streamlit run ui/demo1.py //this is a command to run this demo-1 file
  
import streamlit as st


st.title("Streamlit Demo")
st.header("Streamlit is awesome")
st.subheader("It is easy to use")
st.text("This is a simple text example")
st.write("This is a magical function")
st.markdown("This is a markdown example")
st.success("This is a success message")
st.info("This is an info message")
st.warning("This is a warning message")
st.error("This is an error message")
st.exception("This is an exception message")
st.latex(r'''a+a r^1+a r^2+a r^3''')
st.color_picker('Choose your favorite color')

#st.image('ui/background.jpg')

#st.video(r"")
#st.audio()

name= st.text_input("Enter a name")
cost = st.number_input("Enter the cost")
comment = st.text_area("Enter a message")
status = st.checkbox("save this data")
gender =  st.radio("select a gender",['male','female','others'])
querylist = ['How to use streamlit?',
'Is streamlit free or paid','Is it gonna rain now?']

query = st.selectbox("What the query",querylist)
rating = st.slider("Select the rating",1,5)
btn = st.button("Submit the response")


if btn:
   st.balloons()
   st.write("username:",name)
   st.write("cost:",cost)
   st.write("Comment:",comment)
   st.write("status:",status)
   st.write("gender:",gender)
   st.write("query:",query)
   st.write("rating:",rating)




