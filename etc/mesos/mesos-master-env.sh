# This file contains environment variables that are passed to mesos-master.
# To get a description of all options run mesos-master --help; any option
# supported as a command-line option is also supported as an environment
# variable.

export LD_LIBRARY_PATH=/usr/local/lib
# Some options you're likely to want to set:
export MESOS_log_dir=/var/log/mesos
export MESOS_work_dir=/var/lib/mesos
export MESOS_ip=10.10.8.147
export MESOS_port=5050

export HADOOP_HOME=/usr/local/hadoop-2.5.0-cdh5.2.0
