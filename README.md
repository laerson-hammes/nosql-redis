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