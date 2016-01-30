from troposphere import Ref, ec2, Not, Equals

from stacker.blueprints.base import Blueprint


class SecurityGroupRules(Blueprint):
    def _get_parameters(self):
        return {
            "MinionSecurityGroup": {
                "type": "AWS::EC2::SecurityGroup::Id",
                "description": "Empire Minion Security Group."},
            "MasterAPIDBSecurityGroup": {
                "type": "AWS::EC2::SecurityGroup::Id",
                "description": "API Database security group."}}

    def create_db_rules(self):
        self.template.add_resource(
            ec2.SecurityGroupIngress(
                "MasterAPIDBMinionAccess",
                IpProtocol='tcp', FromPort=3306, ToPort=3306,
                SourceSecurityGroupId=Ref("MinionSecurityGroup"),
                GroupId=Ref('MasterAPIDBSecurityGroup')))

    def create_template(self):
        self.create_db_rules()
