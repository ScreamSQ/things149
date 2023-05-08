import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from datetime import datetime
now = datetime.now() 
logging.basicConfig(level=logging.INFO)


bot = Bot(token='6047987391:AAFAkISTxTxTWUgHyBNZFMQZ1Z44dhLgYIU')
if not os.path.exists('photos'):
    os.makedirs('photos')
if not os.path.exists('audio'):
    os.makedirs('audio')
dp = Dispatcher(bot)
if not os.path.exists('stickers'):
    os.makedirs('stickers')
if not os.path.exists('voice_messages'):
    os.makedirs('voice_messages')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer("👋 Приветсвую в анонимном телеграмм боте канала <b>Мысли 149</b>\n\n\n🚀 Напишите сюда всё, что хотите, и через несколько секунд <b>бот опубликует</b> ваше сообщение, но не будет знать от кого.\n\nЯ поддерживаю форматы: фото, видео, голосовые (.mp3), обычное сообщение, стикер (не анимированный), голосовые сообщения", parse_mode='HTML')

@dp.message_handler(commands=['menu'])
async def menu_command(message: types.Message):
    await message.answer("👋 Приветсвую в анонимном телеграмм боте канала <b>Мысли 149</b>\n\n\n🚀 Напишите сюда всё, что хотите, и через несколько секунд <b>бот опубликует</b> ваше сообщение, но не будет знать от кого.\n\nЯ поддерживаю форматы: фото, видео, голосовые (.mp3), обычное сообщение, стикер (не анимированный), голосовые сообщения", parse_mode='HTML')


@dp.message_handler()
async def send_message_to_channel(message: types.Message):
    username = message.from_user.username
    user_id = message.from_user.id
    try:

        await bot.send_message(chat_id='айди канала', text=f'📩 <b>Получено новое сообщение!</b>\n\n{message.text}\n\n<i>Для того чтобы написать сообщение, напиши мне в личку</i>', parse_mode='HTML')
        await message.answer("✅ <b>Сообщение было успешно отправлено в канал!</b>", parse_mode='HTML')
    except Exception as e:
        await message.answer("❌ <b>Произошла ошибка при отправке сообщения. Попробуйте еще раз.</b>", parse_mode='HTML')

@dp.message_handler(content_types=['photo'])
async def photo_handler(message: types.Message):
    photo = message.photo[-1]
    username = message.from_user.username
    user_id = message.from_user.id
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    caption = message.caption 
    file_id = photo.file_id
    file_path = f'photos/{file_id}.jpg'
    await photo.download(file_path) 
    with open(file_path, 'rb') as photo_file:
        try:            
            
            await bot.send_photo(chat_id='айди канала', photo=photo_file, caption=caption)
            await message.answer("✅ <b>Фото было успешно отправлено в канал!</b>", parse_mode='HTML')
        except Exception as e:
            await message.answer("❌ <b>Произошла ошибка при отправке фото. Попробуйте еще раз.</b>", parse_mode='HTML')

@dp.message_handler(content_types=['audio'])
async def audio_handler(message: types.Message):
    audio = message.audio
    caption = message.caption 
    file_id = audio.file_id
    file_path = f'audio/{file_id}.mp3'
    await audio.download(file_path) 
    username = message.from_user.username
    user_id = message.from_user.id
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    with open(file_path, 'rb') as audio_file:
        try:
            
            await bot.send_audio(chat_id='айди канала', audio=audio_file, caption=caption)
            await message.answer("✅ <b>Аудио было успешно отправлено в канал!</b>", parse_mode='HTML')
        except Exception as e:
            await message.answer("❌ <b>Произошла ошибка при отправке аудио. Попробуйте еще раз.</b>", parse_mode='HTML')
if not os.path.exists('video'):
    os.makedirs('video')
@dp.message_handler(content_types=['video'])
async def video_handler(message: types.Message):
    video = message.video
    caption = message.caption 
    file_id = video.file_id
    file_path = f'video/{file_id}.mp4'
    await video.download(file_path)
    username = message.from_user.username
    user_id = message.from_user.id
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S") 
    
    with open(file_path, 'rb') as video_file:
        try:
         
            await bot.send_video(chat_id='айди канала', video=video_file, caption=caption)
            await message.answer("✅ <b>Ваше видео было успешно отправлено в канал!</b>", parse_mode='HTML')
        except Exception as e:
            await message.answer("❌ <b>Произошла ошибка при отправке видео. Попробуйте еще раз.</b>", parse_mode='HTML')
@dp.message_handler(content_types=['sticker'])
async def sticker_handler(message: types.Message):
    sticker = message.sticker
    file_id = sticker.file_id
    file_path = f'stickers/{file_id}.webp'
    await sticker.download(file_path) # сохраняем стикер в директорию stickers
    # отправляем стикер в канал
    username = message.from_user.username
    user_id = message.from_user.id
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    with open(file_path, 'rb') as sticker_file:
        try:
            
     
            await bot.send_sticker(chat_id='айди канала', sticker=sticker_file)
            await message.answer("✅ <b>Стикер был успешно отправлен в канал!</b>", parse_mode='HTML')
        except:
            await message.answer("❌ <b>Произошла ошибка при отправке стикера. Попробуйте еще раз.</b>", parse_mode='HTML')
@dp.message_handler(content_types=['voice'])
async def voice_handler(message: types.Message):
    voice = message.voice
    file_id = voice.file_id
    file_path = f'voice_messages/{file_id}.ogg'
    await voice.download(file_path) # сохраняем голосовое сообщение в директорию voice_messages
    # отправляем голосовое сообщение в канал
    username = message.from_user.username
    user_id = message.from_user.id
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    with open(file_path, 'rb') as voice_file:
        try:
           
            await bot.send_voice(chat_id='-1001929214018', voice=voice_file)
            await message.answer("✅ <b>Голосовое сообщение успешно отправлен в канал!</b>", parse_mode='HTML')
        except:
            await message.answer("❌ <b>Произошла ошибка при отправке голосового сообщения. Попробуйте еще раз.</b>", parse_mode='HTML')
        
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
