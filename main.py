import redis

redis_client = redis.Redis(host="127.0.0.1", port=6379)
while True:
    with redis_client as client:
        math_expression = input("Enter math expression: ")  # 2+5-1
        if math_expression != "q":
            client.lpush("math_expression", math_expression)
        else:
            break

        calculate_value = client.brpop("answers")[1].decode(encoding="utf-8")
        print(calculate_value)
