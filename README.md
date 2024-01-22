Title:
An image recognition app in Snowflake using Snowpark, Python, PyTorch, Streamlit and OpenAI

Terminologies:

Snowpark: The set of libraries and runtime in Snowflake provides an intuitive library for querying and processing data at scale.

Streamlit is a free and open-source Python framework for building and sharing web apps for data science and machine learning. 

PyTorch is a machine learning framework based on Torch library, used for appliactions such as computer vision and NLP.

What I have built: 

Two web-based image recognition applications in Streamlit. These applications call Snowpark for Python User-Defined Function (UDF) which uses PyTorch for image recognition.

	1. The first application lets the user upload an image
	2. The second application uses OpenAI's DALL-E 2 to generate an image based on user input in text/natural language format.

Application 1: Upload an image 

Converts image data base64 to hex ( base64 -> hex )

What is base64?
Base64 images are primarily used to embed image data in formats like HTML, CSS, or JSON. This can help increase the page load time for smaller images by saving the browser from additional HTTP requests.

• Streamlit's st.set_page_config(), st.header(), st.caption(), st.columns() and st.container() are used to organize and display various components of the application.

Steps in creating the application:

	1) Setting up Environment: Included links to the developer guides of Snowpark, Streamlit and OpenAI for reference.
	2) Imports: Imported necessary libraries including Snowpark,Streamlit and OpenAI.
	3) Creating Snowpark session: The 'create_session' function is used to create a new Snowpark session.
	4) File Upload with Streamlit: 'st.file_uploader' allows users to upload an image file. It is stored in uploaded_file variable.
	5) Uploading Image to Snowflake: The code converts the image data to hexadecimal format and writes it to a Snowflake table named "IMAGES"using Snowpark.
	6) Predicting Image Label: It calls a Snowpark UDF ('image_recognition_using_bytes)' to predict the label for uploaded image.
	7) Displaying results with Streamlit: It displays the uploaded image and the predicted label on the Streamlit app.

How to run the app:

On terminal or command prompt: 

	1) conda activate snowpark-img-rec
	2) streamlit run Snowpark_PyTorch_Streamlit_Upload_Image_Rec.py

This will open Streamlit app where you can proceed with the image recognition.

