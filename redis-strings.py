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

    conn.set("3", "DESIGNER")
    print(conn.get("2"))


if __name__ == '__main__':
    conn: Redis = connection()
    main(conn)
