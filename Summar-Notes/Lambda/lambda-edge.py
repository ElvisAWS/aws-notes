

# Lambda@Edge
    # Synchronous invocation
    # Data traffic on the modern Internet is growing rapidly. To keep up with this growth, website and application 
    # owners have turned to CDNs (Content Delivery Networks) like Amazon CloudFront to cache web content on geographically 
    # dispersed servers located at edge locations around the world. End users can expect faster load times and less 
    # load on the origin server. But what if you need to bring the code and its computing closer to your user? This 
    # is where Lambda@Edge can help.
    # What does this Amazon Web Services Solution do?
        # Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to users of your application, 
        # which improves performance and reduces latency. With Lambda@Edge, you don't have to provision or manage 
        # infrastructure in multiple locations around the world. You pay only for the compute time you consume - 
        # there is no charge when your code is not running. 
        # This solution offers a collection of Lambda@Edge applications, covering most common Lambda@Edge user scenarios. 
        # All the Lambda@Edge applications in this solution can be directly deployed into Amazon Web Services console.
    # CloudFront events that can be used to trigger Lambda@Edge
        # Your functions will automatically trigger in response to the following Amazon CloudFront events:
            # Viewer Request
                # This event occurs when an end-user or a device on the Internet makes an HTTP(S) request to 
                # CloudFront, and the request arrives at the edge location closest to that user.
            # Viewer Response
                # This event occurs when the CloudFront server at the edge is ready to respond to the end-user 
                # or the device that made the request.
            # Origin Request
                # This event occurs when the CloudFront edge server does not already have the requested object 
                # in its cache, and the viewer request is ready to be sent to your backend origin web server 
                # (e.g. Amazon EC2 or Amazon S3).
            # Origin Response
                # This event occurs when the CloudFront server at the edge receives a response from your backend 
                # origin web server.
    # Lambda@Edge use cases
        # Performance
            # One of the biggest benefits of using Lambda@Edge is to improve cache hit rates, either by increasing 
            # the likelihood that content will be cached when it is returned from the origin, or by increasing the 
            # availability of content that is already in a cache condition. You can add or modify cache control 
            # headers on responses.
            # Use query string or user agent normalization to reduce request variability
            # Dynamically route to different origins based on attributes of request headers, cookies, or query 
            # strings
        # Dynamic Content
            # With Lambda@Edge, you can dynamically generate content based on request or response attributes.
            # Resize images based on request attributes
            # Do A/B testing
            # Generate a 302/301 redirection response for all requests to an expired or outdated resource
        # Security
            # Lambda@Edge can also be used to handle custom authentication and authorization.
            # Sign requests to custom origins that enforce access control
            # Set up bot detection
            # Add security headers to the response
        # Origin functions
            # In some cases, the origin requires additional request and response logic. You can run your Lambda@Edge 
            # function in CloudFront instead of code running on the origin server for a more seamless solution. 
            # For example, you can implement logic to do the following:
                # Create a user-friendly URL
                # Manage authentication and authorization for origin requests
                # Manipulate URLs or requests to match your origin directory structure
                # Implement custom load balancing and failover logic
                # User tracking and analysis