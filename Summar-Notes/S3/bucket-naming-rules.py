
# The following rules apply for naming buckets in Amazon S3:

# Bucket names must be between 3 (min) and 63 (max) characters long.
# Bucket names can consist only of lowercase letters, numbers, dots (.), and hyphens (-).
# Bucket names must begin and end with a letter or number.
# Bucket names must not contain two adjacent periods.
# Bucket names must not be formatted as an IP address (for example, 192.168.5.4).
# Bucket names must not start with the prefix xn--.
# Bucket names must not end with the suffix -s3alias. This suffix is reserved for access point alias names. 
# For more information, see Using a bucket-style alias for your access point.
# Bucket names must be unique across all AWS accounts in all the AWS Regions within a partition. A partition 
# is a grouping of Regions. AWS currently has three partitions: aws (Standard Regions), aws-cn (China Regions), 
# and aws-us-gov (AWS GovCloud (US)).
# A bucket name cannot be used by another AWS account in the same partition until the bucket is deleted.
# Buckets used with Amazon S3 Transfer Acceleration can't have dots (.) in their names. For more information 
# about Transfer Acceleration, see Configuring fast, secure file transfers using Amazon S3 Transfer Acceleration.