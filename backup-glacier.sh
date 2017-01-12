#!/bin/bash

# Param 1: AWS_DEFAULT_REGION
# Param 2: AWS_GLACIER_VAULT
# Param 3: Input directory
# Param 4: Months range (eg: 1-6 or 6-12)

./.env/bin/python backup_glacier.py $1 $2 $3 $4