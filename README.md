

| Name | Student ID |Program|
| ------------- | ------------- | ------- |
| Roshanak Behrouz  | SM3800030 |  DSAI  |

## Deployment:
### Reason of choices:
- Nextcloud is a collaboration platform focused on file sharing, synchronization, and productivity, while MinIO is an object storage server optimized for scalable storage of unstructured data. Locust is Python based, open source, developer friendly and easy to use. Nginx is Low resource usage, active community users in case of trouble shooting.

### Docker and Docker Compose:
-	Docker: I used Docker to containerize individual components of my file storage system. This approach isolated dependencies and ensured consistent environments across different stages of development and deployment.
-	Docker Compose: With Docker Compose, I defined and ran multi-container Docker applications. I created a docker-compose.yml file to configure my application’s services, networks, and volumes, which included the Nextcloud instances, database servers, and the Nginx reverse proxy.
-	I made a directory named nextcloud and saved my dockercompose file and other necessary files there.

* ```sudo apt update```
* ```sudo apt install docker-ce docker-ce-cli containerd.io```
* ```sudo systemctl status docker```
* ```docker --version```
* ```sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```
* ```sudo chmod +x /usr/local/bin/docker-compose```
* ```docker-compose --version```
* ```mkdir nextcloud && cd nextcloud```
* ```nano docker-compose.yml```
* ```sudo docker-compose up -d```

### Nginx:
-	Reverse Proxy: Nginx was set up as a reverse proxy to distribute incoming user requests efficiently across the two Nextcloud instances, enabling load balancing and providing better resource utilization and fault tolerance.
-	Configuration: I created a Nginx configuration file specifying the upstream servers (Nextcloud instances I have only 2 instances) and the routing logic. Nginx listened on port 80 and proxied the requests to the appropriate Nextcloud instance based on the defined load-balancing strategy. I used 8081,8082 for nextcloud instance1 and 2 respectively.
-	I started docker-compose.yml with only one nextcloud instance to check if it works, then expanded to two next cloud instances.
### Locust for Load Testing:
-	Load Testing: Locust was used to simulate user behavior and test the scalability and performance of my Nextcloud deployment. I defined user tasks in a Python script to mimic file download operations from Nextcloud.
-	Testing Strategy: I configured Locust to generate a specified number of virtual users to perform downloads of special size files i created, testing the system's response to concurrent user actions and monitoring performance metrics like request failure rates and response times.(8089)

+  ```dd if=/dev/zero of=10kB_file.txt bs=1024 count=10```
+  ```dd if=/dev/urandom of=1MB_file.txt bs=1M count=1```
+  ```dd if=/dev/urandom of=1GB_file.txt bs=1M count=1024```


### User Creation and Credential Management:
-	User Generation Script: I created a Bash script to automate the creation of 30 Nextcloud users. This script utilized Docker's exec command to interact with the Nextcloud instance and add users programmatically.
  
```nano create_users.sh``` ```	chmod +x create_users.sh``` ```./create_users.sh```

-	Credential Storage: After generating the users, I stored their credentials (username and password pairs) in a text file located at ~/nextcloud/credentials.txt. This file acted as a centralized repository for all generated user credentials.
-	Credential Usage in Locust: In my Locust script, I implemented logic to read these credentials from the text file. Each simulated user in my Locust tests was assigned a unique set of credentials from this file, allowing for more realistic and varied simulation scenarios.
-	To address the requirements of the project I enabled registration of users from apps in nextcloud so that user can sign-up
-	I create one role of Users for regular users and assign each user to defined role.
-	i manage to dedicate every user private storage space.
-	Admins have the ability to manage the users.
-	I test if users can upload,download and delete files.

### Deployment Steps Overview:
**1. Compose File Development:** Crafted a docker-compose.yml file to orchestrate the services, networks, and volumes configuration for the Nextcloud environments, databases, and the Nginx proxy.

**2. Nginx Setup:** Configured Nginx to serve as a load balancer, distributing incoming requests across two Nextcloud instances to ensure effective load handling and resource utilization.

**3. User Account Creation:** Utilized a Bash script to automate the creation of 30 distinct Nextcloud user accounts, storing their credentials in a centralized text file for accessibility and future test simulations.

**4. Test File Preparation:** Created various-sized test files (10KB, 1MB, and 1GB) and uploaded them to an admin account within Nextcloud. These files served as the target resources for download operations during load testing.

