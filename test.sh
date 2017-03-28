#!/usr/bin/env bash
for h in $(/opt/openstack-ansible/scripts/inventory-manage.py  -f /etc/rpc_deploy/rpc_inventory.json -l | awk
'/cinder_volumes_container/ {print $2}' ); do
  /opt/openstack-ansible/scripts/inventory-manage.py -f /etc/rpc_deploy/rpc_inventory.json -r $h;
done