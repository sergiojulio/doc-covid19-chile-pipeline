 
# Secret Manager
# Container Registry
# Cloud Scheduler
# Cloud Run

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53

with Diagram("Covid 19 Chile Etl architecture", show=False):
    
    github = ECS("Github")

    with Cluster("Google Cloud Platform"):

        cloud_scheduler = RDS("Cloud Scheduler")

        with Cluster("Execution"):

            cloud_run = RDS("Cloud Run")
            cloud_run << [RDS("Secret Manager"), RDS("Container Registry")]

    cloud_scheduler >> cloud_run

    cloud_run >> github 
    cloud_run << github               