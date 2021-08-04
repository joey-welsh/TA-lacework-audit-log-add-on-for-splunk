### Puropse Of This App
To ingest Lacework Audit Logs. 

### Prequisites
[A Lacework API Token](
https://support.lacework.com/hc/en-us/articles/360011403853-Generate-API-Access-Keys-and-Tokens#:~:text=To%20create%20an%20API%20key,open%20it%20in%20an%20editor)

### How to Install This App

Ensure [git](https://git-scm.com/downloads) is installed on your OS

#### Mac OS
- git clone git@github.com:joey-welsh/TA-lacework-audit-log-add-on-for-splunk.git
- COPYFILE_DISABLE=true
- tar --exclude=".*" -cvzf TA-lacework-audit-log-add-on-for-splunk.tgz TA-lacework-audit-log-add-on-for-splunk

### How to Configure
1. Switch App Context to "Lacework Audit Log Add-on For Splunk"
2. Click "Create New Input"
3. Enter the information requested

Note: Upon installation the Add-on will download the previous 30 days worth of logs.  

My default Lacework limits its customers to 60 API calls per hour.  Therefore, please consider setting your interval to 120 second or more.

### Developer
Author: Joe Welsh - Lacework
Email: joe.welsh@lacework.net
