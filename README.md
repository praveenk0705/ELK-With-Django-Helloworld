# ELK-With-Django-Helloworld
Route Django server logs to ELK(Elastic Search, LogStash, Kibana) stack



ELK SETUP
For Ubuntu

Install ElasticSearch: https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html
Install Kibana:
https://www.elastic.co/guide/en/kibana/current/setup.html
Install Logstash:
https://www.elastic.co/guide/en/logstash/current/installing-logstash.html


Next Steps:
For Django, we will make use of Python-logstash via pip install python-logstash a python logging handler for logstash.

-pip install python-logstash
-pip install django-elasticsearch-dsl

Connect the dots to an existing Django project :
Make changes inside your settings.py
# settings.py 

INSTALLED_APPS = [
  # .... 
    'django_elasticsearch_dsl',
]

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': '%(levelname)s %(message)s'
        },
  },
  'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.TCPLogstashHandler',
            'host': 'localhost',
            'port': 5959, # Default value: 5959
            'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'django',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': False, # Fully qualified domain name. Default value: false.
            'tags': ['django.request'], # list of tags. Default: None.
        },
  },
  'loggers': {
        'django.request': {
            'handlers': ['logstash'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    }
}

--CREATE A logstash.conf file with the following conf
input {
    tcp {
    port => 5959
    codec => json
  }
}
output {
  elasticsearch {
    hosts => ["localhost:9200"]
  }
}


--Then run logstash as ./logstash -f logstash.conf






ADDITIONAL INSTRUCTIONS TO LOG PROPER MESSAGES FROM DJANGO logging package:
1.
2.


Thats it. you are all set to go. make sure all the ELK stack is up and running, and you can see all your logs in kibana. 

