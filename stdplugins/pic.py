import os

from datetime import datetime

from pytz import timezone

from PIL import Image, ImageDraw, ImageFont, ImageFile

from pySmartDL import SmartDL

from telethon.tl import functions

from uniborg.util import admin_cmd

import asyncio

import shutil

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
VERY_PIC = "https://picsum.photos/500" 

@borg.on(admin_cmd(pattern="autopp"))

async def autopic(event):

    downloaded_file_name = "./DOWNLOADS/original_pic.png"

    downloader = SmartDL(VERY_PIC, downloaded_file_name, progress_bar=False)

    downloader.start(blocking=False)

    photo = "photo_pfp.png"

    while not downloader.isFinished():

        place_holder = None

    counter = -5

    while True:
        downloaded_file_name = "./DOWNLOADS/original_pic.png"

        downloader = SmartDL(VERY_PIC, downloaded_file_name, progress_bar=False)

        downloader.start(blocking=False)
        await asyncio.sleep(30)
        shutil.copy(downloaded_file_name, photo)
        
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        im = Image.open(photo)
        file_test = im.save(photo, "PNG")

        now_utc = datetime.now(timezone('UTC'))

        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
     

        current_time = now_asia.strftime("%d %b %Y\n@user_nmr")

        img = Image.open(photo)

        drawn_text = ImageDraw.Draw(img)

        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 25)

        drawn_text.text((350,15), current_time, font=fnt, fill=(0, 102, 204))

        img.save(photo)
        img2 = Image.open(photo)
        draw2 = ImageDraw.Draw(img2)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)

        ct_time = now_asia.strftime("%I:%M %p")
        drawn_text.text((245,430), ct_time, font=fnt, fill=(255, 0, 0))
        img.save(photo)

        file = await event.client.upload_file(photo)  # pylint:disable=E0602

        try:

            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602

                file

            ))

            os.remove(downloaded_file_name)

            counter -= 5

            await asyncio.sleep(35)

        except:

            return
