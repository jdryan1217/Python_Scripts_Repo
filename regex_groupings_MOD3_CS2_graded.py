'''
work with regex - graded module 3 course 2
'''

'''
Complete the secure_website_domain() function so it returns the part of the website between www. and the last part of the url (.com or .co) for only the secure websites. 
'''

def secure_website_domain(website):
 pattern = r"^https://www\.(\w+)\.(com|co)$" # enter the regex pattern here
 result = re.search(pattern, website) # enter the re method here
 if result is None:
  return ""
 return result.group(1)# enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text

'''
You would like to separate this field into two fields, a city field and a state field. In the current field, city and state are separated by either a comma, or a period. Complete the function parse_city_state() to split city and state into two strings and return only the state.
'''

def parse_city_state(text):
    pattern = r"^\s*([A-Za-z\s]+)\s*[,\.]\s*([A-Za-z\s]+)\s*$"
    result = re.search(pattern, text)
    if result is None:
        return ""
    groups = result.groups()
    if len(groups) != 2:
        return ""
    return groups[1]



print(parse_city_state("Hamilton, MN")) # should return MN
print(parse_city_state("Albuquerque, New Mexico")) # should return New Mexico
print(parse_city_state("Portland. Oregon")) # should return Oregon

'''
A company uses unique, 9-character codes that begin with a capital letter, followed by a hyphen (-), followed by 7 or 8 digits as employee ID numbers, in the format: 

A-1234567 or A-12345678 

Project reports submitted to the company include the employee’s ID number and a summary of the work they completed on the project. A data analyst wants to pull all of the employee ID numbers out of these projects. Complete the find_eid() function to extract these employee ID numbers from the reports. 
'''

def find_eid(report):
  pattern = r"[A-Z]-\d{7,8}(?!\d)" #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result


print(find_eid("Employees B-1234567 and C-12345678 worked with products X-123456 and Z-123456789")) # Should return ['B-1234567', 'C-12345678']
print(find_eid("Employees B-1234567 and C-12345678, not employees b-1234567 and c-12345678")) #Should return ['B-1234567', 'C-12345678']

'''

'''