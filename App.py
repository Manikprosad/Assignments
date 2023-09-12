# Display the loaded data as a table
st.write("### Data Preview")
st.write(data)

# Add filters to explore the data
selected_province = st.selectbox("Select a Province:", data["GEO"].unique())
filtered_data = data[data["GEO"] == selected_province]

# Visualize data based on user selection
st.write("### Unemployment Rate Over Time")
st.line_chart(filtered_data.groupby("REF_DATE")["Unemployment rate"].mean())

st.write("### Employment Rate Over Time")
st.line_chart(filtered_data.groupby("REF_DATE")["Employment rate"].mean())
