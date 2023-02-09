"""
This function retrieves a list of files from a publicly accessible Amazon S3 bucket, filtered by a specified prefix.

Parameters:
bucket_name (str): The name of the Amazon S3 bucket.
prefix (str): The prefix to filter the objects in the bucket by.

Returns:
list: A list of keys for the objects in the bucket that match the given prefix.
"""


import boto3


def extract_files(bucket_name, prefix):
    s3 = boto3.resource("s3")
    result = []
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=prefix):
        result.append(obj.key)
    return result


# uncomment the following line of code for example
# print(extract_files("noaa-goes18", "ABI-L1b-RadC/2022/215/05"))
