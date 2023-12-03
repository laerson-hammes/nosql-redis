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

    if not conn.exists(3):
        conn.set(3, "DESIGNER")
        print(conn.get("3"))

    if not conn.exists(1) or not conn.exists(2):
        many = {
            1: "Engenheiro de dados",
            2: "Engenheiro de software"
        }
        print(conn.mset(many))

    if conn.exists(1):
        print("sss")
        print(conn.delete(1))

    print(conn.type(2))

    print(conn.expire(3, 60))
    print(conn.pexpire(2, 5000))

    print(conn.ttl(3))
    print(conn.pttl(2))

    print(conn.persist(2))

    print(conn.getrange(2, 0, 9))

    print(conn.getset(2, "Engenheiro de dados"))

    print(conn.mget(2, 3, 1))

    print(conn.strlen(2))


if __name__ == '__main__':
    conn: Redis = connection()
    main(conn)
