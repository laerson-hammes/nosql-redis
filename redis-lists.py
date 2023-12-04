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

    print(conn.lpush(44, "MySQL", "Oracle", "PostgreSQL", "SQL Server"))
    print(conn.rpush(44, "DB2"))

    print(conn.linsert(44, where="AFTER", refvalue="Oracle", value="Firebird"))
    print(conn.linsert(44, where="BEFORE", refvalue="Firebird", value="SQLite"))

    print(conn.lrange(44, 0, 3))

    print(conn.lset(44, index=1, value="OtherDB"))

    print(conn.lindex(name=44, index=1))

    print(conn.llen(name=44))

    print(conn.lpop(name=44))

    print(conn.rpop(name=44))


if __name__ == '__main__':
    conn: Redis = connection()
    main(conn)
