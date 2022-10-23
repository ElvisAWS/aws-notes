
# Data protection refers to protecting data while in-transit (as it travels to and from Amazon S3) and at rest 
# (while it is stored on disks in Amazon S3 data centers). You can protect data in transit using Secure Socket 
# Layer/Transport Layer Security (SSL/TLS) or client-side encryption. You have the following options for 
# protecting data at rest in Amazon S3:
# During encryption, the bucket policy takes president before the default bucket policy

# Server-Side Encryption – Request Amazon S3 to encrypt your object before saving it on disks in its data centers 
# and then decrypt it when you download the objects. To configure server-side encryption, see Specifying server-
# side encryption with AWS KMS (SSE-KMS) or Specifying Amazon S3 encryption.
    # SSE-S3: Encryption where by keys are handled and managed by AWS. 
        # Keys are managed by S3 service
        # Object is encrypted server side
        # AES-256 Encryption type
        # Must set header "X-amz-serverside-encryption":"AES256"
        # Use HTTPS or HTTP

    # SSE-KMS: This uses AWS Key Management Service
        # Advantages are user control and audit trail
        # Object is encrypted server side
        # Must set header "X-amz-serverside-encryption":"aws:kms"
        # # Use HTTPS or HTTP

    # SSE-C: The customer manages their own Keys
        # User provides their own Key in header
        # Encryption in transit is a must(HTTP)


# Client-Side Encryption – Encrypt data client-side and upload the encrypted data to Amazon S3. In this case, 
# you manage the encryption process, the encryption keys, and related tools. To configure client-side encryption, 
# see Protecting data using client-side encryption.
    # All data must be encrypted before sending to S3
    # Customer manages encryption cycle
    # S3 encryption SDK can be used
