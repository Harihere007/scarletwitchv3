class script(object):
    START_TXT = """đˇđ´đģđžđĻ {},
đŧđĸ đđđđđĻ , <a href='http://t.me/Autofilterbot6_bot'>đŧđžđđ¸đ´đđđ¸đŧđ´ đĻšââ đ§đ</a>, đ¸đ'đ đđđđĸ đđđđĸ đđđđ đđđ đđ đđ đĸđđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đ¸'đđ đđđđđđđ đđđđđđ đđđđđ đ¤
"""
    HELP_TXT = """đˇđ´đ đĻ{}
đđĻđŗđĻ đđ´ đđŠđĻ đđĻđ­đą đđ°đŗ đđē đđ°đŽđŽđĸđ¯đĨđ´."""
    ABOUT_TXT = """
đđĄđĸđŦ đĸđŦ áááŠááá´áĸ á¯ááĸááŧ đĻšââ'đŦ đđđ¨đŽđ­ đĻđŦđ 
âĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩ
ââââââ° ęĒáĨęĒŽęĒđŊ ęĒđ´á§ âąâââąâÛĒÛĒ
ââ­ââââââââââââââââŖ 
ââŖâĒŧ đđ đđŧđđ - <a href="http://t.me/malluchickv3_bot"> áááŠááá´áĸ á¯ááĸááŧ đĻšââ </a>
ââŖâĒŧ âšī¸âēī¸âī¸1 - <a href="http://t.me/Tony_Stark06"> đđžđŊđ </a>
ââŖâĒŧ âšī¸âēī¸âī¸2 - <a href="http://t.me/Harihere007"> đˇđđđđđđđ </a>
ââŖâĒŧ đđ˛đĢđģđĒđģđģđ - đŋđđđžđļđđ°đŧ
ââŖâĒŧ đđĒđˇđ°đžđĒđ°đŽ - đŋđđđˇđžđŊ đš
ââŖâĒŧ đđĒđŊđĒ đđĒđŧđŽ - đŧđžđŊđļđž đŗđą
ââŖâĒŧ đđ¸đŊ đŧđŽđģđŋđŽđģ -  đˇđ´đđžđēđ
ââŖâĒŧ đđžđ˛đĩđ­ đĸđŊđĒđŊđžđŧ - v1.0.1 [ đąđ´đđ° ]
ââ°ââââââââââââââââŖ âââââââââââââââââââââąâÛĒÛĒ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ đđđđ đđđđđđ đđđđđđđ. 
- ÕOáááá´ áOáĒá´ - <a href="http://t.me/malluchickv3_bot"> đđđđđ đđđĨđ </a>

đ đđĻđ§đđĨ:
<a href="http://t.me/malluchickv3_bot"> ââ¯  áááŠááá´áĸ á¯ááĸááŧ đĻšââ  ââŖ </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

âĸ/whois :-give a user full details"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
âĸ /alive - check me alive or deadđ¤§
Just for a rasamđ"""
   
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>đ Commands & Usage:</b>

â /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

â /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""

    FILE_TXT = """â¤ đđđĨđŠ: 
    
  đĨđđđž đ˛đđđđžđđđđ đđđđ đđđđđđđ đ đđđ đđđđđ đđđđđ đđđ đđđđ đĸđđ đ đđđđđđđđđ đđđđ đ đđđ đđđđ đđđđ đ đđđ đđđđđ đđđđ đđđđđ đĸđđ đđđđ đđ đđđđ đđđĸ đđđđđđđ đ đđđđđđ đđđđđđ đđâ¤
  
  đđ¨đĻđĻđđ§đđŦ đđ§đ đđŦđđ đ:
âĒ /plink - đąđžđđđ đđ đēđđ đđžđŊđđē đđ đđžđ đđđđ
âĒ /pbatch - đ´đđž đđđđ đđēđŊđđē đđđđ đđđđ đđđđ đŧđđđđēđđŊ
âĒ /batch - To create link for multiple post

âđ¤đđēđđđđž:/pbatch <code>https://t.me/Sflix2k/497 https://t.me/Sflix2k/498</code>"""
    
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĸ /filter - add a filter in chat.
âĸ /filters - list all the filters of a chat.
âĸ /del - delete a specific filter in chat.
âĸ /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.

<b>đ Commands & Usage:</b>
âĒ /plink :- đąđžđđđ đđ đēđđ đđžđŊđđē đđ đđžđ đđđđ.
âĒ /pbatch :- đ´đđž đđđđ đđēđŊđđē đđđđ đđđđ đđđđ đŧđđđđēđđŊ.
âĒ /batch :- To create link for multiple post."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĸ /connect  - connect a particular chat to your PM.
âĸ /disconnect  - disconnect from a chat.
âĸ /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
âĸ /id - get id of a specifed user.
âĸ /info  - get information about a user.
âĸ /json - get the json details of a message.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on both pm and group.
âĸ These commands can be used by any group member."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
âĸ /imdb  - get the film information from IMDb source.
âĸ /search  - get the film information from various sources.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ More search tools can be found on inline.
âĸ Those commands works on both pm and group."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
âĸ /ban - ban a user.
âĸ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
âĸ /mute - mute a user.
âĸ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
âĸ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on group.
âĸ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĸ /logs - to get the rescent errors.
âĸ /stats - to get status of files in db.
âĸ /delete - to delete a specific file from db.
âĸ /users - to get list of my users and ids.
âĸ /chats - to get list of the my chats and ids.
âĸ /leave - to leave from a chat.
âĸ /disable - do disable a chat.
âĸ /ban_users - to ban a user.
âĸ /unban_users - to unban a user.
âĸ /channel - to get list of total connected channels.
âĸ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**âĻī¸ READ THIS INSTRUCTION âĻī¸**

__đŖ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately đ__

**đ JOIN THIS CHANNEL & TRY AGAIN đ**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""


    CREATOR_REQUIRED = """âYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âī¸ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """đŽ Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """âI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """âī¸ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
