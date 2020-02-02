import time
import telegram
from telegram.ext import *
from static_data import *
import apiai
from chess_scraper import *
from sql_functions import *
from credentials import *
import os


# DATABASE_URL=os.environ['DATABASE_URL']
db=sql_db(database_url)

scr=Scraper()

print('Starting bot')

#Running scraper to get tourament data
result=scr.scraper()

#Saving the results from the scraper into variables
upcoming_text=result[0]
Event_name=result[1]
Event_date=result[2]
Event_deadline=result[3]
Links=result[4]
Days_to_Tourney=result[5]
Days_to_Deadline=result[6]

dash="-"*38


def build_keyboard(buttons, n_cols, header_buttons=None, footer_buttons=None):
    """
    Function to build the menu buttons to show users.
    """
    keyboard = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return keyboard

def build_inline_keyboard(n_cols, inline_buttons, callback_tags):
    """
    Function that takes in button text and callback data to generate the view.
    """
    try:
        button_list = []
        for i in range(len(inline_buttons)):
            button_list.append(telegram.InlineKeyboardButton(inline_buttons[i], callback_data=callback_tags[i]))
        keyboard = build_keyboard(button_list, n_cols)
        return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    except Exception as ex:
        print(ex)
        

reply_markup = telegram.ReplyKeyboardMarkup(build_keyboard(['♚ Upcoming Tournaments', 
                  '♛ Chess Clubs/Meetups in SG','🗺️ Map',' 🗓️ Reminders','💬 Chess Quotes'],1), resize_keyboard=True)

reminder_markup= build_inline_keyboard(1, ["📅 Set Reminders", "🗑️ Delete Reminders", "📝 View Reminders"],["Upcoming", "Delete", "View"])

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):    
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id, text='Hi '+update.message.from_user.first_name+', '+start_text,reply_markup=reply_markup)
    
    chat_ids = db.all_rows('Userdata')
    if update.message.chat_id not in [chat_id['chat_id'] for chat_id in chat_ids]:
        idf = update.message.chat_id
        first_name = update.message.from_user.first_name
        last_name =  update.message.from_user.last_name
        username =  update.message.from_user.username
        db.insert_values('Userdata',['chat_id','first_name','last_name','username'],[idf,first_name,last_name,username ])
        
def maps(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    map_link = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text="Open in Google maps", url="https://drive.google.com/open?id=1Yb62KhG5sHnW26nu_vEOyLJkEvfYHkaD&usp=sharing")]])
    bot.send_photo(chat_id=update.message.chat_id, photo='https://drive.google.com/file/d/17ynPHiHnd2tEAvTYuUk_byemL73CrIH9/view?usp=sharing',reply_markup=map_link)

def tournaments(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id, text=upcoming_text,parse_mode="HTML",disable_web_page_preview=True,reply_markup=reply_markup)

def clubs(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,text=club_info,parse_mode="HTML",disable_web_page_preview=True,reply_markup=reply_markup)

def reminder(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,text="What would you like to do?",reply_markup=reminder_markup)

def help(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,text=commands,reply_markup=reply_markup, parse_mode="HTML")

def quotes(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,text=qt.get_quote(),parse_mode="HTML",reply_markup=reply_markup)

