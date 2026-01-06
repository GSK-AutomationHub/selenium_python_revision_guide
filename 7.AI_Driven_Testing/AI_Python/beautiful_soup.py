
# BS4 - Beautiful Soup 4 [https://pypi.org/project/beautifulsoup4/]
# # !pip install bs4
# from bs4 import BeautifulSoup
# import requests # let's you download webpages into python
# from helper_functions import *
# from IPython.display import HTML, display

'''
# The url from one of the Batch's newsletter
url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

# Getting the content from the webpage's contents
response = requests.get(url)

# Print the response from the requests
print(response)

HTML(f'<iframe src={url} width="60%" height="400"></iframe>')
'''
# Beautiful Soup used to extract all the text paragraphs from the HTML structure that you retrieved,
# and save it as a single string. Here is the code to do this
'''
# Using beautifulsoup to extract the text 
[create obj of beautiful soup by parsing html content in response.text using 'html.parser']
soup = BeautifulSoup(response.text, 'html.parser') 

# Find all the text in paragraph elements on the webpage
all_text = soup.find_all('p')

# Create an empty string to store the extracted text
combined_text = ""

# Iterate over 'all_text' and add to the combined_text string
for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()

# Print the final combined text
print(combined_text)

prompt = f"""Extract the key bullet points from the following text.
Text: {combined_text} """

print_llm_response(prompt)
'''
print(" --------------------------------------------------------------------------------------- ")

# The DeepLearning.AI team has created a third-party package called aisetup that you can use to access
# the helper functions from the course in your own code outside of this learning platform.

'''
!pip install aisetup
from aisetup import get_llm_response
'''
print(" --------------------------------------------------------------------------------------- ")

# Challenge exercise!
'''Write code that uses the bs4 package to create a string that contains the title element 
from the Batch newsletter. This is the text that starts "The World Needs More Intelligence".

# Hint 1: Titles on webpages are often header elements, with tags like <h1> or <h2>. 
# Hint 2: Ask the chatbot for help, using the code you have already written as a starting point.
'''
print(" --------------------------------------------------------------------------------------- ")
'''
# Your code here

# The url from one of the Batch's newsletter
url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

# Getting the content from the webpage's contents
response = requests.get(url)

# Print the response from the requests
print(response)

# Using beautifulsoup to extract the text
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the text in paragraph elements on the webpage
all_titles = soup.find('h1' or 'h2')

# Create an empty string to store the extracted text
expected_title = ""

# Iterate over 'all_text' and add to the combined_text string
for title in all_titles:
    if 'More Intelligence' in title:
        expected_title = title
        print(f"Title= {expected_title}")
    
#+ "\n" + text.get_text()
# Print the final combined text
# print(title)
'''