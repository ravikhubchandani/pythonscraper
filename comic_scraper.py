import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_comics_for_date(date: datetime) -> str:
    """
    Fetches the comic images for a given date
    """
    
    urls = [
        f"https://www.gocomics.com/garfield/{date.year}/{date.month}/{date.day}",
        f"https://www.gocomics.com/adult-children/{date.year}/{date.month}/{date.day}",
        f"https://www.gocomics.com/peanuts/{date.year}/{date.month}/{date.day}",
        f"https://www.gocomics.com/9to5/{date.year}/{date.month}/{date.day}",
        f"https://www.gocomics.com/calvinandhobbes/{date.year}/{date.month}/{date.day}",
        f"https://www.gocomics.com/bc/{date.year}/{date.month}/{date.day}",
        f"https://www.gocomics.com/ziggy/{date.year}/{date.month}/{date.day}"
    ]
    
    img_src_list = []

    for url in urls:
        print(f"Scraping URL {url}")
        
        try:
            res = requests.get(url)
            res.raise_for_status()

            # res.content is the HTML content of the page and contains the image in tag such as
            # <meta property="og:image" content="https://featureassets.gocomics.com/assets/c75ec4a017c5013ea0c4005056a9545d"/>

            soup = BeautifulSoup(res.content, "lxml")
            meta_tag = soup.find("meta", property="og:image")
            img_src = meta_tag['content'] if meta_tag else None
            
            if img_src:
                img_src_list.append(img_src)
            
            else:
                print(f"No image found in {url}")
        
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    
    html_content = "<html><body>"
    
    for img_path in img_src_list:
        html_content += f'<img src="{img_path}"><hr>'
    
    html_content += "</body></html>"

    return html_content