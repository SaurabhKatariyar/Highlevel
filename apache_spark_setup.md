<h1> Setup Apache Spark </h1>

https://www.howtoforge.com/how-to-install-apache-spark-on-ubuntu-22-04/

<h3>Install Java as Apache Spark is based on Java </h3>
<code>sudo apt-get install default-jdk curl -y</code><br>
<h3>Download latest stable Spark</h3>
<code>wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz</code>
<h3>Extract the downloaded file</h3>
<code>tar xvf spark-3.5.1-bin-hadoop3.tgz</code>
<h3>Switch to root user</h3>
<code>sudo su</code>
<h3>Move the extracted file to /opt</h3>
<code>mv spark-3.5.1-bin-hadoop3/ /opt/spark</code>
<h3>Define spark path in .bashrc file</h3>
<h4>Open bash script</h4>
<code>nano ~/.bashrc</code>
<h4>Add following lines to the bashrc file</h4>
<code>export SPARK_HOME=/opt/spark <br>
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
</code>
<h3>Activate the Spark environment variable using the following command</h3>
<code>source ~/.bashrc</code>





![image info](spark_setup.png)



[blog]: https://www.howtoforge.com/how-to-install-apache-spark-on-ubuntu-22-04/