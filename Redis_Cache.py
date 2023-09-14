"""
Connecting to a cluster mode disabled cluster
"""

from redis import Redis
import logging
import time

logging.basicConfig(level=logging.INFO)
redis = Redis(host='primary.xxx.yyyyyy.zzz1.cache.amazonaws.com', port=6379, decode_responses=True, ssl=True, username="example", password="EXAMPLE")

if redis.ping():
    logging.info("Connected to Redis")

# Set and Get strings
keyName='mykey'
currTime=time.ctime(time.time())

# Set the key 'mykey' with the current date and time as value. 
# The Key will expire and removed from cache in 60 seconds.
redis.set(keyName, currTime, ex=60)

# Sleep just for better illustration of TTL (expiration) value
time.sleep(5)

# Retrieve the key value and current TTL
keyValue=redis.get(keyName)
keyTTL=redis.ttl(keyName)

logging.info(f"Key {keyName} was set at {keyValue} and has {keyTTL} seconds until expired")
# ------------------------------------------------------------------------------------------

# Set and Get a hash with multiple items
keyName='mykey'
keyValues={'datetime': time.ctime(time.time()), 'epochtime': time.time()}

# Set the hash 'mykey' with the current date and time in human readable format (datetime field) and epoch number (epochtime field). 
redis.hset(keyName, mapping=keyValues)

# Set the key to expire and removed from cache in 60 seconds.
redis.expire(keyName, 60)

# Sleep just for better illustration of TTL (expiration) value
time.sleep(5)

# Retrieves all the fields and current TTL
keyValues=redis.hgetall(keyName)
keyTTL=redis.ttl(keyName)

logging.info(f"Key {keyName} was set at {keyValues} and has {keyTTL} seconds until expired")
# ------------------------------------------------------------------------------------------

# Publish (write) and subscribe (read) from a Pub/Sub channel

def handlerFunction(message):
    """Prints message got from PubSub channel to the log output

    Return None
    :param message: message to log
    """
    logging.info(message)


# Creates the subscriber connection on "mychannel"
subscriber = redis.pubsub()
subscriber.subscribe(**{'mychannel': handlerFunction})

# Creates a new thread to watch for messages while the main process continues with its routines
thread = subscriber.run_in_thread(sleep_time=0.01)

# Creates publisher connection on "mychannel"
redis.publish('mychannel', 'My message')

# Publishes several messages. Subscriber thread will read and print on log.
for _ in range(10):
    redis.publish('mychannel',time.ctime(time.time()))
    time.sleep(1)



"""
Connecting to a cluster mode enabled cluster
"""

from rediscluster import RedisCluster
import logging

logging.basicConfig(level=logging.INFO)
redis = RedisCluster(startup_nodes=[{"host": "xxx.yyy.clustercfg.zzz1.cache.amazonaws.com","port": "6379"}], decode_responses=True,skip_full_coverage_check=True)

if redis.ping():
    logging.info("Connected to Redis")