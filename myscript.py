from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import  Updater
import constants
import telegram
import webscrape
import datetime
import pytz

def callback_alarm(context: CallbackContext):
    soup = webscrape.webscrape()
    for index,i in enumerate(soup.select('tr[align="left"]')):
        if index != 0:
            mylist=[td.text for td in i.find_all('td')]
            jobtitle = mylist[0]
            jobtype = mylist[1]
            joblocation = mylist[2]
            jobarea = mylist[3]
            joblink='https://careers.a-star.edu.sg/'+i.find('a')['href']
            finaltext = f"""({index}).\nJob title: {jobtitle}\nJob type: {jobtype}\nJob Location: {joblocation}\nJob Field: {jobarea}\nJob Link: {joblink}\n"""
            context.bot.send_message(chat_id=context.job.context, text=finaltext)
    context.bot.send_message(chat_id=context.job.context, text="DONE POSTING.")
def start(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Welcome. I will pull data at 9:00 AM , 12:00 PM and 5:30 PM.')

    context.job_queue.run_daily(callback_alarm,datetime.time(hour=9, minute=00, tzinfo=pytz.timezone('Asia/Singapore')),days=(0, 1, 2, 3, 4, 5, 6) , context=update.message.chat_id)
    context.job_queue.run_daily(callback_alarm,datetime.time(hour=12, minute=00, tzinfo=pytz.timezone('Asia/Singapore')),days=(0, 1, 2, 3, 4, 5, 6) , context=update.message.chat_id)
    context.job_queue.run_daily(callback_alarm,datetime.time(hour=17, minute=30, tzinfo=pytz.timezone('Asia/Singapore')),days=(0, 1, 2, 3, 4, 5, 6) , context=update.message.chat_id)

def main():
    u = Updater(constants.TOKEN, use_context=True)
    timer_handler = CommandHandler('start', start)
    u.dispatcher.add_handler(timer_handler)
    u.start_polling()

if __name__ == '__main__'():
    main()
