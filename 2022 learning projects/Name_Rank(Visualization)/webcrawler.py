"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        # number count
        male_num = 0
        female_num = 0
        for tag in tags:
            data = tag.text.split()
            # print(data)
            # clean garbage string
            for i in range(len(data)-22):
                # select for number
                if i % 5 == 2:
                    # print(data[i])
                    num = data[i].replace(',', '')
                    # print(num)
                    male_num += int(num)
                elif i % 5 == 4:
                    num = data[i].replace(',', '')
                    female_num += int(num)
        print('Male Number: ', male_num)
        print('Female Number: ', female_num)

        pass


if __name__ == '__main__':
    main()
