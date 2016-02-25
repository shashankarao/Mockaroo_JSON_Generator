import requests
import json

""" This script uses Mockaroo API to generate an output json based on a schema passed to it.
Official documentation site: https://www.mockaroo.com/api/docs
"""

# API URL .json at the end refers to the expected format of the output
mockaroo_url = 'http://www.mockaroo.com/api/generate.json'
# API key
mockaroo_key = ''  # your mockaroo key
num_rows_to_generate = 10  # Max 1000 for the free version of the API


def post_request():
    # Generate the URL by appending key and count.
    # key is required parameter
    # if count is not given, default is one object is returned based on schema definition
    url = url = mockaroo_url + '?key=' + mockaroo_key + '&count=' + str(num_rows_to_generate)

    # schema.json refers to the schema definition of the output json to be generated
    # Refer official documentation for supported types and detailed explanation

    with open('schema.json', 'r') as datafile:
        fields = json.load(datafile)
    # Make a post call to the URL
    # Body of the post request is the schema definition of the output expected
    response = requests.post(url=url, json=fields)

    # Write the output to a file (output.json)
    with open('output.json', 'w') as outfile:
        json.dump(response.json(), outfile)


if __name__ == '__main__':
    post_request()
