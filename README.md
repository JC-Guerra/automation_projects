# automation_projects
Personal Python automation projects for practice and portfolio

## Projects:
### send_single_email:
    this code no longer works due to gmail's updated policy on third-party prohibition
### web_scraping:
    Last updated: 03/12/2023
    IMPORTANT: run in virtual environment
    Descrption:
        Logins user based on config.ini credentials
        Obtains header and temperature (dynamic) value of website

    Improvements:
        Changed import time to WebDriverWait to make it robust
        Added error handling and removing driver resources
        Dynamic variables
        Added config.ini file for pseudo-security

### image_processing
    Last updated: 04/12/2023
    Description:
        Program gives option to automate:
        1. converting image to greyscale
        2. resizing image
        3. detecting faces in a photo
        4. watermarking image
    
    To-do:
        Fix validate user input for scale. Loops not recognizing valid input after incorrect value.
        Image to Text
        Improve error handling