def keyboard_query(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

    if(update.message.text=="🗺️ Map"):
        maps(bot, update)
    elif(update.message.text=="♚ Upcoming Tournaments"):        
        tournaments(bot,update)
    elif(update.message.text=="♛ Chess Clubs/Meetups in SG"):
        clubs(bot,update)
    elif(update.message.text=="🗓️ Reminder"):
        reminder(bot,update)
    elif(update.message.text=="💬 Chess Quotes"):
        quotes(bot, update)        
    
    else:
        request = apiai.ApiAI(apiai_token).text_request() # Dialogflow API Token
        request.lang = 'en' 
        request.session_id = 'BatlabAIBot' # ID dialog session (for bot training)
        request.query = update.message.text # Send request to AI with the user message
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech'] # Take JSON answer
        if (response=="Upcoming Tournaments"):
            tournaments(bot,update)
        elif (response=="clubs"):
            clubs(bot,update)
        elif (response=="reminder"):
            reminder(bot,update)
        elif (response=="map"):
            maps(bot,update)    
        elif (response=="functions"):
            bot.send_message(chat_id=update.message.chat_id,text=Functions,reply_markup=reply_markup)
        elif (response=="quotes"):
            quotes(bot,update)
        elif (response):
            bot.send_message(chat_id=update.message.chat_id, text=response)    
        else:
            bot.sendSticker(chat_id=update.message.chat_id,sticker="CAADAQADfgEAAgdGOAp_-D1_e3VfgQI")
            bot.send_message(chat_id=update.message.chat_id,text=default,reply_markup=reply_markup, parse_mode="HTML")     

        
def inline_query(bot,update):
    """Function to handle all the callback queries generated by inline keyboards"""
    query=update.callback_query
    
    if(query.data=="Upcoming"):
        keyboard=[]
        for i in range(len(Event_name)):
            if(Days_to_Tourney[i]>0):
                keyboard.append([telegram.InlineKeyboardButton(Event_name[i][0:63], callback_data=Event_name[i][0:63])])
        upcoming_buttons=telegram.InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=query.message.chat_id, text="Select the tournament for which you would like reminders:", reply_markup=upcoming_buttons)
    
    
    if(query.data=="Delete"):
        inline_markup = build_inline_keyboard(1, ['✔️ Yes', '❌ No'], ['yes', 'no'])
        bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,text="⚠️ By selecting this option, you will be deleting all reminders. Are you sure you want to continue?",reply_markup=inline_markup)
    
    if(query.data=="yes"):
        id_chat=query.message.chat_id
        db.execute("DELETE from Notifications WHERE chat_id="+str(id_chat))
        bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,text="Your reminders have been deleted.")
    
    if(query.data=="no"):
        bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,text="No changes have been made.",reply_markup=reminder_markup)   
        
    if(query.data=="View"):
        
        all_rows = db.all_rows('Notifications')
        rem = False
        for i in range(0,len(all_rows),1):
            if(all_rows[i][0]==query.message.chat_id):
                rem=True
                string=[]
                for j in range(len(all_rows[i])):
                    for k in range(len(Event_name)):
                        if(all_rows[i][j]==Event_name[k]):
                            if(Days_to_Deadline[k]==''):
                                string.append("<b>"+Event_name[k]+"</b>"+"\n"+"Tournament Day: "+str(Days_to_Tourney[k])+" day(s) left")
                            elif(Days_to_Deadline[k]=='Registration Closed'):
                                string.append("<b>"+Event_name[k]+"</b>"+"\n"+"Tournament Day: "+str(Days_to_Tourney[k])+" day(s) left"+"\n"+"Registration Deadline: "+str(Days_to_Deadline[k]))
                            else:
                                string.append("<b>"+Event_name[k]+"</b>"+"\n"+"Tournament Day: "+str(Days_to_Tourney[k])+" day(s) left"+"\n"+"Registration Deadline: "+str(Days_to_Deadline[k])+" day(s) left")
                if(len(string)==1):
                    bot.send_message(chat_id=query.message.chat_id,text="You have {} reminder".format(len(string)))
                else:
                    bot.send_message(chat_id=query.message.chat_id,text="You have {} reminders".format(len(string)))
                for z in string:
                    try:
                        bot.send_message(chat_id=query.message.chat_id,text=z,parse_mode="HTML")
                    except:
                        print(i,'failed')
        if(rem==False):
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,text="You don't have any reminders. To set reminders please use the option below",reply_markup=reminder_markup)
        
    
    #Inseting reminders into database    
    for i in range(len(Event_name)):
            if(query.data==Event_name[i][0:63]):
                bot.edit_message_text(
                    chat_id=query.message.chat_id,
                    message_id=query.message.message_id,
                    text="✅ Your reminder for "+Event_name[i]+" has been set.\nYou will receive a reminder everyday at 9:00 am.",
                    )
                
                
                output=db.all_rows('Notifications')
                #print(output)
                if (len(output)==0):
                    db.insert_values('Notifications', ['chat_id','Tournament_1','Days_left_1'], [query.message.chat_id, Event_name[i], Days_to_Tourney[i]])
                else:                    
                    if query.message.chat_id not in [chat_id['chat_id'] for chat_id in output]:
                        db.insert_values('Notifications', ['chat_id','Tournament_1','Days_left_1'], [query.message.chat_id, Event_name[i], Days_to_Tourney[i]])
                    else:
                        for x in range(len(output)):
                            if(output[x][0]==query.message.chat_id):
                                for y in range(1,len(output[x]),2):
                                    if (output[x][y]==None or output[x][y]=="temp"):
                                        print(db.val_in_row('Notifications', query.data, x))
                                        if(not(db.val_in_row('Notifications', query.data, x))):
                                            db.update('Notifications','Tournament_{}'.format(str(int((y+1)/2))),Event_name[i], 'chat_id',query.message.chat_id)
                                            db.update('Notifications','Days_left_{}'.format(str(int((y+1)/2))),Days_to_Tourney[i], 'chat_id',query.message.chat_id)
                                            break                            
                                    

