"""
Create python script to get data from zendesk (Tickets Data) with API and show the table example

Assumption:
The tickets queried are the all the tickets that has been created by the "user" email
"""


import requests
import pandas as pd

if __name__ == "__main__":

    # Set the request parameters
    url = "https://subdomain.zendesk.com/api/v2/requests.json"
    user = "myemail@subdomain.com" + "/token"

    # pwd is the API token that has been created on the zendesk board
    api_token = "api_token_generated_from_the_web"

    # Do the HTTP get request
    response = requests.get(url, auth=(user, api_token))

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print("Status:", response.status_code, "Problem with the request. Exiting.")
        exit()

    # Decode the JSON response into a dictionary and use the data
    # The response is shown by response.json file in this same directory
    data = response.json()
    ticket_list = data["requests"]

    tickets_df = pd.DataFrame.from_records(ticket_list)
    print(tickets_df)

    # Saving as csv
    # The csv file is shown by tickets.csv file in this same directory
    tickets_df.to_csv(r"tickets.csv", index=False)
