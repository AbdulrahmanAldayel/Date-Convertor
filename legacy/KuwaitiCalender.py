import datetime

def gmod(n, m):
    return ((n % m) + m) % m

def kuwaiticalendar(adjust=0):
    
    today = datetime.datetime.now()
    if adjust:
        adjustmili = 1000 * 60 * 60 * 24 * adjust
        todaymili = today.timestamp() + adjustmili
        today = datetime.datetime.fromtimestamp(todaymili)
    
    day = today.day
    month = today.month
    year = today.year
    m = month + 1
    y = year
    if m < 3:
        y -= 1
        m += 12
    
    a = y // 100
    b = 2 - a + a // 4
    if y < 1583:
        b = 0
    if y == 1582:
        if m > 10:
            b = -10
        if m == 10:
            b = 0
            if day > 4:
                b = -10
    
    jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + day + b - 1524
    
    b = 0
    if jd > 2299160:
        a = int((jd - 1867216.25) / 36524.25)
        b = 1 + a - a // 4
    bb = jd + b + 1524
    cc = int((bb - 122.1) / 365.25)
    dd = int(365.25 * cc)
    ee = int((bb - dd) / 30.6001)
    day = bb - dd - int(30.6001 * ee)
    month = ee - 1
    if ee > 13:
        cc += 1
        month = ee - 13
    year = cc - 4716
    
    if adjust:
        wd = gmod(jd + 1 - adjust, 7) + 1
    else:
        wd = gmod(jd + 1, 7) + 1
    
    iyear = 10631 / 30
    epochastro = 1948084
    epochcivil = 1948085
    shift1 = 8.01 / 60
    
    z = jd - epochastro
    cyc = z // 10631
    z -= 10631 * cyc
    j = (z - shift1) // iyear
    iy = 30 * cyc + j
    z -= j * iyear + shift1
    im = int((z + 28.5001) / 29.5)
    if im == 13:
        im = 12
    id = z - int(29.5001 * im - 29)
    
    myRes = [day, month - 1, year, jd - 1, wd - 1, id, im - 1, iy]
    return myRes

def writeIslamicDate(adjustment=0):
    wdNames = ["Ahad", "Ithnin", "Thulatha", "Arbaa", "Khams", "Jumuah", "Sabt"]
    iMonthNames = ["Muharram", "Safar", "Rabi'ul Awwal", "Rabi'ul Akhir", "Jumadal Ula", 
                   "Jumadal Akhira", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhul Qa'ada", "Dhul Hijja"]
    
    iDate = kuwaiticalendar(adjustment)
    outputIslamicDate = f"{wdNames[iDate[4]]}, {iDate[5]} {iMonthNames[iDate[6]]} {iDate[7]} AH"
    return outputIslamicDate

print(writeIslamicDate())
