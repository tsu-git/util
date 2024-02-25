""" mnist-download

    downlowad training data-sets from MNIST DATABASE and extract data from 
    those gz files
"""
from pathlib import Path
import requests
import gzip

# download data-sets
base_url = "http://yann.lecun.com/exdb/mnist/"
filenames = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"
]

for filename in filenames:
    url = base_url + filename
    print(url)
    res = requests.get(url)
    res.raise_for_status()
    with open(filename, 'wb') as local_file:
        for chunk in res.iter_content(1000000):
            local_file.write(chunk)

# extract data
for filename in filenames:
    extracted_file = Path(filename).stem
    print(extracted_file)
    with gzip.open(filename, 'rb') as f:
        body = f.read()
        with open(extracted_file, 'wb') as w:
            w.write(body)

