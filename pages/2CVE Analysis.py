import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
data_path = r'C:\Users\pradeep dubey\Desktop\NLP_Project\Data\cve_data_cleaned.csv'
df = pd.read_csv(data_path)

# Convert datetime columns to datetime objects
df['Published_Date'] = pd.to_datetime(df['Published_Date'], utc=True)
df['Last_Modified_Date'] = pd.to_datetime(df['Last_Modified_Date'], utc=True)

# Streamlit Sidebar for date selection
st.sidebar.title("🔍 CVE Vulnerability Analysis")

start_date = st.sidebar.date_input("Select start date 📅", value=pd.to_datetime("2021-01-01").date(),
                                   min_value=pd.to_datetime("2010-01-01").date(),
                                   max_value=pd.to_datetime("2030-12-31").date())
end_date = st.sidebar.date_input("Select end date 📅", value=pd.to_datetime("2021-12-31").date(),
                                 min_value=pd.to_datetime("2010-01-01").date(),
                                 max_value=pd.to_datetime("2030-12-31").date())

if not start_date or not end_date:
    st.write("Please enter both the start date and end date to view the analysis.")
else:
    # Filter the dataset based on the selected dates
    filtered_df = df[(df['Published_Date'] >= pd.to_datetime(start_date, utc=True)) & 
                     (df['Published_Date'] <= pd.to_datetime(end_date, utc=True))]

    # Check if filtered data is empty
    if filtered_df.empty:
        st.write(f"No data available between {start_date} and {end_date}. Please select a different date range.")
    else:
        st.markdown("### 📊 Dataset Overview")
        st.write(f"**{len(filtered_df)}** entries between {start_date} and {end_date}")

        # Group by 'Published_Date' and count vulnerabilities per month
        time_df = filtered_df.groupby(filtered_df['Published_Date'].dt.to_period('M')).size().reset_index(name='Count')

        # Convert Period to string for Plotly compatibility
        time_df['Published_Date'] = time_df['Published_Date'].astype(str)

        # Plot the time series
        fig = px.line(time_df, x='Published_Date', y='Count', title='Vulnerabilities Published Over Time',
                      labels={'Published_Date': 'Month', 'Count': 'Number of Vulnerabilities'}, markers=True)
        st.plotly_chart(fig)

        # Numerical and categorical columns
        numerical_columns = ["Impact_Score", "Base_Score", "Exploitability_Score"]
        categorical_columns = ["Access_Complexity", "Access_Vector", "Availability_Impact", "Confidentiality_Impact"]

        ### Categorical vs Categorical Visualizations
        st.markdown("## 🏷️ Categorical vs Categorical Analysis")
        st.markdown("These visualizations show relationships and comparisons across different categorical variables.")

        # Select two categorical columns for comparison
        cat_col1 = st.selectbox('Choose first categorical column', categorical_columns)
        cat_col2 = st.selectbox('Choose second categorical column', categorical_columns)

        col1, col2 = st.columns(2)

        with col1:
            # 1. Count Plot
            st.markdown("### Count Plot")
            fig = px.histogram(filtered_df, x=cat_col1, color=cat_col2, barmode='group',
                               title=f"Count of {cat_col1} by {cat_col2}")
            st.plotly_chart(fig)

            # 2. Pie Chart
            st.markdown("### Pie Chart for Category Proportions")
            fig = px.pie(filtered_df, names=cat_col1, title=f"Proportion of {cat_col1} Categories")
            st.plotly_chart(fig)

        with col2:
            # 3. Heatmap for Categorical Frequencies
            st.markdown("### Frequency Heatmap")
            cat_counts = pd.crosstab(filtered_df[cat_col1], filtered_df[cat_col2])
            fig = px.imshow(cat_counts, text_auto=True, title="Categorical Frequency Heatmap")
            st.plotly_chart(fig)

            # 4. Sunburst Chart
            st.markdown("### Sunburst Chart for Category Hierarchy")
            fig = px.sunburst(filtered_df, path=[cat_col1, cat_col2], title=f"Hierarchical Breakdown of {cat_col1} and {cat_col2}")
            st.plotly_chart(fig)

        ### Numerical vs Numerical Visualizations
        st.markdown("## 🔢 Numerical vs Numerical Analysis")
        st.markdown("These visualizations explore relationships between numerical columns to show trends, correlation, and data distribution.")

        # Select two numerical columns for comparison
        num_col1 = st.selectbox('Choose first numerical column', numerical_columns)
        num_col2 = st.selectbox('Choose second numerical column', numerical_columns)

        col1, col2 = st.columns(2)

        with col1:
            # 1. Scatter Plot with Trend Line
            st.markdown("### Scatter Plot with Trend Line")
            fig = px.scatter(filtered_df, x=num_col1, y=num_col2, trendline="ols",
                             title=f"Relationship between {num_col1} and {num_col2}")
            st.plotly_chart(fig)

            # 2. Histogram for Distribution
            st.markdown("### Histogram for Score Distribution")
            fig = px.histogram(filtered_df, x=num_col1, nbins=30, title=f"Distribution of {num_col1}")
            st.plotly_chart(fig)

        with col2:
            # 3. Correlation Matrix Heatmap
            st.markdown("### Correlation Matrix Heatmap")
            correlation_matrix = filtered_df[numerical_columns].corr()
            fig = px.imshow(correlation_matrix, text_auto=True, title="Correlation Matrix of Scores")
            st.plotly_chart(fig)

            # 4. Additional Plot: Pairwise Relationship
            st.markdown("### Pairwise Plot")
            fig = px.scatter_matrix(filtered_df, dimensions=numerical_columns, title="Pairwise Relationships Between Scores")
            st.plotly_chart(fig)

        ### Numerical vs Categorical Visualizations
        st.markdown("## 🔢🆚🏷️ Numerical vs Categorical Analysis")
        st.markdown("These visualizations analyze the variation of numerical data across different categories.")

        col1, col2 = st.columns(2)

        with col1:
            # 1. Box Plot
            st.markdown("###  Box Plot")
            fig = px.box(filtered_df, x=cat_col1, y=num_col1, title=f"Box Plot of {num_col1} by {cat_col1}")
            st.plotly_chart(fig)

            # 2. Strip Plot
            st.markdown("###  Strip Plot")
            fig = px.strip(filtered_df, x=cat_col1, y=num_col1,
                           title=f"Strip Plot of {num_col1} by {cat_col1}")
            st.plotly_chart(fig)

        with col2:
            # 3. Violin Plot
            st.markdown("### Violin Plot")
            fig = px.violin(filtered_df, x=cat_col1, y=num_col2, box=True,
                            title=f"Violin Plot of {num_col2} by {cat_col1}")
            st.plotly_chart(fig)

            # 4. Additional Plot: Bar Plot of Numerical Mean by Category
            st.markdown("### Bar Plot of Mean Numerical Score by Category")
            fig = px.bar(filtered_df.groupby(cat_col1).agg({num_col1: 'mean'}).reset_index(),
                         x=cat_col1, y=num_col1, title=f"Mean of {num_col1} by {cat_col1}")
            st.plotly_chart(fig)
