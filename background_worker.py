import redis

redis_client = redis.Redis(host="127.0.0.1", port=6379)
with redis_client as client:
    while True:
        math_express_waiting = client.brpop("math_expression")[1].decode(encoding="utf-8")
        # print(math_express_waiting, type(math_express_waiting))

        answer = round(float(eval(math_express_waiting)), 2)
        print(answer, type(answer))

        client.lpush("answers", answer)
