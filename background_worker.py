import redis

redis_client = redis.Redis(host="127.0.0.1", port=6379)
while True:
    with redis_client as client:
        math_express_waiting = client.brpop("math_expression")
        print(math_express_waiting, type(math_express_waiting))
