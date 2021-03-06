#!/usr/bin/env python3

from aws_cdk import core

from hello.hello_stack import HelloStack


app = core.App()
HelloStack(app, "hello", env={'region': 'us-west-2'})

app.synth()
