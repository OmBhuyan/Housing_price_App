# To run in local
-> clone the aws_exploration repo (git clone https://github.com/OmBhuyan/aws_exploration.git)<br>
-> switch to enh/issue#1/EC2-flaskapp branch<br>
-> Run python3 app.py<br>
-> check the localhost:8085 in your browser.<br>

# To run in an EC2 instance
## Launch an Amazon EC2 instance 

Launch a Linux instance using the AWS Management Console.  
Make sure to create EC2 instances in the same region where the S3 bucket has been created. 


Do not choose Proceed without a key pair. Download the key pair after creating. You can't connect to your instance unless you launched it with a key pair for which you have the *.pem* file and you launched it with a security group that allows SSH access from your computer.
Configure the security group to allow incoming traffic only through 8085.   


Check that your instance has passed its status checks. The instance has been launched once the Instance State tab says running along with a green circle.


## Getting started.

### Boto3 Installation


```
$ python -m pip install boto3
```

After installing boto3

Next, set up credentials (in e.g. ``~/.aws/credentials``):

```
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Then, set up a default region (in e.g. ``~/.aws/config``):
```
[default]
region=us-east-1
```

Using Boto3 for reading the contents of the folder
```
$ python test.py
```

## Connect to your EC2 instance
-------------------------------
To access the virtual machine created through AWS. Open your terminal and locate the directory with the *.pem* file.
Type `chmod 600 <my-key-pair>.pem` on the command line in your project directory to restrict read and write permissions to the private key file.
In a terminal window, use the ssh command to connect to the instance. You specify the path and file name of the private key (.pem), the user name for your instance, and the public DNS name or IPv4 address for your instance.  
Specify the ssh command with the path to the private key (.pem) file, the appropriate user name, and the IPv4 address.
```
ssh -i /path/<my-key-pair>.pem ec2-user@my-instance-IPv4-address
```

## Copy files into the EC2-Instance

-> clone the aws_exploration repo (git clone https://github.com/OmBhuyan/aws_exploration.git)<br>
-> switch to enh/issue#1/EC2-flaskapp branch<br>
-> Run python3 app.py<br>
-> check  "http://public-ip:8085/" in your browser.<br>
