import unittest
from unittest.mock import patch
from moto import mock_s3, mock_events
import boto3
from lambda_handler import create_thumbnail

class TestCreateThumbnail(unittest.TestCase):
    @mock_s3
    @mock_events
    @patch("boto3.client")
    def test_process_image(
        self, boto_mock
    ):
        
        s3 = boto3.client("s3",region_name="us-east-1")
        s3.create_bucket(Bucket="photos-yma")
        s3.put_object(
            Bucket ="photos-yma",Key="uploads/test_image.jpg",Body=b"test- data"
        )
        #call the function you are testing and make assertions.
        
    class TestCreateThumbnail(unittest.TestCase):
        @mock_s3
        @mock_events
        @patch("boto3.client")
        def test_create_thumbnail(self.boto_mock):
            s3 = boto3.client("s3",region_name="us-east-1")
            s3.put_object(
                Bucket="photos-yma",key="uploads/test-image.jpg"
            )
            
            event ={
                "Records":[
                    {
                        "s3":{
                            "bucket":{"name":"photos-yma"},
                    "object":{"key":"uploads/test_image.jpg"
                        }
                    }
                ]
            }
    