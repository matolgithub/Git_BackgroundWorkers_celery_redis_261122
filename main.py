import redis

redis_client = redis.Redis(host="127.0.0.1", port=6379)
while True:
    with redis_client as client:
        math_expression = input("Enter math expression: ")  # 2+5-1
        if math_expression == "q":
            break
        else:
            client.lpush("math_expression", math_expression)
