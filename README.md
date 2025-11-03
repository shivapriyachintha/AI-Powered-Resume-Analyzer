# LLM-Resume-Reviewer-App-Using-Google-Gemimi
An app for analyzing your resume against given job Description using google gemimi and deployed using Streamlit
## Project Overview :
The job application process can be daunting, and our resumes serve as the primary representation of ourselves to HR departments. Receiving a rejection without feedback can indeed be disheartening. This inspired me to create an application using Google's generative AI, GEMINI. It provides feedback on resumes and identifies missing keywords, aiming to offer support and insights to job seekers.
## Objectives :
- Developing an intuitive tool to help job seekers match their resumes with job descriptions.
- Utilizing advanced AI technology to analyze and provide feedback on resumes.
- Creating a user-friendly interface to streamline the resume review process.
## Features:
- Resume Upload: Users can upload their resumes in PDF format.
- Job Description Input: A text input field enables users to paste the job description they are targeting.
- AI-Powered Analysis: Leveraging Gemini AI, the application conducts a comprehensive analysis of the resume in context with the job description.
- Feedback on Different Aspects:
-- Resume Review: Provides general feedback on the resume's content and structure.
-- Skills Improvement: Offers suggestions for enhancing skills based on the job requirements.
-- Keywords Analysis: Identifies missing keywords in the resume compared to the job description.
-- Match Percentage: Generates a percentage score indicating the alignment between the resume and the job description.
## Prerequisites/Steps For Execution:
- Python 3.10.0 or above
- Edit  .env file with your google api key
- pip install -r requirements.txt
- streamlit run app.py
## Technologies Used
- Streamlit: Used to develop the web application interface.
- Google Generative AI (Gemini Pro Vision): Employs advanced AI for processing and analyzing resume content.
- Python: Primary programming language utilized for backend development.
- PDF2Image & PIL: Employed for PDF file conversions and image processing tasks.
## Challenges Faced
- Integration with Gemini AI: Facilitating smooth communication between the Streamlit interface and the Gemini AI model.
- PDF Handling: Streamlining the conversion of PDF content into a format compatible with the AI model for analysis.
- User Experience Optimization: Designing an intuitive and responsive UI to enhance user interaction and satisfaction.
## Future Enhancements
- Support for Multiple Pages: Extend functionality to process multi-page resumes seamlessly.
- Customizable Feedback Categories: Enable users to select specific areas for receiving feedback.
- Interactive Resume Editing: Integrate a feature allowing direct resume editing based on AI suggestions.
- Enhanced Error Handling: Improve system robustness in managing diverse file formats and user inputs.
## Conclusion
The Resume Expert Streamlit application stands as a significant tool in bridging the gap between job seekers and their ideal job roles. By harnessing the power of AI, it provides valuable insights and recommendations, making it a pivotal step in enhancing the job application process.


https://github.com/annchirackal/LLM-Resume-Reviewer-App-Using-Google-Gemini/blob/main/README.md --> source


instructions:

make sure to install poppler windows in c/programfilesx86 and add its bin folder to system path.

create/activate new vemnv and install dependincies and run below command.

python -m streamlit un app.py

pass full path ofactivate.bat to actuve venv
