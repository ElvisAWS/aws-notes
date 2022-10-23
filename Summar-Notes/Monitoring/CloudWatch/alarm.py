

# CloudWatch alarms
    # You can add alarms to dashboards, so you can monitor and receive alerts about your AWS resources and applications 
    # across multiple regions. After you add an alarm to a dashboard, the alarm turns gray when it's in the 
    # INSUFFICIENT_DATA state and red when it's in the ALARM state. The alarm is shown with no color when it's in the OK 
    # state.
    # An alarm can watch a metric in the same account. If you have enabled cross-account functionality in your CloudWatch 
    # console, you can also create alarms that watch metrics in other AWS accounts. Creating cross-account composite alarms 
    # is not supported. Creating cross-account alarms that use math expressions is supported, except that the 
    # ANOMALY_DETECTION_BAND, INSIGHT_RULE, and SERVICE_QUOTA functions are not supported for cross-account alarms.
    # You can create metric and composite alarms in Amazon CloudWatch.
    # Metric Alarm
        # A metric alarm watches a single CloudWatch metric or the result of a math expression based on CloudWatch 
        # metrics. The alarm performs one or more actions based on the value of the metric or expression relative 
        # to a threshold over a number of time periods. The action can be sending a notification to an Amazon SNS 
        # topic, performing an Amazon EC2 action or an Amazon EC2 Auto Scaling action, or creating an OpsItem or 
        # incident in Systems Manager.
    # Composit Alarm
        # A composite alarm includes a rule expression that takes into account the alarm states of other alarms that 
        # you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met. 
        # The alarms specified in a composite alarm's rule expression can include metric alarms and other composite 
        # alarms. Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create 
        # a composite alarm and set up alerts only for the composite alarm. For example, a composite might go into ALARM 
        # state only when all of the underlying metric alarms are in ALARM state.