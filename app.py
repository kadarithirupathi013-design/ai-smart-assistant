import streamlit as st

st.set_page_config(
    page_title="AI Smart Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Smart Assistant")
st.caption("Your personal assistant for everyday questions.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask me anything...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    answer = (
        "Thanks for your question! "
        "Connect an AI API to enable real AI-generated answers."
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)import streamlit as st

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
