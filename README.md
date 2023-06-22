# WorldOfLeaks

WorldOfLeaks is a multipurpose website, originally designed for leaks and hacks. The website is fully responsive and can be used on any device. The website is fully customizable and can be used for any purpose.

## Architecture

There are 4 main components of the database :
- the **game** table : create and stock games
- the **category** table : create and stock categories
- the **product** table : create and stock products
- the **CatAndGames** table : link categories and games

When you add a **product**, you can choose the **game** and the **category**. The **product** will be linked to the **game** and the **category** and the **category** automatically added in the **CatAndGames** table if the **category** is not already linked to the **game**.

Each **category** can have 2 links displayed per product and each **product** can have as well 2 links even the category is 1-link one. The links are displayed in the product page.

# Responsive and customizable

You can add as many games and categories as you want. Each page is generated at each request so newly added games and categories as will load real time without having to change the code. We could use the Django Admin panel.

# Installation

- `git clone` this repository
- `pip install -r requirements.txt`
- Tweaks the settings you want in [`wol/settings.py`](wol/settings.py)
- `python manage.py makemigrations` to build necessary migrations
- `python manage.py migrate` to initialize the database
- `python manage.py createsuperuser` to create an admin account for the Django Admin panel
- `python manage.py runserver` to run the server

# Requirements

- Python
- pip
- and that's is all ! (the magic of Django)

# Docker

The application is ready to use with **Docker**. The image can be built using Dockerfile and the following command :

`docker build . -t wol -f Dockerfile`

To be deployed, the image can be uploaded to a Docker registry and then pulled and run on the server using the following command :

`sh docker-build.sh`

# Languages used

<img alt="Python" src="https://img.shields.io/badge/-Python-23272A?style=flat&logo=python"> <img alt="HTML5" src="https://img.shields.io/badge/-HTML5-23272A?style=flat&logo=html5"> <img alt="CSS3" src="https://img.shields.io/badge/-CSS3-23272A?style=flat&logo=css3"> <img alt="JavaScript" src="https://img.shields.io/badge/-JavaScript-23272A?style=flat&logo=javascript"> <img alt="SQL" src="https://img.shields.io/badge/-SQL-23272A?style=flat&logo=postgresql"> <img alt="Markdown" src="https://img.shields.io/badge/-Markdown-23272A?style=flat&logo=markdown">

# Experience

This project took me exactly 24 hours from start to beginning. 

# Contabo 🐶

[Contabo](dz) is the web hoster I recommmand. They are cheap, reliable and have a good support 📒

For example, you could get :
- a private [VPS](dz) with 4 vCores, 8GB RAM, 200GB SSD for 5.99€/month 💴
- a [web hosting service](dz) with 50GB SSD, 20 MySQL DB, 1 domain and 1000 Email Addresses for 2.99€/month 💶
- a [storage VPS](dz) with 2 vCores, 4GB RAM, 400GB SSD, unlimited bandwitch incoming and 32 TB outcoming for 5.99€/month 💷

I personnally think that they are the cheapest and the best web hoster in Europe 🇪🇺

Don't hesistate to take a look at their [website](dz) 🌐

