import git
import os
import pandas as pd
import json
import requests
import mysql.connector
from PIL import Image
import plotly.express as px

import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="phonepe")
mycursor = mydb.cursor(buffered=True)


img = Image.open("C:\\PhonepeProject\\phonepelogo.png")
st.set_page_config(page_title="PhonePe Pulse", page_icon=img, layout="wide", )

SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Top Charts"],
    icons =["book","house","toggles","bar-chart"],
    default_index=2,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white","size":"cover"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"},}
    )

if SELECT == "About":
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("")
        st.markdown("") 
        st.markdown("")
        st.markdown("")
        st.markdown("")              
        st.video("C:\PhonepeProject\pulse-video.mp4")
    with col2:
        st.image(Image.open("C:\PhonepeProject\phonepelogo.png"),width = 200)
        #st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    st.write("---")
    st.title("THE BEAT OF PHONEPE")
    col1,col2 = st.columns(2)    
    with col1:        
        st.write("---")
        st.subheader("Third ET BFSI Innovation Tribe Virtual Summit & Awards")
        st.image(Image.open("C:\PhonepeProject\Award.jpeg"),width = 500)
    with col2:
        st.write("---")
        st.subheader("Phonepe became a leading digital payments company")
        st.image(Image.open("C:\\PhonepeProject\\top.jpeg"),width = 500)

if SELECT == "Home":
    col1,col2, = st.columns(2)
    col1.image(Image.open("C:\PhonepeProject\phonepelogo.png"),width = 500)
    with col1:
        st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video("C:\\PhonepeProject\\upi.mp4")

