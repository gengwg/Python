#!/usr/bin/env python
"""
Usage:
./runNextDay.py

this is used for posting memo for next business day.
"""

# If doing test, put it to 1.
TEST = 0

import telnetlib
import os
import datetime
import time # used for time.sleep
#from mx import DateTime
import msvcrt # for exiting loop with a key press
from dbfpy import dbf
import sys
from math import fabs
import string
import logging

now = datetime.datetime.now()
TODAY = now.strftime("%Y%m%d") # Get date, e.g. '20120820'

######################################
## Logging configuration            ##
######################################

# log file location
logdir = "F:\Teller\\AutoMemoLog"
logname = os.path.splitext(os.path.basename(sys.argv[0]))[0] + ".log" # basename -> split
logfile = logdir + "\\" + TODAY + logname
if TEST:
    logfile = os.path.basename(logfile)

# create logger
logger = logging.getLogger("geng")
logger.setLevel(logging.DEBUG)

# create file handler which logs event debug messages
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)

# create console handler and set level to error
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to console handler ch and file handler fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

######################################

## This function confirms user input.
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt).lower()
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            logger.error("Teller reached max tries for next busyness day. Exiting now." )
            raise IOError('refusenik user')
        print complaint

sleepcycle = 60
if TEST:
    sleepcycle = 3
    
prompt = "Please enter next business day's date in the format of [yyyymmdd]\
(For example, today's date is: " + TODAY +".): "
## Let user input next business day.        
while True:
    s = raw_input(prompt)
    print "The next business day's date you input is:", s
    # remove any white spaces user input. 
    #s = "".join(s.split()) # better can remove more, like remove "-", "." etc.
    s = s.strip()
    # If input is not all digits, or length is not 8, let user input again.
    if not all([s.isdigit(), len(s)==8]):
        print "Date format is wrong, pleasse try again."
        continue
    if ask_ok("Is it correct?[Y/N] ", 10,"Please enter Yes or No. "):
        break

NEXTDAY = s
    
print "Now starting program", sys.argv[0]
print "You may minimize this window now. Please do not close it.\n"
logger.info("Now starting program " + str(sys.argv[0]))
logger.info("Log file location: " + logfile)
time.sleep(2)

# Transaction file to read.
tdjrnlfile = "F:\Teller\\" + NEXTDAY+ "\\TDJRNL.DBF"
if TEST:
    tdjrnlfile = "C:\\Users\\gengwg\\Dropbox\\INBK\\TDJRNL.DBF"
    print tdjrnlfile
logger.info("DBF file location: " + tdjrnlfile)
#print tdjrnlfile

# Profile to get userid, passwd, sleepcycle. if exist.
profile = "F:\Teller\PROFILE.DBF"

def tryOpenFile(opencmd):
    """
    Function to try open the file again and again.
    """
    try:
        exec(opencmd)
    finally:
        print "Retrying in 60 seconds."
        time.sleep(3)
        tryOpenFile(opencmd)
        
def writeDBF():
    """
    Make some log in some fileds in the DBF file,
    so that we know which record was already posted to server.

    Returns -1 if writing failure,
    returns None if successful.
    """
    logger.info("Begin writing data to DBF." )
    logger.info("Now writing field FMCRDB.")
    rec["FMCRDB"] = data["memo"] # credit/debit memo
    logger.info("Now writing field FMDAY.")
    rec["FMDAY"]  = data["postday"] # posting day is today.
    logger.info("Now writing field FMAMT.")
    rec["FMAMT"]  = data["amount"] # amount posted
    logger.info("Now writing field FSEQNO.")
    rec["FSEQNO"] = data["seqno"] # seq number i.e. timestamp to post in DBF
    rec.store()        

    logger.info("Done writing records. Now verifying each field is not empty after writing.")
    if rec["FMCRDB"]=="" or rec["FMDAY"]=="" or rec["FMAMT"]==0.0 or rec["FSEQNO"]=="":
        logger.error("DBF writing was not successful! Please check.")
        return -1
    else:    
        logger.info("Finished writing data to DBF successfully.")
        logger.info("WRITE DBF SUMMARY:")
        logger.info("FMCRDB: " + rec["FMCRDB"] + ", FMDAY: " + rec["FMDAY"] + ", FMAMT: " + str(rec["FMAMT"]) + ", FSEQNO: " + rec["FSEQNO"])
        return
    
