


# Worker-env
    # If your AWS Elastic Beanstalk application performs operations or workflows that take a long time to complete, 
    # you can offload those tasks to a dedicated worker environment. Decoupling your web application front end 
    # from a process that performs blocking operations is a common way to ensure that your application stays 
    # responsive under load.
    # A long-running task is anything that substantially increases the time it takes to complete a request, such 
    # as processing images or videos, sending email, or generating a ZIP archive. These operations can take only 
    # a second or two to complete, but a delay of a few seconds is a lot for a web request that would otherwise 
    # complete in less than 500 ms
# Webserver-env
    # 