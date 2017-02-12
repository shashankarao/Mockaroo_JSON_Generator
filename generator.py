import requests
import json
import argparse
import sys

""" This script uses Mockaroo API to generate an output file based on a json schema passed to it.
Official documentation site: https://www.mockaroo.com/api/docs
"""

parser = argparse.ArgumentParser(description='Retrieve data from Mockaroo API')
# file is required parameter
parser.add_argument('file',
                    help='REQUIRED: Configuratoin file to use')
# key is required parameter
parser.add_argument('-k','--key', nargs=1,
                    help='REQUIRED: Enter the API key for Mockaroo')
parser.add_argument('-n', '--number', nargs=1, default=5, type=int,
                    help='Enter the number of records you would like returned, the default is 5.')
parser.add_argument('-s', '--schema', nargs=1, default=['csv'],
                    choices=['json','csv','txt','custom','sql','xml'],
                    help='Use one of the allowed data formats, if not specified it will use CSV')
args = parser.parse_args()

# convert args into easy to read variables
mockaroo_key = args.key  # your mockaroo API key
num_rows_to_generate = args.number  # Max 1000 for the free version of the API
output_format = args.schema[0]


def post_request():
    # Generate the URL by appending return format.
    # API URL args.schema at the end refers to the expected format of the output
    url = 'http://www.mockaroo.com/api/generate.%s' % args.schema[0]

    # schema.json refers to the schema definition of the output json to be generated
    # Refer official documentation for supported types and detailed explanation

    try:
      with open(args.file, 'r') as datafile:
          fields = json.load(datafile)
    except ValueError as error: #looking for errors in json loaded into script
      print('There was an error with the JSON provided')
      print(args.file)
      print(error)
      sys.exit(1)
    
    # declare arguments required for post request to Mockaroo
    payload = {
            'fields':json.dumps(fields),
            'key': args.key,
            'count':args.number
    }

    # Make a post call to the URL
    # Body of the post request is the schema definition of the output expected, API Key, and number of records to return
    response = requests.post(url, params=payload)

    # Write the output to a file ex. (output.json)
    with open('output.%s' % output_format, 'w') as outfile:
        outfile.write(response.text)


if __name__ == '__main__':
    post_request()
