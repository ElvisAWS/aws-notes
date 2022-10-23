

# By default, an Application Load Balancer routes each request independently to a registered target based on the 
# chosen load-balancing algorithm. However, you can use the sticky session feature (also known as session affinity) 
# to enable the load balancer to bind a user's session to a specific target. This ensures that all requests from 
# the user during the session are sent to the same target. This feature is useful for servers that maintain state 
# information in order to provide a continuous experience to clients. To use sticky sessions, the client must 
# support cookies.

# Application Load Balancers support both duration-based cookies and application-based cookies. Sticky sessions 
# are enabled at the target group level. You can use a combination of duration-based stickiness, application-based 
# stickiness, and no stickiness across your target groups. The key to managing sticky sessions is determining how 
# long your load balancer should consistently route the user's request to the same target. If your application has 
# its own session cookie, then you can use application-based stickiness and the load balancer session cookie follows 
# the duration specified by the application's session cookie. If your application does not have its own session 
# cookie, then you can use duration-based stickiness to generate a load balancer session cookie with a duration 
# that you specify.

# Duration-based cookies:
    # aws elbv2 modify-target-group-attributes --target-group-arn ARN --attributes Key=stickiness.enabled,Value=true Key=stickiness.lb_cookie.duration_seconds,Value=time-in-seconds
# Application-based Cookie:
    # aws elbv2 modify-target-group-attributes --target-group-arn ARN --attributes Key=stickiness.enabled,Value=true Key=stickiness.type,Value=app_cookie Key=stickiness.app_cookie.cookie_name,Value=my-cookie-name Key=stickiness.app_cookie.duration_seconds,Value=time-in-seconds