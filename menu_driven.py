import subprocess
import os
def hadoop():
	while(True):
		os.system("tput setaf 3")
		print("hadoop")
		print("Press 1 : To configure the NameNode")
		print("Press 2 : To start the NameNode")
		print("Press 3 : To stop the NameNode")        
		print("Press 4 : To configure the DataNode") 
		print("Press 5 : To start the DataNode")
		print("Press 6 : To stop the DataNode")
		print("Press 7 : To configure the Client")
		print("Press 8 : To Exit the hadoop menu")
		os.system("tput setaf 7")
	
		ch = int(input("Enter your choice"))

		if ch == 1:
                    os.system("mkdir /namenode")
                    os.system("vi /etc/hadoop/hdfs-site.xml")
                    os.system("vi /etc/hadoop/core-site.xml")
                    print()
                    ch2 = int(input("Enter your choice for master node: "))
                    if ch2 == 2:
                            os.system("hadoop namenode -format")
                            os.system("hadoop-daemon.sh start namenode")
                            os.system("jps")
                    elif ch2 ==3:
                            os.system("hadoop-daemon.sh stop namenode")
                            os.system("jps")
                    else:
                            print("Invalid Choice")

		elif ch == 4:
                    os.system("mkdir /datanode")
                    os.system("vi /etc/hadoop/hdfs-site.xml")
                    os.system("vi /etc/hadoop/core-site.xml")

                    ch2 = int(input("Enter your choice for the slave node: "))
                    if ch2 == 5:
                            os.system("hadoop-daemon.sh start datanode")
                            os.system("jps")
                    elif ch2 ==6:
                            os.system("hadoop-daemon.sh stop namenode")
                            os.system("jps")
                    else:
                            print("Invalid Choice")

		elif ch == 7:
                    os.system("vi /etc/hadoop/core-site.xml")
                    print()
                    print("Press 1 : To upload a file")
                    print("Press 2 : To read a file")
                    print("Press 3 : To create a file in a cluster")
                    print("Press 4 : To create a directory in the cluster")
                    print("Press e : To remove a directory")
                    print()
                    ch3 = int(input("Enter your choice for the client: "))
                    if ch3 == 1:
                            fname = input("Enter file name(with format type): ")
                            os.system("hadoop fs -put /{}".format(fname))
                    elif ch3 ==2:
                            fname = input("Enter file name(with format type): ")
                            os.system("hadoop fs -cat /{}".format(fname))
                    elif ch3 ==3:
                            fname = input("Enter file name(with format type): ")
                            os.system("hadoop fs -touchz /{}".format(fname))
                    elif ch3 == 3:
                            fname = input("Enter file name(with format type): ")
                            os.system("hadoop fs -mkdirz /{}".format(fname))
                    else:
                            print("Invalid Choice")
		else:
                   print("Choice Incorrect")


