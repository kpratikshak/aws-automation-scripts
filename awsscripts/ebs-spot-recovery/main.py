import argparse
import logging

from supercloud.aws_util import AwsUtil 
from supercloud.ec2_manager import EC2Manager 

REGION = 'region_name'

PROFILE_NAME = 'profile_name'
AVAILABILITY_ZONE = 'availability_zone'

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

class VolumeNotFoundException(Exception):
    pass

class EC2Manager(object):
    def __init__(self, region, profile_name, availability_zone):
        self.client = session.client('ec2')
        self.resource = session.resource('ec2')
        self.dry_run = dry_run
        
        def find_instance_by_id(self, instance_id):
            try:
                instance = self.resource.Instance(instance_id)
            except ClientError as e:
                if e.response['Error']['Code'] == 'InvalidInstanceID.NotFound':
                    raise VolumeNotFoundException('Instance {} not found'.format(instance_id))
                else:
                    raise Exception('Could not find region of InstanceId {}'.format(instance_id)),ex)
                '''
            def mount_volume(self, volume_id, instance_id, mount_point=DEFAULT_MOUNT_POINT):
                self.client.get_waiter(VOLUME_AVAILABLE).wait(VolumeIds=[volume_id])
                volume.attach_to_instn
        self.availability_zone = availability_zone
        
        eip_alloc = ec2_manager.find_or_create_eipalloc(args.service) if args .eip else args.mount_eip
        self.eip_alloc = eip_alloc  
                if eip_alloc:
                    LOG.info('Attaching EIP to instance {}'.format(instance_id))
                    ec2_manager.attach_eip(eip_alloc, instance)
                    
                    if args.volume:
                        volume = ec2_manager.find_volume(volume_id)
                        LOG.info('Attaching volume {} to instance {}'.format(volume_id, instance_id))
                        ec2_manager.attach_volume(volume_id, instance_id, args.mount_point)