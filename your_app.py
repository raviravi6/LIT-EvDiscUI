import streamlit as st
import json
import time
import datetime


# Function to load data based on the selected matter
def load_data(matter):
    if matter == "DIG":
        file_name = "dig_data.json"
    elif matter == "Communi3":
        file_name = "communi3_data.json"
    else:
        return None

    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"Data file {file_name} not found.")
        return None
    
# Page setup
st.set_page_config(page_title="Automated Evidence Discovery")

st.markdown("""
    <style>
    [data-testid="stImage"] {
        margin: 0;
        padding: 0;
    }
    .st-emotion-cache-1v0mbdj > img {
        margin-top: 1.4rem;
    }
    .st-emotion-cache-zt5igj {
        margin-top: -0.5rem;
    }
    .small-header {
            font-size: 24px;
            font-weight: 600;
            margin-top: 0.5em;
        }
    </style>
    """, unsafe_allow_html=True)

# Display logo and title
logo, title = st.columns([1, 10])
with logo:
    st.image("burwicklogo.jpeg", width=50)
with title:
    st.title("Automated Evidence Discovery")

# Add subheader to the third column, aligned to the right
st.markdown('<h3 style="text-align: center;">Section 12(a)(1) Claim Analysis</h3>', unsafe_allow_html=True)
st.write("---")  # Horizontal line
# Select Matter
st.subheader("Select Matter")
matters = ['DIG', 'Communi3']
selected_matter = st.selectbox("Matter", ["Select a Matter"] + matters)
data = load_data(selected_matter)

if selected_matter and selected_matter != "Select a Matter":
    # Select Element
    st.subheader("Select Element of the Claim")
    elements = [element["element"] for element in data["elements"]]
    selected_element = st.selectbox("Element", ["Select an Element"] + elements)

    if selected_element and selected_element != "Select an Element":
        # Add "Gather Evidence" button
        if st.button("Gather Evidence"):
            # Create a placeholder for the loading message
            placeholder = st.empty()
            for i in range(5):
                placeholder.write(f"Gathering evidence{'.' * (i + 1)}")
                time.sleep(0.5)
            
            # Clear the loading message
            placeholder.empty()
            
            st.write("---")  # Horizontal line

            st.header(f"{selected_matter}: {selected_element}")

            # Find the selected element data
            element_data = next(element for element in data["elements"] if element["element"] == selected_element)

            for index, fact in enumerate(element_data["facts"], 1):
                st.subheader(f"Fact {index}")
                st.write(fact["description"])

                st.markdown('<p class="small-header">Evidence</p>', unsafe_allow_html=True)
                tweet = fact["source"]
                # Convert timestamp to a more readable format
                timestamp = datetime.datetime.strptime(tweet["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
                readable_timestamp = timestamp.strftime("%B %d, %Y at %I:%M %p")
            
                st.markdown(f"""
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 10px; background-color: #f9f9f9;">
                        <strong>Tweet ID:</strong> {tweet["tweet_id"]}<br>
                        <strong>Username:</strong> @{tweet["username"]}<br>
                        <strong>Timestamp:</strong> {readable_timestamp}<br>
                        <strong>Text:</strong> {tweet["text"]}
                    </div>
                """, unsafe_allow_html=True)

                st.markdown('<p class="small-header">Explanation</p>', unsafe_allow_html=True)
                st.write(fact["explanation"])

                st.write("---")  # Horizontal line between facts