


# Output
        # The optional Outputs section declares output values that you can import into other stacks (to create 
        # cross-stack references), return in response (to describe stack calls), or view on the AWS CloudFormation 
        # console. For example, you can output the S3 bucket name for a stack to make the bucket easier to find.
        # Output values are available after the stack operation is complete. Stack output values aren't available 
        # when a stack status is in any of the IN_PROGRESS status. We don't recommend establishing dependencies 
        # between a service runtime and the stack output value because output values might not be available at all 
        # times.
"""
Outputs:
  Logical ID:
    Description: Information about the value
    Value: Value to return
    Export:
      Name: Name of resource to export
"""

"""
Export:
  Name: !Join [ ":", [ !Ref "AWS::StackName", AccountVPC ] ]
"""

# Stack output
    # In the following example, the output named BackupLoadBalancerDNSName returns the DNS name for the resource 
    # with the logical ID BackupLoadBalancer only when the CreateProdResources condition is true. (The second 
    # output shows how to specify multiple outputs.)

"""
Outputs:
  BackupLoadBalancerDNSName:
    Description: The DNSName of the backup load balancer
    Value: !GetAtt BackupLoadBalancer.DNSName
    Condition: CreateProdResources
  InstanceID:
    Description: The Instance ID
    Value: !Ref EC2Instance
"""

# Fn::ImportValue
    # The intrinsic function Fn::ImportValue returns the value of an output exported by another stack. You 
    # typically use this function to create cross-stack references. In the following example template snippets, 
    # Stack A exports VPC security group values and Stack B imports them.

# Stack A exports
"""
Outputs:
  PublicSubnet:
    Description: The subnet ID to use for public web servers
    Value:
      Ref: PublicSubnet
    Export:
      Name:
        'Fn::Sub': '${AWS::StackName}-SubnetID'
  WebServerSecurityGroup:
    Description: The security group ID to use for public web servers
    Value:
      'Fn::GetAtt':
        - WebServerSecurityGroup
        - GroupId
    Export:
      Name:
        'Fn::Sub': '${AWS::StackName}-SecurityGroupID'
"""

# Stack B imports
"""
Resources:
  WebServerInstance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t2.micro
      ImageId: ami-a1b23456
      NetworkInterfaces:
        - GroupSet:
            - Fn::ImportValue 
              'Fn::Sub': '${NetworkStackNameParameter}-SecurityGroupID'
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: Fn::ImportValue 
            'Fn::Sub': '${NetworkStackNameParameter}-SubnetID'
"""

# Important
    # You can't use the short form of !ImportValue when it contains a !Sub.

"""
# do not use
               !ImportValue 
'Fn::Sub': '${NetworkStack}-SubnetID' 
"""

"""
Fn::ImportValue:
  !Sub "${NetworkStack}-SubnetID"
"""