import streamlit as st
from util import *

# Page title of the application
page_title = "AutoCompensate"
page_icon = "🚗"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Application Title and description
st.title(f'{page_title}🚗💰')
st.write('***:blue[Get Paid for Delays! ⏳💵]***')
st.write("""
*AutoCompensate is a web app that helps vehicle buyers in Pakistan calculate the compensation they are entitled to if 
their car delivery is delayed beyond 60 days. Simply enter your deposit amount, deposit date, and delivery date, 
and the app will compute the amount the company owes you based on the KIBOR rate + 3%. 🚘📅💲*
""")

# Display footer in the sidebar
display_footer()

# Configuration options
st.header('Configuration⚙️:', divider="gray")
st.subheader('Booking Type📝')
payment_option = st.radio('**Booking Type:**', ['Partial Payment Booking', 'Full Payment Booking'], horizontal=True,
                          label_visibility="collapsed")

# Default dates
jan_1_2024 = datetime.date(2024, 1, 1)
oct_1_2024 = datetime.date(2024, 10, 1)
oct_1_2023 = datetime.date(2023, 10, 1)

# Configuration options and compensation calculation if user selects partial payment
if payment_option == 'Partial Payment Booking':
    st.subheader('Payment Amount and Dates💳📅')
    col1, col2 = st.columns(2, border=True)
    with col1:
        pp_amount = st.number_input('Partial Payment Amount:', min_value=0, max_value=10_000_000, value=2_500_000,
                                    step=100_000, placeholder="Enter the Partial Payment Amount ...")
        pp_date = st.date_input('Partial Payment Date:', value=jan_1_2024, max_value="today", key='partial')
    with col2:
        rp_amount = st.number_input('Remaining Payment Amount:', min_value=0, max_value=10_000_000, value=5_890_000, step=100_000,
                                    placeholder="Enter the Remaining Payment Amount ...")
        rp_date = st.date_input('Remaining Payment Date:', value=oct_1_2024, max_value="today", key='remaining')
    st.subheader('Vehicle Delivery Date📅')
    vd_date = st.date_input('Vehicle Delivery Date:', value="today", max_value="today", key='vehicle_partial_payment')
    calculate = st.button('Calculate', type='primary', icon=":material/calculate:", key='button_partial_payment')
    if calculate:
        if pp_amount is None or rp_amount is None:
            st.warning('Enter the Partial or Remaining Payment Amount!', icon=":material/warning:")
        else:
            compensation = calculate_compensation_with_partial_payments(pp_amount, pp_date, rp_amount, rp_date, vd_date)
            compensation = round(compensation)  # Round to nearest integer

            st.subheader('Total Compensation💰')

            if compensation == -1:
                output = ":blue[*No delay in delivery, no compensation required.*]"
                st.write(output)
            else:
                st.write(":blue[*Company owes approximately the following amount to you for delayed delivery:*]")
                st.metric('Compensation Amount', value=f"PKR {compensation:,}/=", label_visibility="collapsed")
                disclaimer()

# Configuration options and compensation calculation if user selects full payment
if payment_option == 'Full Payment Booking':
    st.subheader('Payment Amount and Dates💳📅')
    fp_amount = st.number_input('Full Payment Amount:', min_value=0, max_value=10_000_000, value=8_390_000, step=100_000,
                                placeholder="Enter the Full Payment Amount ...")
    fp_date = st.date_input('Full Payment Date:', value=jan_1_2024, max_value="today", min_value=oct_1_2023,
                            key='full')

    st.subheader('Vehicle Delivery Date📅')
    vd_date = st.date_input('Vehicle Delivery Date:', value="today", max_value="today", min_value=fp_date,
                            key='vehicle_full_payment')
    calculate = st.button('Calculate', type='primary', icon=":material/calculate:", key='button_full_payment')

    if calculate:
        if fp_amount is None:
            st.warning('Enter the Full Payment Amount!', icon=":material/warning:")
        else:
            compensation = calculate_compensation_full_payment(fp_amount, fp_date, vd_date)
            compensation = round(compensation) # Round to nearest integer

            st.subheader('Total Compensation💰')

            if compensation == -1:
                output = ":blue[*No delay in delivery, no compensation required.*]"
                st.write(output)
            else:
                st.write(":blue[*Company owes approximately the following amount to you for delayed delivery:*]")
                st.metric('Compensation Amount', value=f"PKR {compensation:,}/=", label_visibility="collapsed")
                disclaimer()
