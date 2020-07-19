import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import plotly.express as ex
import numpy as np
matplotlib.use('Agg')

def main():
    ### common dataset explorer ###
    st.title("ML dataset explorer")
    st.subheader("Simple Data Science Explorer with dataset")

    html_temp=""" 
    <div style="background-color:tomato"><p>StreamLit App</p></div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    def file_selector(folder_path='./datasets'):
        filenames=os.listdir(folder_path)
        select_filenames=st.selectbox("Select a file",filenames)
        return os.path.join(folder_path,select_filenames)
    filename=file_selector()
    st.info("You have selected {}".format(filename))

    ## Read Data ##
    df=pd.read_csv(filename)
    ## Show Data ##
    if st.checkbox("Show Dataset"):
        number=st.number_input("Number of Rows",1,100)
        st.dataframe(df.head(number))
    ## Show columns ##
    if st.button("Columns Names"):
        st.write(df.columns)

    ## Show shape ##
    if st.checkbox("Shape of the dataset"):
        st.write(df.shape)
        datadim=st.radio("Show dimension by",("Rows","Columns"))
        if datadim=="Rows":
            st.write(df.shape[0])
        elif datadim=="Columns":
            st.write(df.shape[1])
        else:
            st.write(df.shape)

    ## Select columns ##
    if st.checkbox("Select columns to show"):
        all_columns=df.columns.tolist()
        selected_columns=st.multiselect("Select",all_columns)
        new_df=df[selected_columns]
        st.dataframe(new_df)
    ## Show values ##
    if st.button("Value counts"):
        st.text("Value Counts By Target")
        st.write(df.iloc[:,-1].value_counts())

    ## Show Datatypes ##
    if st.button("Data Types"):
        st.write(df.dtypes)
    ## Show summary ##
    if st.checkbox("Show the summary"):
        st.write(df.describe().T)

    ## Plot and Visulaization ##
    st.subheader("Data Visualization")
    ## Correlation
    ## seaborn plot
    if st.checkbox("Correlation plot"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
    ## count plot 
    if st.checkbox("Plot the value count"):
        st.text("Value counts by target")
        all_columns_names=df.columns.tolist()
        primary_col=st.selectbox("Primary columns to group by",all_columns_names)
        selected_columns_names=st.multiselect("Select column",all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot=df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot=df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()

    ## pie charts
    if st.checkbox("Pie plot"):
       all_columns=df.columns.tolist()
       if st.button("Generate plot"):
           st.success("Generating a pie plot")
           st.write(df.iloc[:,-1].value_counts().plot.pie()) 
           st.pyplot()
    
    
    ## customizable plot
    st.subheader("Customizable plots")
    all_columns=df.columns.tolist()
    type_of_plot=st.selectbox("Select type of plot",["area","bar","line","hist","box","kde"])
    selected_columns_names=st.multiselect("Select columns to plot",all_columns)

    if st.button("Generate plot"):
        st.success("Generating customizable plot of {} for {}".format(type_of_plot,selected_columns_names))
        
        if type_of_plot=='area chart':
            cust_data=df[selected_columns_names]
            st.area_chart(cust_data)
        elif type_of_plot=='bar chart':
            cust_data=df[selected_columns_names]
            st.bar_chart(cust_data)
        elif type_of_plot=='line chart':
            cust_data=df[selected_columns_names]
            st.line_chart(cust_data)
        elif type_of_plot:
            cust_plot=df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()




if __name__=='__main__':
    main()
