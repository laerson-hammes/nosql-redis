# nosql-redis
REDIS NoSQL Database - Consumed in Python

## Menu
- [Install Redis on Docker](https://github.com/laerson-hammes/nosql-redis#install-redis-on-docker)
- [Redis Connection](https://github.com/laerson-hammes/nosql-redis#redis-connection)
- [Redis Operations](https://github.com/laerson-hammes/nosql-redis#redis-operations)
    - [Strings Operations](https://github.com/laerson-hammes/nosql-redis#strings-operations)
    - [Hashes Operations](https://github.com/laerson-hammes/nosql-redis#hashes-operations)
    - [Lists Operations](https://github.com/laerson-hammes/nosql-redis#lists-operations)
    - [Sets Operations](https://github.com/laerson-hammes/nosql-redis#sets-operations)

## Install Redis on Docker
```
docker run -d --cap-add sys_resource --name rp -p 8443:8443 -p 9443:9443 -p 12000:12000 redislabs/redis
```

Next, go to https://localhost:8443 and configure redis, you can follow the redis developer guide located at https://developer.redis.com/operate/orchestration/docker/.

After configured, you can access the redis-cli, for this, run the command below:

```
docker exec -it rp bash
```

Next...

```
/opt/redislabs/bin/redis-cli -p {database_port}
```

In my case, database port is 13300, you can see it in database settings.

Then, you need to authenticate with database password:

```
auth {password}
```

Wow, now you can use / consume redis, beautiful...

---
If you want, you can use docker-compose.yml file to run docker and docker-commander, but, for this, you need configure .env file and specify REDIS_PASSWORD, REDIS_COMMANDER_USER and REDIS_COMMANDER_PASS. I prefere this way, its more simple and more flexible.

Just run:
```
docker-compose up -d
```
or, if you want see logs:
```
docker-compose up
```
Now, you can check if always created successfully. You can access http://127.0.0.1:8081/ an try login, or, access redis-cli, for this:
```
docker exec -it redis redis-cli
```
and then, try login typing:
```
auth {REDIS_PASSWORD}
```

##  Redis Connection
```python
from dotenv import load_dotenv
from redis import Redis
import os


load_dotenv('.env', verbose=True)
HOST: str = os.environ.get('REDIS_HOST')
PORT: int = int(os.environ.get('REDIS_PORT'))
PASSWORD: str = os.environ.get('REDIS_PASSWORD')


def connection() -> Redis:
    return Redis(
        host=HOST,
        port=PORT,
        db=0,
        password=PASSWORD,
        charset='utf-8',
        decode_responses=True
    )

def main(conn: Redis):
    if not conn.ping():
        raise "Connection error while trying to ping"


if __name__ == '__main__':
    conn: Redis = connection()
    main(conn)

```
In the code example i import Redis, of course, to stabilish a connection with the database, dotenv to load .env file and os to get environment variables.

Next, create Redis instance and pass to the constructor function env vars, like host, port and password, and pass either, database, default Redis db is 0, pass charset and decode_responses.

Then, in main function i check if connection can be created, raising exception if not.

## Redis Operations
### Strings Operations:
**SET and GET:**

**set**: Set a value. Return boolean.
```python
conn.set(3, "DESIGNER")
```
**get**: Get a value.
```python
print(conn.get("3"))
```
**getset**: Set new value and return old string value
```python
print(conn.getset(2, "Engenheiro de dados"))
```
---
**Multiple Values - SET:**

**mset**: Set multiple values, pass dictionary / key - value. Return boolean.
```python
many = {
    1: "Engenheiro de dados",
    2: "Engenheiro de software"
}
conn.mset(many)
```
**Multiple Values - GET:**

**mget**: Get multiple values, just pass all keys that you intend get. Return list with all values, None if value does not exist.
```python
print(conn.mget(2, 3, 1))
```
---
**exists**: Check if a value exists. Return boolean.
```python
print(conn.exists(1))
```
**delete**: Delete a value. Return 1 (if deleted) or 0.
```python
conn.delete(1)
```
**type**: Return type of value.
```python
print(conn.type(2))
```
**Expiration - SET:**

**expire**: Set in how many seconds the value will expire. Return boolean.
```python
conn.expire(3, 60)
```
**pexpire**: Set in how many milliseconds the value will expire. Return boolean.
```python
conn.pexpire(2, 5000)
```
**Expiration - GET:**

**ttl**: Get how many seconds left until the value expires
```python
print(conn.ttl(3))
```
**pttl**: Get how many milliseconds left until the value expires
```python
print(conn.pttl(2))
```
---
**persist**: Calcel expiration time, and persist the value in memory. Return boolean.
```python
conn.persist(2)
```
**getrange**: Get value range, you specify the string key and next start and end range, same range in python / other programming languages.
```python
print(conn.getrange(2, 0, 9))
```
**strlen**: Get value length
```python
print(conn.strlen(2))
```
### Hashes Operations:
**SET and GET:**

**hset**: Set hash. You can pass a dictionary or just key, value. Returns the number of fields that were added.

Example with dictionary:
```python
conn.hset(name="register", mapping={
    "name": "Josef",
    "years": 29,
    "email": "josef@gmail.com",
    "city": "San Francisco"
})
```
Example with just key, value:
```python
conn.hset(
    name="address",
    key="city",
    value="San Francisco"
)
```
**hgetall**: Return a Python dict of the hash's name / value pairs.
```python
print(conn.hgetall("register"))
```
**hmget**: Get specific fields from hash. Returns a list. In the example bellow, return just name and email values.
```python
print(conn.hmget("register", "name", "email"))
```
**hvals**: Get all values from hash. Returns a list.
```python
print(conn.hvals("register"))
```
---
**hexists**: Check if a field exists in hash. Return a boolean.
```python
print(conn.hexists("register", "name"))
```
**hkeys**: Get all keys from hash. Returns a list.
```python
print(conn.hkeys("register"))
```
**hlen**: Return the number of elements in hash.
```python
print(conn.hlen("register"))
```
**hdel**: Delete key / keys from hash. Return number of keys been deleted.
```python
print(conn.hdel("register", "city"))
```
### Lists Operations:
**Insertion:**

**lpush**: Insert / push a value into the head of the list. Create list if not exists. Return list length.
```python
print(conn.lpush(44, "MySQL", "Oracle", "PostgreSQL", "SQL Server"))
```
**rpush**: Insert / push a value into the tail of the list. Create list if not exists. Return list length.
```python
print(conn.rpush(44, "DB2"))
```
**linsert**: Insert after / before specific value. Returns the new length of the list on success or -1 if refvalue is not in the list.
```python
print(conn.linsert(44, where="AFTER", refvalue="Oracle", value="Firebird"))
```
```python
print(conn.linsert(44, where="BEFORE", refvalue="Firebird", value="SQLite"))
```
---
**lrange**: Get range of values from the list. Return list with values.
```python
print(conn.lrange(44, 0, 3))
```
**lset**: Update list value, you need pass the index to the value that you will update and new value. Return bool.
```python
print(conn.lset(44, index=1, value="OtherDB"))
```
**lindex**: Get list value by index.
```python
print(conn.lindex(name=44, index=1))
```
**llen**: Return list length.
```python
print(conn.llen(name=44))
```
---
**Removing values from the list:**

**lpop**: Remove first value from the list. Return value deleted.
```python
print(conn.lpop(name=44))
```
**rpop**: Remove last value from the list. Return value deleted.
```python
print(conn.rpop(name=44))
```
### Sets Operations:

**Unordered sets:**

**sadd**: Add value / values to the set, create it if doesn't exist. Return number of elements added to the set.

If you add a existing value, return 0, doesn`t add it to the set.
```python
print(conn.sadd(55, "Hadoop", "Spark", "Hive", "Pig"))
```
**smembers**: Get all set members. Return Python set data object.
```python
print(conn.smembers(name=55))
```
**scard**: Return set length.
```python
print(conn.scard(name=55))
```
**sismember**: Ckeck if a value is member / is in the set. Return bool.
```python
print(conn.sismember(name=55, value="Spark"))
```
**srem**: Remove a value / or values from the set. Return number of removed values.
```python
print(conn.srem(55, "Spark"))
```
---
**Unordered Sets operations:**

**sdiff**: Return set with differences between two sets. Note that in the code below i`m checking the difference from the set with key 55 to the set with key 56.
```python
print(conn.sdiff(55, 56))
```
Next, i`m check the difference from the set with key 56 to the set with key 55.
```python
print(conn.sdiff(56, 55))
```
**sinter**: Check sets intersection. Return set.
```python
print(conn.sinter(55, 56))
```
---
**Ordered Sets:**

**zadd**: Add value / values with score in the set, create it if doesn't exist.

Return number of elements added to the set.
```python
print(conn.zadd(name=64, mapping={
    "Hadoop": 0,
    "Solr": 1,
    "Hive": 2,
    "Flume": 3,
}))
```
**zcard**: Return number of set elements.
```python
print(conn.zcard(name=64))
```
**zrank**: Get index of a set element. If you pass withscore=True return a list with the index and the score, by default withscore is equal False.
```python
print(conn.zrank(name=64, value="Solr"))
```
**zcount**: Count how many elements i have between two numbers, min and max.
```python
print(conn.zcount(name=64, min=0, max=3))
```
**zscore**: Get score for set element. Return a float.
```python
print(conn.zscore(name=64, value="Solr"))
```
**zrange**: Return a list with set members by index, start and end. You can specify order, withscores, and more items.
```python
print(conn.zrange(name=64, start=0, end=3))
```
**zrem**: Remove an element or many elements from the set. Return number of elements removed.
```python
print(conn.zrem(name=64, values="Solr"))
```