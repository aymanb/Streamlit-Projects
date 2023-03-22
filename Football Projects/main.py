# Import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# App title
st.title('Karim Benzema Career with Real Madrid')

# Read CSV data, set Season column as an index
df = pd.read_csv("Benzema_RM.csv").set_index('Season')


# Select columns to plot
selected_columns = st.multiselect('Select columns', list(df.columns), list(df.columns))
xlabel = st.text_input('Enter X label') #you can update the lable of the plot
ylabel = st.text_input('Enter Y label') #you can update the lable of the plot

# Create bar plot
fig, ax = plt.subplots()
df[selected_columns].plot.bar(ax=ax)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Display plot
st.pyplot(fig)

# Display DataFrame with all columns
with st.expander('Show Original DataFrame'):
    st.write(df)
# Display Dataframe base on the selected_columns variable
with st.expander('Show Updated DataFrame'):
    st.write(df[selected_columns])