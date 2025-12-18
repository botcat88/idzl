import asyncio
import zalo_bot
from flask import Flask
from threading import Thread

# --- PHẦN GIỮ CHO REPLIT KHÔNG NGỦ ---
app = Flask('')


@app.route('/')
def home():
    return "Bot đang chạy!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


# --- PHẦN CHÍNH GET ID ---
async def main():
    # Thay Token của bạn vào đây
    token = "664627674442828979:uBsiwNKUJAkmGEOQAFCTpskdajIKOJFrxoChTWLZGOPyLbiErMcAeINsHMWnBsfJ"
    bot = zalo_bot.Bot(token)

    keep_alive()  # Chạy server ảo để UptimeRobot ping
    print("Bot Get ID đang khởi động...")

    async with bot:
        while True:
            try:
                update = await bot.get_update(timeout=30)
                if update and update.message and update.message.text:
                    text = update.message.text.strip().lower()
                    chat_id = update.message.chat.id

                    if text == "/id":
                        # Gửi lại ID cho người dùng
                        await bot.send_message(chat_id,
                                               f"ID của bạn là: {chat_id}")
                        print(f"Đã Get ID: {chat_id}")

            except Exception as e:
                # Tránh dừng bot khi timeout hoặc lỗi mạng
                await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
