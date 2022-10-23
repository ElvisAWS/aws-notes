

# Alarms have three main targets
    # EC2
        # Stop
        # Terminate
        # Reboot or Recover
    # Auto Scaling
        # In
        # out
    # SNS
        # Send notifications

# High resolution alarms can be triggered every 1 second with a 10 second interval
# set-alarm-state
    # Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous 
    # value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to 
    # send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an SNS 
    # message.
    # set-alarm-state
        # --alarm-name <value>
        # --state-value <value>
        # --state-reason <value>
        # [--state-reason-data <value>]
        # [--cli-input-json <value>]
        # [--generate-cli-skeleton <value>]
        # [--debug]
        # [--endpoint-url <value>]
        # [--no-verify-ssl]
        # [--no-paginate]
        # [--output <value>]
        # [--query <value>]
        # [--profile <value>]
        # [--region <value>]
        # [--version <value>]
        # [--color <value>]
        # [--no-sign-request]
        # [--ca-bundle <value>]
        # [--cli-read-timeout <value>]
        # [--cli-connect-timeout <value>]
    # Options
        # --alarm-name (string)
            # The name of the alarm.
            # --state-value (string)
            # The value of the state.
            # Possible values:
            # OK
            # ALARM
            # INSUFFICIENT_DATA
