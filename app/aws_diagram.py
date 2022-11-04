from config import OUTPUT_DIRECTORY
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, Route53

with Diagram("Web Service", filename=f"{OUTPUT_DIRECTORY}/web_services", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")


with Diagram(
    "Clustered Web Services",
    filename=f"{OUTPUT_DIRECTORY}/cluster_web_services",
    show=False,
):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"), ECS("web2"), ECS("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
