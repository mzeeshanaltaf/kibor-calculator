import streamlit as st
from util import *

# Page configuration options
page_title = "FAQs"
page_icon = "💬"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide", initial_sidebar_state="expanded")

st.title('FAQs')

expand_all = st.toggle("Expand all", value=True)

# Display footer in the sidebar
display_footer()

kibor_periods = """
    <table border="1">
    <tr>
        <th>Start Date</th>
        <th>End Date</th>
        <th>Kibor Rate</th>
    </tr>
    <tr>
        <td>26-Nov-2023</td>
        <td>10-Jun-2024</td>
        <td>22.0%</td>
    </tr>
    <tr>
        <td>11-Jun-2024</td>
        <td>29-Jul-2024</td>
        <td>20.5%</td>
    </tr>
    <tr>
        <td>30-Jul-2024</td>
        <td>12-Sep-2024</td>
        <td>19.5%</td>
    </tr>
    <tr>
        <td>13-Sep-2024</td>
        <td>4-Nov-2024</td>
        <td>17.5%</td>
    </tr>
    <tr>
        <td>5-Nov-2024</td>
        <td>16-Dec-2024</td>
        <td>15.0%</td>
    </tr>
    <tr>
        <td>17-Dec-2024</td>
        <td>27-Jan-2025</td>
        <td>13.0%</td>
    </tr>
    <tr>
        <td>28-Jan-2025</td>
        <td>6-Feb-2025</td>
        <td>12.0%</td>
    </tr>
</table>
"""

faq_data = {
        'What this Application is about?':
            '<p>A web app that helps vehicle buyers in Pakistan calculate the compensation they are entitled to if their '
            'car delivery is delayed beyond 60 days.</p>',

        'Are there any guidelines/regulations from Government regarding compensation for delayed delivery?':
            '<p>Yes, as per Auto Industry Development and Export Policy (AIDEP), vehicle manufacturer will pay compulsory '
            'payment of KIBOR + 3% interest on initial deposited amount in case of deliver beyond 60 days. For details, '
            'refer to Sr. No 4 of the <a href="https://engineeringpakistan.com/wp-content/uploads/2021/12/AIDEP-Incentives-Final-221221-modified.pdf">AIDEP</a> policy.',

        'What is the KIBOR?':
            "KIBOR stands for Karachi Interbank Offered Rate. It is the benchmark interest rate at which banks in "
            "Pakistan offer to lend unsecured funds to other banks in the Karachi interbank market. KIBOR is a key "
            "financial indicator used in Pakistan's banking and financial sector.",

        'What KIBOR rate is used to calculate the compensation?':
            f"As KIBOR rate kept changing throughout the year, so appropriate KIBOR rate will be used "
            f"as mentioned in the table.If the time span covers multiple periods, different KIBOR rates will be "
            f"applied proportionally based on the number of days in each period. Additionally, a 3% extra charge is "
            f"added to the applicable KIBOR rate to determine the final compensation amount."
            f"{kibor_periods}",

        'I want to make modification in the application. Can I get the application source code?':
            '<p>Yes, Source code of this application is available at: '
            '<a href="https://github.com/mzeeshanaltaf/kibor-calculator">GitHub</a></p>',

    }

# Display expandable boxes for each question-answer pair
for question, answer in faq_data.items():
    with st.expander(r"$\textbf{\textsf{" + question + r"}}$", expanded=expand_all):  # Use LaTeX for bold label
        st.markdown(f'<div style="text-align: justify;"> {answer} </div>', unsafe_allow_html=True)