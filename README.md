# 🚀 YOLO Web 目标检测平台

基于 FastAPI 与 YOLO26 引擎构建的云端目标检测 Web 平台。本项目采用轻量化的前后端分离架构，通过 Python 后端统一接管模型推理与静态网页托管，开箱即用。

## ✨ 核心特性

- **开箱即用的前端 UI**：内置基于 Tailwind CSS 编写的响应式网页，支持点击或拖拽上传 JPG/PNG 格式图片，并带有加载动画提示。
- **内存级急速推理**：后端接收图片后，通过 NumPy 和 OpenCV 进行内存解码与处理，**无需落盘保存**。推理完成后直接向前端返回 JPEG 图片流，极大提升并发速度。
- **单点启动机制**：使用 FastAPI 的静态文件挂载功能，将前端页面挂载至根路径 `/`。只需启动后端脚本，即可同时访问前台页面与后台 API。
- **一键内网穿透**：集成了 `cpolar.bat` 批处理脚本，可快速将本地应用映射至公网，方便分享演示。

---

## 📁 项目结构

| 文件名 | 说明 |
| :--- | :--- |
| `app.py` | 后端核心服务。负责加载 YOLO26 模型、提供 `/detect` 推理接口，并在 `8000` 端口启动服务。 |
| `index.html` | 前端用户界面。处理文件拖拽交互，并通过 Fetch API 将图片上传至后端渲染结果。 |
| `requirements.txt` | Python 依赖清单。包含 FastAPI、YOLO 等必需的环境依赖。 |
| `cpolar.bat` | Windows 内网穿透启动脚本，一键暴露本地 8000 端口至公网。 |

---

## 🛠️ 快速开始

### 1. 克隆项目
将代码克隆到本地机器：
```bash
git clone [https://github.com/Aiyc-02/yolo-web-api.git](https://github.com/Aiyc-02/yolo-web-api.git)
cd yolo-web-api
```
### 2. 安装依赖
建议在 Python 虚拟环境中运行：
```bash
pip install -r requirements.txt
```
### 3. 启动服务
```bash
python app.py
```
注意：首次运行会在本地自动下载轻量级的 yolo26n.pt 模型权重文件（约 6MB），请保持网络畅通。
### 4. 访问系统
终端提示“模型加载完成！”后，打开浏览器访问：
👉 http://127.0.0.1:8000/

## 🌍 外网访问 (Cpolar 内网穿透)
如果您想将运行在自己电脑上的平台分享给其他人访问，可以使用项目内置的脚本：

确保您的电脑上已安装并配置好 Cpolar（默认安装路径需为 D:\cpolar）。

双击运行项目中的 cpolar.bat。

终端会生成一个公网 URL（例如 http://xxxx.cpolar.cn），其他人通过此链接即可直接访问您的 Web 平台！
## 🔌 API 接口文档
如果你想将该检测能力接入其他系统（如小程序、App），可以直接调用后端 API：

接口地址: /detect

请求方式: POST

内容类型: multipart/form-data

请求参数:

file: 上传的图像文件（必填）

响应内容: 直接返回画好检测框的 image/jpeg 图片二进制数据流。如果出错，则返回 JSON 格式报错信息。
