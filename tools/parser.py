#!/usr/bin/env python3
 
import sys
import sqlite3
import apache_log_parser
 
conn = sqlite3.connect('logs.db')
cur = conn.cursor()
 
cur.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    status INTEGER,
                    request_method TEXT,
                    request_url TEXT,
                    date TEXT
                )
            """)
 
# Pattern below is from the LogFormat setting in apache2.conf/httpd.conf file
# You will likely need to change this value to the pattern your system uses
parser = apache_log_parser.make_parser(
                   "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\""
         )
 
 
try:
    for line in sys.stdin:
        #print(line)
        d = parser(line)
        d['date'] = d['time_received_datetimeobj'].date().isoformat()
        cur.execute("""
                    INSERT INTO logs ( status,  request_method,  request_url,  date)
                                VALUES (:status, :request_method, :request_url, :date)
                 """, d)
 
except:
    pass

cur.close()
conn.commit();
conn.close();
