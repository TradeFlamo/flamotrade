"""
Flamotrade Lite - demo skeleton

此文件提供了一个完全本地模拟的 FastAPI 服务。
实际交易逻辑应由闭源/付费版本提供；公开仓库仅演示接口与使用方式。
"""
from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import logging


logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Flamotrade Lite (Demo)")


# ------------------- 配置读取（示例：仅占位符） -------------------
try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
except Exception:
    config = {}


# ------------------- Pydantic 模型 -------------------
class BuySellSignal(BaseModel):
    symbol: str = 'ETHUSDT'
    side:   str = 'BUY'
    amount: str = '0.0'
    usdt:   str = '0'
    tradeTunnel: str | None = None


class ClosePositionSignal(BaseModel):
    symbol: str = 'ETHUSDT'
    side:   str = 'CLOSEBUY'
    amount: str = '0'
    tradeTunnel: str | None = None


# ------------------- FakeTrader（模拟实现） -------------------
class FakeTrader:
    
    """模拟交易器：不会与真实交易所交互。"""

    def __init__(self):
        self._id = 0


    def create_market_order(self, symbol, side, amount, params=None):
        self._id += 1
        logging.info(f"[SIM] market order #{self._id} {side} {symbol} amt={amount} params={params}")
        return {"id": self._id, "status": "simulated", "side": side, "symbol": symbol, "amount": amount}


    def close_position(self, symbol, side, amount):
        self._id += 1
        logging.info(f"[SIM] close #{self._id} {symbol} amt={amount} side={side}")
        return {"id": self._id, "status": "simulated_close", "symbol": symbol, "amount": amount}


# 单实例（演示）
trader = FakeTrader()


# ------------------- 接口 -------------------
@app.post('/buySell')
async def buy_sell(signal: BuySellSignal):
    # 校验 tradeTunnel（示例：如果 config 中启用，则检查）
    if 'tradeTunnel' in config and config.get('tradeTunnel'):
        if signal.tradeTunnel != config.get('tradeTunnel'):
            return {"status": "forbidden"}


    # 仅允许市价下单（lite 版限制）
    try:
        # 解析数量（此处为示例，真实版会更复杂）
        amount = float(signal.amount) if float(signal.amount) > 0 else float(signal.usdt or 0)
    except Exception:
        amount = 0


    if amount <= 0:
        return {"status": "error", "message": "invalid amount"}


    order = trader.create_market_order(symbol=signal.symbol, side=signal.side, amount=amount)
    # 可选：将结果写到本地日志/文件
    return {"status": "success", "order": order}


@app.post('/closePosition')
async def close_position(signal: ClosePositionSignal):
    if 'tradeTunnel' in config and config.get('tradeTunnel'):
        if signal.tradeTunnel != config.get('tradeTunnel'):
            return {"status": "forbidden"}


    try:
        amount = float(signal.amount) if float(signal.amount) > 0 else 0
    except Exception:
        amount = 0


    res = trader.close_position(symbol=signal.symbol, side=signal.side, amount=amount)
    return {"status": "success", "result": res}


# 运行提示（仅供开发测试）
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=7000)
