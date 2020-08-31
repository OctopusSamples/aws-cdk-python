#!/usr/bin/env python3

from aws_cdk import aws_ecs, core


app = core.App()
stack = core.Stack(app)

aws_ecs.Cluster(
    stack,
    cluster_name='mjlCluster',
    id='ecs',
)


app.synth()