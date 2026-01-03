"""
yield 关键字用法演示
yield 用于创建生成器，可以暂停函数执行并返回值
"""


# ==================== 1. 基础用法：yield vs return ====================
def get_numbers_return():
    """使用 return（普通函数）"""
    return [1, 2, 3, 4, 5]
    # 后面的代码永远不会执行


def get_numbers_yield():
    """使用 yield（生成器函数）"""
    yield 1  # 暂停，返回 1
    yield 2  # 恢复，暂停，返回 2
    yield 3  # 恢复，暂停，返回 3
    yield 4
    yield 5


print("=" * 50)
print("基础用法演示")
print("=" * 50)

# return 方式
numbers = get_numbers_return()
print(f"return 返回值: {numbers}")
print(f"return 类型: {type(numbers)}")

# yield 方式
numbers_gen = get_numbers_yield()
print(f"yield 返回值: {numbers_gen}")
print(f"yield 类型: {type(numbers_gen)}")

# 使用 for 循环获取生成器的值
print("\n使用 for 循环遍历生成器:")
for num in get_numbers_yield():
    print(f"  {num}")


# ==================== 2. yield 工作原理 ====================
def countdown(n):
    """演示 yield 的执行流程"""
    print("  开始倒计时")
    while n > 0:
        print(f"  即将 yield {n}")
        yield n  # 暂停并返回 n
        n -= 1
        print(f"  恢复执行，n 变为 {n}")
    print("  倒计时结束")


print("\n" + "=" * 50)
print("yield 工作原理演示")
print("=" * 50)

gen = countdown(3)
print(f"创建生成器: {gen}")
print(f"第1次 next(gen): {next(gen)}")
print(f"第2次 next(gen): {next(gen)}")
print(f"第3次 next(gen): {next(gen)}")

# 第4次会抛出 StopIteration 异常
try:
    print(f"第4次 next(gen): {next(gen)}")
except StopIteration:
    print("  生成器已耗尽，抛出 StopIteration 异常")


# ==================== 3. 高级用法：yield 表达式（接收数据）====================
def echo():
    """yield 可以接收发送的值"""
    while True:
        received = yield  # yield 作为表达式，接收 send() 发送的值
        print(f"  收到: {received}")


print("\n" + "=" * 50)
print("yield 表达式演示（接收数据）")
print("=" * 50)

gen = echo()
print("1. 启动生成器（必须先调用 next 或 send(None)）")
next(gen)  # 启动生成器（必须先调用一次）

print("2. 发送数据到生成器")
gen.send("Hello")
gen.send("World")
gen.send(12345)


# ==================== 4. 生成器表达式 ====================
print("\n" + "=" * 50)
print("生成器表达式演示")
print("=" * 50)

# 列表推导式（一次性生成所有值，占用内存）
print("列表推导式：")
squares_list = [x**2 for x in range(10)]
print(f"  结果: {squares_list}")
print(f"  类型: {type(squares_list)}")
print(f"  内存占用较大（一次性生成所有值）")

# 生成器表达式（惰性生成，节省内存）
print("\n生成器表达式：")
squares_gen = (x**2 for x in range(10))
print(f"  结果: {squares_gen}")
print(f"  类型: {type(squares_gen)}")
print(f"  逐个生成值，节省内存")

print("\n遍历生成器表达式:")
for square in squares_gen:
    print(f"  {square}")


# ==================== 5. 无限序列 ====================
def fibonacci():
    """生成无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n" + "=" * 50)
print("无限序列演示（斐波那契数列）")
print("=" * 50)

fib = fibonacci()
print("前15个斐波那契数:")
fib_sequence = []
for _ in range(15):
    fib_sequence.append(next(fib))
print(f"  {fib_sequence}")


# ==================== 6. 读取大文件（节省内存）====================
def read_large_file(filename):
    """逐行读取大文件，节省内存"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


# 创建一个示例文件
import os
filename = 'temp_example.txt'
with open(filename, 'w', encoding='utf-8') as f:
    for i in range(1, 6):
        f.write(f"这是第 {i} 行数据\n")

print("\n" + "=" * 50)
print("读取大文件演示")
print("=" * 50)

print("使用 yield 逐行读取文件:")
for line in read_large_file(filename):
    print(f"  {line}")

# 清理临时文件
os.remove(filename)


# ==================== 7. 管道处理数据 ====================
def read_lines(filename):
    """读取文件的每一行"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def filter_lines(lines, keyword):
    """过滤包含关键词的行"""
    for line in lines:
        if keyword in line:
            yield line


def uppercase(lines):
    """转换为大写"""
    for line in lines:
        yield line.upper()


def add_prefix(lines, prefix):
    """添加前缀"""
    for line in lines:
        yield f"{prefix}: {line}"


# 创建示例文件
filename = 'log_example.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write("INFO: 系统启动\n")
    f.write("ERROR: 数据库连接失败\n")
    f.write("INFO: 用户登录\n")
    f.write("ERROR: 文件未找到\n")
    f.write("INFO: 系统关闭\n")

print("\n" + "=" * 50)
print("管道处理数据演示")
print("=" * 50)

print("原始日志内容:")
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        print(f"  {line.strip()}")

print("\n过滤出 ERROR 行，转大写，并添加前缀:")
# 链式使用生成器
lines = read_lines(filename)
filtered = filter_lines(lines, "ERROR")
uppercased = uppercase(filtered)
prefixed = add_prefix(uppercased, "⚠️")

for line in prefixed:
    print(f"  {line}")

# 清理临时文件
os.remove(filename)


# ==================== 8. yield from（委托生成器）====================
def sub_generator():
    """子生成器"""
    yield 1
    yield 2
    yield 3


def main_generator():
    """主生成器，使用 yield from 委托给子生成器"""
    print("  主生成器开始")
    yield from sub_generator()  # 委托给子生成器
    yield 4
    yield 5
    print("  主生成器结束")


print("\n" + "=" * 50)
print("yield from 委托生成器演示")
print("=" * 50)

print("使用 yield from:")
for value in main_generator():
    print(f"  {value}")


# ==================== 9. 实际应用：批量处理数据 ====================
def batch_processor(data, batch_size):
    """将数据分批处理"""
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:  # 处理剩余数据
        yield batch


print("\n" + "=" * 50)
print("批量处理数据演示")
print("=" * 50)

data = list(range(1, 11))  # 1 到 10
print(f"原始数据: {data}")
print(f"每批大小: 3")

print("分批结果:")
for i, batch in enumerate(batch_processor(data, 3), 1):
    print(f"  第 {i} 批: {batch}")


# ==================== 10. 协程示例（生产者-消费者）====================
def consumer():
    """消费者协程"""
    print("  消费者启动")
    while True:
        item = yield
        print(f"  消费者处理: {item}")


def producer(consumer_gen, items):
    """生产者"""
    print("生产者启动")
    next(consumer_gen)  # 启动消费者
    for item in items:
        print(f"生产者生成: {item}")
        consumer_gen.send(item)


print("\n" + "=" * 50)
print("协程示例（生产者-消费者）")
print("=" * 50)

cons = consumer()
producer(cons, ["苹果", "香蕉", "橙子"])


print("\n" + "=" * 50)
print("演示完成！")
print("=" * 50)
