# AI 聊天伴侣（极简版） · AI Chat Companion

一个支持多种 AI 模型的角色扮演的聊天应用，体积小，功能简洁，可安装为 Android APK 独立运行，也可作为 PWA 在浏览器中使用。

## ✨ 功能一览

| 功能 | 说明 |
|------|------|
| 🎭 **角色扮演** | 自定义 AI 的名字、性格、开场白、行为准则，打造专属 AI 伴侣 |
| 💬 **流式聊天** | 支持流式输出，打字机效果实时显示 AI 回复 |
| 🧠 **长期记忆** | AI 自动从对话中提取重要信息，也可一键批量提取历史记忆 |
| ✏️ **记忆管理** | 实时查看、编辑、删除长期记忆条目 |
| 🌗 **主题切换** | 浅色 / 深色 / 跟随系统三种模式 |
| ↩️ **消息撤回与编辑** | 用户和 AI 的消息都支持撤回和内联编辑 |
| 📦 **数据导入导出** | 完整导出聊天记录 + 记忆 + 配置，跨设备迁移 |
| 📲 **PWA 支持** | 浏览器打开可「添加到桌面」，离线也能用 |
| 📱 **Android APK** | 独立安装包，无需浏览器 |

## 🚀 快速开始

### 方式一：安装 APK（推荐）

下载 `AI聊天伴侣-v1.0.apk`，传到手机直接安装。首次启动需要允许「安装未知应用」。

### 方式二：浏览器使用

直接在浏览器中打开 `www/index.html`，Chrome/Safari 会自动提示「添加到桌面」。

## ⚙ 配置 API

应用本身不包含 API Key。打开后进入右上角 ⚙ 设置：

1. **API 地址**：默认 `https://api.deepseek.com`，可改为其他兼容 OpenAI 格式的 API
2. **API Key**：填入你的 API Key（支持 DeepSeek、硅基流动、OpenRouter 等）
3. **模型**：推荐 `deepseek-chat` 或 `deepseek-ai/DeepSeek-V3`

> 提示：记忆提取功能推荐使用 DeepSeek 系列模型（对指令跟随任务更友好），部分模型（如 GLM-5.1）可能不兼容。

## 🎭 角色设定指南

在设置 → 🎭 角色人设中可配置：

- **名字**：AI 角色的名字
- **性格描述**：一句话概括性格（如「温柔毒舌的猫系女友」）
- **开场白**：新对话开始时 AI 说的第一句话
- **行为准则**：详细的行为规范（语气、风格、边界等）

角色设定会作为 System Prompt 注入，影响 AI 所有的回复。

## 🧠 记忆系统

### 自动提取

在设置中开启「自动记忆提取」，设定间隔轮数（默认 10 轮）。每 N 轮对话后，AI 会分析最近 N 轮的内容，自动提取值得记住的信息。

### 批量提取

设置 → 数据管理 → 批量提取历史记忆。对已有的所有对话进行一次性记忆提取，适合首次使用或切换 AI 角色后补提。

### 记忆注入

提取的记忆会注入到每次对话的 System Prompt 中，AI 会在合适时机自然引用。记忆注入遵循以下原则：

- 像朋友般自然运用，不刻意展示
- 仅相关话题出现时引用
- 新信息与记忆冲突时以新信息为准
- 引用方式自然：「记得你说过…」「上次我们聊到…」

## 🏗 技术架构

```
ai-companion/
├── www/                 # PWA 前端
│   ├── index.html       # 主应用（纯前端，无框架依赖）
│   ├── manifest.json    # PWA 清单
│   ├── sw.js            # Service Worker（离线支持）
│   └── icons/           # 应用图标
├── android/             # Capacitor Android 项目
├── package.json         # Node.js 依赖
└── capacitor.config.json
```

- **前端**：原生 HTML/CSS/JS，零框架依赖
- **存储**：IndexedDB（主存储）+ localStorage（回退）
- **API 通信**：兼容 OpenAI Chat Completions 格式的 REST API
- **Android 打包**：Capacitor
- **语音输入**：Web Speech API

## 🔧 自行构建 APK

```bash
# 安装依赖
npm install

# 同步前端到 Android
npx cap sync android

# 构建 APK
cd android
./gradlew assembleDebug

# APK 输出路径
# android/app/build/outputs/apk/debug/app-debug.apk
```

构建需要 Java 17+ 和 Android SDK。

## 📋 数据隐私

- 所有聊天记录和记忆仅存储在本地（IndexedDB）
- 数据通过你配置的 API 发送给 AI 服务商
- 导出文件不包含 API Key
- 无任何遥测或数据收集

## 📝 License

MIT
