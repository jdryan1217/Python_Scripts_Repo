'''
Creating reports using Python with CSV and using regular expressions to find a pattern in a string are very useful tools in IT support. You'll likely complete similar tasks regularly throughout your career, so feel free to go through this lab as many times as you need. Remember, practice makes perfect.
'''
#!/usr/bin/env python3

import csv
import re

def contains_domain(address, domain):
    """Returns True if the email address ends with the given domain."""
    pattern = r'[\w\.-]+@' + domain + r'$'
    return re.match(pattern, address) is not None

def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    return re.sub(old_domain + r'$', new_domain, address)

def main():
    old_domain = 'abc.edu'
    new_domain = 'xyz.edu'

    # Correct paths for Coursera environment
    csv_file_location = '/home/student/data/user_emails.csv'
    report_file = '/home/student/data/updated_user_emails.csv'

    # Read CSV
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))

    # Clean header and find email column
    header = [h.strip() for h in user_data_list[0]]
    email_index = header.index('Email Address')

    # Process each row
    for row in user_data_list[1:]:
        email = row[email_index].strip()
        if contains_domain(email, old_domain):
            row[email_index] = replace_domain(email, old_domain, new_domain)

    # Write updated CSV
    with open(report_file, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)

main()