if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "1.Top 10 states based on year and amount of transaction",
               "2.Least 10 states based on type and amount of transaction",
               "3.Top 10 mobile brands based on percentage of transaction",
               "4.Least 10 mobile brands based on percentage of transaction",
               "5.Top 10 Registered-users based on States and District",
               "6.Least 10 registered-users based on Districts and states",
               "7.Top 10 Districts based on states and amount of transaction",
               "8.Least 10 Districts based on states and amount of transaction",
               "9.Top 10 Districts based on states and App_opens",
               "10.Least 10 Districts based on states and App_opens"]
    select = st.selectbox("Select the option",options)
                  
    if select=="1.Top 10 states based on year and amount of transaction":
        mycursor.execute("SELECT DISTINCT State, Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_transaction_district GROUP BY State, Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','Year','Transaction_amount'])
        st.subheader("Top 10 states based on type and amount of transaction")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['State'], df['Transaction_amount'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)
        
    elif select=="2.Least 10 states based on type and amount of transaction":
        mycursor.execute("SELECT DISTINCT State, SUM(Transaction_count) as Total FROM top_transaction_district GROUP BY State ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','Transaction_amount'])
        st.subheader("Least 10 states based on type and amount of transaction")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['State'], df['Transaction_amount'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)

    elif select=="3.Top 10 mobile brands based on percentage of transaction":
        mycursor.execute("SELECT DISTINCT User_brand,SUM(User_percentage) as Total_Percentage FROM aggregated_users GROUP BY User_brand ORDER BY Total_Percentage DESC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['brands','Percentage'])
        st.subheader("Top 10 mobile brands based on percentage of transaction")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['brands'], df['Percentage'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)

    elif select=="4.Least 10 mobile brands based on percentage of transaction":
        mycursor.execute("SELECT DISTINCT User_brand,SUM(User_percentage) as Total_Percentage FROM aggregated_users GROUP BY User_brand ORDER BY Total_Percentage ASC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['brands','Percentage'])
        st.subheader("Least 10 mobile brands based on percentage of transaction")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['brands'], df['Percentage'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)
       
    elif select=="5.Top 10 Registered-users based on States and District":
        mycursor.execute("SELECT DISTINCT State,District,SUM(Registered_user) as Users FROM top_users_district GROUP BY State,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Registered_user'])
        st.subheader("Top 10 Registered-users based on States and District")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['District'], df['Registered_user'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)
        
    elif select=="6.Least 10 registered-users based on Districts and states":
        mycursor.execute("SELECT DISTINCT State,District,SUM(Registered_user) as Users FROM top_users_district GROUP BY State,District ORDER BY Users ASC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Registered_user'])
        st.subheader("Least 10 registered-users based on Districts and states")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['District'], df['Registered_user'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)
        
    elif select=="7.Top 10 Districts based on states and amount of transaction":
        mycursor.execute("SELECT DISTINCT State,District,SUM(Transaction_amount) as Total FROM top_transaction_district GROUP BY State,District ORDER BY Total DESC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Transaction_amount'])
        st.subheader("Top 10 Districts based on states and amount of transaction")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['District'], df['Transaction_amount'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)
        
    elif select=="8.Least 10 Districts based on states and amount of transaction":
        mycursor.execute("SELECT DISTINCT State,District,SUM(Transaction_amount) as Total FROM top_transaction_district GROUP BY State,District ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Transaction_amount'])
        st.subheader("Least 10 Districts based on states and amount of transaction")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['District'], df['Transaction_amount'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)
            
    elif select=="9.Top 10 Districts based on states and App_opens":
        mycursor.execute("SELECT DISTINCT State,District,SUM(App_opens) as Total FROM map_users GROUP BY State,District ORDER BY Total DESC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','App_opens'])
        st.subheader("Top 10 Districts based on states and App_opens")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['District'], df['App_opens'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)


    elif select=="10.Least 10 Districts based on states and App_opens":
        mycursor.execute("SELECT DISTINCT State,District,SUM(App_opens) as Total FROM map_users GROUP BY State,District ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','App_opens'])
        st.subheader("Top Least Districts based on states and App_opens")
        tab1,tab2 = st.tabs(["$\ ANALYSIS $", "$\ BARCHART $"])
        with tab1:
            st.write(df)
        with tab2:
            plt.figure(figsize=(10, 6)) 
            plt.bar(df['District'], df['App_opens'])
            plt.xticks(rotation=45) 
            st.pyplot(plt)

if SELECT == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        
# Top Charts - TRANSACTIONS    
    if Type == "Transactions":        
        tab1,tab2,tab3 = st.tabs(["$\huge State $", "$\huge District $","$\huge Pincode $"])
        
        with tab1:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select State, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from aggregated_transaction where year = {Year} and quarter = {Quarter} group by State order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='State',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with tab2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District , sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total from map_transaction where year = {Year} and quarter = {Quarter} group by District order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                                names='District',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_count'],
                                labels={'Transactions_count':'Transactions_count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with tab3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincode, sum(Transaction_count) as Total_Transactions_count, sum(Transaction_amount) as Total from top_transaction_pincode where year = {Year} and quarter = {Quarter} group by Pincode order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_count','Transaction_amount'])
            fig = px.pie(df, values='Transaction_amount',
                                names='Pincode',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_count'],
                                labels={'Transactions_count':'Transactions_count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

    # Top Charts - USERS          
    if Type == "Users":
        tab1,tab2,tab3,tab4 = st.tabs(["$\huge Brand $", "$\huge District $","$\huge Pincode $","$\huge State $"])
        
        with tab1:
            st.markdown("### :violet[Brands]")
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                mycursor.execute(f"select User_brand, sum(user_count) as Total_Count, avg(user_percentage)*100 as Avg_Percentage from aggregated_users where year = {Year} and quarter = {Quarter} group by user_brand order by Total_Count desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                fig = px.bar(df,
                                title='Top 10',
                                x="Total_Users",
                                y="Brand",
                                orientation='h',
                                color='Avg_Percentage',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)   

        with tab2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_users where year = {Year} and quarter = {Quarter} group by District order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                            title='Top 10',
                            x="Total_Users",
                            y="District",
                            orientation='h',
                            color='Total_Users',
                            color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
                
        with tab3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincode, sum(Registered_user) as Total_Users from top_users_pincode where year = {Year} and quarter = {Quarter} group by Pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                            values='Total_Users',
                            names='Pincode',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with tab4:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select State, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_users where year = {Year} and quarter = {Quarter} group by State order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                                names='State',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Total_Appopens'],
                                labels={'Total_Appopens':'Total_Appopens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)    
            

        