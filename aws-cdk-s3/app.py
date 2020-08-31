#!/usr/bin/env python3

from aws_cdk import aws_s3, core


app = core.App()
stack = core.Stack(app)

app.synth()