def reminders(bot,update):
    """Function to send reminders for upcoming tournaments"""
    
    print('Sending Reminders {}'.format(datetime.now()))
    all_rows = db.all_rows('Notifications')
    global Days_to_Deadline
    global Event_name
    global Days_to_Tourney
    for i in range(0,len(all_rows),1):
        rem_msg=[]
        for j in range(len(all_rows[i])):
            for k in range(len(Event_name)):
                if(all_rows[i][j]==Event_name[k]):
                    if(Days_to_Deadline[k]==''):
                        rem_msg.append("<b>"+Event_name[k]+"</b>"+"\n"+"Tournament Day: "+str(Days_to_Tourney[k])+" day(s) left")
                    elif(Days_to_Deadline[k]=='Registration Closed'):
                        rem_msg.append("<b>"+Event_name[k]+"</b>"+"\n"+"Tournament Day: "+str(Days_to_Tourney[k])+" day(s) left"+"\n"+"Registration Deadline: "+str(Days_to_Deadline[k]))
                    else:
                        rem_msg.append("<b>"+Event_name[k]+"</b>"+"\n"+"Tournament Day: "+str(Days_to_Tourney[k])+" day(s) left"+"\n"+"Registration Deadline: "+str(Days_to_Deadline[k])+" day(s) left")
        for msg in rem_msg:
            try:
                bot.send_message(chat_id=all_rows[i][0],text=msg,parse_mode="HTML")
            except:
                print(i,'failed')

    

def new_tournament(bot,update):
    """Function to check whether a new tournament has been added.
       Runs every 5 mins.
    """
    print('check: {}'.format(datetime.now()))
    global Event_name
    New_events=scr.scraper()[1]
    New_days=scr.scraper()[5]
    event_num=[]
    for i in range(len(New_events)):
        itr=0
        for j in range(len(Event_name)):
            if (New_events[i].strip()!=Event_name[j]):#Comparing Each new event to every single old event and if none of them match then it is considered a new tourney
                itr=itr+1
        if(itr==len(Event_name)):
            if(New_days[i]>0):
                event_num.append(i)
                #print(event_num)
    if(len(event_num)!=0):
        updates('x','y')
    
    user_ids = db.all_rows('Userdata')
    for user in range(0,len(user_ids),1):
        for i in range(len(event_num)):
            try:
                bot.send_message(chat_id=user_ids[user][0],text="New tournament/update has been added :\n"+dash+"\n<b>"+Event_name[event_num[i]]+"</b>"+"\n\n"+"<b>Date</b> : "+Event_date[event_num[i]]+"\n"+Event_deadline[event_num[i]]+"\n"+"<b>Link</b> : "+Links[event_num[i]]+"\n"+dash+"\n",reply_markup=reply_markup,parse_mode="HTML",disable_web_page_preview=True)
            except:
                None
                
