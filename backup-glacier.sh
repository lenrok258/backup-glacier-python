#!/bin/bash

# Param 1: AWS_ACCESS_KEY_ID 
# Param 2: AWS_SECRET_ACCESS_KEY
# Param 3: AWS_DEFAULT_REGION
# Param 4: AWS_GLACIER_VAULT
# Param 5: Zip password
# Param 6: Input directory
# Param 7: Months range (eg: 1-6 or 6-12)

./.env/bin/python backup_glacier.py $1 $2 $3 $4 $5 $6 $7