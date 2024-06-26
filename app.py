import streamlit as st

st.set_page_config(page_title= f"Russell Whealdon Data Portfolio",page_icon="🧑‍🚀",layout="wide")
st.markdown(f"<h1 style='text-align: center; color: white;'>Russell Whealdon Data Portfolio</h1>", unsafe_allow_html=True)

#Set background image for page
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://source.unsplash.com/blue-sky-and-white-clouds-b8dA3eY5VrY");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Page navigation
st.sidebar.markdown(f"<h4 style='text-align: center; color: white;'>Navigation</h4>", unsafe_allow_html=True)
url_home = "https://russellwhealdonportfolio.streamlit.app/"
url_resume = "https://russellwhealdonportfolio-resume.streamlit.app/"
url_hobbies = "https://russellwhealdonportfolio-hobbies.streamlit.app/"
st.sidebar.markdown(f"<h4><a href='{url_home}' target='_blank'>Home</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown(f"<h4><a href='{url_resume}' target='_blank'>Resume</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown(f"<h4><a href='{url_hobbies}' target='_blank'>Hobbies</a></h4>", unsafe_allow_html=True)

### links ###
#if option == 'Home':
#elif option == 'About':
#elif option == 'Contact':

### Set sidebar background ###
sidebar_bg_img = """
<style>
[data-testid="stSidebar"] {
    background-image: url("https://source.unsplash.com/blue-sky-and-white-clouds-b8dA3eY5VrY");
    background-size: cover;
}
</style>
"""

# Inject CSS with Markdown
st.markdown(sidebar_bg_img, unsafe_allow_html=True)

st.markdown(f"<p style='text-align: center; color: white;'>Hi! I'm Russell Whealdon and this my Data portfolio that holds a wide range of interesting Analytics, Machine Learning, and AI related projects. I'm currently a Data Analyst working at an Ad Agency specializing in modeling and data infrastructure. In here you will also find projects from my Masters in Business Analytics program. I hope you find it interesting and would love to hear from you. Please reach out to me directly or connect on Linkedin. Cheers!</p>", unsafe_allow_html=True)

with st.container():
  st.markdown(f"<h2 style='text-align: left; color: white;'>Skills</h2>", unsafe_allow_html=True)
  st.write("")
  col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
  with col1:
    st.write("")
  with col2:
    st.image("images/icons8-python-48.png")
  with col3:
    st.image("images/icons8-mysql-48.png")
  with col4:
    st.image("images/icons8-tableau-software-48.png")
  with col5:
    st.image("images/icons8-google-cloud-48.png")
  with col6:
    st.image("images/Databrickslogo.png")
  with col7:
    st.write("")

with st.container():
    st.markdown(f"<h2 style='text-align: left; color: white;'>Recent Projects</h2>", unsafe_allow_html=True)
    
    ###### CA Wildfire Proj.
    url_WF = "https://russell-whealdon-portfolio-ca-wildfire-analysis.streamlit.app/"
    st.markdown(f"<h4><a href='{url_WF}' target='_blank'>California Wildfire Damage Analysis</a></h4>", unsafe_allow_html=True)    
    st.markdown(f"<p style='text-align: left; color: white;'>This dashboard presents an analysis of the economic impacts of wildfires, developed in collaboration with Deloitte's sustainability arm. The project aims to understand and predict the financial damages caused by wildfires, leveraging data on various environmental and economic factors. The predictive modeling was done using an XGBoost regression model, enhanced with SHAP and LIME for model interpretability.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>Key Skills Displayed:</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        ul.white-text-list {
        color: white;          /* Set the text color to white */
        padding: 10px;         /* Optional: some padding */
        }
    </style>
    <ul class='white-text-list'>
        <li>Data Cleaning w/ Python - Joined multiple datasets, cleaned data, made transformations, and prepped data for modeling</li>
        <li>Data Analysis - Data exploration w/ numpy, correlation analysis, time series, geo mapping</li>
        <li>Machine Learning - Built and tuned XGBoost Model, used multiple forms of feature importance, interpreted model results</li>
        <li>Collaboration with Stakeholders/Communicated Results - Regularly met with reps from Delloite and then presented results to team</li>
    </ul>
    """, unsafe_allow_html=True)

    ###### Reporting Dash Proj.
    url_MLDash = "https://accountoverviewdash-dummydata.streamlit.app/"
    st.markdown(f"<h4><a href='{url_MLDash}' target='_blank'>Reporting Dashboard w/ Custom Visuals using direct BigQuery connection</a></h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>This dashboard uses custom python to create visualizations and metrics for account manager reporting.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>Key Skills Displayed:</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    ul.white-text-list {
    color: white;          /* Set the text color to white */
    padding: 10px;         /* Optional: some padding */
    }
    </style>
    <ul class='white-text-list'>
      <li>Data Visualization w/ Python - Joined multiple datasets, cleaned data, made transformations, and prepped data for modeling</li>
      <li>BigQuery API Connection - Used custom SQL to efficiently pull data from database to create streamlined process for reporting</li>
    </ul>
    """, unsafe_allow_html=True)

    ###### Text Analytics Proj.
    url_TAproj = "https://russell-whealdon-portfolio-textanalytics.streamlit.app/"
    st.markdown(f"<h4><a href='{url_TAproj}' target='_blank'>Text Analytics Movie Review Dashboard using TMID Database</a></h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>This dashboard uses a multiple TMDB API connections to pull in various information about movies and what people are saying about them. It also includes a recommendation system based on movies peole like.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>Key Skills Displayed:</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    ul.white-text-list {
    color: white;          /* Set the text color to white */
    padding: 10px;         /* Optional: some padding */
    }
    </style>
    <ul class='white-text-list'>
      <li>External API connection & mangagement - Used best practices to ensure proper function and health of APIs</li>
      <li>Data Wrangling w/ Python - Used python to clean and process text data to allow for easier analysis and modeling</li>
      <li>Text Data Modeling w/ Spacy and Recmetrics - Use of Open Source Packages to create Recommendation System</li>
    </ul>
    """, unsafe_allow_html=True)


with st.container():
    st.markdown(f"<h2 style='text-align: left; color: white;'>Tableau Projects</h2>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: left; color: white;'>Period over Period Comparison Dashboard</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>This dashboard uses LOD expressions and dynamic parameters to quickly allow account managers to switch between key metrics to see both period over period statistics and custom visuals.</p>", unsafe_allow_html=True)
    st.image("images/TableauPoPChart.gif")
    st.write("    ")
    st.write("    ")
    st.markdown(f"<h4 style='text-align: left; color: white;'>Keyword Analysis Dashboard</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>This dashboard uses processed text data (handled outside tableau) to display performance of keyword campaigns and spend.</p>", unsafe_allow_html=True)
    st.image("images/TableauKeywordDash2.gif")

    st.write("    ")
    st.write("    ")
    st.markdown(f"<h4 style='text-align: left; color: white;'>Creative Testing and Response Rate Dashboard</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>This dashboard uses a variety of visuals to show how well each creative campaign is performing in comparison to it's cost.</p>", unsafe_allow_html=True)
    st.image("images/DatacampTableauDash.png")