**5. File Sharing Configuration:** Configured the admin account to share the created test files with all user accounts, ensuring each simulated user could access them during the testing phase.

**6. Locust Test Script Setup:** Configured Locust to dynamically read user credentials from the generated text file, simulating distinct login and file download actions for each user, focusing on the shared files for download tasks.

**7. System Launch:** Initiated the orchestrated services using docker-compose up, integrating the Nextcloud instances, databases, and Nginx into a cohesive operational framework.

**8. Load Testing Execution:** Deployed the Locust script to conduct comprehensive load testing, simulating concurrent user interactions to validate system performance and resource scaling under varied load conditions.

**9. Performance Monitoring and Analysis:** Monitored critical metrics throughout the load testing process, evaluating the system's responsiveness, throughput, and overall stability to ensure the infrastructure's readiness for scaled deployment and usage.



# challenges I faced and  manage to solve them:
Throughout the process of setting up my Nextcloud instances with Docker and Nginx for load balancing, I encountered various errors and challenges. Here's a summary:
## 1.	Docker Daemon Access Issues:
-	I encountered permission denied errors when attempting to execute Docker commands, indicating issues with accessing the Docker daemon. This is typically due to the current user not having the necessary permissions to interact with Docker.
-	To solve the permission denied errors when accessing Docker, I either prefixed my Docker commands with sudo to gain elevated permissions or added my user to the Docker group using the command sudo usermod -aG docker $USER, followed by logging out and back in for the changes to take effect.
  
  ```sudo usermod -aG docker $USER```

## 2.	Nginx Configuration Errors:
-	I faced issues with the Nginx configuration, including errors related to the upstream directive placement and binding Nginx to port 80 when the port was already in use. Additionally, there were configuration challenges related to setting up load balancing correctly.
-	I resolved the Nginx configuration issues by editing the nginx.conf file to correct syntax errors and ensure proper upstream configuration for load balancing. I also made sure that Nginx was not attempting to bind to a port already in use, typically by changing or ensuring the port was available. I changed the ports to 8081 and 8082 to access my nextcloud instances.
## 3.	Container Identification Issues:
-	Errors like "No such container" were encountered when I tried to interact with containers that were either not running or incorrectly referenced in my commands.
-	To address the "No such container" errors, I ensured that my Docker containers were up and running using docker-compose up and verified their status with docker ps. I corrected  wrong references in my commands.

   ```docker ps```
   
## 4.	Database Connection Issues:
-	I experienced database connection errors, particularly "Failed to connect to the database" and "Temporary failure in name resolution," indicating issues with the database container's network configuration or the Nextcloud application's database access settings. While I was writing docker compose file I decided to use mysql 5.7 and successfully run nextcloud on localhost but when I was checking Security & setup warnings I noticed that I should use mysql 8.0 or mariadb so I changed it but then I started to get errors.
-	After getting lots of errors I uninstalled docker-compose and install it again and start the project from scratch to solve the issues.

## 5.	Storage Issues:
-	I experienced storage issues while I try to run docker compose up after making changes to the docker-compose.
-	When I faced challenges related to storage from previous unsuccessful attempts , using docker system prune helped by cleaning up the environment. This action could have resolved issues like: Running out of disk space due to accumulated unused Docker images and containers.

  ```docker system prune```
  
## 6.	Locust Testing Challenges:
-	During load testing with Locust, I encountered script errors related to user credential unpacking and incorrect file path references. Additionally, there were performance issues with a high failure rate for file downloads.
-	I addressed the script errors in Locust by correcting the user credentials file format and ensuring it was properly parsed. I also fixed file path references to ensure the Locust tasks could accurately request the target files. At first I get errors on unsuccessful login attemps as I didn’t made users to test. Then I write a bash file to create users then remember that in order to be able to download a file from nextcloud first I need to upload some file there. I uploaded the files I created with bash in admin account and then I gave permission of access to users and fixed the problem.( First I test only with one user and I get failures all the time, then I understand that I need to make users)
## 7.	File Operation Limitations:
-	When attempting to download files among multiple users, I ran into limitations or were unsure how to achieve this with Nextcloud and my Locust testing setup.
-	I addressed the script errors in Locust by correcting the user credentials file format and ensuring it was properly parsed. I also fixed file path references to ensure the Locust tasks could accurately request the target files.


