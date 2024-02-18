import requests



url = "https://shym.sergek.kz/api/main/v2/events/get/list"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImEua2VuemhlaGFuIiwiaWQiOjk2ODIsImZpcnN0bmFtZSI6ItCQ0LHQt9Cw0LsiLCJsYXN0bmFtZSI6ItCa0LXQvdC20LXRhdCw0L0iLCJpYXQiOjE3MDgyNDk2MTMsImV4cCI6MTcwODI1MDUxM30.1vE3Xz3iTJMQTWMLJdqd2WRpfMdCRWRJ1hHjrMkVmb8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        #"Cookie": "language=ru; accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImEua2VuemhlaGFuIiwiaWQiOjk2ODIsImZpcnN0bmFtZSI6ItCQ0LHQt9Cw0LsiLCJsYXN0bmFtZSI6ItCa0LXQvdC20LXRhdCw0L0iLCJpYXQiOjE3MDgyNDY2NjMsImV4cCI6MTcwODI0NzU2M30.ZcSqBalmUEiRo4cdWB7679r4Tt6OyI3StvIpDKIEa5c; refreshToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImEua2VuemhlaGFuIiwiaWQiOjk2ODIsImZpcnN0bmFtZSI6ItCQ0LHQt9Cw0LsiLCJsYXN0bmFtZSI6ItCa0LXQvdC20LXRhdCw0L0iLCJpYXQiOjE3MDgyNDY2NjMsImV4cCI6MTcwODMzMzA2M30.hSSyx6gi9bWReRMWEOkRmZiKiWBEJbGVO_p1f2vPsfg; expireTokens=Sun%20Feb%2018%202024%2015:17:44%20GMT+0600%20(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9%20%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD); loginFails=0"
    }

cookies = {'language': 'ru',
           'accessToken' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImEua2VuemhlaGFuIiwiaWQiOjk2ODIsImZpcnN0bmFtZSI6ItCQ0LHQt9Cw0LsiLCJsYXN0bmFtZSI6ItCa0LXQvdC20LXRhdCw0L0iLCJpYXQiOjE3MDgyNDk2MTMsImV4cCI6MTcwODI1MDUxM30.1vE3Xz3iTJMQTWMLJdqd2WRpfMdCRWRJ1hHjrMkVmb8; refreshToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImEua2VuemhlaGFuIiwiaWQiOjk2ODIsImZpcnN0bmFtZSI6ItCQ0LHQt9Cw0LsiLCJsYXN0bmFtZSI6ItCa0LXQvdC20LXRhdCw0L0iLCJpYXQiOjE3MDgyNDk2MTMsImV4cCI6MTcwODMzNjAxM30.aNqJGGq6kiFM-sB7sv5cH3SeBvsN-Y65GbRonZPMfxs; expireTokens=Sun%20Feb%2018%202024%2016:06:54%20GMT+0600%20(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9%20%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD)',
           'loginFails' : '0'
           }

data = {
    'start_date': '18.02.2024 00%3A00%3A00',
    'end_date': '18.02.2024 15%3A47%3A06',
    'car_number': '481AIX17'
}

req = requests.post(url, verify=False, headers=headers, cookies=cookies, json=data)

src = req.text

print(src)

print(req)