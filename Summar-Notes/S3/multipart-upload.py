

# Multi-Part upload
    # Multipart upload allows you to upload a single object as a set of parts. Each part is a contiguous portion 
    # of the object's data. You can upload these object parts independently and in any order. If transmission of 
    # any part fails, you can retransmit that part without affecting other parts. After all parts of your object 
    # are uploaded, Amazon S3 assembles these parts and creates the object. In general, when your object size 
    # reaches 100 MB, you should consider using multipart uploads instead of uploading the object in a single 
    # operation.
        # Using multipart upload provides the following advantages:
            # Improved throughput – You can upload parts in parallel to improve throughput.
            # Quick recovery from any network issues – Smaller part size minimizes the impact of restarting a 
            # failed upload due to a network error.
            # Pause and resume object uploads – You can upload object parts over time. After you initiate a 
            # multipart upload, there is no expiry; you must explicitly complete or stop the multipart upload.
            # Begin an upload before you know the final object size – You can upload an object as you are 
            # creating it.
        # We recommend that you use multipart upload in the following ways:
            # If you're uploading large objects over a stable high-bandwidth network, use multipart upload to 
            # maximize the use of your available bandwidth by uploading object parts in parallel for multi-threaded 
            # performance.
            # If you're uploading over a spotty network, use multipart upload to increase resiliency to network 
            # errors by avoiding upload restarts. When using multipart upload, you need to retry uploading only the 
            # parts that are interrupted during the upload. You don't need to restart uploading your object from the 
            # beginning.
# unfinished parts
    # As a best practice, we recommend you configure a lifecycle rule using the AbortIncompleteMultipartUpload 
    # action to minimize your storage costs. For more information about aborting a multipart upload, see 
    # Aborting a multipart upload.Amazon S3 supports a bucket lifecycle rule that you can use to direct Amazon 
    # S3 to stop multipart uploads that don't complete within a specified number of days after being initiated. 
    # When a multipart upload is not completed within the time frame, it becomes eligible for an abort operation 
    # and Amazon S3 stops the multipart upload (and deletes the parts associated with the multipart upload).
# Aborting a multipart upload
    # After you initiate a multipart upload, you begin uploading parts. Amazon S3 stores these parts, but it 
    # creates the object from the parts only after you upload all of them and send a successful request to 
    # complete the multipart upload (you should verify that your request to complete multipart upload is 
    # successful). Upon receiving the complete multipart upload request, Amazon S3 assembles the parts and 
    # creates an object. If you don't send the complete multipart upload request successfully, Amazon S3 does 
    # not assemble the parts and does not create any object.