# This file contains environment variables that are passed to mesos-slave.
# To get a description of all options run mesos-slave --help; any option
# supported as a command-line option is also supported as an environment
# variable.

# You must at least set MESOS_master.

# The mesos master URL to contact. Should be host:port for
# non-ZooKeeper based masters, otherwise a zk:// or file:// URL.
export MESOS_master=master1:5050
export MESOS_hostname=slave1    # name to display web ui 
export MESOS_ip=10.10.8.147     # ip for host
#Other options you're likely to want to set:


export MESOS_log_dir=/var/log/mesos
export MESOS_work_dir=/var/run/mesos
export MESOS_isolation=cgroups/cpu,cgroups/mem


MESOS_BUILD_DIR=/usr/local/mesos-0.28.2/build
DISTRIBUTE=`echo ${MESOS_BUILD_DIR}/3rdparty/distribute-*/`
MESOS_EGGS=$(find ${MESOS_BUILD_DIR}/src/python/dist -name "*.egg" | tr "\\n" ":")
export PYTHONPATH=$PYTHONPATH:${DISTRIBUTE}:${MESOS_EGGS}
export HADOOP_HOME=/usr/local/hadoop-2.5.0-cdh5.2.0
export LD_LIBRARY_PATH=/usr/local/lib
