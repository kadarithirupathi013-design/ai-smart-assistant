import streamlit as st

st.set_page_config(
    page_title="AI Smart Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Smart Assistant")

st.write(
    "Your smart assistant for productivity, "
    "information, and everyday problem-solving."
)

question = st.text_area("What would you like help with?")

if st.button("Get Answer"):
    if question.strip():
        st.info(
            "Your question has been received! "
            "Connect an AI API to generate real AI answers."
        )
    else:
        st.warning("Please enter a question.")
