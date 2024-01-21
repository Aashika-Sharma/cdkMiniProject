import subprocess
subprocess.run(["pip", "install", "-r", "requirements.txt"])

import streamlit as st
import pandas as pd
import uuid
import base64
from snowflake.connector import connect, ProgrammingError

# Function to convert file to base64
def file_to_base64(file):
    if file is not None:
        return base64.b64encode(file.read()).decode("utf-8")
    return None

# Snowflake connection parameters
snowflake_account = "HX27359"
snowflake_user = "AASHIKA2ND"
snowflake_password = "Aashika@2003"
snowflake_database = "MINIPROJECTDB"
snowflake_schema = "MYSCHEMA"
snowflake_warehouse = "MINIPROJECT"

# Create an HTML input element for file upload
uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False, label_visibility='hidden')

# Establish a connection to Snowflake
try:
    conn = connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema
    )
    cursor = conn.cursor()

    # Check if the table exists, and create it if not
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS IMAGES (
            FILE_NAME STRING,
            IMAGE_BYTES STRING
        )
    """)
    conn.commit()

    # Use the connection in the Streamlit session
    if uploaded_file is not None:
        # Convert image file to base64
        base64_data = file_to_base64(uploaded_file)

        # Generate new image file name
        file_name = 'img_' + str(uuid.uuid4())

        # Write image data in Snowflake table
        cursor.execute("USE SCHEMA {}".format(snowflake_schema))
        cursor.execute("USE WAREHOUSE {}".format(snowflake_warehouse))
        cursor.execute("USE DATABASE {}".format(snowflake_database))
        cursor.execute("""
            INSERT INTO IMAGES (FILE_NAME, IMAGE_BYTES)
            VALUES (%s, %s)
        """, (file_name, base64_data))
        conn.commit()

except ProgrammingError as e:
    st.error(f"Error: {e}")

finally:
    # Close the Snowflake connection
    if conn:
        conn.close()
