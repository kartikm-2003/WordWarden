import streamlit as st
import pickle
import string
import time
import nltk

tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title(":red[Word Warden]")
st.subheader(' ', divider='rainbow')


input_sms=st.text_area("Enter the message you want to post ")

if st.button(':red[CHECK]'):

    vector_input=tfidf.transform([input_sms])

    result=model.predict_proba(vector_input)[:,1]

    if result>0.9:
        with st.status("Checking", expanded=True) as status:
            st.write("Looking for keywords")
            time.sleep(2)
            st.write("Checking the levels of toxicity")
            time.sleep(2)
            status.update(label="Complete!", state="complete", expanded=False)
        st.warning('Sorry you cannot post it on any social media platform. It is Severely toxic, Please check and re-write your message!.', icon="🚨")

    elif result<0.9 and result>0.7:
        with st.status("Checking", expanded=True) as status:
            st.write("Looking for keywords")
            time.sleep(2)
            st.write("Checking the levels of toxicity")
            time.sleep(2)
            status.update(label="Complete!", state="complete", expanded=False)
        st.warning('Sorry you cannot post it on any social media platform. It is toxic, Please check and re-write your message!.', icon="🚨")

    elif result<0.7 and result>0.59:
        with st.status("Checking", expanded=True) as status:
            st.write("Looking for keywords")
            time.sleep(2)
            st.write("Checking the levels of toxicity")
            time.sleep(2)
            status.update(label="Complete!", state="complete", expanded=False)
        st.warning('Sorry, you cannot post it on any social media platform. It is mildly toxic, Please check and re-write your message!.', icon="⚠️")

    elif result<0.59:
        with st.status("Checking", expanded=True) as status:
            st.write("Looking for keywords")
            time.sleep(2)
            st.write("Checking the levels of toxicity")
            time.sleep(2)
            status.update(label="Complete!", state="complete", expanded=False)
        st.success("You can post this message, It is safe.",icon="✅")
        st.balloons()