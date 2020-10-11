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

