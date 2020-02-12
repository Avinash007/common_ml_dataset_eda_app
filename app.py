import streamlit as st
import os

# EDA packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import seaborn as sns

def main():
    """ Common ML dataset explorer
    """
    st.title("Common ML Dataset Explorer")
    st.subheader("Simple Data Science Explorer with Streamlit")

    html_temp = """
    <div style="background-color:tomato;"><p style="color:white; font-size:30px">Exploratory Data Analysis</p></div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    def file_selector(folder_path = "dataset"):
        filenames= os.listdir(folder_path)
        selected_filenames = st.selectbox("Select A file", filenames)
        return os.path.join(folder_path, selected_filenames)

    filename = file_selector()
    st.info("You have selected {}".format(filename))

    # Read Data
    df = pd.read_csv(filename)

    # Show Dataset
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of rows to views", 5,20)  # Dropdown with upper limit and lower limit
        st.dataframe(df.head(number))

    # Show columns
    if st.button("Show Columns"):
        st.write(df.columns)

    # Show Shape
    if st.checkbox("Shape of dataset"):
        
        data_dim = st.radio("Show Dimension By ",("Rows", "Columns"))
        if data_dim == 'Columns':
            st.text("Number of columns")
            st.write(df.shape[1])

        elif data_dim == 'Rows':
            st.text("Number of rows")
            st.write(df.shape[0])
        else:
            st.write(df.shape)

    
    # Select Columns
    if st.checkbox("Select Columns To Show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)
    
    # Show value counts
    if st.button("Value Counts"):
        st.text("Value Counts By Target/Class")
        st.write(df.iloc[:,-1].value_counts())

    # Show Data Types
    if st.button("Data Types"):
        st.write(df.dtypes)

    # Show Summary
    if st.checkbox("Summary"):
        st.write(df.describe())

    # Plot and Visualization

    st.subheader("Data Visualization")

    # Correlation Seaborn Plot

    if st.checkbox("Correlation Plot"):
        st.write(sns.heatmap(df.corr(), annot=True))
        st.pyplot()
    



    # Pie Chart
    if st.checkbox("Pie Plot of Label"):
        if st.button("Generate A Pie Plot"):
            st.success("Generating a pie plot")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

    # Customizable Plot

    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select type of plot", ["area", "bar", "line", "hist", "box", "kde"])
    selected_columns_names = st.multiselect("Select Columns to Plot", all_columns_names)
  
    if st.button("Generate Plot"):
        st.success("Generating a customizable plot of {} for {}".format(type_of_plot, selected_columns_names))

        if type_of_plot == "area":
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == "bar":
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == "line":
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        # Custom Plot

        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

    if st.button("Thanks"):
        st.balloons()

if __name__ == "__main__":
    main()
    