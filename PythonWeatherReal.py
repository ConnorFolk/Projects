import requests
from datetime import datetime
from datetime import timedelta
import pandas as pd

api_key = 'da90a42a2ed3b50b581560d82613e6d8'
URL = 'https://api.openweathermap.org/data/2.5/forecast?'
location = [ \
    ["Anchorage,Alaska"], \
    ["Chennai,India"], \
    ["Jiangbei,China"], \
    ["Kathmandu,Nepal"], \
    ["Kothagudem,India"], \
    ["Lima,Peru"], \
    ["Manhasset,New York"], \
    ["Mexico City,Mexico"], \
    ["Nanaimo,Canada"], \
    ["Peterhead,Scotland"], \
    ["Polevskoy,Russia"], \
    ["Round Rock,Texas"], \
    ["Seoul,South Korea"], \
    ["Solihull,England"], \
    ["Tel Aviv,Israel"] \
    ]

pist = []
tempmin = []
tempmax = []

for y in range(0, len(location)):
    print(''.join(location[y]))
    URL = URL + "q=" + ''.join(location[y]) + "&units=metric&appid=" + api_key
    print(URL)
    response = requests.get(URL)  # using get function from requests package that gets http pages
    #  These status codes are http pages status codes
    pist.append(location[y])
    if response.status_code == 200:  # Success
        data = response.json()
        #  Get date and time in UTC, then convert it to a Python
        #  datetime object

        #  Offset the UTC time by the city's timezone offset to
        #  get the city's local time

        #  Print UTC and local times

        for i in range(0, len(data['list'])):
            dt_str = data['list'][i]['dt_txt']
            # dt_strbefore = data['list'][i - 1]['dt_txt']
            dt_tm = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
            # dt_tmbefore = datetime.strptime(dt_strbefore, '%Y-%m-%d %H:%M:%S')
            tz_offset = data['city']['timezone']
            dt_tm = dt_tm + timedelta(seconds=tz_offset)
            # dt_tmbefore = dt_tmbefore + timedelta(seconds=tz_offset)
            local_str = dt_tm.strftime('%Y-%m-%d %H:%M:%S')
            # print(dt_tm.day)
            # print(dt_str)
            print(dt_tm.day)
            print(datetime.today().day)
            if dt_tm.day == datetime.today().day:
                print("still today")
            else:
                break
        for j in range(i+1, len(data['list'])):
            first_day = dt_str = data['list'][i]['dt_txt']
            dt_str = data['list'][j]['dt_txt']
            dt_strbefore = data['list'][j - 1]['dt_txt']
            dt_tm = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
            dt_tmbefore = datetime.strptime(dt_strbefore, '%Y-%m-%d %H:%M:%S')
            tz_offset = data['city']['timezone']
            dt_tm = dt_tm + timedelta(seconds=tz_offset)
            dt_tmbefore = dt_tmbefore + timedelta(seconds=tz_offset)
            local_str = dt_tm.strftime('%Y-%m-%d %H:%M:%S')
            tempmin.append(data["list"][j - 1]['main']['temp_min'])
            tempmax.append(data["list"][j - 1]['main']['temp_max'])
            print(data["list"][j - 1]['main']['temp_max'])
            if (dt_tm.day != dt_tmbefore.day) :
                print(dt_tm)
                pist[y].append(min(tempmin))
                pist[y].append(max(tempmax))
                tempmin=[]
                tempmax=[]
                # print(pist)
                if len(pist[y]) > 10:
                    break
            if (j == (len(data['list']) - 1)):
                tempmin.append(data["list"][j]['main']['temp_min'])
                tempmax.append(data["list"][j]['main']['temp_max'])
                pist[y].append(min(tempmin))
                pist[y].append(max(tempmax))
                tempmin = []
                tempmax = []


        # else: print("I'm confused")
    else:  # Failure
        print('Error:', response.status_code)

    URL = 'https://api.openweathermap.org/data/2.5/forecast?'

pd.options.display.float_format = "{:,.2f}".format

weather = pd.DataFrame(pist)
weather.columns = ['Country', 'temperatureMin1', 'temperatureMax1', 'temperatureMin2', 'temperatureMax2',
                   'temperatureMin3', 'temperatureMax3', 'temperatureMin4', 'temperatureMax4', 'temperatureMin5',
                   'temperatureMax5',
                   ]

mincol = weather.loc[:, weather.filter(like='Min').columns]
maxcol = weather.loc[:, weather.filter(like='Max').columns]
print(weather)
weather['MinAVG'] = round((mincol.mean(axis=1)), 2)
weather['MaxAVG'] = round(maxcol.mean(axis=1), 2)

print(weather)

weather.to_csv('weather.csv', float_format='%.2f')