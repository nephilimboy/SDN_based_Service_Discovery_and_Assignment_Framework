#!/usr/bin/env bash

# Commands
# Running Apache web server(httpd) -> sudo docker run -dit --name app1 -p 8080:80 httpd_final


# Modify these parameters before running
DIR=/var/www/html/
RootDir=/var/www/
ContainerNamePrefix=app
ContainerHistoryNamePrefix=history_

# Clean The Log Folder
#rm -rf $DIR*

# Main Loop
while :
do
    # get all running docker container names
    containers=$(sudo docker ps | awk '{if(NR>1) print $NF}')
    # get all log files and delete the ones that its container does not exist
    # (log file's name is always equal to container's name)

    allContainerStats=$(docker stats --no-stream )
    # loop through all containers
	for container in $containers
    do
        # Check whether Container's name start with specific prefix or not
            # Out put would be like below
                #CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
                #e230251af571        app1                0.01%               14.55MiB / 5.752GiB   0.25%               3.09kB / 10.1kB     7.2MB / 0B          82
            containerStats=$(echo "$allContainerStats" | grep $container)
            # Cpu
            cpu=$(echo $containerStats | awk '{print $3}')
            # Memory Usage
            memoryUsage=$(echo $containerStats | awk '{print $7}')

            # Get container's IP address
            containerIP=$(docker exec -it $container ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)

            # Saving extracted data to files (current data file with ">" command & history available file with ">>" command)
            # Creating current log file
            echo  "Cpu $cpu" > $DIR$containerIP
            echo "MemoryUsage $memoryUsage" >> $DIR$containerIP
    done
done




