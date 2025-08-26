kafka to mongo and mongo to endpoint

kafka image running container
3 images created local

first app is a publisher of data 
that get 20 messages form sklearn
divided to 2 groups interesting
and not interesting 
the publisher publish the data in two topics in 
kafka
trigger by a endpoint get that publish the 
messages on kafka broker 

second app is a consumer that consume
the interesting topic from the kafka broker
trigger by endpoint get
than saving all data in a mongo db  
by the collection "interesting"
and another endpoint publish the data
reading it from the mongo collection

third app is a consumer that consume
the not_interesting topic from the kafka broker
than saving all data in a mongo db  
by the collection "not_interesting"
and another endpoint publish the data
reading it from the mongo collection


endpoints
producer = localhost:8000/producer
consume interesting = localhost:8001/consume
read interesting = localhost:8001/data
consume not interesting = localhost:8002/consume
read not interesting = localhost:8002/data


mongodb = localhost:27017
kafka = localhost:9092

note:
Kafka topics must exist before publishing messages.
Publisher divides messages automatically into interesting and not_interesting.
Consumer endpoints allow you to trigger the processing manually.




Kafka_to_mongoDB/
├── .gitignore
├── docker-compose.yml
├── README.md
├── requirements.txt
├── .idea/
│   ├── .gitignore
│   ├── Kafka_to_mongoDB.iml
│   ├── misc.xml
│   ├── modules.xml
│   ├── vcs.xml
│   ├── workspace.xml
│   └── inspectionProfiles/
│       ├── profiles_settings.xml
│       └── Project_Default.xml
├── core/
│   ├── consumer.py
│   ├── manage_mongo.py
│   ├── mongo_dal.py
│   └── mongo_WR.py
├── interesting/
│   ├── consumer_interesting_api.py
│   └── Dockerfile
├── not_interesting/
│   ├── consumer_not_interesting_api.py
│   └── Dockerfile
└── producer/
    ├── Dockerfile
    ├── manage_producer.py
    ├── producer_api.py
    ├── producer_conn.py
    └── data/
        └── get_data.py

