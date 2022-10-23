

# Vieweer Protocol policy
    # make sure all request going into Cloud front are secured by doing the below
        # Redirect HTTP to HTTPS
        # Use HTTPS only
    # Origin Protocol Policy (HTTP or S3)
        # HTTPS only
        # Match viewer (HTTP => HTTP & HTTPS => HTTPS)

# **** S3 websites do not support HTTPS


