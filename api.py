from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

ec2_instances = {
    "Reservations": [
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "StateReason": {
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
                        "Code": "Client.UserInitiatedShutdown"
                    },
                    "PublicDnsName": "",
                    "RootDeviceType": "ebs",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "EbsOptimized": False,
                    "LaunchTime": "2018-11-28T22:48:12.000Z",
                    "ProductCodes": [],
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "StateTransitionReason": "User initiated (2018-11-28 22:50:39 GMT)",
                    "InstanceId": "i-02bf8222becfd36e9",
                    "ImageId": "ami-7c807d14",
                    "PrivateDnsName": "",
                    "SecurityGroups": [
                        {
                            "GroupName": "AWS-OpsWorks-Web-Server",
                            "GroupId": "sg-edae7186"
                        },
                        {
                            "GroupName": "AWS-OpsWorks-Default-Server",
                            "GroupId": "sg-fdae7196"
                        }
                    ],
                    "ClientToken": "3b80c500-d1c0-4b1a-ba23-3262656cf80d",
                    "InstanceType": "t1.micro",
                    "NetworkInterfaces": [],
                    "Placement": {
                        "Tenancy": "default",
                        "GroupName": "",
                        "AvailabilityZone": "us-east-1a"
                    },
                    "Hypervisor": "xen",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "Status": "attached",
                                "DeleteOnTermination": True,
                                "VolumeId": "vol-0fc0f377508bf0cc9",
                                "AttachTime": "2018-11-28T22:48:12.000Z"
                            }
                        }
                    ],
                    "Architecture": "x86_64",
                    "KernelId": "aki-919dcaf8",
                    "IamInstanceProfile": {
                        "Id": "AIPAI7ZZ6TN4RVESZQHLI",
                        "Arn": "arn:aws:iam::975658547626:instance-profile/aws-opsworks-ec2-role"
                    },
                    "RootDeviceName": "/dev/sda1",
                    "VirtualizationType": "paravirtual",
                    "Tags": [
                        {
                            "Value": "SILO Scale Stack",
                            "Key": "opsworks:stack"
                        },
                        {
                            "Value": "it-aws04-manager",
                            "Key": "Owner"
                        },
                        {
                            "Value": "Static Web Server",
                            "Key": "opsworks:layer:web"
                        },
                        {
                            "Value": "crumble",
                            "Key": "opsworks:instance"
                        },
                        {
                            "Value": "NEW_TAG",
                            "Key": "NEW_TAG"
                        },
                        {
                            "Value": "DEFAULT",
                            "Key": "Shutdown"
                        },
                        {
                            "Value": "SILO Scale Stack - crumble",
                            "Key": "Name"
                        },
                        {
                            "Value": "2019-02-26",
                            "Key": "DeleteAfter"
                        }
                    ],
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "AmiLaunchIndex": 0
                }
            ],
            "ReservationId": "r-0f5d0aed4a762d2f0",
            "RequesterId": "497757851421",
            "Groups": [
                {
                    "GroupName": "AWS-OpsWorks-Web-Server",
                    "GroupId": "sg-edae7186"
                },
                {
                    "GroupName": "AWS-OpsWorks-Default-Server",
                    "GroupId": "sg-fdae7196"
                }
            ],
            "OwnerId": "975658547626"
        }
    ]
}

