#!/bin/bash

# Loop to create users on only one Nextcloud instance
for user in $(seq 0 29); do
    # Create user using Docker exec with the specified password
    docker exec -e OC_PASS=14070929@R --user www-data nextcloud_app1_1 /var/www/html/occ user:add --password-from-env "User${user}"
done

