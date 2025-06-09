from collections import defaultdict

import boto3

ec2_sns = "SNS-Topic:"
ec2_rec = "arn:aws:automate:eu-west-1:ec2:recover"

"""

"""

def lambda_handler(event,context):
    ec2 = boto3.resource("ec2")
    cw = boto3.client("cloudwatch")
    ec2info = defaultdict()
    running_instances = ec2.instances.filter(Filters[{"Name":"tag-key","Values":[
        (Filters=[{Name:"tag-key","Values":[
            (Filters[{"Name":"tag-key","Values":[
                "cloudwatch"],}])
        for instance in running_instances:
            for tag in instance.tags:
                if "Name" in tag["Key"]:
                    name = tag["Value"]
                    
                    ec2info[instance_id] = {"Name":name,"InstanceId":instance.instance_id,}
                    
                    attributes=["Name","InstanceId"]
                    
                    for instance in running_instances:
                        for tag in instance.tags:
                            if "Name" in tag ["Key"]:
                                name = tag["Value"]
                        
            ec2info[instance_id] = {"Name",instance_id,}
            
            attributes= ["Name","InstanceId":instance.instanceId,}
            
         for instance_id, instance in ec2info.items():
             instanceid = instance["InstanceId"]
             nameinsta = instance["Name"]
             print(instanceid,nameinsta)
             
             AlarmName = (nameinsta) + "_CPU_Load_(Lambda)",
             AlarmDescription="CPU Utilization",
             ActionsEnabled=True,
             AlarmActions=["ec2_sns",],
             MetricName="CPUUtilization",
             Namespace="AWS/EC2",
             Statistics="AVERAGE",
             Dimensions=[{"Name":"InstanceId","Value":instace_id},],
             Period=300,
             EvaluationPeriods=1,
             Threshold=70.0,
             ComparisonOperator="GreaterThanOrEqualToThresold")
                   cw.put_metric_alarm(
             AlarmName =(nameinsta) + "_Network_Bandwidth_(Lambda)",
             AlarmDescription="NetworkOut",
             ActionsEnabled=True,
             AlarmActions=["ec2_sns"],
             MetricName="NetworkOut",
             Namespace="AWS/EC2",
             Statistics="Average"
             Dimensions=[{"Name":"InstanceId","Value":instaceid},],
             Period=300,
             EvaluationPeriods=1,
             Threshold=500000000,
             ComparisonOperator=   "GreaterThanOrEqualToThresold")
            cw.put_metric_alarm(
                AlarmName= (nameinsta) + "_StatusCheckFailed_(Lambda)",
                AlarmDescription = "_StatusCheckFailed",
                Name="AWS/EC2",
                Statistics="Average"
                Dimensions=[{"Name":"InstaceId",
                Period=900,
                EvaluationPeriods=1,
                Threshold=1,
                ComparisonOperator="GreaterThanOrEqualToThreshold")
                cw.put_metric_alarm(
                    AlarmName= (nameinsta) + "_StatusCheckFailed_System(Lambda)",
                    ActionsEnabled=True,
                    AlarmActions=[ec2_rec,ec2_sns],
                    MetricName="StatusCheckFailed_System","Value":instanceid},],
                    Period=900,
                    EvaluationPeriods=1,
                    Threshold=1,
                    ComparisonOperator="GreatherThanOrEqualTo"
                    Namespace="AWS/EC@2",
                    Statistics="Average",
                    Dimensions=[{"Name":"InstanceId","Value":instace_id},],
                    Period=900,
                    EvaluationPeriods=1
                    Threshold=2500,
                    ComparisonOperator="GreaterThanOrEqualToThresold")
            cw.put_metric_alarm(
                AlarmName=(nameinsta) + "_DiskReadOps_(Lambda)",
                AlarmDescription="DiskReadOps",
                ActionsEnabled=True,
                AlarmActions="DiskReadOps",
                NameSpace="AWS/EC2",
                Statistics="Average",
                Dimensions="Name":"InstanceId","Value":instace_id},],
                  Period=900,
                  EvaluationPeriods=1,
                  Threshold=2500,
                  ComparisonOperator="GreaterThanOrEqualToThresold")
         cw.put_metric_alarm(
             AlarmName= (nameinsta) + "MemoryUtlization(Lambda)",
             AlarmDescription="MemoryUtilization",
             ActionsEnabled=["ec2_sns",],
             MetricName="MemoryUtilization",
             NameSpace="System/Linux",
             Statistics="Average",
             Dimensions=[{"Name":"InstanceId","}]
             Dimensions=[{"Name":"InstanceId","Value:}]
         )
            )
                )
            )

                   )
            ]}])
        ]}])
    ]