def aws() :
			while(True) :
				os.system("tput setaf 3")
				print("""
				press 1 : Check AWS version
				press 2 : AWS configuration
				press 3 : AWS login
				press 4 : Create key-pair
				press 5 : Describe key-pair
				press 6 : Delete key-pair
				press 7 : Create security group
				press 8 : Describe security group
				press 9 : Delete security group
				press 10: Launch new EC2 instance
				press 11: Start the stopped instance
				press 12: Stop an running instance
				press 13: View all running and stopped instances
				press 14: Launch new EBS volumn
				press 15: Attach EBS volumn to ec2 instance 
				press 16: View volumes 
				press 17: Delete volume 		
				press 18: Exit the AWS menu 
				""")
				os.system("tput setaf 7")
	
				op =int(input("Enter your choice :"))	
		
				if op==1 :
					os.system("aws --version")

	
				if op==2 :

					os.system("curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\"")					
					os.system("unzip awscliv2.zip")
					os.system("sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin")

				if op==3 :
					os.system("aws configure")

				if op==4 :
					kp=input("Enter key name : \t")
					os.system("aws ec2 create-key-pair --key-name {}".format(kp))

				if op==5 :
					os.system("aws ec2 describe-key-pairs ")

				if op==6 :
					op=input("Enter whether you want to provide key name or key id or both : \t")
					if op=="name" :
						name = input("Enter key name :\t")
						os.system("aws ec2 delete-key-pair --key-name {}".format(name))

					elif op=="id" :
						id=input("Enter key-id : \t")		
						os.system("aws ec2 delete-key-pair --key-pair-id {}".format(id))

					elif op=="both" :
						name=input("Enter key-name : \t")		
						id=input("Enter key-id : \t")		
						os.system("aws ec2 delete-key-pair--key-name {} --key-pair-id {} ".format(name,id))

				if op==7 :
					gname=input("Enter security group name : \t")		
					desc=input("Enter Security group description : \t")
					os.system("aws ec2 create-security-group --description {} --group-name {}".format(desc,gname))

				if op==8 :
					os.system("aws ec2 describe-security-groups")

				if op==9 :
					op=input("Enter whether you want to provide security group name or id or both : \t")
					if op=="name" :
						name = input("Enter security group name :\t")
						os.system("aws ec2 delete-security-group --group-name {}".format(name))

					elif op=="id" :
						id=input("Enter security group id : \t")		
						os.system("aws ec2 delete-security-group --group-id {} ".format(id))

					elif op=="both" :
						name=input("Enter security group name : \t")		
						id=input("Enter security group id : \t")		
						os.system("aws ec2 delete-security-group --group-id {} --group-name {}".format(name,id))


				if op==10 :
					imageid = input("Enter Image id :\t")
					itype = input("Enter Instance type :\t")
					c = input("Enter count(no of devices you want to launch at a time ) :\t")
					kname = input("Enter key name :\t")
					sname = input("Enter security group name :\t")

					os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --key-name {} --security-groups {} ".format(imageid,itype,c,kname,sname))

				if op==11 :
					id=input("Enter instance id : \t" )
					os.system("aws ec2 start-instances --instance-ids {}".format(id))

				if op==12 :
					id=input("Enter instance id : \t" )
					os.system("aws ec2 stop-instances --instance-ids {}".format(id))

				if op==13 :
					os.system("aws ec2 describe-instances")

				if op==14 :
					az=input("Enter Availabilty zone : \t" )
					size=input("Enter size of volume : \t" )
					os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az,size))

				if op==15 :
					id=input("Enter Instance id : \t" )
					vid=input("Enter volume id : \t" )
					device=input("Enter device : \t" )
					os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(device,id,vid))

				if op==16 :
					os.system("aws ec2  describe-volumes")

				if op==17 :
					vid=input("Enter volume id : \t" )
					os.system("aws ec2  delete-volume --volume-id {} ".format(vid))

				if op==18 :
					break


def docker():
	while(True) :
		os.system("tput setaf 3")
		print("""
		press 1 : Configure Docker(Need to Configure Docker then only you can run remaining commands)
		press 2	: Check Docker version
		press 3 : Check docker status
		press 4 : Start docker
		press 5 : Stop docker
		press 6 : Pull Docker Image
		press 7 : Search Docker Image in Docker Hub
		press 8 : Create A new Container
		press 9 : Start stopeed containers
		press 10: Stop running containers
		press 11: Kill Running Docker Container immediately
		press 12: List All Running containers
		press 13: List All Running and exited containers
		press 14: Attach to Running container
		press 15: Create new Image from an edited container
		press 16: List locally stored Docker images
		press 17: Delete stopped container
		press 18: Delete locally stored Docker image 
		press 19: Exit the Docker menu 
		""")
		os.system("tput setaf 7")

	
		op =int(input("Enter your choice :"))	
		
		if op==1 :
			print("""
			press a : Enter filename of docker repo  
			press b : Want to create docker repo file
			""")
			op1=input("Enter your choice : \t")
			if op1=="a":
				fname=input("Enter filename: \t")
			elif op1=="b":
				fname=input("Enter filename to write docker url: \t")
				os.system("touch {}".format(fname))	
				os.system("gedit {}".format(fname))
			os.system("cp {} /etc/yum.repos.d/".format(fname))	
			os.system("yum install docker-ce --nobest")			
		if op==2 :
			os.system("docker --version")			

		if op==3 :
			os.system("systemctl status docker ")
	
		if op==4 :
			os.system("systemctl start docker ")
	
		if op==5 :	
			os.system("systemctl stop docker ")			

		if op==6 :
			image=input("Enter image name and version (if not then it will download latest version of image) : \t")
			os.system("docker pull {}".format(image))
			
		if op==7 :
			image=input("Enter image name and version : \t")
			limit = input("Enter no of images you want to see :\t") 
			limit=limit if limit!=25 else 25
			#print(limit)		
			os.system("docker search --limit {} {}".format(limit,image))
			
		if op==8 :
			ans1 = input("You want to enter name for this newly launched container(y/n) :\t") 				
			if ans1=="y":		
				name = input("Enter name  :\t") 
			ans2 = input("You want interactive/interactive teriminal of this newly launched container(i/it) :\t") 
			
			iname =input("Enter image name : \t")
			if ans1=="n" :
				if ans2=="i":
					os.system("docker run -i {}".format(iname))
		
				if ans2=="it":
					os.system("docker run  -it {}".format(iname))
			else:		
				if ans2=="i":	
					os.system("docker run  -i --name {} {}".format(name,iname))
		
				if ans2=="it":		
					os.system("docker run  -it --name {} {}".format(name,iname))
				
		if op==9 :
			cname = input("Enter container name  :\t") 		
			ans = input("You want interactive teriminal of this newly launched container(y/n) :\t") 
			if ans=="y":
				os.system("docker container start -i {}".format(cname))	
			else:
				os.system("docker container start {}".format(cname))
	
		if op==10 :
			
			cid=input("Enter container id to stop : \t")		
			os.system("docker container stop {}".format(cid))		

		if op==11:
			cid=input("Enter container id to kill immediately: \t")					
			os.system("docker container kill {}".format(cid))		
		
		if op==12:
			os.system("docker ps")
		
		if op==13:
			os.system("docker ps -a")
	
		
		if op==14 :
			cname=input("Enter container name : \t" )
			os.system("docker attach {}".format(cname))
		
		if op==15 :
			cid=input("Enter Coutainer id  of which you want to create the image: \t" )
			iname=input("Enter Image name : \t" )
			os.system("docker commit {} {}".format(cid,iname))
		
		if op==16 :
			os.system("docker images")
		
		if op==17 :
			c=input("Enter Coutainer id or countainer name to delete : \t" )		
			os.system("docker rm {}".format(c))
		
		if op==18 :
			i=input("Enter Image id or Image name : \t" )
			os.system("docker rmi {}".format(i))
		
		if op==19 :
			break

	
