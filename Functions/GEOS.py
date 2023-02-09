"""
This script encompasses the functionalities for extracting metadata,
synchronizing files from the GEOS S3 bucket to our own S3 storage, and executing
file retrieval procedures utilizing the inputs documented in the accompanying
technical documentation.
"""

import boto3
s3 = boto3.client('s3')


def list_directories(bucket_name, prefix="ABI-L1b-RadC", depth=0):
    directories = []
    paginator = s3.get_paginator("list_objects_v2")
    for result in paginator.paginate(Bucket=bucket_name, Delimiter='/', Prefix=prefix):
        for prefix in result.get("CommonPrefixes"):
            directories.append(prefix.get("Prefix"))
            if depth < 3:
                directories.extend(list_directories(bucket_name, prefix=prefix.get("Prefix"), depth=depth + 1))
    return directories


bucket_name = 'noaa-goes18'
directories = list_directories(bucket_name)
print(directories)

f = open('GEOS.txt', 'w')
for files in directories:
    f.write(files + '\n')

f.close()
