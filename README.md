# Whatsapp-Message-Parser

## Overview
A Parser made for using exported Whatsapp messages (more than 40k) to analize chat data.
Tutorial modified for 2024 from the following sources (might be useful if you encounter errors):
- https://www.reddit.com/r/DataHoarder/comments/a7c0yq/full_whatsapp_chat_export_40000_messages/

## Under 40k messages
Follow the tutorial from [this link](https://faq.whatsapp.com/1180414079177245/?cms_platform=android)

## Over 40k messages
1. Enable Developer options (Settings->System->About Phone->Software Information-> 7 x click on Build Number) on your Android. Return to settings and from the new section Developer options enable USB Debugging.
2. Install Python on the PC/laptop.
3. Install Java on the PC/laptop.
4. Grab the WhatsApp Key/Database Extractor from [here](https://github.com/YuvrajRaghuvanshiS/WhatsApp-Key-Database-Extractor)(Code->Download zip) and unzip it.
5. From your phone, take a backup of your chats (Whatsapp Settings->Chat Settings->Chat Backup).
6. Turn off your phone's internet/mobile data so you don't lose any new messages.
7. Connect your phone via USB to the PC/laptop.
8. Browse the files and if you see a folder "Android/media/com.whatsapp" copy it somewhere safe before running the script, new versions of WhatsApp are saving media here (images and videos)
9. Open the unziped folder in the terminal

    ---------
If on Windows 11, Right click inside the folder --> Open in terminal. If on Windows 10, SHIFT + Right click inside the folder --> Open in terminal. If on other systems, good luck pal, you're on your own.

In Windows Terminal/PowerShell, type: python3 .\wa_kdbe.py or simply python3 wa and then hit TAB, it should automatically complete the command with wa_kdbe.py.

Read the instructions on screen. They are just gonna be repetitions of what you just read here and on the GitHub page.

The executable will, in essence, replace your current WhatsApp version with an older one in order to be able to extract your messages.

At some point, you will be prompted to look at your phone. There, you will be signalled that your phone installed an old version of WhatsApp and will ask you to either check for updates or to continue. Tell it to fuck off.

You will now have to confirm the backup process. DON'T FORGET TO PUT A SECURITY CODE! I tried twice to complete the extraction without one, but it always ended in an error, for some reason. Put a stupid code, like 0000 and hit begin.

After a few moments, your backup will have been extracted and you will be prompted (on your PC) to insert a username (optional) and to insert a password for the archive (optional).

If god was on your side, you should have your archive under WhatsAppExtractorDirectory/extracted/usernameYouInputted, and the most important files are key, msgstore.db (containing your messages), and wa.db.

If god was not on your side (he was probably drinking tea while you were extracting), then simply open WhatsApp again, insert your phone number and stuff, wait for it to load the messages (you don't need to wait for it to restore all the media), and then try again. My first few tries did not work for some reason, first because I didn't put a password before beginning the backup and then for some obscure reasons, even when I correctly put the password. Don't give up, my brother in christ!

Now, download whatsapp-viewer. In my specific case, version 1.15 was used. Just click on WhatsApp.Viewer.zip under Assets and extract it.

Don't get overly excited. As of now, reading your archive won't work because the archive itself (as of today) comes in a format that makes the extractor whine (no such table: chat_list), but don't worry, we have plot armor.

Luckily for us, user ReMiOS (god bless your divine soul) made an amazing little program that you can grab from here that allows you to fix the archive. Download it and put it in the same folder as the archive, then run it.

Finally, open WhatsApp Viewer. Click on File, select the msgstore.db under File, input your account email under Account name (just put the email you use for your Play Store account), and select the wa.db file under wa.db (optional).

Hit OK and cry of joy.
