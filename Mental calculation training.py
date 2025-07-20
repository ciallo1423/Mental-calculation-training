import random
import winsound

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
        num2 = random.randint(1, 10)
        num1 = num2 * random.randint(1, 10)
    question = f"{num1} {operator} {num2}"
    answer = eval(str(num1) + operator + str(num2))
    return question, answer

print("算数训练开始！输入 'exit' 退出。")
n=0
total=0
while True:
    total += 1
    question, answer = generate_question()
    user_input = input(f"{question} = ")
    if user_input.lower() == 'exit':
        print("训练结束！")
        break
    try:
        if float(user_input) == answer:
            print("正确！")
        else:
            print(f"错误，正确答案是：{answer}")
            winsound.MessageBeep()
            n+=1
    except ValueError:
        print("请输入有效的数字或 'exit' 退出。")
print(f"你总共答了 {total} 次, 错误 {n} 次。")