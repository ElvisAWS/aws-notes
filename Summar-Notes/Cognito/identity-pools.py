

# Identity pools
    # Get temporary AWS credentials
    # Give them access through cognito identity pool
    # Login through a third party
        # Open ID Connect
        # Public providers e.g FaceBook
        # SAML identity providers
        # Developer authenticated identities
    # Guest Users
        # Create a guest user policy to allow unauthenticated guest access
    # Integrate with User pools, all user in the user pool can access AWS temporary credentials#
    # With an identity pool, your users can obtain temporary AWS credentials to access AWS services, such 
    # as Amazon S3 and DynamoDB. Identity pools support anonymous guest users, as well as the following 
    # identity providers that you can use to authenticate users for identity pools:
        # Amazon Cognito user pools
        # Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple
        # OpenID Connect (OIDC) providers
        # SAML identity providers
        # Developer authenticated identities
        # To save user profile information, your identity pool needs to be integrated with a user pool.