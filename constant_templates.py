Job_Description_Template = """
    From the given job posting on a company's webpage, please extract key details including the job responsibilities, 
    required qualifications, the company culture, any unique aspects of the company, compensation, and benefits.
    If the information isn't available, please indicate as "not found". Also, do never make up information, this is crucial.
    >>> {requests_result} <<<
    Extracted:
"""

Task_Description_Template = """
Assume the role of a professional cover letter writer with knowledge of Applicant Tracking Systems (ATS).

You are a state-of-the-art AI language model that has been tasked with creating a cover letter based on the provided job 
information for a {role} at {name_of_company} and the candidate's resume {resume}.

Your are expected to generate a cover letter that effectively aligns the candidate's qualifications, experiences, and 
aspirations with the requirements and responsibilities outlined in the job description {job_information}. Your cover letter 
should be concise and contain between 250 to 400 words.

Your cover letter should accomplish the following:

1. Create a compelling narrative that logically and emotionally explains why the job responsibilities, qualifications, 
and company culture are appealing. This narrative should align with the candidate's background, experience, and aspirations 
as depicted in the candidate's resume. 

2. Identify key skills, qualifications, and experiences from the candidate's resume that directly align with the requirements 
and responsibilities specified in the job description.

3. Incorporate the action verbs, phrases, and keywords from the job description into the cover letter where they appropriately 
describe the candidate's skills and experiences. These terms should also be ATS-friendly to increase the chances of the 
cover letter passing the ATS screening.

4. Maintain a professional tone and language throughout the cover letter.

The aim is to craft a cover letter that not only meets the job requirements but also captivates the reader, making the 
candidate a compelling choice for the {role} at {name_of_company}. 
It should also be optimized for an Applicant Tracking System (ATS), using keywords from the job description where they 
accurately represent the candidate's qualifications.

Your cover letter should replace the [Your Name] placeholder with {name_of_candidate} provided, [Email Address] placeholder with {email},
[Date] placeholder with {today_date} and if {hr_name} is provided then only replace [Recipient's Name] placeholder with 
{hr_name}, otherwise replace it with "Hiring Manager". 

Remove unnecessary placeholders which are [Your Address], [City, State, ZIP Code], [Phone Number], [Recipient's Job Title],
[Company Address] and [Address].

Note: The cover letter should not include any information not present in the provided resume. The objective is to enhance 
the candidate's qualifications as depicted in the resume to fit the job description, not to fabricate details.

Avoid mentioning compensation details in the cover letter.
"""