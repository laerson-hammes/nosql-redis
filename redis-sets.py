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

    print(conn.sadd(55, "Hadoop", "Spark", "Hive", "Pig"))

    print(conn.smembers(name=55))

    print(conn.scard(name=55))

    print(conn.sismember(name=55, value="Spark"))

    print(conn.srem(55, "Spark"))

    print(conn.sadd(56, "Hadoop", "Solr", "Hive", "Flume"))
    print(conn.sdiff(55, 56))
    print(conn.sdiff(56, 55))
    print(conn.sinter(55, 56))

    print(conn.zadd(name=64, mapping={
        "Hadoop": 0,
        "Solr": 1,
        "Hive": 2,
        "Flume": 3,
    }))

    print(conn.zcard(name=64))

    print(conn.zrank(name=64, value="Solr", withscore=True))

    print(conn.zcount(name=64, min=0, max=3))

    print(conn.zscore(name=64, value="Solr"))

    print(conn.zrange(name=64, start=0, end=3, withscores=True))

    print(conn.zrem(64, "Solr", "Flume"))


if __name__ == '__main__':
    conn: Redis = connection()
    main(conn)
