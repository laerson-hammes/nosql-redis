# nosql-redis
REDIS NoSQL Database - Consumed in Python

## Menu
- [Install Redis on Docker](https://github.com/laerson-hammes/nosql-redis#install-redis-on-docker)
- [Redis Connection](https://github.com/laerson-hammes/nosql-redis#redis-connection)
- [Redis Operations](https://github.com/laerson-hammes/nosql-redis#redis-operations)
    - [String Operations](https://github.com/laerson-hammes/nosql-redis#strings-operations)
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
If you want, you can use docker-compose.yml file to run docker and docker-commander, but, for this, you need configure .env file and specify REDIS_PASSWORD, REDIS_COMMANDER_USER and REDIS_COMMANDER_PASS. I intend this way, its more simple and more flexible.

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
### String Operations:
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
---
**delete**: Delete a value. Return 1 (if deleted) or 0.
```python
conn.delete(1)
```
---
**type**: Return type of value.
```python
print(conn.type(2))
```
---
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
---
**getrange**: Get value range, you specify the string key and next start and end range, same range in python / other programming languages.
```python
print(conn.getrange(2, 0, 9))
```
---
**strlen**: Get value length
```python
print(conn.strlen(2))
```
### Hashes Operations:
### Lists Operations:
### Sets Operations: