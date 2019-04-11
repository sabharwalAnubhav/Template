Pre-requisites to run CloudFormation template :

1. Create a key pair for the hosted region and add the key pair name in the template.
   Step to add a new key pair:
   Go to Management console-> Click on EC2-> Click on key Pair on the left side bar under Network and Security-> Create new key pair
2. Find out the AMI id to launch an instance and add in the template. AMI Id’s are specific to regions.
    Go to Management console-> Click on EC2-> Click on Launch Instance-> Copy AMI ID
3. AWS CLI must be installed on your machine to launch Stack.   
4. To launch CloudFormation Stack use the following command:
    aws cloudformation create-stack --stack-name StackName --template-body file://$PWD/yourFileName.yml  --profile yourProfileName 
    
    
    Note: profileName can be create via aws configure --profile yourProfileName
    
 5. After launch of CloudFormation Template.
    SSH to the EC2 instance and run docker container using below command
    
    
    -> docker start -a containerID or docker attach containerID or docker exec -it containerID /bin/bash  
    -> run the python script available at /tmp/udpclient.py to send message to server.
