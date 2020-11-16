#!/bin/bash

rosrun gazebo_ros spawn_model -file box_make.urdf -sdf -model $1 -y $2 -x $3 -z 5