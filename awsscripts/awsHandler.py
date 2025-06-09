def create_ec2(client):
    client.run_instance(Imageid=ami_id,MinCount=count,MaxCount=count)
    
    def create_ec2_volume(client,AZ):
        ab = client.create_ec2_volume(AZ)
        return ab 
    
    def create_vpc(client,cidr_block):
        client.create_vpc(cidr_block)
    