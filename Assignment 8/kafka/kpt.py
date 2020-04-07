from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['sandbox-hdp.hortonworks.com:6667'])


