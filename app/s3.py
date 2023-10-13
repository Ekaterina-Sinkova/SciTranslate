import os
from typing import BinaryIO
import uuid
from minio import Minio


class S3Handler:    
    """
    Creates Minio client and provides high-level interface to
    put and get operations.
    """
    def __init__(self):
        MINIO_HOST = os.getenv('MINIO_HOST')
        MINIO_PORT = os.getenv('MINIO_PORT')
        MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
        MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')

        self.client = Minio(
            endpoint=f"{MINIO_HOST}:{MINIO_PORT}",
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False
        )

    def upload_to_s3(self, bucket_name: str, file: BinaryIO) -> str:
        """Puts a binary file-like object to the S3 storage."""
        object_uuid = str(uuid.uuid4())
        self.client.put_object(
            bucket_name=bucket_name,
            object_name=object_uuid,
            data=file,
            length=file.getbuffer().nbytes
        )
        return object_uuid
    
    def get_from_s3(self, bucket_name: str, object_uuid: str) -> bytes:
        """Gets a bytes object from the S3 storage by object name."""
        response = self.client.get_object(
            bucket_name=bucket_name,
            object_name=object_uuid
        )
        return response.read()
