# ArXiv Paper Trends Analyzer 🚀

一个基于 Python 的自动化工具，旨在帮助研究者快速追踪 arXiv 上的最新科研动态。支持按关键词检索论文、自动导出数据并生成词云图。

---

## 🌟 核心功能

- **自动化爬取**：调用 arXiv API，支持自定义关键词（如 Multi-Agent, LLM, Computer Vision）。
- **数据结构化**：自动提取论文标题、摘要、作者及链接，保存至 `data/paper.csv`。
- **可视化分析**：利用 `wordcloud` 库对论文标题进行高频词分析，一键生成视觉直观的词云图。
- **轻量易用**：针对 Windows 用户提供 `.bat` 一键启动脚本。

## 📂 项目结构

```text
├── main.py                # 程序主入口，协调爬虫与分析模块
├── spider.py              # 核心爬虫逻辑（负责与 arXiv API 交互）
├── analyzer.py            # 数据处理模块（负责分词与词云生成）
├── arxiv爬虫机器人.bat     # Windows 环境一键执行脚本
├── requirements.txt       # 项目依赖库清单
├── .gitignore             # Git 忽略配置（排除 venv 与缓存）
└── data/                  # 数据存储目录（存放生成的 CSV 与图片）
```

---

## 🛠️ 快速开始

## 1. 环境准备

确保你的电脑已安装 **Python 3.8+**。建议创建虚拟环境以保持环境纯净：

```
python -m venv venv
# 激活环境 (Windows)
.\venv\Scripts\activate
# 激活环境 (Mac/Linux)
source venv/bin/activate
```

## 2. 安装依赖

在终端中运行以下命令安装必要的第三方库：

```
pip install -r requirements.txt
```



## 3. 运行项目

你可以通过以下任一方式启动程序：

- **命令行启动**：

  ```
  python main.py
  ```

- **快捷启动**： Windows 用户可直接双击根目录下的 `arxiv爬虫机器人.bat`。

## 4. 查看结果

程序运行结束后，结果将自动保存在 `data/` 文件夹下：

- `paper.csv`: 抓取到的论文详细列表。
- `wordcloud.png`: 自动生成的论文标题词云图。

------

## 📊 效果展示
<img width="2000" height="1200" alt="weekly_report" src="https://github.com/user-attachments/assets/c6f9c056-7859-4c27-a572-821d1f40e829" />

