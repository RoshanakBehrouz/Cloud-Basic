# Cloud-Basic Final Project

| Name | Student ID |Program|
| ------------- | ------------- | ------- |
| Roshanak Behrouz  | SM3800030 |  DSAI  |

# challenges I faced and solved:
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
-	To address the "No such container" errors, I ensured that my Docker containers were up and running using docker-compose up and verified their status with docker ps. I corrected  wrong references in my commands or scripts.

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
-	I addressed the script errors in Locust by correcting the user credentials file format and ensuring it was properly parsed. I also fixed file path references to ensure the Locust tasks could accurately request the target files. At first I get errors on unsuccessful login attemps as I didn’t made users to test. Then I write a bash file to create users then remmeber that in order to be able to download a file from nextcloud first I nedd to upload some file there. I uploaded the files I created with bash in admin account and then I gave permission of access to users and fixed the problem.( First I test only with one user and I get failures all the time, then I understand that I need to make users)
## 7.	File Operation Limitations:
-	When attempting to upload or share files among multiple users, I ran into limitations or were unsure how to achieve this with Nextcloud and my Locust testing setup.
-	I addressed the script errors in Locust by correcting the user credentials file format and ensuring it was properly parsed. I also fixed file path references to ensure the Locust tasks could accurately request the target files.
## 8.	File Path and Access Issues in Scripts:
-	There were challenges with file paths and accessing specific files within the Nextcloud environment for testing purposes.
-	Finally I fixed it by uploading the file to admin account and share amonug users.
## 9.	Deployment and Monitoring Complexities:
-	Throughout deployment and monitoring, I adjusted my docker-compose.yml to ensure proper service dependencies and network configurations.

By iteratively addressing each issue with targeted adjustments and verifications, I successfully resolved the challenges and progressed with my Nextcloud deployment and load testing.

