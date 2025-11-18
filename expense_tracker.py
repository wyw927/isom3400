import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expanse Tracker")

if 'expenses' not in st.session_state:
  st.session_state.expenses = pd.DataFrame(columns=['Date','Category','Description'])

with st.form("expenses_form"):
  st.subheader("Add New Expenses")
  date = st.date_input("Date")
  category = st.selectbox("Category",["Food","Transport","Entertainment","Bill","Other"]
  amount = st.number_input("Amount",min_value=0.0,step=0.01) #max_value
  description = st.text_input("Description")


  submitted = st.form_submit_button("Add Expanse")
  if submitted :
    new_expense = pd.DataFrame({
      'Date':[date],
      'Category':[category],
      'Amount':[amount],
      'Description':[description]
    })
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense),ignore _index=True)
    st.success("Expanse added successfully!")


if not st.session_state.expenses.empty:
  st.subheader("Your Expanse")
  st.dataframe(st.session_state.expanses)

  st.subheader("Summary")
  total_spent = st.session_state.expenses['Amount'].sum()
  st.write(f"Total Spent: ${total.spent:.2f}")

  category_totals = st.session_state.expenses.groupby('Category')['Amount'].sum()
  
  fig,ax = plt.subplots(figsize=(10,6))
  ax.pie(category_totals.value, labels=category_totals.index, autopct='%1.1f%%')
  ax.set_title("Expenses by Category")
  st.pyplot(fig)
else:
  st.info("No expenses recordes")
