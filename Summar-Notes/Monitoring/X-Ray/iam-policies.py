

# IAM managed policies for X-Ray
    # To make granting permissions easy, IAM supports managed policies for each service. A service can update these 
    # managed policies with new permissions when it releases new APIs. AWS X-Ray provides managed policies for read 
    # only, write only, and administrator use cases.
    # AWSXRayDaemonWriteAccess 
        # Write permissions for using the X-Ray daemon, AWS CLI, or AWS SDK to upload segment documents and telemetry 
        # to the X-Ray API. Includes read permissions to get sampling rules and report sampling results.

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "xray:PutTraceSegments",
                "xray:PutTelemetryRecords",
                "xray:GetSamplingRules",
                "xray:GetSamplingTargets",
                "xray:GetSamplingStatisticSummaries"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

    # AWSXrayReadOnlyAccess 
        # Read permissions for using the X-Ray console, AWS CLI, or AWS SDK to get trace data and service maps from 
        # the X-Ray API. Includes permission to view sampling rules.

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "xray:GetSamplingRules",
                "xray:GetSamplingTargets",
                "xray:GetSamplingStatisticSummaries",
                "xray:BatchGetTraces",
                "xray:GetServiceGraph",
                "xray:GetTraceGraph",
                "xray:GetTraceSummaries",
                "xray:GetGroups",
                "xray:GetGroup",
                "xray:GetTimeSeriesServiceStatistics",
                "xray:GetInsightSummaries",
                "xray:GetInsight",
                "xray:GetInsightEvents",
                "xray:GetInsightImpactGraph"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}