import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home - Cybersecurity App", page_icon="🏠", layout="wide")

# Custom CSS for modern and professional look
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f0f4f8, #8e44ad);
            font-family: 'Arial', sans-serif;
            animation: fadeIn 1.5s ease-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        .combined-box {
            background: linear-gradient(135deg, #8e44ad, #3498db);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
            text-align: center;
            color: white;
            margin-top: 20px;
            transition: transform 0.3s ease-in-out;
        }

        .combined-box:hover {
            transform: scale(1.05);
        }

        .combined-box h1 {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
            animation: slideIn 1.5s ease-out;
        }

        @keyframes slideIn {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(0);
            }
        }

        .combined-box p {
            font-size: 1.1em;
            margin: 0;
            padding: 5px 0;
            line-height: 1.6;
        }

        .highlight-box {
            background-color: #2c3e50;
            color: white;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            margin-top: 15px;
            animation: fadeInUp 1.5s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .highlight-box h3 {
            font-size: 1.5em;
            margin-bottom: 10px;
        }

        .highlight-box ul {
            list-style-type: none;
            padding-left: 0;
            font-size: 1.1em;
            margin-top: 10px;
        }

        .highlight-box li {
            margin-bottom: 3px; /* Reduced space here */
            line-height: 1.4;
        }

        .highlight-box li:hover {
            color: #3498db;
            cursor: pointer;
        }

        .project-details {
            background-color: #2980b9;
            color: white;
            padding: 18px;
            border-radius: 12px;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.25);
            margin-top: 23px;
            text-align: center;
            animation: bounceIn 1.5s ease-out;
        }

        @keyframes bounceIn {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .project-details h3 {
            font-size: 1.8em;
            font-weight: bold;
            margin-bottom: 3px;  /* Reduced space here */
        }

        .project-details ul {
            list-style-type: none;
            padding-left: 0;
            font-size: 1.1em;
            margin-top: 3px;  /* Reduced space here */
        }

        .project-details ul li {
            margin-bottom: 3px;  /* Reduced space here */
        }

        .project-details ul li:hover {
            color: #f39c12;
        }

        .button {
            background-color: #f39c12;
            color: white;
            padding: 8px 18px;
            border-radius: 8px;
            cursor: pointer;
            text-align: center;
            margin-top: 12px;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #e67e22;
        }

        .container {
            margin: 0;
            padding: 20px;
        }

        .name-group {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            font-size: 1.2 em;
        }

        .name-group span {
            margin: 6px; /* Reduced space here */
            font-weight: bold;
            font-family: 'Verdana', sans-serif;
            text-transform: uppercase;
            color: #f39c12;
        }

        .supervision-text {
            font-size: 1.2em;  /* Reduced space here */
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
            color: #ecf0f1;
            margin-top: 3px;  /* Reduced space here */
        }
    </style>
""", unsafe_allow_html=True)

# Home page content
st.markdown("""
    <div class="combined-box">
        <h1>🏠 Welcome to the Cybersecurity Application</h1>
        <p>Explore powerful tools to predict vulnerabilities and analyze CVE data. Select an option from the sidebar to get started!</p>
        <div class="highlight-box">
            <h3>🛡️ Key Features</h3>
            <ul>
                <li><b>Vulnerability Prediction</b>: Predict potential cybersecurity vulnerabilities based on detailed descriptions.</li>
                <li><b>CVE Analysis</b>: Explore Common Vulnerabilities and Exposures (CVEs) with interactive visualizations.</li>
            </ul>
        </div>
    </div>

    <div class="project-details">
        <h3>👨‍💻 Data Mining Project: Cybersecurity Vulnerability Predictor</h3>
        <p class="supervision-text">Under the supervision Sandeep Sir</p>
        <div class="name-group">
            <span>Created by</span>
            <span>Pradeep Dubey</span>
            <span></span>
            <span></span>
        </div>
    </div>
""", unsafe_allow_html=True)
#The Certificate Trust Policy component in Apple Mac OS X before 10.6.8 does not perform CRL checking for Extended Validation (EV) certificates that lack OCSP URLs, which might allow man-in-the-middle attackers to spoof an SSL server via a revoked certificate.
