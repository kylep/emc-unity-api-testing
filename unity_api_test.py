#!/usr/bin/env python3

import os
import urllib3

from storops import UnitySystem  # https://github.com/emc-openstack/storops
from hurry.filesize import size


# Load the config from environment variables
SAN_IP = os.environ["UNITY_SAN_IP"]
USER = os.environ["UNITY_USER"]
PASSWORD = os.environ["UNITY_PASSWORD"]


# Squelch HTTPS warnings
urllib3.disable_warnings()


# Connect to Unity
unity = UnitySystem(SAN_IP, USER, PASSWORD)


# Collect some basic information - List the storage pools
print("Listing Pools:")
pools = unity.get_pool()
for pool in pools.list:
    print(f"   {pool.name}")


# Show usage details of a specific pool
print("Usage in pool1:")
pool1 = unity.get_pool(name="pool1")
print(f"   Used: {size(pool1.size_used)}")
print(f"   Free: {size(pool1.size_free)}")
print(f"   Total: {size(pool1.size_total)}")
