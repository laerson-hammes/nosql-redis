# nosql-redis
REDIS NoSQL Database - Consumed in Python

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