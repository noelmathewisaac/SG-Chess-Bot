import random 

club_info="""
<b>MONDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
No chess site known at present

<b>TUESDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
<a href="https://www.facebook.com/groups/BishanChessClub">Bishan Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/DRf5T3e31SWw9uox6">Bishan CC</a>/<a href="https://goo.gl/maps/MFcToNcRNrhxf7Q8A">Bishan Public Library</a> (Please check their <a href="https://www.facebook.com/groups/BishanChessClub">facebook page</a> for the exact location)
<b>When :</b> 6:30pm to 9:00pm
<b>Membership fee :</b> None
------------------------------------
<a href="https://www.facebook.com/groups/519571975119442/">Senja-Cashew CC Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/eRqjfdVgFPPg8kwD6">Senja-Cashew Community Club</a>, Cashew 3G Wellness Centre, Activity Room
<b>When :</b> 7:30pm to 9:30pm
<b>Membership fee :</b> None


<b>WEDNESDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
<a href="https://www.meetup.com/Singapore-Chess-Meetup/">The Singapore Chess Meetup</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/PwwuYUAeUXLquhLZ8">Asia Square Tower One</a> (nearest MRT station is Downtown Station, Downtown "Blue" line)
<b>When :</b> 6:30pm onwards
<b>Membership fee :</b> None

<b>THURSDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
<a href="https://www.facebook.com/NUS-Intellectual-Games-Club-268102093792288/">NUS Intellectual Games Club (NUS IGC)</a>
\n<b>Where :</b> National University of Singapore (NUS), Kent Ridge Campus, Multi Purpose Sports Hall (<a href="https://goo.gl/maps/PwGzBdNnpTQC3UTA9">MPSH4</a>)
<b>When :</b> 6:30pm to 9pm
<b>Note :</b> Non-NUS students may contact Yan Han (<code>sps08.lauyanhan@gmail.com</code>) to be brought in.
------------------------------------
<a href="https://www.facebook.com/groups/519571975119442/">Senja-Cashew CC Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/eRqjfdVgFPPg8kwD6">Senja-Cashew Community Club</a>, Cashew 3G Wellness Centre, Activity Room
<b>When :</b> 7:30pm to 9:30pm
<b>Membership fee :</b> None
------------------------------------
<a href="https://www.facebook.com/groups/BishanChessClub">Bishan Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/DRf5T3e31SWw9uox6">Bishan CC</a>/<a href="https://goo.gl/maps/MFcToNcRNrhxf7Q8A">Bishan Public Library</a> (Please check their <a href="https://www.facebook.com/groups/BishanChessClub">facebook page</a> for the exact location)
<b>When :</b> 6:30pm to 9:00pm
<b>Membership fee :</b> None

<b>FRIDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
<a href="https://www.facebook.com/groups/429263043763052/">Thomson CC Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/7VJTZRHfkc4Cpq4B7">Thomson Community Club</a>, level 3
<b>When :</b> 6:30pm to 9pm
<b>Membership fee :</b> $18/year (aged 13 and above), $12/year (aged 12 and below), requires PAssion Card membership to join.
<b>Note: </b> From April 2019 onwards, due to renovations, the sessions shall be at Classroom 4 in Bishan East CC
------------------------------------
<a href="https://www.facebook.com/groups/cashewchessclub/">Cashew Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/2MJorTYfc3vHQaS69">Cashew RC Zone 5</a> (Opposite Bukit Panjang Plaza McDonald’s)
<b>When :</b> 8pm onwards
<b>Membership fee :</b> None

<b>SATURDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
<a href="http://www.nuss.org.sg/event-category/social-recreation/join-the-chess-interest-group" >NUSS Chess Interest Group</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/CwiQbrUncPM3Qegy9">Kent Ridge Guild House</a>, Lobby / Activity Room
<b>When :</b> 1st Saturday of each month (2:15pm to 5:15pm)
<b>Membership fee :</b> Free for NUSS members, $5 for Guests
------------------------------------
<b>Cairnhill CC Chess Club</b>
\n<b>Where :</b> <a href="https://goo.gl/maps/qv84LmSCz5xpXACF7">Cairnhill Community Club</a>
<b>When :</b> Saturday afternoon (5pm to 7pm)
<b>Membership fee :</b> Unknown

<b>SUNDAY</b>
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝
<a href="https://www.meetup.com/pubxchess/">Cafe X Chess</a>
\n<b>Where :</b> Different Cafe locations across Singapore -- venue is determined only the week / days before (please keep a lookout on the meetup page)
<b>When :</b> 10am to 1pm (Please check the meetup page before the event to confirm)
<b>Membership fee :</b> None (Participants are encouraged to patronize the cafe)
<b>Eligibility :</b> Everyone (more suited to kids and casual players who are early risers)
<b>Note :</b> Rapid Training Games with time control 25|10 will be played
------------------------------------
<a href="https://www.meetup.com/pubxchess/">Pub X Chess</a>
\n<b>Where :</b> Different Pub locations across Singapore -- venue is determined only the week / days before (please keep a lookout on the meetup page or the facebook page)
<b>When :</b> Usually starts at 3:30pm sharp (Please check the meetup page before the event to confirm)
<b>Membership fee :</b> None (Participants are encouraged to patronize the bar)
<b>Eligibility :</b> With effect from 15 Dec 2019, the session is specially catered for adults and minors with FIDE or in-house rating above 1700
<b>Note :</b> There is a blitz tournament (Round-robin/Swiss-system depending on the number of atendees) every week.
------------------------------------
<a href="https://www.onepa.sg/interest/details/i000013847" >Nanyang CC Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/iZrzLhRL2shfZjHZ9">Nanyang Community Club</a>, ground floor, "glass room"
<b>When :</b> 3pm to 5pm
<b>Membership fee :</b> None
------------------------------------
<a href="https://chessqcc.site123.me/">Queenstown CC Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/tyddJ7ScyiugadCaA" >Queenstown Community Centre</a>
<b>When :</b> 3pm to 7pm
<b>Membership fee :</b>
1 year – $10 (under 20) | $20 (Adults)
3 years — $ 25 (under 20) | $50 (Adults)
------------------------------------
<a href="https://www.facebook.com/singaporechessfederation/photos/a.530047600438480/889336877842882/?type=1&theater">Siglap South CC Chess Club</a>
\n<b>Where :</b> <a href="https://goo.gl/maps/dE8AJdcSm7s8R46v8">Siglap South Community Club</a>, Room #02-07
<b>When :</b> 3pm to 6pm
<b>Membership fee :</b>
$4 for members aged 13 and below for 1/2 year (or $8 per annum)
$9 for members aged above 13 for 1/2 year (or $18 per annum)
♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝♝

<a href="https://drive.google.com/open?id=1Yb62KhG5sHnW26nu_vEOyLJkEvfYHkaD&usp=sharing">Map of Chess Clubs/Meetups</a>

Reference : <a href="https://forksandpins.blogspot.com/2020/01/where-to-play-chess-in-singapore-2020.html">https://forksandpins.blogspot.com</a>

"""

