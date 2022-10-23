

# Mappings
    # When you know in advance what the value is supposed to be, if you do not know, use a parameter
    # The optional Mappings section matches a key to a corresponding set of named values. For example, if you want 
    # to set values based on a region, you can create a mapping that uses the region name as a key and contains the 
    # values you want to specify for each specific region. You use the Fn::FindInMap intrinsic function to retrieve 
    # values in a map. You can't include parameters, pseudo parameters, or intrinsic functions in the Mappings section.
"""
AWSTemplateFormatVersion: "2010-09-09"
Mappings: 
  RegionMap: 
    us-east-1:
      HVM64: ami-0ff8a91507f77f867
      HVMG2: ami-0a584ac55a7631c0c
    us-west-1:
      HVM64: ami-0bdb828fd58c52235
      HVMG2: ami-066ee5fd4a9ef77f1
    eu-west-1:
      HVM64: ami-047bb4163c506cd98
      HVMG2: ami-0a7c483d527806435
    ap-northeast-1:
      HVM64: ami-06cd52961ce9f0d85
      HVMG2: ami-053cdd503598e4a9d
    ap-southeast-1:
      HVM64: ami-08569b978cc4dfa10
      HVMG2: ami-0be9df32ae9f92309
Resources: 
  myEC2Instance: 
    Type: "AWS::EC2::Instance"
    Properties: 
      ImageId: !FindInMap [RegionMap, !Ref "AWS::Region", HVM64]
      InstanceType: m1.small

"""