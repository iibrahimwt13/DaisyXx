"""
MIT License
Copyright (c) 2021 TheHamkerCat
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os

from pyrogram import filters

from DaisyX.function.pluginhelpers import member_permissions
from DaisyX.services.pyrogram import pbot as app


@app.on_message(filters.command("setgrouptitle") & ~filters.private)
async def set_chat_title(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("Yeterli İznin yok.")
            return
        if len(message.command) < 2:
            await message.reply_text("**Kullanım:**\n/set_chat_title Yenİ AD")
            return
        old_title = message.chat.title
        new_title = message.text.split(None, 1)[1]
        await message.chat.set_title(new_title)
        await message.reply_text(
            f"Successfully Changed Group Title From {old_title} To {new_title}"
        )
    except Exception as e:
        print(e)
        await message.reply_text(e)


@app.on_message(filters.command("settitle") & ~filters.private)
async def set_user_title(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        from_user = message.reply_to_message.from_user
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("Yeterli İznin yok.")
            return
        if len(message.command) < 2:
            await message.reply_text(
                "**Kullanım:**\n/set_user_title YENI YÖNETICI BAŞLıĞı"
            )
            return
        title = message.text.split(None, 1)[1]
        await app.set_administrator_title(chat_id, from_user.id, title)
        await message.reply_text(
            f"Başarıyla Değiştirildi {from_user.mention}'s Yönetici Başlığı {title}"
        )
    except Exception as e:
        print(e)
        await message.reply_text(e)


@app.on_message(filters.command("setgrouppic") & ~filters.private)
async def set_chat_photo(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id

        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("Yeterli İznin yok.")
            return
        if not message.reply_to_message:
            await message.reply_text("Fotoğrafı olarak ayarlamak için yanıtlama chat_photo")
            return
        if not message.reply_to_message.photo and not message.reply_to_message.document:
            await message.reply_text("Fotoğrafı olarak ayarlamak için yanıtlama chat_photo")
            return
        photo = await message.reply_to_message.download()
        await message.chat.set_photo(photo)
        await message.reply_text("Grup Fotoğrafı Başarıyla Değiştirildi")
        os.remove(photo)
    except Exception as e:
        print(e)
        await message.reply_text(e)


__mod_name__ = "Admin"

__help__ = """
Yönetici modülü ile kullanıcıları tanıtmayı ve indirgemeyi kolaylaştırın!

<b>Available komutları:</b>
- /promote (kullanıcı) (?admin'in başlığı): Kullanıcıyı yöneticiye yükseltiyor.
- /demote (kullanıcı): Kullanıcıyı yöneticiden indirger.
- /adminlist: Sohbetin tüm yöneticilerini gösterir.
- /admincache: Yeni yöneticiler /yönetici izinlerini dikkate almak için yönetici önbelleğini güncelleyin.
- /ban: bir kullanıcıyı yasaklar
- /unban: kullanıcıyı unbans
- /mute: kullanıcıyı sessize alma
- /unmute: kullanıcının sesini açmaYönetici modülü ile kullanıcıları tanıtmayı ve indirgemeyi kolaylaştırın!

<b>Available komutları:</b>
- /promote (kullanıcı) (?admin'in başlığı): Kullanıcıyı yöneticiye yükseltiyor.
- /demote (kullanıcı): Kullanıcıyı yöneticiden indirger.
- /adminlist: Sohbetin tüm yöneticilerini gösterir.
- /admincache: Yeni yöneticiler /yönetici izinlerini dikkate almak için yönetici önbelleğini güncelleyin.
- /ban: bir kullanıcıyı yasaklar
- /unban: kullanıcıyı unbans
- /mute: kullanıcıyı sessize alma
- /unmute: kullanıcının sesini açma
- /tban [varlık] : kullanıcıyı zaman aralığı için geçici olarak yasaklar.
- /tmute [varlık] : zaman aralığı için bir kullanıcıyı geçici olarak sessize alır.
- /kick: bir kullanıcıyı tekmeler
- /settitle [varlık] [başlık]: yönetici için özel bir başlık ayarlar. Hiçbir [başlık] sağlanmadıysa varsayılan değer "Yönetici"
- /setgrouptitle [metin] küme grubu başlığı
- /setgrouppic: grup fotoğrafı olarak ayarlanan bir görüntüyü yanıtlayın
- /setdescription: Grup açıklamasını ayarla
- /setsticker: Grup etiketini ayarla
- /unmuteall: Sessize alınan tüm üyelerin sesini aç
- /unbanall: Unban tüm banne- /tban [varlık] : kullanıcıyı zaman aralığı için geçici olarak yasaklar.
- /tmute [varlık] : zaman aralığı için bir kullanıcıyı geçici olarak sessize alır.
- /kick: bir kullanıcıyı tekmeler
- /settitle [varlık] [başlık]: yönetici için özel bir başlık ayarlar. Hiçbir [başlık] sağlanmadıysa varsayılan değer "Yönetici"
- /setgrouptitle [metin] küme grubu başlığı
- /setgrouppic: grup fotoğrafı olarak ayarlanan bir görüntüyü yanıtlayın
- /setdescription: Grup açıklamasını ayarla
- /setsticker: Grup etiketini ayarla
- /unmuteall: Sessize alınan tüm üyelerin sesini aç
- /unbanall: Unban tüm banlananları kaldırır. 
"""