# default user id and passwd.
host = {"ip": "192.170.3.4", "port": "23", "user": "TELMEMO", "passwd": "xxxxxxxxxx"}
data = {} # declare an empty dictionary to host data.
data["postday"] = "N" # Post day is next day.

def verifyScreen(keyword, screen):
    """
    screen verifying utility
    """
    if keyword not in screen:
        logger.error("Screen verification failed.")
    else:
        logger.info("Screen verification successful.")
    logger.debug("Screen verification keyword is: " + keyword)
    return keyword in screen

def postMemo():
    """
    ## This function logs on to the IBM/AS 400 server,
    ## and write necessary data.

    Returns "Success" if memo posted, otherise return None.
    """
    memosleep = 4
    logger.info("Logging on to AS/400-JHA." )
    logger.info(str(host))

    # Telent to IBM/AS 400 on port 23, time out 30 seconds 
    try:
        tn = telnetlib.Telnet(host["ip"], host["port"], 30)
    except:
        print "Can't log on to JHA. Retrying in " + str(sleepcycle) + " seconds."
        logger.error("Can't log on to JHA. Retrying in " + str(sleepcycle) + " seconds.")
        return
    tn.write("\n")# This newline is necessary for server to respond with Sign On Screen.
    time.sleep(memosleep)

    SignOnScreen = tn.read_very_eager()
    #print SignOnScreen
    
    # Input the user name and passwd.
    tn.write(host["user"] + "\t")
    tn.write(host["passwd"] + "\r\n") # this \r is important.
    time.sleep(memosleep)

    PrevSignOnScreen = tn.read_very_eager()
    print PrevSignOnScreen
    if not verifyScreen("Previous sign-on", PrevSignOnScreen):
        return
    
    # This is the welcome page after log in
    tn.write("\r\n") # Press Enter to continue.
    time.sleep(memosleep)
    # testScreen could be "allocated to another job" or "Inquiry Menu" page.
    # if it's "allocated", do extra enter, then esc.
    # if not, just assign it to InquiryMenuScreen.
    testScreen = tn.read_very_eager()
    InquiryMenuScreen = testScreen 

    if "allocated to another job" in testScreen:
        logger.warning(host["user"] + " is allocated to another job.")
        AllocatedJobScreen = testScreen
        # print AllocatedJobScreen
        tn.write("\r\n") # Enter
        time.sleep(memosleep)
        InquiryMenuScreen = tn.read_very_eager()

    if not verifyScreen("Inquiry Menu", InquiryMenuScreen):
        return    

    # Input Option: 3 for "Deposit inquiry"
    tn.write("3\r\n")
    time.sleep(memosleep)
    
    DepositInquiryScreen = tn.read_very_eager()
    #print DepositInquiryScreen
    if not verifyScreen("Name or account no", DepositInquiryScreen):
        return
    
    # Input account number.
    if TEST:
        data["acctno"] = "80055"
    tn.write(data["acctno"])
    time.sleep(memosleep)

    AccountInfoScreen = tn.read_very_eager()
    print AccountInfoScreen
    # May need better keyword for this page.
    if not verifyScreen("Current balance", AccountInfoScreen):
        return
   
    # input F11 pf key, in order to enter debit/credit memo page
    tn.write("\x1b[23~") # F11 key equals sequence \x1b[23~
    time.sleep(memosleep)

    MemoScreen = tn.read_very_eager()
    print MemoScreen
    if not verifyScreen("Today/Next Day", MemoScreen):
        return
    
    # Input Debit or Credit memo.
    tn.write("\x1b[A") # This is the UP key.
    tn.write("N")
    tn.write(data["memo"])
    tn.write(str(int(data["amount"]*100)) + "\t")
    tn.write("5069\t")
    tn.write(data["teller"] + "\r\n")
    time.sleep(memosleep)

    MemoPostScreen = tn.read_very_eager()
    print MemoPostScreen
    if not verifyScreen("Debit or credit", MemoPostScreen):
        return

    # Exit JHA
    tn.write("\x1bOR") #F3
    time.sleep(memosleep)
    print tn.read_very_eager()

    tn.write("90\r\n")# Option: 90 to exit
    time.sleep(memosleep)
    print tn.read_very_eager()

    tn.close()
    logger.info("Memo post successful. Logged out of AS/400-JHA.")
    logger.info("MEMOPOST SUMMARY:")
    logger.info(str(data))
    return "Success"
    
def myExit():
    """
    This function let user exit the program by pressing Esc.
    """
    #print "Exit program by pressing Esc..."
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            print "Exiting program due to pressing Esc..."
            logger.warn("Program exited due to pressing Esc.")          
            sys.exit(0)

