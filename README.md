# Whatsapp-Message-Parser

## Overview
A Parser made for using exported Whatsapp messages (more than 40k) to analize chat data.
Tutorial modified for 2024 from the following sources (might be useful if you encounter errors):
- https://www.reddit.com/r/DataHoarder/comments/a7c0yq/full_whatsapp_chat_export_40000_messages/

## Under 40k messages
Follow the tutorial from [this link](https://faq.whatsapp.com/1180414079177245/?cms_platform=android)

## Over 40k messages
- You can get the full chat in other ways, the problem is that after a certain Whatsapp version, they are stored encrypted so you will be unable to view/analize them with another app.
1. Enable Developer options (Settings->System->About Phone->Software Information-> 7 x Click on Build Number) on your Android. Return to settings and from the new section Developer options enable USB Debugging.
2. Install Python on the PC/laptop.
3. Install Java on the PC/laptop.
4. Grab the WhatsApp Key/Database Extractor from [here](https://github.com/YuvrajRaghuvanshiS/WhatsApp-Key-Database-Extractor) (Code->Download zip) and unzip it.
5. From your phone, take a backup of your chats (Whatsapp Settings->Chat Settings->Chat Backup).
6. Turn off your phone's internet/mobile data so you don't lose any new messages.
7. Connect your phone via USB to the PC/laptop.
8. Browse the files and if you see a folder "Android/media/com.whatsapp" copy it somewhere safe before running the script, new versions of WhatsApp are saving media here (images and videos)
9. Open the unziped folder in terminal. If on Windows 11, Right Click inside the folder -> Open in terminal. If on Windows 10, SHIFT + Right Click inside the folder -> Open in terminal.
10. In Windows Terminal/PowerShell, type: python3 .\wa_kdbe.py or simply python3 wa and then hit TAB, it should automatically complete the command with wa_kdbe.py.
11. Read the instructions on screen. They are just gonna be repetitions of what you just read here and on the GitHub page. The executable will, in essence, replace your current WhatsApp version with an older one in order to be able to extract your messages.
12. At some point, you will be prompted unlock your phone. There, you will be signalled that your phone installed an old version of WhatsApp and will ask you to either check for updates or to continue. Click OK. 
13. If you take to much time at any step, the program will print "Our work with device has finished, it is safe to remove it now". In this case, hit Ctrl+C and restart the process.
14. You will now have to confirm the backup process and **DO NOT ENTER** a password for the file.
15. After a few moments, your backup will have been extracted and you will be prompted (on your PC) to insert a username (name of the to-be-created folder) and to insert the previously prompted password (just click Enter).
16. You will receive the following error: *"encrypted_backup.key" is not present in tarfile, if you have crypt15 backups then visit "https://github.com/YuvrajRaghuvanshiS/WhatsApp-Key-Database-Extractor/issues/94" for more details*. You can ignore it, as you did not enter a password to encrypt the file and the program is looking for the required files to decrypt it.
17. You are asked if you want to create a password to the archive. Type n.
18. After you click enter, the program will automatically close and the newly created folder will open (WhatsAppExtractorDirectory/extracted/<usernameYouInputted>).
19. Download [whatsapp-viewer](https://github.com/andreas-mausch/whatsapp-viewer/releases?page=1) (Code->Download zip) and unzip it.
20. We need to format the data we extracted from Whatsapp so that the viewer can open it. For that we use [this program](https://github.com/andreas-mausch/whatsapp-viewer/files/9438508/wav_create_table.zip), which we'll unzip and copy the .exe file into our previously made folder (WhatsAppExtractorDirectory/extracted/<usernameYouInputted>).
21. Run the .exe. For a brief moment, two more files appeared in the folder. That means the execution was a success.
22. Finally, open WhatsApp Viewer. Click on File, select the msgstore.db under File, input your account email under Account name (just put the email you use for your Play Store account), and select the wa.db file under wa.db.
23. Select one of the chats and export it to .json.

## This is where my python code proves usefull
You can view your messages here, or export them in .html to see all the messages for a specific chat. However, if you want to analize them ([like ChatCharts](https://chatcharts.co.uk), but for free, you can parse them to a format that is easily recognized by different free Chat Analizer Apps:
- [Chat Stats for WhatsApp](https://play.google.com/store/apps/details?id=com.joseluisgalan.android.chatstats&hl=en_US)
- to be added