def updates(arg1,arg2):
    """Function to update the list of upcoming tournaments and the days left for each tournament.
       Runs once a day or whenever a new tournament is added.
    """
    
    print('Updates: {}'.format(datetime.now()))
    ups=scr.scraper()
    global upcoming_text
    upcoming_text=ups[0]
    global Event_name
    Event_name=ups[1]
    global Event_date
    Event_date=ups[2]
    global Event_deadline
    Event_deadline=ups[3]
    global Links
    Links=ups[4]
    global Days_to_Tourney
    Days_to_Tourney=ups[5]
    global Days_to_Deadline
    Days_to_Deadline=ups[6]
                
    output=db.all_rows('Notifications')
    
    #Updating the Days_left_count for tournaments
    for i in range(len(output)):
        for j in range(len(output[i])):
            for k in range(len(Event_name)):
                if(output[i][j]==Event_name[k]):
                    db.update('Notifications', 'Days_left_{}'.format(str(int((j+1)/2))), Days_to_Tourney[k], 'chat_id', output[i][0])
                                        
    #Removing tournaments which are completed (Days_left < 1)
    output=db.all_rows('Notifications')
    
    #Set all empty cells to the right of the cell with tournament to remove with temporary values
    for i in range(len(output)):
        for j in range(len(output[i])):
            if(type(output[i][j])==int):
                if((output[i][j])<1):
                    for k in range(j,len(output[i])-1,1):
                        if(output[i][k+1]==None):
                            db.update('Notifications', 'Tournament_{}'.format(str(int((k+2)/2))),'temp','chat_id', output[i][0])
                            db.update('Notifications', 'Days_left_{}'.format(str(int((k+2)/2))), 9999,'chat_id', output[i][0])
                                                        
        
                    output=db.all_rows('Notifications')
                
                    #Shifting all the tournaments once to the left to remove the tournament which is completed
                    for l in range(j,len(output[i])-2,2):
                            db.update('Notifications', 'Tournament_{}'.format(str(int((l+1)/2))),output[i][l+1],'chat_id', output[i][0])
                            db.update('Notifications', 'Days_left_{}'.format(str(int((l+1)/2))),output[i][l+2],'chat_id', output[i][0])
                    
                    output=db.all_rows('Notifications')
                    
                    #Set all empty cells with temporary values
                    for m in range(0,len(output[i])-1,1):
                        if(output[i][m]==9999):
                            db.update('Notifications', 'Tournament_{}'.format(str(int((m+1)/2))),'temp','chat_id', output[i][0])
                            db.update('Notifications', 'Days_left_{}'.format(str(int((m+1)/2))),9999,'chat_id', output[i][0])
                            
                    output=db.all_rows('Notifications')
                    
    
        
def main():

    updater = Updater(token=token)
    j = updater.job_queue
    dp = updater.dispatcher

    job_minute = j.run_repeating(new_tournament, interval=300, first=5) 
    reminder_job=j.run_daily(reminders,datetime.strptime('09:00', '%H:%M').time())
    update_job=j.run_daily(updates,datetime.strptime('00:00', '%H:%M').time())



    start_handler = CommandHandler('start', start) 
    keyboard_handler = MessageHandler(Filters.text, keyboard_query)
    query_handler = CallbackQueryHandler(inline_query)
    map_handler = CommandHandler('map', maps) 
    tournament_handler = CommandHandler('tournaments', tournaments)
    club_handler = CommandHandler('clubs', clubs) 
    reminder_handler = CommandHandler('reminder', reminder)
    quote_handler = CommandHandler('quotes', quotes)
    help_handler = CommandHandler('help', help)


    dp.add_handler(start_handler)
    dp.add_handler(keyboard_handler)
    dp.add_handler(query_handler)  
    dp.add_handler(map_handler)
    dp.add_handler(tournament_handler)
    dp.add_handler(club_handler)
    dp.add_handler(reminder_handler)
    dp.add_handler(quote_handler)
    dp.add_handler(help_handler)
    
    updater.start_polling()
    updater.idle()
        
if __name__ == '__main__':
    main()        


