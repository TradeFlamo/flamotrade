# <img src="flamo.png" width="20"/> flamotrade Lite —— TradingView 到 Binance 的轻量级自动交易工具
![Downloads](https://img.shields.io/github/downloads/TradeFlamo/flamotrade/total.svg)
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

0. 具备 vps+域名（如api.abc.xyz并指向此 vps）
1. caddy 反向代理 http://127.0.0.1:7000
2. 下载二进制（Releases 中）
3. 编辑同目录下的 `flamoconfig.json`:
   填入：
   * tradeTunnel (TradingView警报里填的值的要与此处相同！)
   * Binance API KEY / SECRET
   * Telegram BOT Token / Chat ID
4. 启动 webhook 服务:
./flamotrade-lite
5. 浏览器查看相同自动生成的接口文档  
   本地运行服务输入http://127.0.0.1:7000/docs  
   vps 运行服务输入https://api.abc.xyz/docs  
7. TradingView 警报配置: Webhook URL:"https://api.abc.xyz/buySell"(或另一接口closePosition)   
   警报内容json格式示例:  
   <键名要与下面完全相同。值全为字符串，大小写均可，但tradeTunnel的值大小写敏感)>
```json
警报买卖json
{
  "symbol": "ETHUSDT",             # 可以是Binance永续合约上线的其它加密币
  "side": "BUY",                   # 可用:buy/sell
  "amount": "1.5",                 # 买卖数量
  "usdt": "100",                   # 买卖所用的usdt。amount为0时使用
  "multiple": "0.3*5",             # 账户可用usdt的比例*当前杠杆。amount与usdt均为0时使用
  "price": "0",                    # 买卖价格。市价单不用此值
  "orderType": "market",           # 也可limit。但Lite免费版不支持limit，pro版支持
  "cancelLast": "false",           # 也可true。是否取消此前的所有买卖挂单(非止盈止损单)
  "closeLast": "reverse",          # 可用:true/false/reverse。true为下此单前市价平掉所有持仓，reverse为下此单前只市价平相反方向的持仓
  "reduceOnly": "false",           # 也可true。是否只对持仓减仓。用它与closeLast的reverse实现同方向多次下单只执行第一次下单
  "tradeTunnel": "Tunnel password" # 为TradingView警报json传输安全而设计。应与配置文件中完全相同，否则不接受此次订单
}
警报平仓json
{
  "symbol": "ETHUSDT",
  "side": "CLOSEBUY",              # 可用:closeBuy/closeSell/x。X为平掉任何方向的持仓
  "amount": "0",
  "ratio": "1.0",                  # 当前持仓的比例。amount为0时使用
  "price": "{{close}}*1.01",
  "orderType": "limit",            # 也可market，Lite免费版都支持
  "cancelLast": "true",
  "tradeTunnel": "Tunnel password"
}


# 📦 配置文件flamoconfig.json示例

{
  "tradeTunnel":"tunnel password",
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
* 规避交易所对vps的IP执行的限流
* 多交易所（Binance + OKX）
* 高级订单（止盈、止损、入场价止损、买卖单带止盈止损、撤单、平仓等增强版）
* 更高速的执行引擎
* Telegram 全链路操作报告
* 单信号 50+ 账户批处理（含速率控制）
* SaaS 跨用户级多账户系统

你可以购买 **FlamoTrade Pro（闭源付费编译版）**。

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
