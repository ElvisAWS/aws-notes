# SSL/TLS:
    # An SSL/TLS certificate is a digital object that allows systems to verify the identity & subsequently 
    # establish an encrypted network connection to another system using the Secure Sockets Layer/Transport Layer 
    # Security (SSL/TLS) protocol. Certificates are used within a cryptographic system known as a public key 
    # infrastructure (PKI). PKI provides a way for one party to establish the identity of another party using 
    # certificates if they both trust a third-party - known as a certificate authority. SSL/TLS certificates thus 
    # act as digital identity cards to secure network communications, establish the identity of websites over the 
    # Internet as well as resources on private networks.
# When you want to use the same public IP address for multiple websites, you have to leverage the SNI extension. 
# Server Name Indication (SNI) is an extension to the Transport Layer Security (TLS) protocol which allows a 
# client to indicate which hostname it wants to connect to. This allows a server to present specific certificates 
# on the same IP address and hence allows multiple secure (HTTPS) websites to be served by the same server.
# The NSX-T Load Balancer supports SNI Certificates on a single Virtual Server (IP Address) with different 
# Server Pools in the backend. This article explains how to configure SNI-based Load Balancing with 3 different 
# secure HTTPS Websites on a single IP Address with the NSX-T 3.1 Load Balancer.