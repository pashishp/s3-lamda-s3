import boto3
import csv
from io import StringIO
from datetime import date

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    # Extracting bucket and file name from Lambda event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    print("Source Bucket:", bucket_name, " Source File: ", file_name)
    # Ensure that the event is coming from the desired bucket
    if bucket_name != "rawbucketaz":
        return "Wrong bucket. Ignored."

    # Fetching file from S3
    file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    file_content = file_obj["Body"].read().decode('utf-8')

    # Processing the CSV data
    csv_input = StringIO(file_content)
    csv_output = StringIO()
    reader = csv.DictReader(csv_input)
    fieldnames = reader.fieldnames + ['processed_date']
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        row['processed_date'] = date.today().strftime('%Y-%m-%d')  # Adding current date
        writer.writerow(row)

    # Writing the modified CSV to consolidatedbucketaz
    s3_client.put_object(Bucket="consolidatedbucketaz", Key=file_name, Body=csv_output.getvalue())

    return "File processed and saved to consolidatedbucketaz."

