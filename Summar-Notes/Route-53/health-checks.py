
# Checks mainly public resources
# Three health checks
    # Health checks that monitor endpoints
    # Health checks that monitor other health checks (Calculated)
    # Health checks that monitor cloud watch alarm
# Health checks are intergrated with Cloudwatch metrics
# Health checks will only pass if u have 2xx or 3xx status code from the LB
# Private resource health-check
    # Route 53 service lives out in the web thus can't access your VPC or private end points
    # Create a Cloudwatch Metric and accossiate a cloud watch alarm, then create a Health Check that checks 
    # the alarm itself
