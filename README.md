# Apache logs from s3 buckets

## Requirements 

- Python 3.x

#### AWS Credentials.

- Assumed to be in .aws/credentials

#### Using python tool and goaccess docker image

- For more info on goaccess go to [url](https://goaccess.io/)
- Generate html report using tools/s3.py 

```
pip install boto3
docker pull  allinurl/goaccess
cd tools
./s3.py <bucket_name> | docker run --rm -i allinurl/goaccess -a -o html --log-format COMBINED - > report.html
```

#### Using python tools and sqlite3

- For more info on apache-log-parser go to [url](https://pypi.org/project/apache-log-parser/)
- For more info on sqlite3  go to [url](https://www.sqlite.org/index.html)
- Use sqlite command line to view logs table in logs.db


```
pip install boto3
pip install apache-log-parser 
cd tools
./s3.py <bucket_name> | parser.py 
```

#### Using logstash

- logstash sample file that downloads gz files from s3 is under logstash directory
