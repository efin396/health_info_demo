import streamlit as st

def patient_risk_assessment():
    st.title("Patient Risk Assessment")
    patient = st.session_state.get("selected_patient")
    
    if not patient:
        st.error("No patient selected. Please return to the search page.")
        if st.button("Back to Search"):
            st.switch_page("pages/search.py")
        return

    st.header(f"Patient: {patient['name']}")
    
    st.markdown("### Risk Factors")
    # Example risk factors (this might come from a database or model in a real app)
    risk_factors = ["Age > 65", "Smoking", "Diabetes", "Hypertension"]
    for factor in risk_factors:
        st.markdown(f"- {factor}")

    st.markdown("### Overall Risk Assessment")
    st.info("High Risk")

    # A button to return to the search page
    if st.button("Back to Search"):
        st.switch_page("pages/search.py")

patient_risk_assessment()