import os
import boto3

# הגדרת משתנה סביבה ל-Pulumi (אם נדרש)
os.environ["PULUMI_CONFIG_PASSPHRASE"] = ""

# יצירת לקוח EC2 של AWS
ec2 = boto3.client("ec2")

class EC2Service:
    @staticmethod
    def list_instances():
        """ מחזיר רשימה של כל מופעי EC2 שנוצרו על ידי Pulumi """
        response = ec2.describe_instances(Filters=[{"Name": "tag:CreatedBy", "Values": ["Pulumi"]}])
        instances = []
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "instance_id": instance["InstanceId"],
                    "state": instance["State"]["Name"],
                    "type": instance["InstanceType"],
                    "ami": instance["ImageId"],
                    "name": next((tag["Value"] for tag in instance.get("Tags", []) if tag["Key"] == "Name"), "N/A")
                })
        return {"instances": instances}

    @staticmethod
    def start_instance(instance_id: str):
        """מתחיל מופע EC2 לפי ה-ID"""
        response = ec2.describe_instances(InstanceIds=[instance_id])
        state = response["Reservations"][0]["Instances"][0]["State"]["Name"]

        if state == "stopped":
            ec2.start_instances(InstanceIds=[instance_id])
            return {"message": f"Instance {instance_id} is now starting..."}
        elif state == "running":
            return {"message": f"Instance {instance_id} is already running."}
        else:
            return {"message": f"Instance {instance_id} is in state: {state}."}

    @staticmethod
    def stop_instance(instance_id: str):
        """עוצר מופע EC2 לפי ה-ID"""
        ec2.stop_instances(InstanceIds=[instance_id])
        return {"message": f"Instance {instance_id} is stopping..."}

    @staticmethod
    def terminate_instance(instance_id: str):
        """מסיים מופע EC2 לפי ה-ID"""
        ec2.terminate_instances(InstanceIds=[instance_id])
        return {"message": f"Instance {instance_id} is terminating..."}
