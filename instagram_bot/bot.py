from instabot import Bot
import os
import glob

# Delete the existing cookie file if it exists to avoid login issues
cookie_del = glob.glob("config/*cookie.json")
if cookie_del:
    os.remove(cookie_del[0])

bot = Bot()
bot.login(username="parthh_350", password="Rbk@1234")

# Upload photo with a caption
# bot.upload_photo("./img/img.jpg", caption="2025")

# bot.unfollow("shutter_peek")
# bot.send_messages("Hello I love PYTHON",["parth_r_d","iam_anish_998"])
# followers=bot.get_user_followers("parthh_350")
# for follower in followers:
#     print(bot.get_user_info(follower))