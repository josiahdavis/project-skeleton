import boto3
import os


def make_dir_if_needed(local_dir):
    """Creates a directory if doesn't already exist.

    Args:
        local_dir (str): a directory.

    Returns:
        Nothing except a imple print confirmation

    """
    if not os.path.isdir(local_dir):
        os.mkdir(local_dir)
        print(f"Created {local_dir}")


def download_objects(s3_client, bucket, s3_keys, local_dir, verbose=False):
    """Downloads multiple objects from s3 to a local directory.

    Args:
        s3_client (obj): a low-level client of AWS S3.
        bucket (str): the bucket name.
        s3_keys (list[str]): the path to the s3 object along with the object name.
        local_dir (str): where the files should be downloaded toi.
        verbose (bool): whether to print out files as they are being downloaded. 
    
    Returns:
        List of local files and their location.
    """
    make_dir_if_needed(local_dir)
    local_keys = []
    for s3_key in s3_keys:
        file_name = s3_key.split("/")[-1]
        local_key = os.path.join(local_dir, file_name)
        download_object(s3_client, bucket, s3_key, local_key, verbose=verbose)
        local_keys.append(local_key)
    return local_keys


def download_object(s3_client, bucket, s3_key, local_key=None, verbose=False):
    """Downloads a single object from s3 to a local directory.

    Args:
        s3_client (obj): a low-level client of AWS S3.
        bucket (str): the bucket name.
        s3_key (str): the path to the s3 object along with the object name.
        local_key (str): where the files should be downloaded to and file name.
        verbose (bool): whether to print out a file as it is being downloaded. 
    
   """

    if not local_key:
        file_name = s3_key.split("/")[-1]
        local_key = os.path.join(".", file_name)
    s3_client.download_file(bucket, s3_key, local_key)
    if verbose:
        print(f"downloaded {s3_key} --> {local_key}")


def list_objects(s3_client, bucket, prefix="", extensions=None, max_items=2147483647):
    """Lists out objects within s3.

    Args:
        s3_client: a low-level client of AWS S3.
        bucket (str): the bucket name
        prefix: (str, optional): bucket prefix
        extensions (str, list, optional): file extensions to filter results by
        max_items (int, optional): only return a subset of items

    Returns:
        keys (list of strings): files within the bucket matching all of the 
            conditions. Files will include prefix.

    Examples:
        >>> s3_client = boto3.client('s3')
        >>> bucket = 'nose-recognition'
        >>> list_objects(s3_client, bucket, prefix='data/train', extensions=['jpg', 'jpeg'])
        [data/train/nose0.jpeg, data/train/nose1.jpg, data/train/nose2.jpeg, data/train/nose3.jpg]
    """
    paginator = s3_client.get_paginator("list_objects_v2")
    page_iterator = paginator.paginate(
        Bucket=bucket, Prefix=prefix, PaginationConfig={"MaxItems": max_items}
    )
    results = page_iterator.search("Contents")
    keys = [el["Key"] for el in results]
    if extensions:
        return [k for k in keys if k.split(".")[-1] in set(extensions)]
    else:
        return keys
