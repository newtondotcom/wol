######SPECIFIC FUNCTIONS FOR FLIGHT SIMULATOR WEBSITE######
from datas.models import *
import requests
from bs4 import BeautifulSoup
import re


import requests
from bs4 import BeautifulSoup
import re

def scrape_simplaza(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    title_element = soup.find('h1', {'class':'title entry-title'})
    title = title_element.text if title_element else None
    if title is None:
        return None, None, None, None, None, None
    category_tags = soup.select('[rel="category tag"]')
    is_airplane = False
    is_plugin = False
    for j in category_tags:
        if 'Aircraft' in j.text:
            type2 = 'aircraft'
            is_airplane = True
            break
        if 'Misc' in j.text:
            type2 = 'plugin'
            is_airplane = True
            break
    if not is_airplane and not is_plugin:
        type2 = 'scenery'
        
    changelog_elements = soup.findAll('div', {'class':'su-spoiler-content su-u-clearfix su-u-trim'})
    changelog = changelog_elements[0].text if len(changelog_elements) > 1 else ''
    description = changelog_elements[1].text if len(changelog_elements) > 1 else changelog_elements[0].text
    note_elements = soup.findAll('div', {'class':'su-box-content su-u-clearfix su-u-trim'})
    note = note_elements[0].text if note_elements else ''
    if "Rapidgator" in note_elements[0].text:
        note = None
    pattern = re.compile(r'https://simplaza.org/wp-content/uploads/[\w/.-]+')
    image_list = pattern.findall(str(soup))
    image = image_list[16] if image_list else None
    return title, type2, image, description, changelog, note

#print(scrape_simplaza("https://simplaza.org/jeppeson2001-niagara-falls-city-pack-v1-1-0/"))
    
import requests
from bs4 import BeautifulSoup
import re

def scrape_aviaworld(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    pattern = re.compile(r'https://aviaworld.org/wp-content/uploads/[\w/.-]+')
    image_list = pattern.findall(str(soup))
    image = image_list[17] if image_list else None
    pattern = re.compile(r'https://modsfire.com/[\w/.-]+')
    source_code = r.text
    matches = re.findall(pattern, source_code)
    if len(matches) > 2:
        url1 = matches[0:2]
        url2 = matches[2:]
    else:
        url1 = matches[0] if matches else None
        url2 = matches[1] if len(matches) > 1 else None
    description_element = soup.find('div', {'class':'wp-block-group is-vertical is-layout-flex wp-container-1'})
    description = description_element.text if description_element else None
    note_elements = soup.findAll('div', {'class':'wp-block-ub-content-toggle-accordion-content-wrap'})
    note = note_elements[0].text if len(note_elements) > 1 else None
    changelog = note_elements[1].text if len(note_elements) > 1 else note_elements[0].text
    if changelog and "MODSFIRE" in changelog:
        changelog = None
    if "Info" not in source_code:
        note = None
    if "Changelog" not in source_code:
        changelog = None
    title_element = soup.find('h1', {'class':'elementor-heading-title elementor-size-default'})
    if "P3D" in title_element.text :
        game = "p3d"
    if "XP" in title_element.text :
        game = "xplane"
    title = title_element.text.split('] ')[-1] if title_element else None
    return title, image, description, changelog, note, url1, url2, game


#print(scrape_aviaworld("https://aviaworld.org/p5d-imaginesim-wsss-singapore-changi-intl-airport-2023/"))

from django.core.files.storage import FileSystemStorage
import zipfile

def create_archive(name, link, game, link2=None):
    # Edit the readme.txt template
    with open('./wol/readme.txt', 'r') as file:
        string = file.read()
        string = string.replace('RESSOURCENAME', name)
        if link2 == None:
            string = string.replace('LINK', link)
        else:
            nametemp = name
            if game == "mfs2020":
                temp = "\nPart 1: " + link 
                name = "Part1_"+nametemp
                temp2 = "\nPart 2: " + link2
                name2 = "Part2_"+nametemp
            if isinstance(link,list):
                link = '\n Part 1: ' + link[0] + '\n Part 2: ' + link[1]
            if isinstance(link2,list):
                link2 = '\n Part 1: ' + link2[0] + '\n Part 2: ' + link2[1]
            if game == "p3d":
                temp = "\nP3DV4: " + link 
                name = "P3DV4_"+nametemp
                temp2 = "\nP3DV5: " + link2
                name2 = "P3DV5_"+nametemp
            elif game == "xplane":
                temp = "\n XP11: " + link 
                name = "XP11_"+nametemp
                temp2 = "\n XP12: " + link2
                name2 = "XP12_"+nametemp
            string2 = string
            string2 = string2.replace('LINK', temp2)
            string = string.replace('LINK', temp)
        with open('./static/README.txt', 'w') as file:
            file.write(string)

        with zipfile.ZipFile('./static/'+name+'.zip', 'w') as zf:
            zf.write('./static/README.txt')
        
        if link2 is not None:
            with open('./static/README.txt', 'w') as file:
                file.write(string2)
            with zipfile.ZipFile('./static/'+name2+'.zip', 'a') as zf:
                zf.write('./static/README.txt')
        
    
    return '/static/'+name+'.zip', '/static/'+name2+'.zip' if link2 else None