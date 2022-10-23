

# Amazon ECS cluster capacity provider
    # Determine the infrastructure to use for your tasks. Each cluster has one or more capacity providers and an 
    # optional default capacity provider strategy. The capacity provider strategy determines how the tasks are 
    # spread across the capacity providers. When you run a task or create a service, you may either use the 
    # cluster’s default capacity provider strategy or specify a capacity provider strategy that overrides the cluster’s 
    # default strategy.
# Capacity providers can be used for ECS Fargate tasks, and ECS EC2 backed tasks.
    # Fargate capacity provider
        # enable you to use both Fargate and Fargate Spot capacity with your Amazon ECS 
        # tasks. Fargate Spot uses spare compute capacity and provides up to 70% savings compared to Fargate. When 
        # AWS needs the capacity back, your tasks will be interrupted with a two-minute warning. With Fargate Spot 
        # you can run interruption tolerant Amazon ECS tasks at a fraction of the cost.
    # Amazon ECS on EC2 capacity provider
        # enable customers to use Cluster Auto Scaling, allowing the focus of the customer to shift from managing 
        # autoscaling the backend infrastructure, to focusing on supporting the application. With EC2 Capacity 
        # providers, customers can also spread their tasks across different Auto Scaling groups, for example spreading 
        # tasks across an on-demand Auto Scaling group and an Auto Scaling group composed of EC2 Spot instances.

"""
resource "aws_ecs_cluster" "example" {
  name = "my-cluster"
}

resource "aws_ecs_cluster_capacity_providers" "example" {
  cluster_name = aws_ecs_cluster.example.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}
"""