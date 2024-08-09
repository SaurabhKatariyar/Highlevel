# Setup Apache Spark
### Deployment is motivated by the below blog but a lot of customization were made on top. 

https://www.howtoforge.com/how-to-install-apache-spark-on-ubuntu-22-04/

### Install Java as Apache Spark is based on Java 
```bash
sudo apt-get install default-jdk curl -y
```
### Download latest stable Spark
```bash
wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
```
### Extract the downloaded file
```bash
tar xvf spark-3.5.1-bin-hadoop3.tgz
```
### Switch to root user
```bash
sudo su
```
### Move the extracted file to /opt
```bash
mv spark-3.5.1-bin-hadoop3/ /opt/spark
```
### Define spark path in .bashrc file
#### Open bash script
```bash
nano ~/.bashrc```
```
#### Add following lines to the bashrc file
```bash
export SPARK_HOME=/opt/spark 
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```
### Activate the Spark environment variable using the following command
```bash
source ~/.bashrc
```
### Create a dedicated user to run Apache Spark
```bash
useradd spark
```
### Next, change the ownership of the /opt/spark to spark user and group
```bash
chown -R spark:spark /opt/spark
```
### Create a Systemd Service File for Apache Spark
#### First, create a service file for Spark master using the following command:
```bash
nano /etc/systemd/system/spark-master.service
```
#### Add following lines to the file
```bash
[Unit]
Description=Apache Spark Master
After=network.target

[Service]
Type=forking
User=spark
Group=spark
ExecStart=/opt/spark/sbin/start-master.sh
ExecStop=/opt/spark/sbin/stop-master.sh

[Install]
WantedBy=multi-user.target
```
#### Create a service file for Spark slave/ worker:
```bash
nano /etc/systemd/system/spark-slave.service
```
#### Add following lines to the file
```bash
[Unit]
Description=Apache Spark Worker
After=network.target

[Service]
Type=forking
User=spark
Group=spark
ExecStart=/opt/spark/sbin/start-worker.sh spark://192.168.1.14:7077
ExecStop=/opt/spark/sbin/stop-worker.sh

[Install]
WantedBy=multi-user.target
```
##### Ensure to add the IP and port of master for proper mapping of worker to master.

### Make following changes in spark-env file
#### First copy template file to shell script
```bashcp /opt/spark/conf/spark-env.sh.template /opt/spark/conf/spark-env.sh```
#### Add following line to the shell script
```bash
export SPARK_MASTER_HOST=192.168.1.14
export SPARK_WORKER_MEMORY=1g
export SPARK_WORKER_CORES=2
export SPARK_MASTER_URL=spark://192.168.1.14:7077
export SPARK_WORKER_INSTANCES=4
export SPARK_EXECUTOR_CORES=2
```
##### Configuration for 4 worker nodes is done here in the conf file
### Reload the systemd daemon to apply the changes
```bashsystemctl daemon-reload```

## Setup Spark Cluster
### Enable spark master node
```bash
systemctl start spark-master
systemctl enable spark-master
# Check status
systemctl status spark-master
```
#### Spark master can be seen on UI on this IP https://192.168.1.14:8080

### Launch worker nodes
```bash
sudo -u spark /opt/spark/sbin/start-worker.sh spark://192.168.1.14:7077 --webui-port 8081
sudo -u spark /opt/spark/sbin/start-worker.sh spark://192.168.1.14:7077 --webui-port 8082
sudo -u spark /opt/spark/sbin/start-worker.sh spark://192.168.1.14:7077 --webui-port 8083
sudo -u spark /opt/spark/sbin/start-worker.sh spark://192.168.1.14:7077 --webui-port 8084
```
#### The above will deploy worker node on the ports 8081,8082,8083 and 8084 each with 2 cores and 1 GB memory as specified in spark_conf.sh file above.

## Spark UI after successful deployment
![image info](spark_setup.png)

## Testing the cluster
```bash
spark-submit --master spark://192.168.1.14:7077 --executor-memory 1G --executor-cores 2 --total-executor-cores 4 test_app.py
```
#### The above test_case.py file is included in the repo and was used to test the spark job. Testing was successful with the script running in desired # worker nodes
 
--executor-cores is number of cores each worker will use<br>
--total-executor-cores is total core<br>

So the above job is submitted on 2 nodes only as we have each node with 2 cores and total ask is for 4 cores


