 
# Secret Manager
# Container Registry
# Cloud Scheduler
# Cloud Run
from diagrams import Cluster, Diagram
from diagrams.gcp.security import KeyManagementService as Secret
from diagrams.gcp.devtools import Scheduler
from diagrams.gcp.devtools import ContainerRegistry
from diagrams.gcp.compute import Run
from diagrams.onprem.vcs import Github

with Diagram("Covid 19 Chile Etl architecture", show=False):
    
    github = Github("Github")

    with Cluster("Google Cloud Platform"):

        cloud_scheduler = Scheduler("Cloud Scheduler")

        with Cluster("Execution"):

            cloud_run = Run("Cloud Run")
            cloud_run << [Secret("Secret Manager"), ContainerRegistry("Container Registry")]

    cloud_scheduler >> cloud_run

    cloud_run >> github 
    cloud_run << github               