sl1_config = {
    "0": {
        "object_info": {
            "5006": {
                "name": "Instance ID",
                "descr": "The unique identifier of this instance."
            },
            "5007": {
                "name": "Image ID",
                "descr": "The Amazon Machine Image (AMI) id which this instance is booted from."
            },
            "5008": {
                "name": "Platform",
                "descr": "A high-level name of the operating system running on the instance. If such instance is Linux/Unix based the Collection Object won't be visible, only if it is Windows"
            },
            "5009": {
                "name": "Root Device",
                "descr": "The root block device (filesystem) of the instance."
            },
            "5010": {
                "name": "Instance Type",
                "descr": "The cpu, core, and memory capacity type-name of this instance.  For example: t1.micro, c1.medium, m1.xlarge."
            },
            "5011": {
                "name": "Instance State",
                "enum": {
                    "pending": "pending",
                    "running": "running",
                    "shutting-down": "shutting-down",
                    "terminated": "terminated",
                    "stopping": "stopping"
                },
                "descr": "The string representation of the instances current state."
            },
            "5012": {
                "name": "Monitoring Level",
                "descr": "Whether or not AWS CloudWatch metrics are reported on a &#39;basic&#39; (5 min.) or &#39;detailed&#39; (1 min.) intervals."
            },
            "5013": {
                "name": "Groups",
                "descr": "A list of all current groups to which this EC2 instance belongs.  Within a VPC, this can change post-launch."
            },
            "5014": {
                "name": "Group",
                "descr": "The name of the initial security group to which this EC2 instance is assigned."
            },
            "5015": {
                "name": "Public DNS Name",
                "descr": "The Public DNS Name (if any) associated with the instance.  This DNS name is generally Internet routable and associated with one or more Elastic IPs."
            },
            "5016": {
                "name": "Private DNS Name",
                "descr": "The private AWS Cloud DNS name associated with the instance.  Each instance will always have at least one Private DNS name."
            },
            "5017": {
                "name": "Private IP Address",
                "descr": "The AWS cloud-local IP address."
            },
            "5018": {
                "name": "Launch Time",
                "descr": "The UTC time when this instance was launched."
            },
            "5019": {
                "name": "Virtualization Type",
                "descr": "This is always listed as &#39;paravirtual&#39; or &#39;hvm&#39; (xen or ovm)."
            },
            "5020": {
                "name": "Reservation",
                "descr": "The unique identifier associated with the Reservation which launched this instance."
            },
            "5021": {
                "name": "Kernel ID",
                "descr": "The kernel&#39;s unique identifier for this Amazon Machine Image (AMI).  This is most useful when running a User Provided Kernel (UPK)."
            },
            "5022": {
                "name": "Persistent Lifecycle",
                "descr": "Whether or not Termination Protection is enabled."
            },
            "5023": {
                "name": "Ramdisk ID",
                "descr": "The unique identifier of the ramdisk (if any) associated with the instance."
            },
            "5024": {
                "name": "AMI Launch Index",
                "descr": "The Amazon Machine Image (AMI) index within the EC2&#39;s launch reservation list."
            },
            "5025": {
                "name": "Elastic IP",
                "descr": "One or more elastic IP addresses assigned to the EC2 instance."
            },
            "5026": {
                "name": "Tenancy",
                "descr": "Multi IAM placement status"
            },
            "5027": {
                "name": "Placement Group",
                "descr": "The Security Group where the instance is placed upon association with a Virtual Private Cloud (VPC)."
            },
            "5028": {
                "name": "Availability Zone",
                "descr": "The Availability Zone under which the EC2 instance will be launched."
            },
            "5029": {
                "name": "Lifecycle",
                "descr": "Whether or not this instance is &#39;normal&#39; or &#39;spot&#39;.  A &#39;spot&#39; lifecycle means this instance&#39;s compute-time was purchased in the &#39;spot market&#39; and has limitations on how, where, and when it can run."
            },
            "5030": {
                "name": "Key Pair Name",
                "descr": "The name of the SSH key associated with the instance."
            },
            "5031": {
                "name": "Instance Index",
                "descr": "The \"device name\" (if any) of this instance along with its zone and ID.  The \"device name\" is the value of the &#39;Name&#39; key in the instance&#39;s launch-time tag set."
            },
            "5032": {
                "name": "Region",
                "descr": "The AWS Region (datacenter) where the instance is located."
            },
            "5033": {
                "name": "Subnet ID",
                "descr": "If associated with a VPC, this is the AWS identifier of the subnet within the VPC where the instance resides."
            },
            "5034": {
                "name": "VPC ID",
                "descr": "If associated with a Virtual Private Cloud (VPC), this is the VPC AWS identifier."
            },
            "5035": {
                "name": "Hypervisor",
                "descr": "The type of root device that the instance uses. Type: String. Valid values: ebs | instance-store"
            },
            "5036": {
                "name": "Architecture",
                "descr": "The instance architecture. Type: String.  Valid values: i386 | x86_64"
            },
            "5037": {
                "name": "Client Token",
                "descr": "The idempotency token you provided when you launched the instance.  Type: String"
            },
            "5038": {
                "name": "EBS Optimized",
                "descr": "Indicates whether the instance is optimized for EBS I/O. Type: xsd:boolean"
            },
            "5039": {
                "name": "Root Device Type",
                "descr": "The type of root device that the instance uses. Type: String. Valid values: ebs | instance-store"
            },
            "5040": {
                "name": "Monitoring State",
                "descr": "Indicates whether monitoring is enabled for the instance. Type: String. Valid values: disabled | enabled"
            },
            "5041": {
                "name": "State Reason",
                "descr": "The reason for the most recent state transition, typically \"User initiated\", that the state of the instance has changed."
            },
            "5054": {
                "name": "Distinguished Name",
                "descr": "The internal EM7 distinguished name of the AWS component.  This follows closely the format of the AWS Amazon Resource Name (ARN)."
            },
            "5055": {
                "name": "Public IP Address",
                "descr": "The public IP address of the instance."
            },
            "5067": {
                "name": "Subnet Component Unique Identifier",
                "descr": "The EM7 component unique identifier for the associated subnet, if any."
            }
        },
        "group_label": "",
        "data": {
            "5006": {
                "0": "i-02bf8222becfd36e9"
            },
            "5007": {
                "0": "ami-7c807d14"
            },
            "5009": {
                "0": "/dev/sda1"
            },
            "5010": {
                "0": "t1.micro"
            },
            "5011": {
                "0": "stopped"
            },
            "5012": {
                "0": "basic"
            },
            "5018": {
                "0": "2018-11-28 22:48:12+00:00"
            },
            "5019": {
                "0": "paravirtual"
            },
            "5020": {
                "0": "r-0f5d0aed4a762d2f0"
            },
            "5021": {
                "0": "aki-919dcaf8"
            },
            "5024": {
                "0": "0"
            },
            "5025": {
                "0": None
            },
            "5026": {
                "0": "default"
            },
            "5028": {
                "0": "us-east-1a"
            },
            "5029": {
                "0": "normal"
            },
            "5031": {
                "0": "SILO Scale Stack - crumble: t1.micro: i-02bf8222becfd36e9"
            },
            "5032": {
                "0": "us-east-1"
            },
            "5035": {
                "0": "xen"
            },
            "5036": {
                "0": "x86_64"
            },
            "5037": {
                "0": "3b80c500-d1c0-4b1a-ba23-3262656cf80d"
            },
            "5038": {
                "0": "False"
            },
            "5039": {
                "0": "ebs"
            },
            "5040": {
                "0": "disabled"
            },
            "5041": {
                "0": "User initiated (2018-11-28 22:50:39 GMT)"
            },
            "5054": {
                "0": "arn:aws:ec2:us-east-1:975658547626:instance/i-02bf8222becfd36e9"
            }
        }
    },
    "18": {
        "object_info": {
            "5048": {
                "name": "Security Group Name",
                "descr": "The name of the security group."
            },
            "5049": {
                "name": "Security Group Id",
                "descr": "The ID of the security group."
            }
        },
        "group_label": "Security Groups",
        "data": {
            "5048": {
                "sg-fdae7196": "AWS-OpsWorks-Default-Server",
                "sg-edae7186": "AWS-OpsWorks-Web-Server"
            },
            "5049": {
                "sg-fdae7196": "sg-fdae7196",
                "sg-edae7186": "sg-edae7186"
            }
        }
    },
    "20": {
        "object_info": {
            "5042": {
                "name": "Block Device Attach Time",
                "descr": "The attach time for an Amazon EBS volume mapped to the instance (for example, 2010-09-15T17:15:20.000Z)"
            },
            "5043": {
                "name": "Block Device Delete On Termination",
                "descr": "Indicates whether the Amazon EBS volume is deleted on instance termination."
            },
            "5044": {
                "name": "Block Device Status",
                "descr": "The status for the Amazon EBS volume. Valid values: attaching | attached | detaching | detached"
            },
            "5045": {
                "name": "Block Device Name",
                "descr": "The device name exposed to the instance (for example, /dev/sdh, or xvdh)."
            },
            "5046": {
                "name": "AWS EC2/EBS Volume",
                "descr": "The volume ID of the Amazon EBS volume."
            }
        },
        "group_label": "Block Device Mapping",
        "data": {
            "5042": {
                "/dev/sda1": "2018-11-28 22:48:12+00:00"
            },
            "5043": {
                "/dev/sda1": "True"
            },
            "5044": {
                "/dev/sda1": "attached"
            },
            "5045": {
                "/dev/sda1": "/dev/sda1"
            },
            "5046": {
                "/dev/sda1": "vol-0fc0f377508bf0cc9"
            }
        }
    },
    "25": {
        "object_info": {
            "5051": {
                "name": "Key",
                "descr": "The tag key.  Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account&#39;s Amazon EC2 instances that helps you track each instance&#39;s owner and stack level. We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add."
            },
            "5052": {
                "name": "Value",
                "descr": "The tag value. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account&#39;s Amazon EC2 instances that helps you track each instance&#39;s owner and stack level. We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add."
            }
        },
        "group_label": "Tags",
        "data": {
            "5051": {
                "opsworks:stack": "opsworks:stack",
                "opsworks:layer:web": "opsworks:layer:web",
                "shutdown": "Shutdown",
                "deleteafter": "DeleteAfter",
                "name": "Name",
                "owner": "Owner",
                "new_tag": "NEW_TAG",
                "opsworks:instance": "opsworks:instance"
            },
            "5052": {
                "opsworks:stack": "SILO Scale Stack",
                "opsworks:layer:web": "Static Web Server",
                "shutdown": "DEFAULT",
                "deleteafter": "2019-02-26",
                "name": "SILO Scale Stack - crumble",
                "owner": "it-aws04-manager",
                "new_tag": "NEW_TAG",
                "opsworks:instance": "crumble"
            }
        }
    },
    "26": {
        "object_info": {
            "5072": {
                "name": "EC2 Unique ID",
                "descr": "The unique identifier of the EC2 Instance that matches the identifier given by the CCC application."
            },
            "5073": {
                "name": "AWS EC2 Identifier Namespace",
                "descr": "The namespace used to link the CCC application."
            }
        },
        "group_label": "CCC Application in AWS EC2 Instance",
        "data": {
            "5072": {
                "0": "i-02bf8222becfd36e9"
            },
            "5073": {
                "0": "ccc_application_aws_ec2_instance_namespace"
            }
        }
    }
}


class EC2(Resource):
    def get(self):
        return ec2_instances, 200


class SL1Config(Resource):
    def get(self):
        return sl1_config, 200


api.add_resource(EC2, "/instances")
api.add_resource(SL1Config, "/device/config_data")

app.run(debug=True)
