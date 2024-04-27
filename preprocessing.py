# from IPython.display import JSON

import json
from unstructured_client import UnstructuredClient
from unstructured.partition.html import partition_html
from unstructured.staging.base import dict_to_elements, elements_to_json
from Utils import Utils
utils = Utils()

DLAI_API_KEY = utils.get_dlai_api_key()
DLAI_API_URL = utils.get_dlai_url()

s = UnstructuredClient(
    api_key_auth=DLAI_API_KEY,
    server_url=DLAI_API_URL,
)


filename = "data/medium_blog.html"
elements = partition_html(filename=filename)
element_dict = [el.to_dict() for el in elements]


example_output = json.dumps(element_dict[:], indent=2)
print(example_output)

