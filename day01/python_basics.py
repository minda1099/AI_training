"""
Day 1: Python 核心语法速览 - 20 个练习脚本
对比 JavaScript，快速掌握 Python 核心特性
"""

# ============================================================
# 1. 变量与基本类型
# JS: let name = "Minda"; const age = 15;
# ============================================================
name = "Minda"
age = 15
is_engineer = True
print(f"1. 变量: {name}, 年龄: {age}, 工程师: {is_engineer}")

# ============================================================
# 2. f-string 格式化（类比 JS 模板字符串 `${}`）
# ============================================================
years = 15
role = "AI工程师"
intro = f"我是 {name}，拥有 {years} 年前端经验，目标成为 {role}"
print(f"2. f-string: {intro}")

# ============================================================
# 3. 列表操作（类比 JS Array）
# ============================================================
skills = ["TypeScript", "Next.js", "React", "Node.js"]
skills.append("Python")          # JS: push()
skills.insert(0, "AI Engineering")  # JS: unshift()
print(f"3. 列表: {skills}")
print(f"   最后一个: {skills[-1]}")   # 负索引是 Python 特色

# ============================================================
# 4. 列表推导式（JS 中用 map/filter）
# ============================================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n ** 2 for n in numbers]           # JS: numbers.map(n => n**2)
evens = [n for n in numbers if n % 2 == 0]   # JS: numbers.filter(n => n%2===0)
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
print(f"4. 列表推导: 平方={squares[:5]}..., 偶数={evens}, 双倍偶数={doubled_evens}")

# ============================================================
# 5. 字典操作（类比 JS Object / Map）
# ============================================================
engineer = {
    "name": "Minda",
    "skills": ["TypeScript", "Python"],
    "experience": 15,
    "target": "AI Engineer"
}
engineer["day"] = 1                          # JS: obj.day = 1
print(f"5. 字典: {engineer.get('name')}, 技能数: {len(engineer['skills'])}")
print(f"   所有键: {list(engineer.keys())}")

# ============================================================
# 6. 字典推导式
# ============================================================
word_lengths = {word: len(word) for word in ["Python", "JavaScript", "LangChain"]}
print(f"6. 字典推导: {word_lengths}")

# ============================================================
# 7. 元组（不可变列表，JS 中无直接对应）
# ============================================================
coordinates = (37.7749, -122.4194)   # 不可变
x, y = coordinates                   # 解包（JS 解构赋值类似）
print(f"7. 元组解包: x={x}, y={y}")

# ============================================================
# 8. 集合（去重 + 集合运算，JS 中用 Set）
# ============================================================
frontend = {"HTML", "CSS", "JavaScript", "TypeScript", "React"}
backend = {"Python", "Node.js", "SQL", "TypeScript"}
both = frontend & backend   # 交集
only_front = frontend - backend  # 差集
print(f"8. 集合运算: 共同技能={both}, 前端独有={only_front}")

# ============================================================
# 9. 函数定义（与 JS 的差异）
# ============================================================
def greet(name: str, role: str = "开发者") -> str:
    """带类型注解和默认参数的函数"""
    return f"你好，{name}！你是一位出色的 {role}。"

# JS: function greet(name, role="开发者") { return `你好，${name}...` }
message = greet("Minda", "AI工程师")
print(f"9. 函数: {message}")

# ============================================================
# 10. *args 和 **kwargs（可变参数）
# ============================================================
def summarize(*skills, **info):
    """*args = JS rest params (...args); **kwargs 是 Python 特色"""
    skill_list = ", ".join(skills)
    detail = ", ".join(f"{k}={v}" for k, v in info.items())
    return f"技能: [{skill_list}] | 信息: {{{detail}}}"

result = summarize("Python", "LangChain", "RAG", name="Minda", days=30)
print(f"10. 可变参数: {result}")

# ============================================================
# 11. Lambda（类比 JS 箭头函数）
# ============================================================
# JS: const square = (n) => n ** 2
square = lambda n: n ** 2
sorter = lambda item: item["priority"]

tasks = [
    {"name": "学 Python", "priority": 1},
    {"name": "调用 LLM API", "priority": 3},
    {"name": "写练习代码", "priority": 2},
]
sorted_tasks = sorted(tasks, key=sorter)
print(f"11. Lambda 排序: {[t['name'] for t in sorted_tasks]}")

# ============================================================
# 12. 条件表达式（三元运算符）
# ============================================================
# JS: const level = age >= 10 ? "senior" : "junior"
level = "senior" if years >= 10 else "junior"
print(f"12. 三元: {level}")

# ============================================================
# 13. 字符串操作
# ============================================================
text = "  Hello, AI World!  "
print(f"13. 字符串:")
print(f"    strip: '{text.strip()}'")
print(f"    upper: '{text.strip().upper()}'")
print(f"    split: {text.strip().split(', ')}")
print(f"    replace: '{text.strip().replace('World', 'Engineer')}'")
print(f"    startswith: {text.strip().startswith('Hello')}")

# ============================================================
# 14. 字符串切片（Python 特色，JS 用 slice()）
# ============================================================
s = "Python is awesome"
print(f"14. 切片: '{s[7:]}' | 反转: '{s[::-1][:10]}'")

# ============================================================
# 15. enumerate 和 zip（JS 中无直接对应）
# ============================================================
days = ["Day1", "Day2", "Day3"]
topics = ["Python基础", "Python进阶", "LLM API"]
for i, (day, topic) in enumerate(zip(days, topics), start=1):
    print(f"15. enumerate+zip: [{i}] {day}: {topic}")

# ============================================================
# 16. 列表的 map/filter（Python 版）
# ============================================================
# JS: [1,2,3].map(x => x*2).filter(x => x > 2)
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x > 4, doubled))
print(f"16. map/filter: doubled={doubled}, filtered={filtered}")

# ============================================================
# 17. 异常处理（类比 JS try/catch）
# ============================================================
def safe_divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("17. 捕获异常: 除数不能为0！")
        return 0.0
    except TypeError as e:
        print(f"17. 类型错误: {e}")
        return 0.0
    else:
        print(f"17. 成功: {a} / {b} = {result}")
        return result
    finally:
        print("    finally 永远执行（清理资源）")

safe_divide(10, 2)
safe_divide(5, 0)

# ============================================================
# 18. 推导式生成嵌套结构
# ============================================================
# 30天计划矩阵
plan = {
    f"week_{week}": [f"day_{week*7 - 6 + d}" for d in range(7)]
    for week in range(1, 5)
}
print(f"18. 嵌套推导: week_1={plan['week_1']}")

# ============================================================
# 19. 字符串 join（JS: array.join()）
# ============================================================
ai_stack = ["Python", "LangChain", "FastAPI", "ChromaDB", "Docker"]
print(f"19. join: {' → '.join(ai_stack)}")

# ============================================================
# 20. any() / all() 内置函数
# ============================================================
requirements = {
    "python_installed": True,
    "api_key_ready": True,
    "vscode_setup": True,
    "github_account": True,
}
all_ready = all(requirements.values())
any_missing = not all_ready
print(f"20. any/all: 全部就绪={all_ready}, 有缺失={any_missing}")
print(f"    缺失项: {[k for k, v in requirements.items() if not v]}")

print("\n" + "="*50)
print("✅ Day 1 完成！20 个 Python 核心语法练习全部通过")
print("🚀 明天：Python 进阶 - OOP + 异步 + 文件操作")
print("="*50)
