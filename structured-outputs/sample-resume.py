from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

client = OpenAI()

load_dotenv()


job_application = """
Name: Sarah Thompson  
Email: sarah.thompson@example.com  
Phone: (555) 123-4567  
LinkedIn: linkedin.com/in/sarahthompson  

Summary:  
A highly motivated Data Scientist in machine learning, data analysis, and cloud computing. Passionate about deriving insights from data and deploying scalable AI models.  

Work Experience:  
- Data Scientist at TechCorp (2021 - Present)  
  - Developed predictive models that improved customer retention by 15%.  
  - Deployed machine learning pipelines on AWS.  

- Data Analyst at Insights Ltd. (2019 - 2021)  
  - Analyzed large datasets to provide actionable insights for business strategies.  

Education:  
- M.S. in Computer Science, University of California, Berkeley (2019)  
- B.S. in Statistics, University of Texas at Austin (2017)  

Skills:  
- Python, SQL, TensorFlow, AWS, Data Visualization  

Certifications:  
- AWS Certified Machine Learning  Specialty  
- Google Data Analytics Professional Certificate  

Desired Position: Senior Data Scientist  
"""


class JobApplication(BaseModel):
    name: str = Field(description="Full name of the applicant")
    email: str = Field(description="Email address of the applicant")
    skills: List[str] = Field(description="List of the key skills present in the resume")
    years_of_experiece: int = Field(description="Total years of experience. Calculate the years of experience based on the current year " + str(datetime.now().year))
    desired_position: str = Field(description="The job role the applicant is applying for")


response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "You are an AI assistant that extracts structured information from job applications."},
        {"role": "user", "content": job_application}
    ],
    text_format=JobApplication
)

print(response.output[0].content[0].text)








