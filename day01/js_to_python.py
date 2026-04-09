"""
Day 1 对比练习：JS → Python 翻译
将前端熟悉的 JS 模式翻译成等价的 Python 代码
帮助前端工程师快速建立 Python 语感
"""

# ============================================================
# 1. 数组操作对比
# ============================================================
print("=== 1. 数组 / 列表操作 ===")

# JS: const nums = [3, 1, 4, 1, 5, 9, 2, 6]
# JS: const sorted = [...nums].sort((a, b) => a - b)
# JS: const sum = nums.reduce((acc, n) => acc + n, 0)
# JS: const max = Math.max(...nums)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(nums)           # 不修改原列表
nums_copy = nums[:]                  # 类比 [...nums]
nums_copy.sort()                     # 原地排序
total = sum(nums)                    # 内置 sum，无需 reduce
maximum = max(nums)                  # 内置 max
unique = list(set(nums))             # JS: [...new Set(nums)]

print(f"原始: {nums}")
print(f"排序: {sorted_nums}")
print(f"求和: {total}")
print(f"最大: {maximum}")
print(f"去重: {sorted(unique)}")

# ============================================================
# 2. 对象 / 字典操作对比
# ============================================================
print("\n=== 2. 对象 / 字典操作 ===")

# JS:
# const user = { name: "Minda", age: 15, skills: ["TS", "React"] }
# const { name, ...rest } = user                  // 解构
# const updated = { ...user, role: "AI Engineer" } // 展开合并
# Object.keys(user), Object.values(user), Object.entries(user)

user = {"name": "Minda", "experience": 15, "skills": ["TS", "React"]}

# 解构（Python 用多重赋值或解包）
name = user["name"]
experience = user.get("experience", 0)   # get 带默认值

# 合并字典（Python 3.9+ 用 | 运算符，3.5+ 用 **）
extra = {"role": "AI Engineer", "day": 1}
merged = {**user, **extra}          # 类比 { ...user, ...extra }
# Python 3.9+: merged = user | extra

print(f"name: {name}, experience: {experience}")
print(f"keys: {list(user.keys())}")
print(f"values: {list(user.values())}")
print(f"items: {list(user.items())[:2]}...")
print(f"合并后: {merged}")

# ============================================================
# 3. 函数式编程对比
# ============================================================
print("\n=== 3. 函数式编程对比 ===")

projects = [
    {"name": "电商AI客服", "day": 7,  "difficulty": "medium"},
    {"name": "RAG知识库",   "day": 14, "difficulty": "hard"},
    {"name": "MultiAgent", "day": 21, "difficulty": "hard"},
    {"name": "代码审查",   "day": 28, "difficulty": "expert"},
]

# JS: projects.filter(p => p.difficulty === "hard").map(p => p.name)
hard_projects = [p["name"] for p in projects if p["difficulty"] == "hard"]

# JS: projects.find(p => p.day > 14)
first_late = next((p for p in projects if p["day"] > 14), None)

# JS: projects.every(p => p.day > 0)
all_valid = all(p["day"] > 0 for p in projects)

# JS: projects.some(p => p.difficulty === "expert")
has_expert = any(p["difficulty"] == "expert" for p in projects)

print(f"困难项目: {hard_projects}")
print(f"第一个超过14天: {first_late['name']}")
print(f"全部有效: {all_valid}")
print(f"有专家级: {has_expert}")

# ============================================================
# 4. 异步模式对比（预览，Day 2 深入）
# ============================================================
print("\n=== 4. 异步模式预览 ===")

# JS:
# async function fetchData(url) {
#   const res = await fetch(url)
#   return await res.json()
# }
# Promise.all([fetchData(url1), fetchData(url2)])

import asyncio

async def simulate_api_call(name: str, delay: float) -> dict:
    """模拟异步 API 调用"""
    await asyncio.sleep(delay)  # 类比 JS: await new Promise(r => setTimeout(r, delay))
    return {"api": name, "status": "success"}

async def fetch_all():
    """类比 JS: await Promise.all([...])"""
    results = await asyncio.gather(
        simulate_api_call("DeepSeek", 0.01),
        simulate_api_call("OpenAI", 0.01),
        simulate_api_call("Claude", 0.01),
    )
    return results

# asyncio.run() 类比 JS 中顶层 await（Node.js）
results = asyncio.run(fetch_all())
for r in results:
    print(f"  ✓ {r['api']}: {r['status']}")

# ============================================================
# 5. 错误处理对比
# ============================================================
print("\n=== 5. 错误处理对比 ===")

# JS:
# class ApiError extends Error {
#   constructor(message, statusCode) {
#     super(message)
#     this.statusCode = statusCode
#   }
# }

class ApiError(Exception):
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code

    def __str__(self):
        return f"[{self.status_code}] {super().__str__()}"

def call_api(endpoint: str, api_key: str | None = None):
    # JS: if (!apiKey) throw new ApiError("Missing API key", 401)
    if not api_key:
        raise ApiError("Missing API key", 401)
    return {"data": f"Response from {endpoint}"}

try:
    result = call_api("/v1/chat", api_key=None)
except ApiError as e:
    print(f"捕获 ApiError: {e}")
except Exception as e:
    print(f"未知错误: {e}")

# ============================================================
# 6. 字符串处理对比
# ============================================================
print("\n=== 6. 字符串处理对比 ===")

# JS: template literals, includes, startsWith, endsWith
text = "Hello, AI Engineer Minda!"

# JS: text.includes("AI")
print(f"includes: {'AI' in text}")

# JS: text.split(", ")
parts = text.split(", ")
print(f"split: {parts}")

# JS: text.toLowerCase(), text.toUpperCase()
print(f"大小写: {text.lower()} | {text.upper()}")

# 多行字符串（类比 JS 模板字符串）
multiline = """
第1天目标:
- 安装 Python 环境
- 完成 20 个语法练习
- GitHub 首次 commit
""".strip()
print(f"多行字符串:\n{multiline}")

print("\n" + "="*50)
print("✅ JS → Python 对比练习完成！")
print("💡 核心差异: 列表推导 | 缩进语法 | 内置函数丰富 | 无分号/花括号")
print("="*50)
