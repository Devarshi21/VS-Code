import streamlit as st

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
    st.title(' Loan Calculator -Devarshi')
    # Subheader
    st.subheader("Provide the Details below")
    # Getting P,N,R as input
    P = st.number_input("Principal (INR) : ", min_value=0.00, step=0.01)
    N = st.number_input("Number of Years : ", min_value=0.00, step=0.01)
    R = st.number_input("Rate of intrest : ", min_value=0.00, max_value=100.00, step=0.01)
    # Adding button to perform application
    butt = st.button("Calculate")
    # After butt is clicked
    if butt:
        emi, amt, I, perI = loanCalc(P,N,R)
        st.subheader("Calculated Loan Details")
        st.write(f"**EMI** : {emi:.0f} INR")
        st.write(f"**Amount** : {amt:.0f} INR")
        st.write(f"**Intrest** : {I:.0f} INR")
        st.write(f"**Percentage Intrest** : {perI:.2f} %")




# Main application 
if __name__ == "__main__":
    application()