def linux():
	
	while(True):
		os.system("tput setaf 3")
		print(""" 
		\t\t\tpress 1 : Print date 
		\t\t\tpress 2 : Print cal 
		\t\t\tpress 3 : Configure web
		\t\t\tpress 4 : Print docker 
		\t\t\tpress 5 : Add user
		\t\t\tpress 6 : Delete user
		\t\t\tpress 7 : Create file 
		\t\t\tpress 8 : Create folder
		\t\t\tpress 9 : Exit 
		""")
		os.system("tput setaf 7")

		ch=int(input("Enter your choice: "))

		if ch == 1:
			os.system("date")
		
		elif ch == 2:
			os.system("cal")

		elif ch == 3:
			os.system("yum install httpd -y")
			os.system("systemctl start httpd")
			os.system("systemctl status httpd")

		elif ch == 4:
			os.system("yum install docker-ce -y")
			os.system("systemctl start docker")
			os.system("systemctl status docker")
	
		elif ch == 5:
			new_user = input("Enter the name of new user: ")
			os.system("sudo useradd {}".format(new_user))
			os.system("id -u {}".format(new_user))
	
		elif ch == 6:
			del_user = input("Enter the name of the user to delete: ")
			os.system("sudo userdel {}".format(del_user))
	
		elif ch == 7:
			filename = input("Enter the filename: ")
			f = os.system("sudo touch {}".format(filename))
			if f != 0:
				print("Some error occurred")
			else:
				print("File created successfully")
	
		elif ch == 8:	
			foldername = input("Enter the foldername: ")
			f = os.system("sudo mkdir {}".format(foldername))
			if f != 0:
				print("Some error occurred")
			else:
				print("Folder created successfully")
		elif ch == 9:
			print("Exiting application")
			break
		else:
			print("Invalid entry")
			input("Press enter to continue")	
			os.system("clear")


os.system("tput setaf 3")
#subprocess.run("tput setaf 3")
while(True) :
	os.system("tput setaf 3")
	print("\t\t\tMenu Driven program ")
	print("\t\t\t*************************")
	print("\t\t\tpress 1 : Run Docker Related commands")
	print("\t\t\tpress 2 : Run Linux commands")
	print("\t\t\tpress 3 : Run Hadoop ")
	print("\t\t\tpress 4 : Aws")
	print("\t\t\tpress 5 : Exit")
	os.system("tput setaf 7")
	op =int(input("Enter option \t"))
	print(" \n ")
	if op==1 :
		docker()
	if op==2 :
		linux()
	if op==3 :
		hadoop()
	if op==4 :
		aws()

	if op==5 :
		break
	
