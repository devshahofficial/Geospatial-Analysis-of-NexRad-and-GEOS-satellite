import boto3
import io


def upload_file_to_s3(file_name, prefix, source_bucket_name, target_bucket_name):
    """
    Uploads a file from one publicly accessible S3 bucket to another S3 bucket and returns the URL of the uploaded file.

    Parameters:
    file_name (str): The name of the file to be uploaded.
    prefix (str): The prefix of the file to be uploaded.
    source_bucket_name (str): The name of the source S3 bucket.
    target_bucket_name (str): The name of the target S3 bucket.

    Returns:
    str: The URL of the uploaded file.
    """
    # Create an S3 client and an S3 resource
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    # Get file from source bucket
    # Create a source object from the S3 resource
    source_object = s3_resource.Object(source_bucket_name, prefix + file_name)
    # Get the content of the file from the source object
    file_content = source_object.get()['Body'].read()

    # Upload file to target bucket
    # Create a target object from the S3 resource
    target_object = s3_resource.Object(target_bucket_name, prefix + file_name)
    # Upload the content of the file to the target object
    target_object.upload_fileobj(io.BytesIO(file_content))
    # Print a message indicating that the file has been uploaded
    print(f"File {file_name} with prefix {prefix} uploaded to S3 bucket {target_bucket_name}.")

    # Return link to uploaded file
    # Construct the URL of the uploaded file
    uploaded_file_url = f"https://{target_bucket_name}.s3.amazonaws.com/{prefix}{file_name}"
    return uploaded_file_url


# Call the function to upload a file from one S3 bucket to another S3 bucket
url = upload_file_to_s3("OR_ABI-L1b-RadC-M6C01_G18_s20222491701170_e20222491703543_c20222491703582.nc",
                        "ABI-L1b-RadC/2022/249/17/", "noaa-goes18", "the-data-guys")
# Print the URL of the uploaded file
print(f"URL of uploaded file: {url}")