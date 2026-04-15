from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta
import os
from telethon import TelegramClient
from telethon.tl.types import PeerChannel
import asyncio

app = FastAPI(title="Telegram Parser API")

class ParseRequest(BaseModel):
    channels: List[str]
    topics: List[str]
    days: int

@app.post("/api/telegram/parse")
async def parse_channels(request: ParseRequest):
    # Заглушка: здесь будет реальная авторизация и парсинг
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    if not api_id or not api_hash:
        raise HTTPException(status_code=500, detail="Telegram credentials not set")

    client = TelegramClient("session", int(api_id), api_hash)
    
    posts = []
    try:
        await client.start()
        cutoff_date = datetime.now() - timedelta(days=request.days)
        
        for channel_str in request.channels:
            # Заглушка парсинга: iter_messages с offset_date и limit
            # TODO: добавить реальную фильтрацию по topics (message.text.lower().contains())
            async for message in client.iter_messages(channel_str, offset_date=cutoff_date, limit=100):
                if message.text:  # Только текстовые посты
                    posts.append({
                        "channel": channel_str,
                        "text": message.text[:500],  # Обрезаем для примера
                        "date": message.date.isoformat(),
                        "link": f"https://t.me/{channel_str.replace('@', '')}/{message.id}"
                    })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Parse error: {str(e)}")
    finally:
        await client.disconnect()
    
    return posts
