import requests
import json
import argparse

""" This script uses Mockaroo API to generate an output json based on a schema passed to it.
Official documentation site: https://www.mockaroo.com/api/docs
"""

parser = argparse.ArgumentParser(description='Retrieve data from Mockaroo API')
parser.add_argument('file',
                    help='Configuratoin file to use')
parser.add_argument('-k','--key', nargs=1,
                    help='Enter the API key for Mockaroo')
parser.add_argument('-n', '--number', nargs=1, default=5, type=int,
                    help='Enter the number of records you would like returned')
parser.add_argument('-s', '--schema', nargs=1, default=['csv'],
                    choices=['json','csv','txt','custom','sql','xml'],
                    help='Use one of the allowed data formats, if not spacified it will use CSV')
args = parser.parse_args()

# API URL .json at the end refers to the expected format of the output
mockaroo_url = 'http://www.mockaroo.com/api/generate.%s' % args.schema[0]
# API key
mockaroo_key = args.key  # your mockaroo key
num_rows_to_generate = args.number  # Max 1000 for the free version of the API


def post_request():
    # Generate the URL by appending key and count.
    # key is required parameter
    # if count is not given, default is one object is returned based on schema definition
    url = mockaroo_url + '?key=' + mockaroo_key + '&count=' + str(num_rows_to_generate)

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
