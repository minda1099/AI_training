# 📁 AI_training 项目结构说明

> 30 天 AI 工程师冲刺计划 — 完整目录规划

```
AI_training/
│
├── README.md                        # 项目总览 + 每日打卡记录
├── PROJECT_STRUCTURE.md             # 本文件：目录结构说明
│
├── day01/                           # ✅ Day 1: Python 环境 + 核心语法速览
│   ├── python_basics.py             # 20 个核心语法练习（列表/字典/函数/异常）
│   └── js_to_python.py              # JS → Python 对比翻译练习
│
├── day02/                           # ⬜ Day 2: Python 进阶 — OOP + 异步 + 文件操作
│   ├── oop_dataclass.py             # DataClass 定义错误上报数据模型
│   ├── async_concurrent.py          # async httpx 并发请求（对比 Promise.all）
│   └── json_kv_store.py             # 本地 JSON KV 存储工具类
│
├── day03/                           # ⬜ Day 3: LLM API 基础 — DeepSeek / OpenAI
│   ├── single_turn.py               # Python 版单轮对话调用
│   ├── streaming.py                 # 流式输出（stream=True），实时打印 token
│   ├── multi_turn.py                # 多轮对话（维护 messages 历史列表）
│   └── llm_client.ts                # TypeScript + OpenAI SDK 同步实现
│
├── day04/                           # ⬜ Day 4: Prompt Engineering — 系统提示与思维链
│   ├── prompt_experiments.py        # System Prompt 实验 + CoT 对比
│   └── ecommerce_prompts.md         # 5 个电商场景 Prompt 模板 + 效果对比报告
│
├── day05/                           # ⬜ Day 5: Function Calling — 让 AI 操作外部世界
│   ├── tools_definition.py          # 3 个工具函数（查天气/查库存/发邮件 Mock）
│   ├── tool_calling_agent.py        # LLM 自动决策调用工具，处理多步骤任务
│   └── parallel_tools.py            # 并行工具调用（LLM 一次调用多个 tool）
│
├── day06/                           # ⬜ Day 6: 结构化输出 + 错误处理 + 最佳实践
│   ├── structured_output.py         # Pydantic 强类型 LLM 输出解析器
│   ├── review_analyzer.py           # 商品评价结构化分析（情感/问题/评分）
│   └── retry_decorator.py           # 指数退避重试装饰器（优雅处理 API 限流）
│
├── day07/                           # ⬜ Day 7: 🎉 项目一：电商智能客服 CLI
│   ├── main.py                      # 主入口：多轮对话 + Function Calling + 流式
│   ├── tools/
│   │   ├── order_tool.py            # 查订单工具
│   │   └── product_tool.py          # 查商品工具
│   ├── frontend/                    # Next.js 界面（加分项）
│   ├── .env.example                 # 环境变量示例
│   ├── requirements.txt
│   └── README.md                    # 项目说明 + 演示 GIF
│
├── day08/                           # ⬜ Day 8: LangChain 核心架构 — LCEL
│   ├── lcel_chains.py               # 3 种 Chain（基础/历史/检索）
│   └── prompt_factory.py            # PromptTemplate 动态变量注入工厂
│
├── day09/                           # ⬜ Day 9: LangChain Tools — 自定义工具
│   ├── custom_tools.py              # @tool 装饰器 + StructuredTool
│   └── react_agent.py               # ReAct Agent 多步骤推理演示
│
├── day10/                           # ⬜ Day 10: RAG 基础 — 文档处理与 Embedding
│   ├── document_loaders.py          # 5 种格式文档加载（PDF/DOCX/HTML/CSV/TXT）
│   ├── chunk_strategies.py          # 3 种分割策略对比实验
│   └── embedding_viz.py             # Embedding 可视化脚本
│
├── day11/                           # ⬜ Day 11: 向量数据库 — ChromaDB
│   ├── chroma_setup.py              # ChromaDB 本地部署 + 1000 条商品向量存储
│   ├── semantic_search.py           # 相似商品搜索 + 语义去重 + 分类过滤
│   └── keyword_vs_semantic.md       # 关键词 vs 语义搜索对比测试报告
│
├── day12/                           # ⬜ Day 12: 完整 RAG Pipeline
│   ├── rag_pipeline.py              # 完整 RAG Pipeline（加载→切割→向量化→检索→生成）
│   ├── conversational_rag.py        # 对话历史感知 RAG
│   └── cache_layer.py               # 缓存层（避免重复 Embedding 计算）
│
├── day13/                           # ⬜ Day 13: LangGraph — 有状态工作流
│   ├── basic_graph.py               # 问题分类 → 路由 → 专门处理流程
│   ├── human_in_loop.py             # 带人工审批节点的 AI 工作流
│   └── workflow_diagram.mmd         # Mermaid 工作流可视化图
│
├── day14/                           # ⬜ Day 14: 🎉 项目二：RAG 知识库问答系统
│   ├── backend/
│   │   ├── main.py                  # FastAPI 后端
│   │   ├── rag_engine.py            # RAG 核心引擎
│   │   └── Dockerfile
│   ├── frontend/                    # Next.js：聊天 UI + 文档上传 + 来源高亮
│   ├── docker-compose.yml
│   └── README.md
│
├── day15/                           # ⬜ Day 15: Agent 设计模式
│   ├── react_from_scratch.py        # 手写 ReAct（Thought/Action/Observation 循环）
│   ├── plan_execute_agent.py        # Plan-Execute Agent（Planner + Executor 分离）
│   └── reflection_agent.py          # Reflection 机制（自我评价并修正）
│
├── day16/                           # ⬜ Day 16: MultiAgent — AutoGen & CrewAI
│   ├── autogen_demo.py              # 产品经理 + 开发工程师双 Agent 协作
│   ├── crewai_demo.py               # 研究 + 撰写 + 审核三 Agent 内容生成
│   └── framework_comparison.md      # AutoGen vs CrewAI 对比分析
│
├── day17/                           # ⬜ Day 17: Agent 记忆系统
│   ├── short_term_memory.py         # 滑动窗口 + 摘要压缩
│   ├── long_term_memory.py          # ChromaDB 长期记忆（按相关性检索）
│   └── memory_api.py                # 记忆增删改查 API
│
├── day18/                           # ⬜ Day 18: 上下文工程最佳实践
│   ├── context_strategies.py        # 4 种上下文压缩策略对比
│   ├── token_counter.py             # Token 计数器 + 成本估算工具
│   └── context_quality_report.md    # 量化对比实验报告
│
├── day19/                           # ⬜ Day 19: Dify 平台部署
│   ├── docker-compose.dify.yml      # Dify 本地部署配置
│   ├── custom_provider/             # 自定义 LLM Provider
│   └── workflow_screenshot.png      # 工作流截图
│
├── day20/                           # ⬜ Day 20: FastGPT 部署与前端嵌入
│   ├── docker-compose.fastgpt.yml   # FastGPT + MongoDB + PgVector
│   └── nextjs-embed/                # FastGPT 嵌入 Next.js 示例
│
├── day21/                           # ⬜ Day 21: 🎉 项目三：3 Agent 内容生成系统
│   ├── agents/
│   │   ├── planner.py               # Planner Agent：分析需求，制定大纲
│   │   ├── writer.py                # Writer Agent：生成内容 + 搜索工具
│   │   └── reviewer.py              # Reviewer Agent：审核 + 触发重写
│   ├── frontend/                    # 实时显示 Agent 思考过程的可视化界面
│   └── README.md
│
├── day22/                           # ⬜ Day 22: Docker 化 AI 应用
│   ├── Dockerfile                   # 多阶段构建（< 500MB）
│   └── docker-compose.yml           # FastAPI + ChromaDB + Nginx 编排
│
├── day23/                           # ⬜ Day 23: FastAPI 最佳实践
│   ├── sse_streaming.py             # SSE 流式返回（前端实时看到 AI 输出）
│   ├── websocket_agent.py           # WebSocket 实时 Agent 状态推送
│   └── middleware.py                # 限流 + JWT 认证 + 请求日志
│
├── day24/                           # ⬜ Day 24: 可观测性 — 监控、日志、追踪
│   ├── langfuse_integration.py      # LangFuse 集成 Token 消耗追踪
│   ├── structured_logger.py         # JSON 结构化日志
│   └── alert_system.py              # 错误率告警（钉钉通知）
│
├── day25/                           # ⬜ Day 25: 明星项目① 升级版电商客服
├── day26/                           # ⬜ Day 26: 明星项目① 部署 + 演示
├── day27/                           # ⬜ Day 27: 明星项目② 前端错误监控 + AI 根因
├── day28/                           # ⬜ Day 28: 明星项目③ AI 代码审查 Agent
├── day29/                           # ⬜ Day 29: GitHub 作品集 + 技术博客
├── day30/                           # ⬜ Day 30: 模拟面试 + 下一步规划
│
├── cheatsheets/                     # 知识速查表（持续更新）
│   ├── python_vs_js.md              # Python / JS 对比速查
│   ├── llm_api.md                   # LLM API 参数速查
│   ├── langchain.md                 # LangChain 核心 API 速查
│   └── interview_qa.md              # 面试高频题 + 答案（Day 30 前完成）
│
└── .env.example                     # 所有项目通用环境变量模板
```

---

## 🗂 目录命名规范

| 类型 | 命名格式 | 示例 |
|------|---------|------|
| 每日练习目录 | `dayXX/` | `day01/`, `day14/` |
| 练习脚本 | `snake_case.py` | `async_concurrent.py` |
| 配置文件 | 标准名称 | `Dockerfile`, `docker-compose.yml` |
| 文档报告 | `snake_case.md` | `keyword_vs_semantic.md` |
| 前端项目 | `frontend/` | Next.js 子项目 |

## 🌿 Git 提交规范

```
feat(day01): add 20 Python syntax exercises
feat(day03): implement streaming LLM chat
fix(day07): handle empty order response
docs(day14): update RAG system README with demo GIF
refactor(day25): upgrade ecommerce agent with RAG
```

## 📦 环境要求

```bash
# Python
python >= 3.11
pip install langchain langchain-openai chromadb fastapi pydantic httpx

# Node.js（前端项目）
node >= 20
pnpm install

# 环境变量
cp .env.example .env
# 填写 DEEPSEEK_API_KEY, OPENAI_API_KEY 等
```
