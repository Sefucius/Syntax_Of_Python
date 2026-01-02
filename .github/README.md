# AI 编码指南 - Syntax_Of_Python

## 概述
这是一个教育性的 Python 代码库，涵盖从基础到高级的语法主题。每个章节（chap1-chap14）包含课程笔记（课程笔记）和作业（章节作业），演示特定概念。

## 代码结构
- **文件命名**：课程笔记和作业文件使用数字前缀（如 `001函数的定义和调用.py`）
- **目录**：
  - `课程笔记/` 用于演示脚本
  - `章节作业/` 或 `章节习题/` 用于练习
- **语言**：所有代码使用 Python 3.x，注释和变量名常使用中文

## 依赖项
根据需要安装外部库（无集中式 requirements.txt）。常见包：
- 数据处理：`pandas`、`numpy`、`openpyxl`
- 可视化：`matplotlib`、`pyecharts`
- 网络爬取：`requests`、`pdfplumber`
- 图像处理：`Pillow`
- 文本处理：`jieba`
- GUI：`wxpython`

安装示例：
```bash
pip install requests pandas matplotlib pyecharts pillow jieba openpyxl pdfplumber
```

## 运行代码
- 直接执行脚本：`python chap10/课程笔记/008爬取景区的天气预报.py`
- 某些脚本需要网络访问（网络爬取示例）
- 多进程/线程示例可能需要小心执行以避免冲突

## 模式和约定
- **导入**：先分组标准库导入，然后第三方库
- **主守卫**：对包含多进程的脚本使用 `if __name__ == '__main__':`
- **错误处理**：教育示例中最小化；为生产代码添加 try-except
- **注释**：中英混合；优先使用清晰、描述性注释

## 关键示例
- 网络编程：见 `chap12/课程笔记/`
- 并发：`chap13/课程笔记/` 用于多进程和线程
- 数据可视化：`chap10/课程笔记/014Pandas和Matplotlib绘制饼图.py`
- 网络爬取：`chap10/课程笔记/008爬取景区的天气预报.py`

## 开发工作流
- 无构建系统；单独运行脚本进行测试
- 按现有编号添加新章节（chap15 等）
- 新依赖项在脚本注释中记录安装方式

## 文件参考
- 基础语法：`chap2/001print/demo1_helloworld.py`
- 函数：`chap8/课程笔记/001函数的定义和调用.py`
- 类：`chap9/课程笔记/`
- 模块：`chap10/课程笔记/001模块的导入.py`