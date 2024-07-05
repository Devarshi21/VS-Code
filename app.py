import streamlit as st
import pandas as pd
import plotly.express as px
from warnings import filterwarnings
filterwarnings('ignore')

def loanCalc(P,N,R):
    # Converting years to months
    n = N*12
    r = R/1200

    #Calculating EMI
    x = (1+r)**n
    emi = P*r*x/(x-1)

    #Calculating Amount
    amt = emi*n

    # Calculating intrest
    I = amt - P
    
    #Calculating percent Intrest
    perI = (I/amt)*100

    return emi, amt, I, perI


# Creating the web application
def application():
    # Header of appliaction
    st.set_page_config(page_title="Loan Calculator  - Devarshi")
    # Show Application Title
    st.title(' Loan Calculator by Devarshi')
    st.subheader("Input Data")

    # Getting P,N,R as input
    col1, col2, col3 = st.columns(3)
    P = col1.number_input("Principal (INR) ", min_value=0, value=1000000)
    N = col2.number_input("Number of Years", min_value=0, value=5)
    R = col3.number_input("Rate of intrest", min_value=0.00, max_value=100.00, value=5.5)

    # Adding button to perform application
    butt = st.button("Calculate")

    # After butt is clicked
    if butt:
        emi, amt, I, perI = loanCalc(P,N,R)

        col1, col2 = st.columns(2)
        col1.metric(label="Monthly EMI", value=f"Rs {emi:,.0f}")
        col1.metric(label="Total Intrest", value=f"Rs {I:,.0f}")
        col1.metric(label="Total Amount", value=f"Rs {amt:,.0f}")
        
        # Creatig Visuals
        d = {"details":["Principal","Intrest"],
             "values": [P, I]}
        df = pd.DataFrame(d)
        fig = px.pie(data_frame=df, names="details", values="values", color_discrete_sequence=["green", "orange"])
        col2.plotly_chart(fig)



# Main application 
if __name__ == "__main__":
    application()
