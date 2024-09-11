# Whatsapp-Message-Parser

## Overview
A Parser made for using exported Whatsapp messages (more than 40k) to analyze your chat data with another person.
Tutorial modified for 2024 from [this source](https://www.reddit.com/r/DataHoarder/comments/a7c0yq/full_whatsapp_chat_export_40000_messages/
) (might be useful if you encounter errors).

## Under 40k messages
Follow the tutorial from [this link](https://faq.whatsapp.com/1180414079177245/?cms_platform=android)

## Over 40k messages
- You can get the full chat in other ways, but after a certain Whatsapp version, they are stored encrypted so you will be unable to view/analyze them with another app.
1. Enable Developer options (Settings->System->About Phone->Software Information-> 7 x Click on Build Number) on your Android. Return to settings and from the new section Developer options enable USB Debugging.
2. Install Python on the PC/laptop.
3. Install Java on the PC/laptop.
4. Grab the WhatsApp Key/Database Extractor from [here](https://github.com/YuvrajRaghuvanshiS/WhatsApp-Key-Database-Extractor) (Code->Download zip) and unzip it.
5. From your phone, take a backup of your chats (Whatsapp Settings->Chat Settings->Chat Backup).
6. Turn off your phone's internet/mobile data so you don't lose any new messages.
7. Connect your phone via USB to the PC/laptop.
8. Browse the files and if you see a folder "Android/media/com.whatsapp" copy it somewhere safe before running the script, new versions of WhatsApp are saving media here (images and videos)
9. Open the unziped folder in terminal. If on Windows 11, Right Click inside the folder -> Open in terminal. If on Windows 10, SHIFT + Right Click inside the folder -> Open in terminal.
10. In Windows Terminal/PowerShell, type: ```python3 .\wa_kdbe.py``` or simply ```python3 wa``` and then hit TAB, it should automatically complete the command with wa_kdbe.py.
11. Read the instructions on screen. They are just gonna be repetitions of what you just read here and on the GitHub page. The executable will, in essence, replace your current WhatsApp version with an older one in order to be able to extract your messages.
12. At some point, you will be prompted to unlock your phone. There, you will be signalled that your phone installed an old version of WhatsApp and will ask you to either check for updates or to continue. Click OK. 
13. If you take too much time at any step, the program will print ```Our work with device has finished, it is safe to remove it now```. In this case, hit ```Ctrl+C``` and restart the process.
14. You will now have to confirm the backup process and **DO NOT ENTER** a password for the file.
15. After a few moments, your backup will have been extracted and you will be prompted (on your PC) to insert a username (name of the to-be-created folder) and to insert the previously prompted password (just click Enter).
16. You will receive the following error: ```"encrypted_backup.key" is not present in tarfile, if you have crypt15 backups then visit "https://github.com/YuvrajRaghuvanshiS/WhatsApp-Key-Database-Extractor/issues/94" for more details```. You can ignore it, as you did not enter a password to encrypt the file and the program is looking for the required files to decrypt it.
17. You are asked if you want to create a password to the archive. Type ```n```.
18. After you click Enter, the program will automatically close and the newly created folder will open (WhatsAppExtractorDirectory/extracted/<usernameYouInputted>).
19. Download [whatsapp-viewer](https://github.com/andreas-mausch/whatsapp-viewer/releases?page=1) (Code->Download zip) and unzip it.
20. We need to format the data we extracted from Whatsapp so that the viewer can open it. For that we use [this program](https://github.com/andreas-mausch/whatsapp-viewer/files/9438508/wav_create_table.zip), which we'll unzip and copy the .exe file into our previously made folder (WhatsAppExtractorDirectory/extracted/<usernameYouInputted>).
21. Run the .exe. For a brief moment, two more files appeared in the folder. That means the execution was a success.
22. Finally, open WhatsApp Viewer. Click on File, select the msgstore.db under File, input your account email under Account name (just put the email you use for your Play Store account), and select the wa.db file under wa.db.
23. Select one of the chats and export it to .json.

## This is where my python code proves useful
You can view your messages in WhatsApp Viewer, or export them in .html to see all the messages for a specific chat like a website. However, if you want to analyze them (like [ChatCharts](https://chatcharts.co.uk), but diy) you can parse them to a format that is easily recognized by different free Chat Analyzer Apps (all tested as of 2024):
- [Chat Stats for WhatsApp](https://play.google.com/store/apps/details?id=com.joseluisgalan.android.chatstats&hl=en_US)
- [Chatilyzer](https://chatilyzer.com)
- [ChatAnalyzer](https://chatanalyzer.moritzwolf.com)
- [DoubleText](https://app.doubletext.me/whatsapp)
- [Whatsapp Group Chat Analyzer](https://whats-chat-detective.streamlit.app)
1. Grab this Python code (Code->Download zip) and unzip it.
2. Copy the .json file in this folder.
3. Open the unziped folder in terminal. If on Windows 11, Right Click inside the folder -> Open in terminal. If on Windows 10, SHIFT + Right Click inside the folder -> Open in terminal.
4. Run with command ```python3 ./main.py```.

![Screenshot 2024-09-11 105221](https://github.com/user-attachments/assets/873a0ac8-aeee-4a82-8aae-88bfe9941a8b)

5. You will be prompted to type the source file, which is the .json file acquired from the previous section, as well as a name for the file that will store the messages to be analyzed (must be with .txt extension, more details about the formats in the next section).
6. Then you will be prompted to enter your Whatsapp name, as well as the name of the person you exchanged messages with. These name will appear in the stats from any used analyzer.
7. Depending on the number of messages, it may take a while. A new file will appear in the folder, which you can use with any of the above analyzers and many more.

![Screenshot 2024-09-11 105630](https://github.com/user-attachments/assets/289f0700-461f-4f16-82a0-66985553e3da)

## Explanation about the different formats used
Files exported from WhatsApp Viewer don't have the format of the file you can get from downloading a Whatsapp chat in 2024, the one most chat analyzers use.
Even exporting to .txt file will give the following format, which doesn't include the names of the participants. Plus, if someone sent an image, it will be recorded as a blank message:

![image](https://github.com/user-attachments/assets/52ca8911-cfa2-4bdd-9062-f4e0e09575cd)

However, when exporting to .json, each message has a lot more data associated:


