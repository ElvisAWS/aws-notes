


# Conditions
    # The optional Conditions section contains statements that define the circumstances under which entities are 
    # created or configured. For example, you can create a condition and then associate it with a resource or output 
    # so that AWS CloudFormation only creates the resource or output if the condition is true. Similarly, you can 
    # associate the condition with a property so that AWS CloudFormation only sets the property to a specific value 
    # if the condition is true. If the condition is false, AWS CloudFormation sets the property to a different value 
    # that you specify.
# Condition intrinsic functions
    # You can use the following intrinsic functions to define conditions:
    # Fn::And
    # Fn::Equals
    # Fn::If
    # Fn::Not
    # Fn::Or

# Examples
    # Simple condition
    # The following sample template includes an EnvType input parameter, where you can specify prod to create a stack 
    # for production or test to create a stack for testing. For a production environment, AWS CloudFormation creates 
    # an Amazon EC2 instance and attaches a volume to the instance. For a test environment, AWS CloudFormation creates 
    # only the Amazon EC2 instance.
    # The CreateProdResources condition evaluates to true if the EnvType parameter is equal to prod. In the sample 
    # template, the NewVolume and MountPoint resources are associated with the CreateProdResources condition. 
    # Therefore, the resources are created only if the EnvType parameter is equal to prod.

"""
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  EnvType:
    Description: Environment type.
    Default: test
    Type: String
    AllowedValues:
      - prod
      - test
    ConstraintDescription: must specify prod or test.
Conditions:
  CreateProdResources: !Equals 
    - !Ref EnvType
    - prod
Resources:
  EC2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      ImageId: ami-0ff8a91507f77f867
  MountPoint:
    Type: 'AWS::EC2::VolumeAttachment'
    Condition: CreateProdResources
    Properties:
      InstanceId: !Ref EC2Instance
      VolumeId: !Ref NewVolume
      Device: /dev/sdh
  NewVolume:
    Type: 'AWS::EC2::Volume'
    Condition: CreateProdResources
    Properties:
      Size: 100
      AvailabilityZone: !GetAtt 
        - EC2Instance
        - AvailabilityZone
"""