start_text="""
I help you keep up to date on chess events in SG.

What would you like to do?

/map - Map of Chess Clubs & Meetups
/tournaments - Upcoming Chess Tournaments
/clubs - List of Chess Clubs & Meetups
/reminder - Set a reminder for upcoming tournaments
/quotes - Get a famous chess quote
/help - See a list of commands

You can also use the keyboard below to do the same.
"""

commands="""
List of commands:

/start - Start or restart the bot
/map - Map of Chess Clubs & Meetups
/tournaments - Upcoming Chess Tournaments
/clubs - List of Chess Clubs & Meetups
/reminder - Set a reminder for upcoming tournaments
/quotes - Get a famous chess quote
/help - See a list of commands

For suggestions/contributions please refer to the <a href = "https://github.com/noelmathewisaac/SG-Chess-Bot">Github Repo</a>
"""

default="""
Sorry, I didn't understand your message. Please select one of the following options:

/start - Start or restart the bot
/map - Map of Chess Clubs & Meetups
/tournaments - Upcoming Chess Tournaments
/clubs - List of Chess Clubs & Meetups
/reminder - Set a reminder for upcoming tournaments
/quotes - Get a famous chess quote
/help - See a list of commands

For suggestions/contributions please refer to the <a href = "https://github.com/noelmathewisaac/SG-Chess-Bot">Github Repo</a>
"""

Functions="""
I can help you with the following:

♚ View a list of upcoming tournaments (from websites of Singapore Chess Federation & Chess Academy Singapore)
♛ View a map and list of Chess Clubs/Meetups
♜ Receive notifications when a new tournament is added
♝ Set reminders for tournament dates and registration deadlines
♞ Read famous chess quotes
"""

