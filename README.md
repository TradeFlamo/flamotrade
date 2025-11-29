# flamotrade Lite —— TradingView 到 Binance 的轻量级自动交易工具

> 🎯 一个极简、稳定、可真实下单的开源小工具，让你用 TradingView 的警报自动执行交易指令（单账号版）。

Flamotrade Lite 是一个 **轻量级、可自行部署** 的Tradingview警报自动交易 Agent：

* 支持 TradingView Webhook
* 自动执行 **买入 / 卖出 / 平仓**
* 市价单即时成交
* Telegram 实时通知
* 仅需一个 JSON 配置 + 一个二进制文件即可运行

👉 **非常适合：**

* 想体验自动交易流程的小伙伴
* 想测试 TradingView 下单链路是否可靠
* 想先试试自动化策略，但暂时不需要复杂功能的人

Light 版仅支持 **单账户 / 基础市价单 / 买卖平仓**，保证极小且稳定。

---

# ✨ 特性

### ✔ 单账户 Binance 永续合约U本位自动下单

TradingView → Webhook → FlamoTrade Lite → Binance 市价成交。

### ✔ 买入 / 卖出 / 平仓

支持最常用的轻量交易指令。

### ✔ Telegram 推送

每笔订单的执行状态、成功/失败会自动推送至 Telegram。

### ✔ 极轻量架构

无数据库
无后台管理
仅一个配置文件
最适合部署在 5 美元的 VPS 上运行。

### ✔ 纯本地运行，安全

你自己的 API Key 只保留在你自己 VPS 的配置文件中。

---

# 🚀 快速开始

1. 下载二进制（Releases 中）
2. 编辑 `flamotrade.json`
3. 填入：
   * tradeTunnel
   * Binance API KEY / SECRET
   * Telegram BOT Token / Chat ID
4. 启动：

```
./flamotrade-lite
```

5. TradingView 配置 Webhook URL:https://xxx.xxx.xxx/buySell(or closePosition)，内容格式示例：

```
{
  "symbol": "ETHUSDT",
  "side": "BUY",
  "amount": "1.5",
  "usdt": "100",
  "multiple": "0.3*5",
  "price": "0",
  "orderType": "market",
  "cancelLast": "false",
  "closeLast": "reverse",
  "reduceOnly": "false",
  "tradeTunnel": "your tradeTunnel password"
}
---or---
{
  "symbol": "ETHUSDT",
  "side": "CLOSEBUY",
  "amount": "0",
  "ratio": "1.0",
  "price": "{{close}}*1.01",
  "orderType": "limit",
  "cancelLast": "true",
  "tradeTunnel": "your tradeTunnel password"
}
---

# 📦 配置文件示例

```json
{
  "tradeTunnel":"your json transport password",
  "binance": {
    "api_key": "YOUR_KEY",
    "api_secret": "YOUR_SECRET"
  },
  "telegram": {
    "token": "YOUR_TELEGRAM_BOT_TOKEN",
    "chat_id": "123456"
  }
}
```

---

# 🔒 关于完整版本

如果你需要：

* 统一的 webhook 接口
* 多账户同时下单
* 异步并行执行
* 下单失败重试（网络、交易所等短暂失败）
* 表达式解析（如 *数量 × 百分比*）
* 完美规避交易所对VPS的Ip执行的限流
* 多交易所（Binance + OKX）
* 高级订单（止盈、止损、入场价止损、买卖单带止盈止损、撤单、平仓等增强版）
* 更高速的执行引擎
* Telegram 全链路操作报告
* 单信号 50+ 账户批处理（含速率控制）
* SaaS 跨用户级多账户系统

你可以购买 **FlamoTrade Pro（付费编译版）**。

👉 购买地址：
🔗 [https://lemon-link](https://lemon-link) （你之后填）

---

# 📝 免责声明

本项目仅用于个人学习与研究自动化流程。
所有交易行为均由用户本人承担风险。
请务必在小额资金下测试后再投入生产环境。

---

# ❤️ 许可协议

MIT License（可商用，可修改）。
请在 fork / 二次开发时保留原作者署名。

---
