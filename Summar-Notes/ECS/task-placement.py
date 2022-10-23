

# Task Placement Strategy
    # A task placement strategy is an algorithm for selecting EC2 instances for task placement or tasks for termination. 
    # Task placement strategies can be specified when either running a task or creating a new service. The task placement 
    # strategies can be updated for existing services as well.
    # Types of task placement strategy
        # binpack
            # Tasks are placed on container instances so as to leave the least amount of unused CPU or memory. This 
            # strategy minimizes the number of container instances in use.
            # When this strategy is used and a scale-in action is taken, Amazon ECS terminates tasks. It does this 
            # based on the amount of resources that are left on the container instance after the task is terminated. 
            # The container instance that has the most available resources left after task termination has that task 
            # terminated.
"""
"placementStrategy": [
    {
        "field": "memory",
        "type": "binpack"
    }
]
"""
    
        # random
            # Tasks are placed randomly.
"""
"placementStrategy": [
    {
        "type": "random"
    }
]
"""
        # spread
            # Tasks are placed evenly based on the specified value. Accepted values are instanceId (or host, which 
            # has the same effect), or any platform or custom attribute that's applied to a container instance, such 
            # as attribute:ecs.availability-zone.
            # When the spread strategy is used and a scale-in action is taken, Amazon ECS selects tasks to terminate 
            # that maintain a balance across Availability Zones. Within an Availability Zone, tasks are selected at 
            # random.
"""
"placementStrategy": [
    {
        "field": "attribute:ecs.availability-zone",
        "type": "spread"
    }
]


"placementStrategy": [
    {
        "field": "instanceId",
        "type": "spread"
    }
]
"""


# Task Placement Constraint
    # A task placement constraint is a rule that's considered during task placement. Task placement constraints 
    # can be specified when either running a task or creating a new service. The task placement constraints can 
    # be updated for existing services as well.
    # Amazon ECS supports the following types of task placement constraints:
        # distinctInstance
            # Place each task on a different container instance. This task placement constraint can be specified 
            # when either running a task or creating a new service.
        # memberOf
            # Place tasks on container instances that satisfy an expression.
            # The memberOf task placement constraint can be specified with the following actions:
                # Running a task
                # Creating a new service
                # Creating a new task definition
                # Creating a new revision of an existing task definition
        # ecs.os-family
            # LINUX or WINDOWS_SERVER_<OS_Release>_<FULL or CORE>.
            # The valid values are LINUX or WINDOWS_SERVER_<OS_Release>_<FULL or CORE>. For example, 
            # WINDOWS_SERVER_2022_FULL, WINDOWS_SERVER_2022_CORE, WINDOWS_SERVER_20H2_CORE, WINDOWS_SERVER_2019_FULL, 
            # WINDOWS_SERVER_2019_CORE, and WINDOWS_SERVER_2016_FULL.
            # The ecs.os-family task placement constraint can be specified with the following actions:
            # Running a task
            # Creating a new service
            # Creating a new task definition
            # Creating a new revision of an existing task definition

