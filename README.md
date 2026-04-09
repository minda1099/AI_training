# 🚀 AI 工程师 30 天冲刺 — Minda

> **目标**：30 天从前端老兵转型世界级 AI 应用工程师  
> **开始日期**：2026 年 4 月 9 日  
> **核心理念**：Learn by Building — 每天必须有可运行的代码产出

## 📊 总体进度

| 阶段 | 时间 | 主题 | 状态 |
|------|------|------|------|
| 阶段一 | Day 1–7 | Python + LLM 基础 · 地基建设 | 🟡 进行中 |
| 阶段二 | Day 8–14 | LangChain + RAG · 框架掌握 | ⬜ 待开始 |
| 阶段三 | Day 15–21 | Agent + Dify · Agent 架构 | ⬜ 待开始 |
| 阶段四 | Day 22–30 | 生产部署 + 作品集 · 全面就绪 | ⬜ 待开始 |

---

## ✅ 每日打卡记录

### 阶段一：Python + LLM 基础（Day 1–7）

#### ✅ Day 1 · Python 环境 + 核心语法速览

**学习内容**
- Python 3.11 核心数据类型：变量、字符串、列表、字典、元组、集合
- 列表推导式 / 字典推导式（对比 JS `map`/`filter`）
- 函数定义：类型注解、默认参数、`*args`、`**kwargs`
- 异常处理：`try/except/else/finally`
- 异步预览：`asyncio.gather` 对比 `Promise.all`

**今日交付**
- [x] `day01/python_basics.py` — 20 个核心语法练习脚本（全部可运行）
- [x] `day01/js_to_python.py` — JS → Python 对比翻译练习

**JS → Python 关键对比速查**

| JavaScript | Python |
|-----------|--------|
| `arr.map(x => x*2)` | `[x*2 for x in arr]` |
| `arr.filter(x => x>0)` | `[x for x in arr if x>0]` |
| `arr.find(x => x.id===1)` | `next((x for x in arr if x['id']==1), None)` |
| `{...obj, key: val}` | `{**obj, 'key': val}` |
| `Promise.all([...])` | `asyncio.gather(...)` |
| `` `Hello ${name}` `` | `f"Hello {name}"` |
| `arr.includes(x)` | `x in arr` |
| `Math.max(...arr)` | `max(arr)` |

---

### ⬜ Day 2 · Python 进阶：OOP + 异步 + 文件操作
### ⬜ Day 3 · LLM API 基础 — DeepSeek / OpenAI 调用
### ⬜ Day 4 · Prompt Engineering — 系统提示与思维链
### ⬜ Day 5 · Function Calling — 让 AI 操作外部世界
### ⬜ Day 6 · 结构化输出 + 错误处理 + 最佳实践
### ⬜ Day 7 · 🎉 周末大作战：电商智能客服 CLI

---

## 🛠 技术栈

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-14+-000000?logo=nextdotjs&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?logo=langchain&logoColor=white)

## 📁 项目结构

详见 [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md)

## 🎯 30 天目标产出

| # | 项目 | 完成时间 | 技术亮点 |
|---|------|---------|---------|
| 1 | 电商智能客服 CLI | Day 7 | 多轮对话 + Function Calling + 流式输出 |
| 2 | RAG 知识库问答系统 | Day 14 | 混合检索 + 引用来源 + Next.js 前端 |
| 3 | 3 Agent 协作内容生成 | Day 21 | Planner + Writer + Reviewer MultiAgent |

---

*每天提交代码，每周一篇学习笔记，30 天后复盘。加油，Minda！🚀*
