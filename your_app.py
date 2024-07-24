import streamlit as st
from dummy_data import matters, elements, facts, evidence_documents, explanations

# Page setup
st.set_page_config(page_title="Automated Evidence Discovery")

# Display logo and title
logo, title = st.columns([1, 10])
with logo:
    st.image("burwicklogo.jpeg", width=50)
with title:
    st.title("Automated Evidence Discovery")

# Select Matter
st.subheader("Select Matter")
selected_matter = st.selectbox("Matter", matters)

if selected_matter and selected_matter != "Select a Matter":
    # Select Element
    st.subheader("Select Element of the Claim")
    selected_element = st.selectbox("Element", elements[selected_matter])

    if selected_element and selected_element != "Select an Element":
        st.write("---")  # Horizontal line

        st.header(f"{selected_matter}: {selected_element}")

        st.subheader("Fact")
        st.write(facts[selected_matter][selected_element])

        st.subheader("Evidence Documents")
        for doc in evidence_documents[selected_matter][selected_element]:
            st.markdown(f"""
                <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 10px; background-color: #f9f9f9;">
                    {doc}
                </div>
            """, unsafe_allow_html=True)

        st.subheader("Explanation")
        st.write(explanations[selected_matter][selected_element])
