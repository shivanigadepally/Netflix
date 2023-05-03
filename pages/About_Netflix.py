import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from st_btn_select import st_btn_select

st.set_page_config(layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

data=load_data("prices.csv")
subscription = load_data("Netflix Subscriber.csv")
revenue = load_data("Netflix Revenue.csv")


st.header("About the Netflix")

page = st_btn_select(
  # The different pages
  ('Netflix subscription and Revenue', 'Netflix Prices', 'Conclusion'),
  # Enable navbar
  nav=False
)

if page == 'Netflix subscription and Revenue':
    tab1, tab2 = st.tabs(['Netflix Subscribers','Netflix Revenue'])
    
    with tab1:
        line_chart = alt.Chart(subscription).mark_line(color='Purple').encode(
        x='Years',
        y='Subscribers'
        ).properties(
        width=700,
        height=600
        )
        st.altair_chart(line_chart, use_container_width=True)    
        st.write("Netflix has become a household name across the globe since its inception in 1997. One of the reasons for its immense popularity is its vast number of subscribers. One of the factors that have contributed to the growth in the number of Netflix subscribers is its original content. Over the years, Netflix has invested heavily in producing original content, including TV shows and movies, that are exclusive to its platform. This has given subscribers a reason to stay subscribed to the platform, as they have access to content that they cannot find anywhere else. One of the factors that have contributed to the growth in the number of Netflix subscribers is its original content. Over the years, Netflix has invested heavily in producing original content, including TV shows and movies, that are exclusive to its platform. This has given subscribers a reason to stay subscribed to the platform, as they have access to content that they cannot find anywhere else. Over the last 2.5 years. According to the final month of the quarter 2020(March) was being the start of the global coronavirus pandemic in many countries, Netflix noted that it added 26 million paid new subscribers in the first two quarters of 2020 alone; in 2019, the company added 28 million subscribers in total.")

    with tab2:
        clist = revenue['Area'].unique()
        area = st.selectbox("Select a Region:",clist)

        df = revenue[revenue['Area'] == area]
        df['Quarter'] = df['Years'].str.split(' - ').str[0]

        ASV_Chart = alt.Chart(df,title = 'Revenue of Netflix', height= 600, width= 700).mark_bar().encode(
            #x = alt.X('Years', sort=alt.EncodingSortField('Revenue', order='ascending')),
            x='Years',
            y = 'Revenue',
            color='Quarter'
            ).interactive()
        st.altair_chart(ASV_Chart)
        st.write('')
        st.write('In 2018, Netflix had a total revenue of $15.79 billion. In 2019, Netflix revenue increased to $20.16 billion, which represents a growth rate of 27.6 percent from the previous year.  In 2020, Netflix revenue grew even further to $24.99 billion, a growth rate of 24 percent from the previos year. The above graph shows the revenuw in terms of quaters of that particular year. The revenue have always been increased from previous quater and the graph shows data specific to the region.')

if page == 'Netflix Prices':

    #st.markdown("<h1 style='text-align: center;'>Netflix </h1>", unsafe_allow_html=True)
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
    
    sort_options = ['Cost Per Month - Basic ($)', 'Cost Per Month - Standard ($)', 'Cost Per Month - Premium ($)']
    sort_by = st.selectbox('Sort by:', sort_options)
    data_sorted = data.sort_values(by=sort_by)
    fig = px.bar(data_sorted, x="Country", y=["Cost Per Month - Basic ($)", "Cost Per Month - Standard ($)", "Cost Per Month - Premium ($)"])
    fig.update_layout(width=900, height=500, title='Netflix usage in 2021',
                  xaxis_title='Country',
                  yaxis_title='Cost per month')
    st.write(fig)
    st.write('Netflix prices vary across different countries, with the prices influenced by a variety of factors such as the economic conditions, competition, and regulatory policies. Netflix offers three pricing tiers: the basic plan, the standard plan and and the premium plan. The above shows the most and least paying countries and can be sorted according to the plan and see which country pays the most.')

if page == 'Conclusion':
    st.write("Netflix has revolutionized the entertainment industry by providing users with a convenient and affordable way to access a vast library of content. With its emphasis on original programming and innovative use of technology, Netflix is poised to continue to be a major player in the streaming industry for years to come.")
    
    link ='To have more information about the Netflix use this [link](https://www.comparitech.com/blog/vpn-privacy/countries-netflix-cost/)'
    st.markdown(link,unsafe_allow_html=True)