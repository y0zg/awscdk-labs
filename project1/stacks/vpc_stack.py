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