#!/usr/bin/env python3

import os
import gzip
import boto3
import sys

# 'gov-lbl-aes-mybucket'
bucket_name = sys.argv[1]
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    if obj.key.endswith('.gz'):
        gz_file = os.path.basename(obj.key)
        bucket.download_file(obj.key, gz_file)

        with gzip.open(gz_file,'r') as fin:        
            for line in fin:        
                print(str(line, 'UTF-8').strip())
