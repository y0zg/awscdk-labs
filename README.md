# awscdk-labs

Documentation: https://github.com/y0zg/docs/blob/master/aws_cdk.md

```
.
├── app.py
├── cdk.json
├── requirements.txt
└── stacks
    └── vpc_stack.py
```


`cdk.json` - contains context variables which are required for our stack to run

`"app": "python app.py",` - runtime (python) and main application file

context variables used in all stacks

```
    "context":{
        "project_name": "serverless",
        "env": "dev"
    }
```

`requirements.txt` - contains all CDK modules that need to be installed using python `pip`

#

```
cdk ls
(node:3442717) ExperimentalWarning: The fs.promises API is experimental
The stack vpc already includes a CDKMetadata resource
vpc
```

```
cdk synth vpc --profile my
```
New file `tree.json` is created which show project structure

```
tree .
.
├── app.py
├── cdk.json
├── cdk.out
│   ├── cdk.out
│   ├── manifest.json
│   ├── tree.json
│   └── vpc.template.json
├── requirements.txt
└── stacks
    ├── __pycache__
    │   └── vpc_stack.cpython-37.pyc
    └── vpc_stack.py
```

`vpc.template.json` - result of `cdk synth` , it generates enture CloudFormation template 

`cdk diff vpc --profile my` - takes existing state and compare  it with change we made

```
[+] AWS::EC2::VPC dev-VPC devVPC1AA5A1CF 
[+] AWS::EC2::Subnet dev-VPC/PublicSubnet1/Subnet devVPCPublicSubnet1Subnet5E7031F3 
[+] AWS::EC2::RouteTable dev-VPC/PublicSubnet1/RouteTable devVPCPublicSubnet1RouteTable1A216D76 
[+] AWS::EC2::SubnetRouteTableAssociation dev-VPC/PublicSubnet1/RouteTableAssociation devVPCPublicSubnet1RouteTableAssociation91008A4E 
[+] AWS::EC2::Route dev-VPC/PublicSubnet1/DefaultRoute devVPCPublicSubnet1DefaultRouteDCEC8BBC 
[+] AWS::EC2::EIP dev-VPC/PublicSubnet1/EIP devVPCPublicSubnet1EIP9AD09B43 
[+] AWS::EC2::NatGateway dev-VPC/PublicSubnet1/NATGateway devVPCPublicSubnet1NATGatewayAC901F3E 
[+] AWS::EC2::Subnet dev-VPC/PublicSubnet2/Subnet devVPCPublicSubnet2Subnet88BE79F5 
[+] AWS::EC2::RouteTable dev-VPC/PublicSubnet2/RouteTable devVPCPublicSubnet2RouteTableFA06D055 
[+] AWS::EC2::SubnetRouteTableAssociation dev-VPC/PublicSubnet2/RouteTableAssociation devVPCPublicSubnet2RouteTableAssociation5F050B60 
[+] AWS::EC2::Route dev-VPC/PublicSubnet2/DefaultRoute devVPCPublicSubnet2DefaultRouteF43440BE 
[+] AWS::EC2::Subnet dev-VPC/PrivateSubnet1/Subnet devVPCPrivateSubnet1SubnetE87A13E1 
[+] AWS::EC2::RouteTable dev-VPC/PrivateSubnet1/RouteTable devVPCPrivateSubnet1RouteTable94C03E5A 
[+] AWS::EC2::SubnetRouteTableAssociation dev-VPC/PrivateSubnet1/RouteTableAssociation devVPCPrivateSubnet1RouteTableAssociationAC478763 
[+] AWS::EC2::Route dev-VPC/PrivateSubnet1/DefaultRoute devVPCPrivateSubnet1DefaultRouteED6B2E94 
[+] AWS::EC2::Subnet dev-VPC/PrivateSubnet2/Subnet devVPCPrivateSubnet2Subnet1CEB740F 
[+] AWS::EC2::RouteTable dev-VPC/PrivateSubnet2/RouteTable devVPCPrivateSubnet2RouteTable58846670 
[+] AWS::EC2::SubnetRouteTableAssociation dev-VPC/PrivateSubnet2/RouteTableAssociation devVPCPrivateSubnet2RouteTableAssociationA10B1144 
[+] AWS::EC2::Route dev-VPC/PrivateSubnet2/DefaultRoute devVPCPrivateSubnet2DefaultRoute2E1F9DE4 
[+] AWS::EC2::Subnet dev-VPC/IsolatedSubnet1/Subnet devVPCIsolatedSubnet1Subnet638EA78D 
[+] AWS::EC2::RouteTable dev-VPC/IsolatedSubnet1/RouteTable devVPCIsolatedSubnet1RouteTable129ACA00 
[+] AWS::EC2::SubnetRouteTableAssociation dev-VPC/IsolatedSubnet1/RouteTableAssociation devVPCIsolatedSubnet1RouteTableAssociation9C8C5FAE 
[+] AWS::EC2::Subnet dev-VPC/IsolatedSubnet2/Subnet devVPCIsolatedSubnet2Subnet6F571C09 
[+] AWS::EC2::RouteTable dev-VPC/IsolatedSubnet2/RouteTable devVPCIsolatedSubnet2RouteTableFB3DBAE2 
[+] AWS::EC2::SubnetRouteTableAssociation dev-VPC/IsolatedSubnet2/RouteTableAssociation devVPCIsolatedSubnet2RouteTableAssociation9FA69C9E 
[+] AWS::EC2::InternetGateway dev-VPC/IGW devVPCIGWE80F99AC 
[+] AWS::EC2::VPCGatewayAttachment dev-VPC/VPCGW devVPCVPCGW6D377A17 
[+] AWS::SSM::Parameter private-subnet-1 privatesubnet1ABCDFA53 
[+] AWS::SSM::Parameter private-subnet-2 privatesubnet2260E229D 
```

```
cdk deploy vpc --profile my

vpc: deploying...
vpc: creating CloudFormation changeset...
[███████████████████████████████▊··························] (17/31)

6:30:24 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack            | vpc
[███████████████████████████████████▌······················] (19/31)
```

