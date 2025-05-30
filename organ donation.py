import streamlit as st
import csv

st.title("Welcome to the Organ Donation Website. ")

option = st.radio(
    "Choose an option:",
    ('Donor', 'Receiver')
)

file_path = r"C:\Users\Dell\Desktop\strides\read.csv"

if option == 'Donor':
    st.write("Enter the details of the donor ")
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ('Male', 'Female', 'Other'))
    organ = st.selectbox("Select organ to donate", ('Eyes', 'Kidney', 'Heart', 'Liver'))
    diseases = st.text_input("Diseases")
    contact_number = st.text_input("Contact number")

    if st.button('Submit'):
        data = [name, gender, organ, diseases, contact_number]
        with open(file_path, 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        st.success("Data appended successfully.")

elif option == 'Receiver':
    st.write("Enter your requirements")
    organ_needed = st.selectbox("Which organ do you need?", ('Eyes', 'Kidney', 'Heart', 'Liver'))

    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        all_data = [row for row in reader]


    filtered_data = [row for row in all_data if row[2] == organ_needed]

    if len(filtered_data) > 0:
        st.write("The available donors for", organ_needed, "are:")
        st.table(filtered_data)
    else:
        st.write("No organ found.")