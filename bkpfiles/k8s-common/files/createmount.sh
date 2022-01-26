#!/bin/bash

for dir in 1 2 3 4 5 6 7 8 9 10; do
  mkdir /u02/kafka/lpv/$dir
  mkdir /u02/kafka/bind/$dir
  # Add our bind mounts to fstab
  echo "/u02/kafka/lpv/$dir /u02/kafka/bind/$dir none bind 0 0" >> /etc/fstab
done