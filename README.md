**Entrepreneur Image Classifier**

**Overview**

This project is a web-based application designed to classify images of renowned entrepreneurs from around the world and India. The application features a drag-and-drop interface for ease of use, processes images with OpenCV, and employs a Support Vector Machine (SVM) model to accurately identify entrepreneurs. In addition to image classification, the app presents valuable information on each entrepreneur’s business journey and achievements, alongside a financial trend graph.

**Entrepreneurs Covered:**

Worldwide: Elon Musk, Jeff Bezos, Bill Gates, Mark Zuckerberg, Warren Buffett
Indian: Mukesh Ambani, Ratan Tata, Gautam Adani, Azim Premji, Narayana Murthy

**Key Features**

1. Image Classification
   
Drag-and-Drop Interface: Users can drag and drop an image of one of the top entrepreneurs.
Preprocessing with OpenCV: Images are processed to enhance quality, making classification more accurate.
SVM Model Classification: A Support Vector Machine model, trained on a labeled dataset, identifies the entrepreneur in the image.

2. Business Information Display
   
Entrepreneur Profile Summary: The app showcases key facts about the entrepreneur’s career, companies, and business impact.
Achievements & Milestones: Lists major business achievements and significant contributions made by the entrepreneur in their industry.

3. Financial Data Visualization
   
Regression Graph for Last 5 Years: A line graph visualizes selected financial data (such as revenue or stock price) over the past five years.
Insightful Business Trends: Enables users to see growth patterns or changes in the entrepreneur’s company performance over time.

4. Responsive & Interactive User Interface

User-Friendly Design: Developed with HTML, CSS, and JavaScript to ensure smooth interaction and responsiveness across devices.
Easy Navigation: Simple drag-and-drop setup makes it accessible to users with any level of technical expertise.

**Technologies Used**

1. OpenCV
   
Employed for image processing tasks, including resizing, grayscaling, and other preprocessing steps to prepare images for accurate classification.

2. SVM (Support Vector Machine)
   
Core of the classification model, trained on a curated dataset to identify top entrepreneurs with high accuracy.

3. Matplotlib
   
Used for plotting a regression line that displays financial performance metrics over the last five years for each entrepreneur.

4. Flask
   
Serves as the backend server, handling image upload, processing requests, running the model, and managing API endpoints.

5. HTML/CSS/JavaScript
   
Powers the frontend, ensuring a responsive and dynamic interface that’s easy for users to interact with and navigate.

**Setup & Installation**

1.Clone Repository

git clone https://github.com/yourusername/entrepreneur-classifier.git
cd entrepreneur-classifier

2.Install Dependencies

pip install -r requirements.txt

3.Run the Flask Server

flask run
The server will start on localhost:5000 by default.

4.Launch Application

Open a web browser and navigate to http://localhost:5000 to access the application.

**Usage**

1.Upload an Image
Drag and drop an image of one of the ten supported entrepreneurs into the designated area on the web page.

2.Classification
The app will preprocess the image and run the SVM classifier to determine the identity of the entrepreneur.

3.View Results
After classification, the app displays the entrepreneur's profile summary and a regression line graph showing their financial metrics over the past five years.

**Project Structure**

/static: Contains all static files (CSS, JavaScript, images)

/templates: Holds HTML templates for Flask to render pages

/models: Contains the pre-trained SVM model for image classification

app.py: Main Flask application file

requirements.txt: Lists required Python libraries

**Future Improvements**

Additional Entrepreneurs: Expand the dataset to include more global and Indian entrepreneurs.

Real-Time Data Integration: Automate financial data retrieval for the graph from online sources for more current stats.

Enhanced Model Accuracy: Train the SVM model with a larger dataset and possibly incorporate deep learning to improve classification accuracy.









