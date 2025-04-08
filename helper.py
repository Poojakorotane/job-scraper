def get_url(start=0, postion=1, location='London', job_title='Graduate (Programming Language)'):
    """
    Function to get the url for the job postings
    :param start: The starting point for the job postings
    :param postion: The position of the job postings
    :return: The url for the job postings
    """
    return f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={job_title}&location={location}&geoId=100293800&currentJobId={postion}&start={start}'




def new_fuction():
    return 'test'