def all_quotes():
    string='''
 “ɪ ʜᴀᴠᴇ ᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴘᴇʀsᴏɴᴀʟ ᴄᴏɴᴄʟᴜsɪᴏɴ ᴛʜᴀᴛ ᴡʜɪʟᴇ ᴀʟʟ ᴀʀᴛɪsᴛs ᴀʀᴇ ɴᴏᴛ ᴄʜᴇss ᴘʟᴀʏᴇʀs, ᴀʟʟ ᴄʜᴇss ᴘʟᴀʏᴇʀs ᴀʀᴇ ᴀʀᴛɪsᴛs.” – ᴍᴀʀᴄᴇʟ ᴅᴜᴄʜᴀᴍᴘ
 “ᴜɴʟɪᴋᴇ ᴏᴛʜᴇʀ ɢᴀᴍᴇs ɪɴ ᴡʜɪᴄʜ ʟᴜᴄʀᴇ ɪs ᴛʜᴇ ᴇɴᴅ ᴀɴᴅ ᴀɪᴍ, [ᴄʜᴇss] ʀᴇᴄᴏᴍᴍᴇɴᴅs ɪᴛsᴇʟғ ᴛᴏ ᴛʜᴇ ᴡɪsᴇ ʙʏ ᴛʜᴇ ғᴀᴄᴛ ᴛʜᴀᴛ ɪᴛs ᴍɪᴍɪᴄ ʙᴀᴛᴛʟᴇs ᴀʀᴇ ғᴏᴜɢʜᴛ ғᴏʀ ɴᴏ ᴘʀɪᴢᴇ ʙᴜᴛ ʜᴏɴᴏʀ. ɪᴛ ɪs ᴇᴍɪɴᴇɴᴛʟʏ ᴀɴᴅ ᴇᴍᴘʜᴀᴛɪᴄᴀʟʟʏ ᴛʜᴇ ᴘʜɪʟᴏsᴏᴘʜᴇʀ’s ɢᴀᴍᴇ.” – ᴘᴀᴜʟ ᴍᴏʀᴘʜʏ
 “ᴛʜᴇ ʙᴇᴀᴜᴛʏ ᴏғ ᴄʜᴇss ɪs ɪᴛ ᴄᴀɴ ʙᴇ ᴡʜᴀᴛᴇᴠᴇʀ ʏᴏᴜ ᴡᴀɴᴛ ɪᴛ ᴛᴏ ʙᴇ. ɪᴛ ᴛʀᴀɴsᴄᴇɴᴅs ʟᴀɴɢᴜᴀɢᴇ, ᴀɢᴇ, ʀᴀᴄᴇ, ʀᴇʟɪɢɪᴏɴ, ᴘᴏʟɪᴛɪᴄs, ɢᴇɴᴅᴇʀ, ᴀɴᴅ sᴏᴄɪᴏᴇᴄᴏɴᴏᴍɪᴄ ʙᴀᴄᴋɢʀᴏᴜɴᴅ. ᴡʜᴀᴛᴇᴠᴇʀ ʏᴏᴜʀ ᴄɪʀᴄᴜᴍsᴛᴀɴᴄᴇs, ᴀɴʏᴏɴᴇ ᴄᴀɴ ᴇɴᴊᴏʏ ᴀ ɢᴏᴏᴅ ғɪɢʜᴛ ᴛᴏ ᴛʜᴇ ᴅᴇᴀᴛʜ ᴏᴠᴇʀ ᴛʜᴇ ᴄʜᴇss ʙᴏᴀʀᴅ.” – sɪᴍᴏɴ ᴡɪʟʟɪᴀᴍs
 “ᴄʜᴇss ɪs ᴛʜᴇ sᴛʀᴜɢɢʟᴇ ᴀɢᴀɪɴsᴛ ᴛʜᴇ ᴇʀʀᴏʀ.” – ᴊᴏʜᴀɴɴᴇs ᴢᴜᴋᴇʀᴛᴏʀᴛ
 “ᴇᴠᴇʀʏ ᴄʜᴇss ᴍᴀsᴛᴇʀ ᴡᴀs ᴏɴᴄᴇ ᴀ ʙᴇɢɪɴɴᴇʀ.” – ɪʀᴠɪɴɢ ᴄʜᴇʀɴᴇᴠ
 “ᴀᴠᴏɪᴅ ᴛʜᴇ ᴄʀᴏᴡᴅ. ᴅᴏ ʏᴏᴜʀ ᴏᴡɴ ᴛʜɪɴᴋɪɴɢ ɪɴᴅᴇᴘᴇɴᴅᴇɴᴛʟʏ. ʙᴇ ᴛʜᴇ ᴄʜᴇss ᴘʟᴀʏᴇʀ, ɴᴏᴛ ᴛʜᴇ ᴄʜᴇss ᴘɪᴇᴄᴇ.” – ʀᴀʟᴘʜ ᴄʜᴀʀᴇʟʟ
 “ᴄʜᴇss ᴍᴀᴋᴇs ᴍᴇɴ ᴡɪsᴇʀ ᴀɴᴅ ᴄʟᴇᴀʀ-sɪɢʜᴛᴇᴅ.” – ᴠʟᴀᴅɪᴍɪʀ ᴘᴜᴛɪɴ
 “ᴄʜᴇss ɪs ᴛʜᴇ ɢʏᴍɴᴀsɪᴜᴍ ᴏғ ᴛʜᴇ ᴍɪɴᴅ.” – ʙʟᴀɪsᴇ ᴘᴀsᴄᴀʟ
 “ᴄʜᴇss ʜᴏʟᴅs ɪᴛs ᴍᴀsᴛᴇʀ ɪɴ ɪᴛs ᴏᴡɴ ʙᴏɴᴅs, sʜᴀᴄᴋʟɪɴɢ ᴛʜᴇ ᴍɪɴᴅ ᴀɴᴅ ʙʀᴀɪɴ sᴏ ᴛʜᴀᴛ ᴛʜᴇ ɪɴɴᴇʀ ғʀᴇᴇᴅᴏᴍ ᴏғ ᴛʜᴇ ᴠᴇʀʏ sᴛʀᴏɴɢᴇsᴛ ᴍᴜsᴛ sᴜғғᴇʀ.” – ᴀʟʙᴇʀᴛ ᴇɪɴsᴛᴇɪɴ
 “ᴄʜᴇss ɪs ᴀ ᴡᴀʀ ᴏᴠᴇʀ ᴛʜᴇ ʙᴏᴀʀᴅ. ᴛʜᴇ ᴏʙᴊᴇᴄᴛ ɪs ᴛᴏ ᴄʀᴜsʜ ᴛʜᴇ ᴏᴘᴘᴏɴᴇɴᴛ’s ᴍɪɴᴅ.” – ʙᴏʙʙʏ ғɪsᴄʜᴇʀ
 “ɪ ᴀᴍ ᴄᴏɴᴠɪɴᴄᴇᴅ, ᴛʜᴇ ᴡᴀʏ ᴏɴᴇ ᴘʟᴀʏs ᴄʜᴇss ᴀʟᴡᴀʏs ʀᴇғʟᴇᴄᴛs ᴛʜᴇ ᴘʟᴀʏᴇʀ’s ᴘᴇʀsᴏɴᴀʟɪᴛʏ. ɪғ sᴏᴍᴇᴛʜɪɴɢ ᴅᴇғɪɴᴇs ʜɪs ᴄʜᴀʀᴀᴄᴛᴇʀ, ᴛʜᴇɴ ɪᴛ ᴡɪʟʟ ᴀʟsᴏ ᴅᴇғɪɴᴇ ʜɪs ᴡᴀʏ ᴏғ ᴘʟᴀʏɪɴɢ.” – ᴠʟᴀᴅɪᴍɪʀ ᴋʀᴀᴍɴɪᴋ
 “ᴛʜᴇ ɢᴀᴍᴇ ᴏғ ᴄʜᴇss ɪs ɴᴏᴛ ᴍᴇʀᴇʟʏ ᴀɴ ɪᴅʟᴇ ᴀᴍᴜsᴇᴍᴇɴᴛ. sᴇᴠᴇʀᴀʟ ᴠᴇʀʏ ᴠᴀʟᴜᴀʙʟᴇ ǫᴜᴀʟɪᴛɪᴇs ᴏғ ᴛʜᴇ ᴍɪɴᴅ, ᴜsᴇғᴜʟ ɪɴ ᴛʜᴇ ᴄᴏᴜʀsᴇ ᴏғ ʜᴜᴍᴀɴ ʟɪғᴇ, ᴀʀᴇ ᴛᴏ ʙᴇ ᴀᴄǫᴜɪʀᴇᴅ ᴏʀ sᴛʀᴇɴɢᴛʜᴇɴᴇᴅ ʙʏ ɪᴛ… ʟɪғᴇ ɪs ᴀ ᴋɪɴᴅ ᴏғ ᴄʜᴇss, ɪɴ ᴡʜɪᴄʜ ᴡᴇ ʜᴀᴠᴇ ᴏғᴛᴇɴ ᴘᴏɪɴᴛs ᴛᴏ ɢᴀɪɴ, ᴀɴᴅ ᴄᴏᴍᴘᴇᴛɪᴛᴏʀs ᴏʀ ᴀᴅᴠᴇʀsᴀʀɪᴇs ᴛᴏ ᴄᴏɴᴛᴇɴᴅ ᴡɪᴛʜ.” – ʙᴇɴᴊᴀᴍɪɴ ғʀᴀɴᴋʟɪɴ
 “ᴀs ᴘʀᴏᴠᴇᴅ ʙʏ ᴇᴠɪᴅᴇɴᴄᴇ, [ᴄʜᴇss ɪs] ᴍᴏʀᴇ ʟᴀsᴛɪɴɢ ɪɴ ɪᴛs ʙᴇɪɴɢ ᴀɴᴅ ᴘʀᴇsᴇɴᴄᴇ ᴛʜᴀɴ ᴀʟʟ ʙᴏᴏᴋs ᴀɴᴅ ᴀᴄʜɪᴇᴠᴇᴍᴇɴᴛs; ᴛʜᴇ ᴏɴʟʏ ɢᴀᴍᴇ ᴛʜᴀᴛ ʙᴇʟᴏɴɢs ᴛᴏ ᴀʟʟ ᴘᴇᴏᴘʟᴇ ᴀɴᴅ ᴀʟʟ ᴀɢᴇs; ᴏғ ᴡʜɪᴄʜ ɴᴏɴᴇ ᴋɴᴏᴡs ᴛʜᴇ ᴅɪᴠɪɴɪᴛʏ ᴛʜᴀᴛ ʙᴇsᴛᴏᴡᴇᴅ ɪᴛ ᴏɴ ᴛʜᴇ ᴡᴏʀʟᴅ, ᴛᴏ sʟᴀʏ ʙᴏʀᴇᴅᴏᴍ, ᴛᴏ sʜᴀʀᴘᴇɴ ᴛʜᴇ sᴇɴsᴇs, ᴛᴏ ᴇxʜɪʟᴀʀᴀᴛᴇ ᴛʜᴇ sᴘɪʀɪᴛ.” – sᴛᴇғᴀɴ ᴢᴡᴇɪɢ
 “ᴄʜᴇss ᴅᴏᴇsɴ’ᴛ ᴅʀɪᴠᴇ ᴘᴇᴏᴘʟᴇ ᴍᴀᴅ, ɪᴛ ᴋᴇᴇᴘs ᴍᴀᴅ ᴘᴇᴏᴘʟᴇ sᴀɴᴇ.” – ʙɪʟʟ ʜᴀʀᴛsᴛᴏɴ
 “ɪɴ ʟɪғᴇ, ᴀs ɪɴ ᴄʜᴇss, ᴏɴᴇ’s ᴏᴡɴ ᴘᴀᴡɴs ʙʟᴏᴄᴋ ᴏɴᴇ’s ᴡᴀʏ.  ᴀ ᴍᴀɴ’s ᴠᴇʀʏ ᴡᴇᴀʟᴛʜ, ᴇᴀsᴇ, ʟᴇɪsᴜʀᴇ, ᴄʜɪʟᴅʀᴇɴ, ʙᴏᴏᴋs, ᴡʜɪᴄʜ sʜᴏᴜʟᴅ ʜᴇʟᴘ ʜɪᴍ ᴛᴏ ᴡɪɴ, ᴍᴏʀᴇ ᴏғᴛᴇɴ ᴄʜᴇᴄᴋᴍᴀᴛᴇ ʜɪᴍ.” – ᴄʜᴀʀʟᴇs ʙᴜxᴛᴏɴ
 “ᴄʜᴇss ɪs ʟɪғᴇ ɪɴ ᴍɪɴɪᴀᴛᴜʀᴇ. ᴄʜᴇss ɪs ᴀ sᴛʀᴜɢɢʟᴇ, ᴄʜᴇss ʙᴀᴛᴛʟᴇs.” – ɢᴀʀʀʏ ᴋᴀsᴘᴀʀᴏᴠ
 “ᴄʜᴇss, ʟɪᴋᴇ ʟᴏᴠᴇ, ʟɪᴋᴇ ᴍᴜsɪᴄ, ʜᴀs ᴛʜᴇ ᴘᴏᴡᴇʀ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇɴ ʜᴀᴘᴘʏ.” – sɪᴇɢʙᴇʀᴛ ᴛᴀʀʀᴀsᴄʜ
 “ғᴏʀ ɪɴ ᴛʜᴇ ɪᴅᴇᴀ ᴏғ ᴄʜᴇss ᴀɴᴅ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴏғ ᴛʜᴇ ᴄʜᴇss ᴍɪɴᴅ ᴡᴇ ʜᴀᴠᴇ ᴀ ᴘɪᴄᴛᴜʀᴇ ᴏғ ᴛʜᴇ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ sᴛʀᴜɢɢʟᴇ ᴏғ ᴍᴀɴᴋɪɴᴅ.” – ʀɪᴄʜᴀʀᴅ ʀéᴛɪ
 “ɪ ᴅᴏɴ’ᴛ ʙᴇʟɪᴇᴠᴇ ɪɴ ᴘsʏᴄʜᴏʟᴏɢʏ. ɪ ʙᴇʟɪᴇᴠᴇ ɪɴ ɢᴏᴏᴅ ᴍᴏᴠᴇs.” – ʙᴏʙʙʏ ғɪsᴄʜᴇʀ
 “ᴘʟᴀʏ ᴛʜᴇ ᴏᴘᴇɴɪɴɢ ʟɪᴋᴇ ᴀ ʙᴏᴏᴋ, ᴛʜᴇ ᴍɪᴅᴅʟᴇɢᴀᴍᴇ ʟɪᴋᴇ ᴀ ᴍᴀɢɪᴄɪᴀɴ, ᴀɴᴅ ᴛʜᴇ ᴇɴᴅɢᴀᴍᴇ ʟɪᴋᴇ ᴀ ᴍᴀᴄʜɪɴᴇ.” – ʀᴜᴅᴏʟᴘʜ sᴘɪᴇʟᴍᴀɴɴ
 “ɪ ᴜsᴇᴅ ᴛᴏ ᴀᴛᴛᴀᴄᴋ ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡᴀs ᴛʜᴇ ᴏɴʟʏ ᴛʜɪɴɢ ɪ ᴋɴᴇᴡ. ɴᴏᴡ ɪ ᴀᴛᴛᴀᴄᴋ ʙᴇᴄᴀᴜsᴇ ɪ ᴋɴᴏᴡ ɪᴛ ᴡᴏʀᴋs ʙᴇsᴛ.” – ɢᴀʀʀʏ ᴋᴀsᴘᴀʀᴏᴠ
 “ɪᴛ ɪs ᴍʏ sᴛʏʟᴇ ᴛᴏ ᴛᴀᴋᴇ ᴍʏ ᴏᴘᴘᴏɴᴇɴᴛ ᴀɴᴅ ᴍʏsᴇʟғ ᴏɴ ᴛᴏ ᴜɴᴋɴᴏᴡɴ ɢʀᴏᴜɴᴅs. ᴀ ɢᴀᴍᴇ ᴏғ ᴄʜᴇss ɪs ɴᴏᴛ ᴀɴ ᴇxᴀᴍɪɴᴀᴛɪᴏɴ ᴏғ ᴋɴᴏᴡʟᴇᴅɢᴇ; ɪᴛ ɪs ᴀ ʙᴀᴛᴛʟᴇ ᴏғ ɴᴇʀᴠᴇs.” – ᴅᴀᴠɪᴅ ʙʀᴏɴsᴛᴇɪɴ
 “ᴄʜᴇss ɪs ʀᴀʀᴇʟʏ ᴀ ɢᴀᴍᴇ ᴏғ ɪᴅᴇᴀʟ ᴍᴏᴠᴇs. ᴀʟᴍᴏsᴛ ᴀʟᴡᴀʏs, ᴀ ᴘʟᴀʏᴇʀ ғᴀᴄᴇs ᴀ sᴇʀɪᴇs ᴏғ ᴅɪғғɪᴄᴜʟᴛ ᴄᴏɴsᴇǫᴜᴇɴᴄᴇs ᴡʜɪᴄʜᴇᴠᴇʀ ᴍᴏᴠᴇ ʜᴇ ᴍᴀᴋᴇs.” – ᴅᴀᴠɪᴅ sʜᴇɴᴋ
 “ᴡʜᴇɴ ʏᴏᴜ sᴇᴇ ᴀ ɢᴏᴏᴅ ᴍᴏᴠᴇ, ʟᴏᴏᴋ ғᴏʀ ᴀ ʙᴇᴛᴛᴇʀ ᴏɴᴇ.” – ᴇᴍᴀɴᴜᴇʟ ʟᴀsᴋᴇʀ
 “ᴀғᴛᴇʀ ᴀ ʙᴀᴅ ᴏᴘᴇɴɪɴɢ, ᴛʜᴇʀᴇ ɪs ʜᴏᴘᴇ ғᴏʀ ᴛʜᴇ ᴍɪᴅᴅʟᴇ ɢᴀᴍᴇ. ᴀғᴛᴇʀ ᴀ ʙᴀᴅ ᴍɪᴅᴅʟᴇ ɢᴀᴍᴇ, ᴛʜᴇʀᴇ ɪs ʜᴏᴘᴇ ғᴏʀ ᴛʜᴇ ᴇɴᴅɢᴀᴍᴇ. ʙᴜᴛ ᴏɴᴄᴇ ʏᴏᴜ ᴀʀᴇ ɪɴ ᴛʜᴇ ᴇɴᴅɢᴀᴍᴇ, ᴛʜᴇ ᴍᴏᴍᴇɴᴛ ᴏғ ᴛʀᴜᴛʜ ʜᴀs ᴀʀʀɪᴠᴇᴅ.” – ᴇᴅᴍᴀʀ ᴍᴇᴅɴɪs
 “ɢɪᴠᴇ ᴍᴇ ᴀ ᴅɪғғɪᴄᴜʟᴛ ᴘᴏsɪᴛɪᴏɴᴀʟ ɢᴀᴍᴇ, ɪ ᴡɪʟʟ ᴘʟᴀʏ ɪᴛ. ʙᴜᴛ ᴛᴏᴛᴀʟʟʏ ᴡᴏɴ ᴘᴏsɪᴛɪᴏɴs, ɪ ᴄᴀɴɴᴏᴛ sᴛᴀɴᴅ ᴛʜᴇᴍ.” – ʜᴇɪɴ ᴅᴏɴɴᴇʀ
 “ᴛʜᴇʀᴇ ɪs ɴᴏ ʀᴇᴍᴏʀsᴇ ʟɪᴋᴇ ᴛʜᴇ ʀᴇᴍᴏʀsᴇ ᴏғ ᴄʜᴇss.” – ʜ. ɢ. ᴡᴇʟʟs
 “ʜᴀʟғ ᴛʜᴇ ᴠᴀʀɪᴀᴛɪᴏɴs ᴡʜɪᴄʜ ᴀʀᴇ ᴄᴀʟᴄᴜʟᴀᴛᴇᴅ ɪɴ ᴀ ᴛᴏᴜʀɴᴀᴍᴇɴᴛ ɢᴀᴍᴇ ᴛᴜʀɴ ᴏᴜᴛ ᴛᴏ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇʟʏ sᴜᴘᴇʀғʟᴜᴏᴜs. ᴜɴғᴏʀᴛᴜɴᴀᴛᴇʟʏ, ɴᴏ ᴏɴᴇ ᴋɴᴏᴡs ɪɴ ᴀᴅᴠᴀɴᴄᴇ ᴡʜɪᴄʜ ʜᴀʟғ.” – ᴊᴀɴ ᴛɪᴍᴍᴀɴ
 “ᴇᴠᴇɴ ᴀ ᴘᴏᴏʀ ᴘʟᴀɴ ɪs ʙᴇᴛᴛᴇʀ ᴛʜᴀɴ ɴᴏ ᴘʟᴀɴ ᴀᴛ ᴀʟʟ.” – ᴍɪᴋʜᴀɪʟ ᴄʜɪɢᴏʀɪɴ
 “ᴛᴀᴄᴛɪᴄs ɪs ᴋɴᴏᴡɪɴɢ ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ᴡʜᴇɴ ᴛʜᴇʀᴇ ɪs sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴅᴏ; sᴛʀᴀᴛᴇɢʏ ɪs ᴋɴᴏᴡɪɴɢ ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ᴡʜᴇɴ ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴛᴏ ᴅᴏ.” – sᴀᴠɪᴇʟʟʏ ᴛᴀʀᴛᴀᴋᴏᴡᴇʀ
 “ɪɴ ʟɪғᴇ, ᴀs ɪɴ ᴄʜᴇss, ғᴏʀᴇᴛʜᴏᴜɢʜᴛ ᴡɪɴs.” – ᴄʜᴀʀʟᴇs ʙᴜxᴛᴏɴ
 “ʏᴏᴜ ᴍᴀʏ ʟᴇᴀʀɴ ᴍᴜᴄʜ ᴍᴏʀᴇ ғʀᴏᴍ ᴀ ɢᴀᴍᴇ ʏᴏᴜ ʟᴏsᴇ ᴛʜᴀɴ ғʀᴏᴍ ᴀ ɢᴀᴍᴇ ʏᴏᴜ ᴡɪɴ. ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ʟᴏsᴇ ʜᴜɴᴅʀᴇᴅs ᴏғ ɢᴀᴍᴇs ʙᴇғᴏʀᴇ ʙᴇᴄᴏᴍɪɴɢ ᴀ ɢᴏᴏᴅ ᴘʟᴀʏᴇʀ.” – ᴊᴏsé ʀᴀúʟ ᴄᴀᴘᴀʙʟᴀɴᴄᴀ
 “ᴘᴀᴡɴs ᴀʀᴇ ᴛʜᴇ sᴏᴜʟ ᴏғ ᴛʜᴇ ɢᴀᴍᴇ.” – ғʀᴀɴçᴏɪs-ᴀɴᴅʀé ᴅᴀɴɪᴄᴀɴ ᴘʜɪʟɪᴅᴏʀ
 “ᴛʜᴇ ᴘᴀssᴇᴅ ᴘᴀᴡɴ ɪs ᴀ ᴄʀɪᴍɪɴᴀʟ, ᴡʜᴏ sʜᴏᴜʟᴅ ʙᴇ ᴋᴇᴘᴛ ᴜɴᴅᴇʀ ʟᴏᴄᴋ ᴀɴᴅ ᴋᴇʏ. ᴍɪʟᴅ ᴍᴇᴀsᴜʀᴇs, sᴜᴄʜ ᴀs ᴘᴏʟɪᴄᴇ sᴜʀᴠᴇɪʟʟᴀɴᴄᴇ, ᴀʀᴇ ɴᴏᴛ sᴜғғɪᴄɪᴇɴᴛ.” – ᴀʀᴏɴ ɴɪᴍᴢᴏᴡɪᴛsᴄʜ
 “ᴍᴏᴅᴇʀɴ ᴄʜᴇss ɪs ᴛᴏᴏ ᴍᴜᴄʜ ᴄᴏɴᴄᴇʀɴᴇᴅ ᴡɪᴛʜ ᴛʜɪɴɢs ʟɪᴋᴇ ᴘᴀᴡɴ sᴛʀᴜᴄᴛᴜʀᴇ. ғᴏʀɢᴇᴛ ɪᴛ, ᴄʜᴇᴄᴋᴍᴀᴛᴇ ᴇɴᴅs ᴛʜᴇ ɢᴀᴍᴇ.” – ɴɪɢᴇʟ sʜᴏʀᴛ
 “ᴘᴀᴡɴ ᴇɴᴅɪɴɢs ᴀʀᴇ ᴛᴏ ᴄʜᴇss ᴡʜᴀᴛ ᴘᴜᴛᴛɪɴɢ ɪs ᴛᴏ ɢᴏʟғ.” – ᴄᴇᴄɪʟ ᴘᴜʀᴅʏ
 “ɴᴏʙᴏᴅʏ ᴇᴠᴇʀ ᴡᴏɴ ᴀ ᴄʜᴇss ɢᴀᴍᴇ ʙʏ ʀᴇsɪɢɴɪɴɢ.” – sᴀᴠɪᴇʟʟʏ ᴛᴀʀᴛᴀᴋᴏᴡᴇʀ
 “ᴛʜᴇ ʙʟᴜɴᴅᴇʀs ᴀʀᴇ ᴀʟʟ ᴛʜᴇʀᴇ ᴏɴ ᴛʜᴇ ʙᴏᴀʀᴅ, ᴡᴀɪᴛɪɴɢ ᴛᴏ ʙᴇ ᴍᴀᴅᴇ.” – sᴀᴠɪᴇʟʟʏ ᴛᴀʀᴛᴀᴋᴏᴡᴇʀ
 “ɪᴛ’s ᴀʟᴡᴀʏs ʙᴇᴛᴛᴇʀ ᴛᴏ sᴀᴄʀɪғɪᴄᴇ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ’s ᴍᴇɴ.” – sᴀᴠɪᴇʟʟʏ ᴛᴀʀᴛᴀᴋᴏᴡᴇʀ
 “ᴏɴᴇ ᴅᴏᴇsɴ’ᴛ ʜᴀᴠᴇ ᴛᴏ ᴘʟᴀʏ ᴡᴇʟʟ, ɪᴛ’s ᴇɴᴏᴜɢʜ ᴛᴏ ᴘʟᴀʏ ʙᴇᴛᴛᴇʀ ᴛʜᴀɴ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ.” – sɪᴇɢʙᴇʀᴛ ᴛᴀʀʀᴀsᴄʜ
 “ᴜᴘ ᴛᴏ ᴛʜɪs ᴘᴏɪɴᴛ, ᴡʜɪᴛᴇ ʜᴀs ʙᴇᴇɴ ғᴏʟʟᴏᴡɪɴɢ ᴡᴇʟʟ-ᴋɴᴏᴡɴ ᴀɴᴀʟʏsɪs. ʙᴜᴛ ɴᴏᴡ ʜᴇ ᴍᴀᴋᴇs ᴀ ғᴀᴛᴀʟ ᴇʀʀᴏʀ: ʜᴇ ʙᴇɢɪɴs ᴛᴏ ᴜsᴇ ʜɪs ᴏᴡɴ ʜᴇᴀᴅ.” – sɪᴇɢʙᴇʀᴛ ᴛᴀʀʀᴀsᴄʜ
 “ᴏғ ᴄʜᴇss, ɪᴛ ʜᴀs ʙᴇᴇɴ sᴀɪᴅ ᴛʜᴀᴛ ʟɪғᴇ ɪs ɴᴏᴛ ʟᴏɴɢ ᴇɴᴏᴜɢʜ ғᴏʀ ɪᴛ, ʙᴜᴛ ᴛʜᴀᴛ ɪs ᴛʜᴇ ғᴀᴜʟᴛ ᴏғ ʟɪғᴇ, ɴᴏᴛ ᴄʜᴇss.” – ᴡɪʟʟɪᴀᴍ ɴᴀᴘɪᴇʀ
 “ᴄʜᴇss ɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴇɴᴏᴜɢʜ ᴛᴏ ᴡᴀsᴛᴇ ʏᴏᴜʀ ʟɪғᴇ ғᴏʀ.” – ʜᴀɴs ʀᴇᴇ
 “ᴀ ᴄʜᴇss ɢᴀᴍᴇ ɪɴ ᴘʀᴏɢʀᴇss ɪs… ᴀ ᴄᴏsᴍᴏs ᴜɴᴛᴏ ɪᴛsᴇʟғ, ғᴜʟʟʏ ɪɴsᴜʟᴀᴛᴇᴅ ғʀᴏᴍ ᴀɴ ɪɴғᴀɴᴛ’s ᴄʀʏ, ᴀɴ ᴇʀᴏᴛɪᴄ ɪɴᴠɪᴛᴀᴛɪᴏɴ, ᴏʀ ᴡᴀʀ.” – ᴅᴀᴠɪᴅ sʜᴇɴᴋ
 “ɪᴛ ᴡɪʟʟ ʙᴇ ᴄʜᴇᴇʀɪɴɢ ᴛᴏ ᴋɴᴏᴡ ᴛʜᴀᴛ ᴍᴀɴʏ ᴘᴇᴏᴘʟᴇ ᴀʀᴇ sᴋɪʟʟғᴜʟ ᴄʜᴇss ᴘʟᴀʏᴇʀs, ᴛʜᴏᴜɢʜ ɪɴ ᴍᴀɴʏ ɪɴsᴛᴀɴᴄᴇs ᴛʜᴇɪʀ ʙʀᴀɪɴs, ɪɴ ᴀ ɢᴇɴᴇʀᴀʟ ᴡᴀʏ, ᴄᴏᴍᴘᴀʀᴇ ᴜɴғᴀᴠᴏʀᴀʙʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏɢɴɪᴛɪᴠᴇ ғᴀᴄᴜʟᴛɪᴇs ᴏғ ᴀ ʀᴀʙʙɪᴛ.” – ᴊᴀᴍᴇs ᴍᴏʀᴛɪᴍᴇʀ
 “ᴛʜᴇ ᴘɪɴ ɪs ᴍɪɢʜᴛɪᴇʀ ᴛʜᴀɴ ᴛʜᴇ sᴡᴏʀᴅ.” – ғʀᴇᴅ ʀᴇɪɴғᴇʟᴅ
 “ᴛʜᴇ ᴏɴʟʏ ᴛʜɪɴɢ ᴄʜᴇss ᴘʟᴀʏᴇʀs ʜᴀᴠᴇ ɪɴ ᴄᴏᴍᴍᴏɴ ɪs ᴄʜᴇss.” – ʟᴏᴅᴇᴡɪᴊᴋ ᴘʀɪɴs
 “ᴛʜᴏsᴇ ᴡʜᴏ sᴀʏ ᴛʜᴇʏ ᴜɴᴅᴇʀsᴛᴀɴᴅ ᴄʜᴇss, ᴜɴᴅᴇʀsᴛᴀɴᴅ ɴᴏᴛʜɪɴɢ.” – ʀᴏʙᴇʀᴛ ʜüʙɴᴇʀ
 “ᴏɴᴇ ʙᴀᴅ ᴍᴏᴠᴇ ɴᴜʟʟɪғɪᴇs ғᴏʀᴛʏ ɢᴏᴏᴅ ᴏɴᴇs.” – ʙᴇʀɴʜᴀʀᴅ ʜᴏʀᴡɪᴛᴢ
 “ɪғ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ ᴏғғᴇʀs ʏᴏᴜ ᴀ ᴅʀᴀᴡ, ᴛʀʏ ᴛᴏ ᴡᴏʀᴋ ᴏᴜᴛ ᴡʜʏ ʜᴇ ᴛʜɪɴᴋs ʜᴇ’s ᴡᴏʀsᴇ ᴏғғ.” – ɴɪɢᴇʟ sʜᴏʀᴛ
 “sᴏᴍᴇ ᴘᴇᴏᴘʟᴇ ᴛʜɪɴᴋ ᴛʜᴀᴛ ɪғ ᴛʜᴇɪʀ ᴏᴘᴘᴏɴᴇɴᴛ ᴘʟᴀʏs ᴀ ʙᴇᴀᴜᴛɪғᴜʟ ɢᴀᴍᴇ, ɪᴛ's ᴏᴋᴀʏ ᴛᴏ ʟᴏsᴇ. ɪ ᴅᴏɴ'ᴛ. ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ʙᴇ ᴍᴇʀᴄɪʟᴇss.” – ᴍᴀɢɴᴜs ᴄᴀʀʟsᴇɴ
 “ɪ ᴀᴍ ᴛʀʏɪɴɢ ᴛᴏ ʙᴇᴀᴛ ᴛʜᴇ ɢᴜʏ sɪᴛᴛɪɴɢ ᴀᴄʀᴏss ғʀᴏᴍ ᴍᴇ ᴀɴᴅ ᴛʀʏɪɴɢ ᴛᴏ ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴍᴏᴠᴇs ᴛʜᴀᴛ ᴀʀᴇ ᴍᴏsᴛ ᴜɴᴘʟᴇᴀsᴀɴᴛ ғᴏʀ ʜɪᴍ ᴀɴᴅ ʜɪs sᴛʏʟᴇ.” – ᴍᴀɢɴᴜs ᴄᴀʀʟsᴇɴ
 “ᴄʜᴇss sᴛʀᴇɴɢᴛʜ ɪɴ ɢᴇɴᴇʀᴀʟ ᴀɴᴅ ᴄʜᴇss sᴛʀᴇɴɢᴛʜ ɪɴ ᴀ sᴘᴇᴄɪғɪᴄ ᴍᴀᴛᴄʜ ᴀʀᴇ ʙʏ ɴᴏ ᴍᴇᴀɴs ᴏɴᴇ ᴀɴᴅ ᴛʜᴇ sᴀᴍᴇ ᴛʜɪɴɢ.” – ɢᴀʀʀʏ ᴋᴀsᴘᴀʀᴏᴠ
 “ᴛʜᴇ ʜɪɢʜᴇsᴛ ᴀʀᴛ ᴏғ ᴛʜᴇ ᴄʜᴇssᴘʟᴀʏᴇʀ ʟɪᴇs ɪɴ ɴᴏᴛ ᴀʟʟᴏᴡɪɴɢ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ ᴛᴏ sʜᴏᴡ ʏᴏᴜ ᴡʜᴀᴛ ʜᴇ ᴄᴀɴ ᴅᴏ.” – ɢᴀʀʀʏ ᴋᴀsᴘᴀʀᴏᴠ
 “ᴡʜᴇɴ ʏᴏᴜʀ ʜᴏᴜsᴇ ɪs ᴏɴ ғɪʀᴇ, ʏᴏᴜ ᴄᴀɴ’ᴛ ʙᴇ ʙᴏᴛʜᴇʀᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ɴᴇɪɢʜʙᴏʀs. ᴏʀ, ᴀs ᴡᴇ sᴀʏ ɪɴ ᴄʜᴇss, ɪғ ʏᴏᴜʀ ᴋɪɴɢ ɪs ᴜɴᴅᴇʀ ᴀᴛᴛᴀᴄᴋ, ᴅᴏɴ’ᴛ ᴡᴏʀʀʏ ᴀʙᴏᴜᴛ ʟᴏsɪɴɢ ᴀ ᴘᴀᴡɴ ᴏɴ ᴛʜᴇ ǫᴜᴇᴇɴ sɪᴅᴇ.” – ɢᴀʀʀʏ ᴋᴀsᴘᴀʀᴏᴠ
 “ɪɴ ᴄʜᴇss, ᴋɴᴏᴡʟᴇᴅɢᴇ ɪs ᴀ ᴠᴇʀʏ ᴛʀᴀɴsɪᴇɴᴛ ᴛʜɪɴɢ. ɪᴛ ᴄʜᴀɴɢᴇs sᴏ ғᴀsᴛ ᴛʜᴀᴛ ᴇᴠᴇɴ ᴀ sɪɴɢʟᴇ ᴍᴏᴜsᴇ-sʟɪᴘ sᴏᴍᴇᴛɪᴍᴇs ᴄʜᴀɴɢᴇs ᴛʜᴇ ᴇᴠᴀʟᴜᴀᴛɪᴏɴ.” – ᴠɪsʜᴡᴀɴᴀᴛʜᴀɴ ᴀɴᴀɴᴅ
 “ᴛʜᴇʀᴇ ɪs ᴀʟᴡᴀʏs ᴛʜᴇ ʀɪsᴋ ᴏғ ʙᴇɪɴɢ ᴏᴠᴇʀ-ᴄᴏɴғɪᴅᴇɴᴛ ᴡʜᴇɴ ʏᴏᴜ ᴀʀᴇ ᴘʀᴇᴘᴀʀɪɴɢ ᴛᴏ ғᴀᴄᴇ ᴀ ᴡᴇᴀᴋᴇʀ ᴘʟᴀʏᴇʀ.” – ᴠɪsʜᴡᴀɴᴀᴛʜᴀɴ ᴀɴᴀɴᴅ
    '''
    chess_quotes=string.split('\n')
    for i in range(len(chess_quotes)):
        chess_quotes[i]=chess_quotes[i].strip()
        try:
	        x=chess_quotes[i].split('–')        
	        q='{}\n – <b>{}</b>'.format(x[0],x[1].strip())
	        chess_quotes[i]=q
        except:
	        None
    return chess_quotes



class quotes():
    def __init__(self):
        self.all_quotes=list(filter(lambda a: a != '',all_quotes()))
        self.temp=[]
        
    def get_quote(self):  
        quote=random.choice(self.all_quotes)
        self.temp.append(quote)
        self.all_quotes.remove(quote)
        if(len(self.all_quotes)==0):
            self.temp=[]
            self.all_quotes=all_quotes()
        return quote

qt=quotes()