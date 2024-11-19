import streamlit as st

st.set_page_config(page_title="Column Information", page_icon="✨", layout="wide")

# Load CSS styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.markdown("<h1 class='custom-sub'>Column Information</h1>", unsafe_allow_html=True)
    
    # Access data from session state
    if 'data' in st.session_state:
        data = st.session_state.data
        
        # Column search option
        selected_columns = st.multiselect("Select columns to view", options=data.columns, default=data.columns)
        
        # Display data summary in a grid layout
        columns = st.columns(2)  # Create 2 columns
        col_index = 0  # Initialize column index
        
        for column in selected_columns:
            with columns[col_index]:
                with st.expander(f"{column}"):
                    dtype = data[column].dtype
                    num_unique = data[column].nunique()
                    total_rows = len(data)
                    is_categorical = num_unique <= 0.1 * total_rows and dtype == "object"
                    
                    st.write(f"**Data Type:** {dtype}")
                    st.write(f"**Null Values:** {data[column].isnull().sum()}")
                    
                    if is_categorical:
                        st.write(f"**Categorical Data:** Yes")
                        st.write(f"**Unique Values:** {num_unique}")
                    else:
                        st.write(f"**Categorical Data:** No")

                    st.write(data[column].head())    
            col_index = (col_index + 1) % 2  # Move to the next column, wrap around after 2 columns
    else:
        st.write("No data available.")

if __name__ == "__main__":
    main()