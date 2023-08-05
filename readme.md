 ## About
 AWS S3 Raw Data Bucket -> AWS Lamda -> AWS S3 Consolidated Data Bucket

1. S3 Event Trigger: An object is created in rawbucketaz, which triggers Process_Raw_Data.
2. Lambda Function:
   1. Reads the new object from rawbucketaz.
   2. Processes the data to add a new column with the current date and time. 
   3. Writes the modified data to a new file in consolidatedbucketaz.

 ## Python Code
Code from lamda_handler.py can be copied to lamda code

 ## AWS IAM permisions
For the Role that has been created for AWS lamda 
Roles
Process_Raw_Data-role-xxxxx
need to add AmazonS3FullAccess (as this is for testing purpose or can specify access only to the required bucket, rather
than all buckets)
```json{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "*"
        }
    ]
}
