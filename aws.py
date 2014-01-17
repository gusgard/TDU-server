AWS_ACCESS_KEY = 'AKIAJZI75BMMVHTMVVOA' #Your access key
AWS_SECRET_KEY = 'ERwNNG8TCbW4ZOOtm6aWYHIzY+BfeKfhvevvAxAW' #Your secret key

key = AWS_ACCESS_KEY
sk = AWS_SECRET_KEY

import boto.ec2

conn = boto.ec2.connect_to_region(
    'us-west-2',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY,
      )
instances = []

for r in conn.get_all_instances():
    instances.extend(r.instances)
    for item in instances:
        print item.dns_name #for example.

#
#from boto.ec2.autoscale import AutoScalingGroup, LaunchConfiguration, ScalingPolicy
#from boto.ec2.cloudwatch import MetricAlarm
#
#AWS_ACCESS_KEY = 'AKIAJZI75BMMVHTMVVOA' #Your access key
#AWS_SECRET_KEY = 'ERwNNG8TCbW4ZOOtm6aWYHIzY+BfeKfhvevvAxAW' #Your secret key
#
#LAUNCH_CONFIG_NAME = 'foo'
#AMI_ID = 'ami-f83f59c8'
#KEY_NAME = 'pruebaServer'
#LOAD_BALANCER_NAME = 'loadbalancer2'
#SECURITY_GROUPS = ['launch-wizard-5']
#AVAILABILITY_ZONES = ['us-west-1a', 'us-west-1b']
#INSTANCE_TYPE = 'm1.small' # Type of instance to use for new servers.
#GROUP_NAME = 'groupnamehere'
#
## Stuff to do on boot.
#USER_DATA = """#!/bin/sh
#/path/to/do_stuff
#""".strip()
#
#def set_up_aws():
#    lc = LaunchConfiguration(
#        name=LAUNCH_CONFIG_NAME,
#        image_id=AMI_ID,
#        key_name=KEY_NAME,
#        security_groups=SECURITY_GROUPS,
#        user_data=USER_DATA,
#        instance_type=INSTANCE_TYPE,
#        instance_monitoring=True,
#    )
#    conn = boto.connect_autoscale()
#    conn.create_launch_configuration(lc)
#
#    ag = AutoScalingGroup(
#        group_name=GROUP_NAME,
#        load_balancers=[LOAD_BALANCER_NAME],
#        availability_zones=AVAILABILITY_ZONES,
#        launch_config=lc,
#        min_size=2,
#        max_size=20,
#        connection=conn,
#    )
#    conn.create_auto_scaling_group(ag)
#
#    scale_up_policy = ScalingPolicy(
#        name='scale_up',
#        adjustment_type='ChangeInCapacity',
#        as_name=GROUP_NAME,
#        scaling_adjustment=2,
#        cooldown=180,
#    )
#    conn.create_scaling_policy(scale_up_policy)
#    scale_up_policy = conn.get_all_policies(as_group=GROUP_NAME, policy_names=['scale_up'])[0]
#    scale_down_policy = ScalingPolicy(
#        name='scale_down',
#        adjustment_type='ChangeInCapacity',
#        as_name=GROUP_NAME,
#        scaling_adjustment=-1,
#        cooldown=180,
#    )
#    conn.create_scaling_policy(scale_down_policy)
#    scale_down_policy = conn.get_all_policies(as_group=GROUP_NAME, policy_names=['scale_down'])[0]
#
#    cloudwatch = boto.connect_cloudwatch()
#    alarm_dimensions = {'AutoScalingGroupName': GROUP_NAME}
#    scale_up_alarm = MetricAlarm(
#        name='scale_up_on_cpu',
#        namespace='AWS/EC2',
#        metric='CPUUtilization',
#        statistic='Average',
#        comparison='>',
#        threshold='80',
#        period='60', # seconds
#        evaluation_periods=2, # How many `period`s it should wait until the alarm is set off.
#        alarm_actions=[scale_up_policy.policy_arn],
#        dimensions=alarm_dimensions,
#    )
#    cloudwatch.create_alarm(scale_up_alarm)
#    scale_down_alarm = MetricAlarm(
#        name='scale_down_on_cpu',
#        namespace='AWS/EC2',
#        metric='CPUUtilization',
#        statistic='Average',
#        comparison='<',
#        threshold='40',
#        period='60', # seconds
#        evaluation_periods=2, # How many `period`s it should wait until the alarm is set off.
#        alarm_actions=[scale_down_policy.policy_arn],
#        dimensions=alarm_dimensions,
#    )
#    cloudwatch.create_alarm(scale_down_alarm)