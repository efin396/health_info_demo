import streamlit as st

# Example patient data
PATIENTS = [
    {"name": "John Doe", "id": "JD001"},
    {"name": "Jane Smith", "id": "JS002"},
    {"name": "Mike Brown", "id": "MB003"},
]

def patient_search():
    st.title("Patient Search")
    query = st.text_input("Search for a patient by name")
    
    # Only filter if a query is provided, otherwise no results
    if query:
        results = [p for p in PATIENTS if query.lower() in p["name"].lower()]
    else:
        results = []
    
    # Display results only if there is a search query
    if query:
        if results:
            st.markdown("### Results")
            for patient in results:
                # Create a button for each patient
                if st.button(patient["name"], key=patient["id"]):
                    st.session_state["selected_patient"] = patient
                    name = patient["name"].replace(" ", "")
                    st.switch_page("pages/" + name + ".py")
        else:
            st.info("No patients found. Try a different search query.")
    else:
        st.info("Enter a patient name to search.")

patient_search()