## Main function.
if __name__=="__main__":
    while (1):
        print "Idle to", sleepcycle, "seconds, please wait."
        logger.info("Idle to " \
                    + str(sleepcycle) + " seconds before processing DBF.")
        time.sleep(sleepcycle)

        logger.info("Now begin reading and processing " + tdjrnlfile)
        ## Re-read the DBF file every sleep cycle. 
        # If error opening DBF, retry after sleep cycle.
        try:
            db = dbf.Dbf(tdjrnlfile)
        except:
            print "Can't open " + tdjrnlfile
            print "Retrying in " + str(sleepcycle) + " seconds."
            logger.warn("Can't open " + tdjrnlfile\
                        + ". Retrying in " + str(sleepcycle) + " seconds.")
            continue
        
        ## Read user id info from PROFILE.DBF, if exists.
        try:
            db2 = dbf.Dbf(profile)
        except:
            print "Can't open " + profile
            print "Retrying in " + str(sleepcycle) + " seconds."
            logger.warn("Can't open " + profile\
                        + ". Retrying in " + str(sleepcycle) + " seconds.")            
            continue
        
        if "FMUSERID" in db2.fieldNames:
            if db2[0]["FMUSERID"] != "":
                host["user"] = db2[0]["FMUSERID"]
        if "FMPSWD" in db2.fieldNames:
            if db2[0]["FMPSWD"] != "":
                host["passwd"] = db2[0]["FMPSWD"]
        if "FMCYCLE" in db2.fieldNames:
            if db2[0]["FMCYCLE"] != 0.0:
                sleepcycle = db2[0]["FMCYCLE"]
                
        db2.close()
                
        ## Read the parameters from DBF file
        for rec in db: # loop over each record.    
            # We only consider DDA. if not, skip and look at next record.
            if rec["FTYPE"] != "D":
                continue
            
            # If we already posted memo,skip and look at next record.
            if rec["FSTATUS"] == "" and rec["FSEQNO"] != "":
                continue

            # If teller reversed transaction, and we have not write a memo to JHA,
            # skip and look at next record.
            if rec["FSTATUS"] == "!" and rec["FSEQNO"] == "":
                continue
            
            # If teller reversed transaction, and we already posted a memo to JHA,
            # and we already posted a reversed memo, skip and look at next record.
            if rec["FSTATUS"] == "!" and rec["FSEQNO"][-1] == "R":
                continue

            # Judging if memo should be credit or debit
            diff = rec["FCASHIN"] - rec["FCASHOUT"] - rec["FSPLITOUT"]
            if diff > 0.0:
                data["memo"] = "C"
            elif diff < 0.0:
                data["memo"] = "D"
            else:
                continue

            #if all these conditions unsatisfied, now processing...
            print "Begin processing record."
            logger.info("Begin processing record.")

            data["amount"] = fabs(diff)# posted amount is always positive.
            data["teller"] = rec["FTELLER"]
            data["acctno"] = rec["FACCTNO"]
            
            now = datetime.datetime.now()
            data["seqno"] = now.strftime("%H%M%S") # serno is timestamp w/o date

            logger.debug("memo before reverse is " + data["memo"])
            
            # If teller reversed transaction, and we already posted memo,
            # then we post a reversed memo, and add R to the timestamp.
            if rec["FSTATUS"] == "!" and rec["FSEQNO"][-1] != "R":
                data["seqno"] = now.strftime("%H%M%S") + "R" # serno is timestamp + "R"
                # ReverseMemo()
                if data["memo"] == "C":
                    data["memo"] = "D"
                elif data["memo"] == "D":
                    data["memo"] = "C"
                else:
                    print "Memo is not C or D. Possible error?"
                    logger.error("Memo is not C or D. Possible error? Please check!!")                    

            logger.debug("memo after reverse is " + data["memo"])
            
            print "This DDA record is being written to AS/400-JHA:"
            print str(data)
            logger.info("This DDA record is being written to AS/400-JHA:")
            logger.info(str(data))

            postMemoResult = postMemo()
            # only if posted memo successfully, we can write back to DBF.
            if postMemoResult != "Success":
                continue

            writeDBF()

            del rec
            print "Finished processing this record. Continue on to next record."
            logger.info("Finished processing this record. Continue on to next record.")

        db.close() # done using db, so close it.
        logger.info("Finished processing DBF.")
        
        myExit()
        
    print "Good bye!"
    sys.exit(0)
