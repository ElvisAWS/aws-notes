# Encryption using AWS-KMS must be defined at lunch time
# If the master is not encrypted, read-replicas will not be encrypted
# To encrypt an un-encrypted DB, create a snapshot of the instance, encrypt and restore the DB
# No SSH available except for custom RDS
# Enable CloudWatch logs for log generation
# RDS Security
    # When you evaluate at IT infrastructure from a business standpoint, security is always your number one priority. 
    # When it comes to AWS, databases are run on instances within a VPC, so your network is the first layer of defense. 
    # If you are connecting to AWS from an on-premise data center, make sure you are using Direct Connect (a private 
    # dedicated connection between you and AWS) or a VPN. Utilizing Security Groups and Network Access Lists is also 
    # a must, no matter where you are connecting from. This ensures that only the IP addresses and ports you are using 
    # are allowed, and no one else can access your data. During the creation of the database, you will assign a master 
    # user who will have full administration rights, but only use them to define other database users and grant them 
    # access. You also can choose whether your database will be publicly accessible or not. While keeping your database 
    # private (without a public IP) is better, unless you have a private connection to AWS or you connect only from 
    # within your cloud infrastructure, you will have to make the database public. In this case, use a restrictive 
    # security group for extra protection.
# Encryption
    # Securing access to your database is of great importance, but so is the protection of the data itself. RDS allows 
    # you to protect your data by using encryption, both in transit and at rest. For encryption in transit, SSL is 
    # supported by all six database engines. RDS will create a certificate and install it on an instance when it is 
    # provisioned. You can download the public key from Amazon and use it to encrypt your connection in order to secure 
    # the traffic between you and the database on AWS. Encryption at rest is also supported by every database engine 
    # run by RDS and is applied not only to the instance storage, but also to read replicas, automated backups, and 
    # snapshots. Encryption at rest is handled by AWS Key Management Service (KMS) and is enabled during the 
    # provisioning of the database. When the instance is up and running, it will request a data key (each database 
    # will have its own unique key) from KMS and will use it to encrypt the data. Encryption is also important when 
    # it comes to compliance, so make sure you enable it when setting up your database.