
# S3 Select
    # Enables applications to retrieve only a subset of data from an object by using simple SQL expressions. By 
    # using S3 Select to retrieve only the data needed by your application, you can achieve drastic performance 
    # increases – in many cases you can get as much as a 400% improvement.
        # As an example, let’s imagine you’re a developer at a large retailer and you need to analyze the weekly 
        # sales data from a single store, but the data for all 200 stores is saved in a new GZIP-ed CSV every day. 
        # Without S3 Select, you would need to download, decompress and process the entire CSV to get the data you 
        # needed. With S3 Select, you can use a simple SQL expression to return only the data from the store you’re 
        # interested in, instead of retrieving the entire object. This means you’re dealing with an order of magnitude 
        # less data which improves the performance of your underlying applications.
import boto3
s3 = boto3.client('s3')

r = s3.select_object_content(
            Bucket='jbarr-us-west-2',
            Key='sample-data/airportCodes.csv',
            ExpressionType='SQL',
            Expression="select * from s3object s where s.\"Country (Name)\" like '%United States%'",
            InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}},
            OutputSerialization = {'CSV': {}},
    )

for event in r['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            print(records)
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            print(statsDetails['BytesScanned'])
            print("Stats details bytesProcessed: ")
            print(statsDetails['BytesProcessed'])

# Glacier Select
    # Some companies in highly regulated industries like Financial Services, Healthcare, and others, write data 
    # directly to Amazon Glacier to satisfy compliance needs like SEC Rule 17a-4 or HIPAA. Many S3 users have 
    # lifecycle policies designed to save on storage costs by moving their data into Glacier when they no longer 
    # need to access it on a regular basis. Most legacy archival solutions, like on premise tape libraries, have 
    # highly restricted data retrieval throughput and are unsuitable for rapid analytics or processing. If you 
    # want to make use of data stored on one of those tapes you might have to wait for weeks to get useful results. 
    # In contrast, cold data stored in Glacier can now be easily queried within minutes.
    # This unlocks a lot of exciting new business value for your archived data. Glacier Select allows you to to 
    # perform filtering directly against a Glacier object using standard SQL statements. Glacier Select works just 
    # like any other retrieval job except it has an additional set of parameters you can pass in initiate job 
    # request. SelectParameters

import boto3
glacier = boto3.client("glacier")

jobParameters = {
    "Type": "select", "ArchiveId": "ID",
    "Tier": "Expedited",
    "SelectParameters": {
        "InputSerialization": {"csv": {}},
        "ExpressionType": "SQL",
        "Expression": "SELECT * FROM archive WHERE _5='498960'",
        "OutputSerialization": {
            "csv": {}
        }
    },
    "OutputLocation": {
        "S3": {"BucketName": "glacier-select-output", "Prefix": "1"}
    }
}

glacier.initiate_job(vaultName="reInventSecrets", jobParameters=jobParameters)

    