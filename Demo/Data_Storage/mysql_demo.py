import pymysql

config = {
          	'host':'127.0.0.1',
         	 'port':3306,
          	'user':'root',
        	  'password':'root',
       	  	 'db':'mysql',
        	  'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

