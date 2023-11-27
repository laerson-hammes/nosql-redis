# nosql-redis
REDIS NoSQL Database - Consumed in Python

## Install Redis on Docker
`docker run -d --cap-add sys_resource --name rp -p 8443:8443 -p 9443:9443 -p 12000:12000 redislabs/redis`

Next, go to https://localhost:8443 and configure redis, you can follow the redis developer guide located at https://developer.redis.com/operate/orchestration/docker/.

After configured, you can access the redis-cli, for this, run the command below:

`docker exec -it rp bash`

Next...

`/opt/redislabs/bin/redis-cli -p {database_port}`

In my case, database port is 13300, you can see it in database settings.

Then, you need to authenticate with database password:

`auth {password}`

Wow, now you can use / consume redis, beautiful...

