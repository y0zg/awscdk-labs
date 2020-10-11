from aws_cdk import (
    aws_ec2 as ec2,
    aws_ssm as ssm,
    core
) 

class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ENV variables
        prj_name = self.node.try_get_context("project_name")
        env_name = self.node.try_get_context("env")

        # Self varibales are used if we need to share resources among multiple stacks
        # In CDK 
        # all route tables are defined automatically
        # Internet gateway is configured by default
        self.vpc = ec2.Vpc(self,'dev-VPC',
            cidr="172.32.0.0/16",
            max_azs=2,
            # Allow to get default public dns provided by amazon
            enable_dns_hostnames=True,
            # IP x.x.x.2 leverages amazon dns servers
            # not needed if own dns is used
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                # requires nat gateway
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE,
                    cidr_mask=24
                ),
                # Databases
                ec2.SubnetConfiguration(
                    name="Isolated",
                    subnet_type=ec2.SubnetType.ISOLATED,
                    cidr_mask=24
                )
            ],
            nat_gateways=1
        )

        # get list of subnet ids
        priv_subnets =[subnet.subnet_id for subnet in self.vpc.private_subnets]

        # equal to traditional format
        # ll = []
        # for subnet in self.vpc.private_subnets:
        #     ll.apend(subnet.subnet_id)
        
        # store subnet ids in parameter store
        count = 1
        for ps in priv_subnets:
            ssm.StringParameter(self,'private-subnet-'+str(count),
                string_value=ps,
                parameter_name='/'+env_name+'/private-subnet'+str(count)
            )
            count+=1