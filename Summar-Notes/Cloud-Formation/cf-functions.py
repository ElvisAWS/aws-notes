

# Intrinsic Functions
    # Fn::FindInMap
        # Returns the value of the specified key
    # Fn::GetAtt
        # returns the list of attributes of the specified resource
    # Fn::GetAZs
        # Returns the availability zones
    # Fn::If
        # Condition
    # Fn::ImportValue
        # Import values from another stack by referencing the exporte name
    # Fn::Join
        # Join strings
        # !Join [ delimiter, [ comma-delimited list of values ] ]
        # !Join [ ":", [ a, b, c ] ]
    # Fn::Sub
        # To substitute values
        # !Sub String
"""
!Sub
  - String
  - Var1Name: Var1Value
    Var2Name: Var2Value
"""
    # FN::Ref
        # !Ref returns the value of the parameter or the ID of the resource specified