import streamlit as st
from datetime import datetime

def determine_engagement(user_id, interaction_score):
    """Determine if a user is at risk and generate a notification."""
    if interaction_score < 0.5:
        notification_type = "Email" if interaction_score >= 0.3 else "SMS"
        message = (
            "Hey there! We noticed you haven’t visited in a while. "
            "Check out our latest offers just for you!" if notification_type == "Email" 
            else "Come back and enjoy exclusive discounts on your favorite items!"
        )
    else:
        notification_type = "None"
        message = "User is engaged, no notification needed."
    
    return notification_type, message

# Streamlit UI
st.title("📢 Churn Risk-Based Customer Engagement System")
st.write("Enter customer details to determine engagement status and send retention notifications.")

# User Inputs
user_id = st.text_input("User ID")
interaction_score = st.slider("Interaction Score (0-1)", 0.0, 1.0, 0.5)

if st.button("Check Engagement Status"):
    notification_type, message = determine_engagement(user_id, interaction_score)
    
    st.subheader("📊 Engagement Status")
    st.write(f"**User ID:** {user_id}")
    st.write(f"**Notification Type:** {notification_type}")
    st.write(f"**Message:** {message}")
