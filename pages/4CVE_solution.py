
import streamlit as st
from groq import Groq
import re

# Initialize the Groq API client
API_KEY = "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"
client = Groq(api_key=API_KEY)

def query_groq_api(prompt):
    try:
        # Make the API call to Groq with a refined prompt
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract raw content from the API response directly
        raw_content = str(completion)  # Convert response to string if needed
        
        # Debug: Print the raw content to check the structure
        st.text_area("Raw API Response", raw_content, height=200)

        # Define regex patterns for Impact and Fix sections
        impact_pattern = r"(\*\*Impact\*\*.*?)(?=\*\*|$)"
        fix_pattern = r"(\*\*Fix\*\*.*?)(?=\*\*|$)"
        vulnerability_pattern = r"(\*\*Vulnerability\*\*.*?)(?=\*\*|$)"
        affected_products_pattern = r"(\*\*Affected Products\*\*.*?)(?=\*\*|$)"
        severity_pattern = r"(\*\*Severity\*\*.*?)(?=\*\*|$)"

        # Search for matches using regex
        vulnerability_match = re.search(vulnerability_pattern, raw_content, re.DOTALL)
        impact_match = re.search(impact_pattern, raw_content, re.DOTALL)
        fix_match = re.search(fix_pattern, raw_content, re.DOTALL)
        affected_products_match = re.search(affected_products_pattern, raw_content, re.DOTALL)
        severity_match = re.search(severity_pattern, raw_content, re.DOTALL)

        # If matches are found, extract and return them
        if all([vulnerability_match, impact_match, fix_match, affected_products_match, severity_match]):
            vulnerability = vulnerability_match.group(1).strip()
            impact = impact_match.group(1).strip()
            fix = fix_match.group(1).strip()
            affected_products = affected_products_match.group(1).strip()
            severity = severity_match.group(1).strip()

            # Structuring the result for better readability
            return f"""
            **Vulnerability**:
            {vulnerability}

            **Impact**:
            {impact}

            **Fix**:
            {fix}

            **Affected Products**:
            {affected_products.replace("\n", " \n- ").strip()}

            **Severity**:
            {severity}
            """
        else:
            missing_details = []
            if not vulnerability_match:
                missing_details.append("Vulnerability")
            if not impact_match:
                missing_details.append("Impact")
            if not fix_match:
                missing_details.append("Fix")
            if not affected_products_match:
                missing_details.append("Affected Products")
            if not severity_match:
                missing_details.append("Severity")
            
            return f"Could not extract the required details from the API response. Missing details: {', '.join(missing_details)}. Please check the CVE ID and try again."

    except Exception as e:
        st.error(f"Error querying Groq API: {e}")
        return None

# Streamlit UI for entering the CVE prompt and displaying the response
st.title("CVE Solution Finder")

prompt = st.text_area("Enter the CVE ID and details:", "CVE-2022-22947")

# Update the prompt format before passing it to the API
custom_prompt = f"""
I am looking for detailed information about the CVE ID: {prompt}. 
Please provide the following sections:
1. **Vulnerability**: A brief description of the vulnerability.
2. **Impact**: A detailed explanation of the impact if the vulnerability is exploited.
3. **Fix**: Steps to mitigate or fix the vulnerability.
4. **Affected Products**: List of affected products.
5. **Severity**: The CVSS score or severity rating of the vulnerability.

Please return the information in this exact format.
"""

if st.button("Get Solution"):
    solution = query_groq_api(custom_prompt)
    
    if solution:
        st.subheader("Solution and Recommendations:")
        st.markdown(solution)
