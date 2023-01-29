 
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.gcp.compute import Run

with Diagram("pipeline-cloud-run", show=False):
    ELB("lb") >> Run("web") >> RDS("userdb")