import requests
import os
from dotenv  import load_dotenv
from csv import reader

load_dotenv()

# For Future Update: using a user API token to invite users (does not bypass SSO & needs to have org admin permissions for all orgs)
# Currently, we're using a service account intentionally to bypass SSO

# SNYK_TOKEN is an API token for a Snyk service account with admin role at either the group level or org level for org users are invited to
# Navigate to org or group settings and click Service Accounts. Create a Service account with an admin role
# Copy API Token
# create a file in this repo with the contents SNYK_TOKEN = "token Token goes here"
# Replace 'Token goes here' with the API token you copied
# Save with the following file name: .env

snyk_token = os.getenv("SNYK_TOKEN") 

# For Future Update: third column of CSV should have org ID of org being added to and an entry for each unique combo of user + org to iterate through
# Currently iterating through users to be invited
# List of users should be in CSV format -- if in Google Sheets or Microsoft Excel, you can export as CSV.
# CSV should not have a header row, and the first column should have names, second should have email addresses, and third should have the name of the org the user is being invited to 
# Save CSV in this repo and replace 'csvfilename.csv' with the file name of your CSV

# This opens the CSV fiile in read mode
with open('csvfilename.csv', 'r') as read_obj:
    # This passes the file to the reader
    csv_reader = reader(read_obj)
    # Iterate through each row
    for row in csv_reader:
        user_email_address = row[1]
        invite_body_params = {
            "email": user_email_address
            }
        # Replace orgId in the line below with the orgId found in Snyk in the Org settings for the org you're inviting users to
        invite_users_endpoint = "https://snyk.io/api/v1/org/orgId/invite"
        invite_users_post=requests.post(invite_users_endpoint,headers={"Authorization": snyk_token},data=invite_body_params)
        response_from_invite = invite_users_post.json()
        print(response_from_invite)
        
        