import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import pyfiglet
from colorama import init, Fore

init(autoreset=True)

def get_html_code(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def get_css_code(base_url, css_url):
    if not css_url.startswith('http'):
        css_url = urljoin(base_url, css_url)

    response = requests.get(css_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def get_js_code(base_url, js_url):
    if not js_url.startswith('http'):
        js_url = urljoin(base_url, js_url)
    response = requests.get(js_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def code_analysis(code, code_type):
    if code:
        lines = code.split('\n')
        num_lines = len(lines)
        print(Fore.CYAN + f"{code_type} Code Analysis:")
        print(Fore.CYAN + f"Number of Lines: {num_lines}" + Fore.RESET)
    else:
        print(Fore.YELLOW + f"No {code_type} code found." + Fore.RESET)

def download_images(base_url, html_code, image_folder):
    soup = BeautifulSoup(html_code, 'html.parser')
    img_tags = soup.find_all('img')
    
    if img_tags:
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(base_url, img_url)
                response = requests.get(img_url)
                if response.status_code == 200:
                    img_content = response.content
                    img_name = os.path.basename(urlparse(img_url).path)
                    img_file_path = os.path.join(image_folder, img_name)
                    with open(img_file_path, 'wb') as img_file:
                        img_file.write(img_content)
                    print(Fore.GREEN + f"Downloaded image: {img_name}" + Fore.RESET)
                else:
                    print(Fore.RED + f"Failed to download image: {img_url}" + Fore.RESET)
    else:
        print(Fore.YELLOW + "No images found on the webpage." + Fore.RESET)

banner = pyfiglet.figlet_format("WICK TOOL", font="slant")
print(Fore.BLUE + banner)

while True:
    url = input(Fore.GREEN + "Enter the website URL (or 'exit' to exit) : " + Fore.RESET)

    if url.lower() == 'exit':
        break

    parsed_url = urlparse(url)
    website_name = parsed_url.netloc
    
    html_folder = 'html_codes'
    css_folder = 'css_codes'
    js_folder = 'js_codes'
    image_folder = 'images'
    os.makedirs(html_folder, exist_ok=True)
    os.makedirs(css_folder, exist_ok=True)
    os.makedirs(js_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    
    
    print("Choose an option:")
    print("1. Get HTML code")
    print("2. Get CSS code")
    print("3. Get JavaScript code")
    print("4. Download Images")

    choice = input(Fore.GREEN + "Enter your choice (1/2/3/4): " + Fore.RESET)

    if choice == "1":
        
        html_code = get_html_code(url)
        if html_code:
            print("HTML Code:")
            print(html_code)
            
            
            html_file_name = os.path.join(html_folder, f"{website_name}.html")
            with open(html_file_name, 'w', encoding='utf-8') as file:
                file.write(html_code)
            print(Fore.GREEN + f"HTML code saved to '{html_file_name}'" + Fore.RESET)
            
            code_analysis(html_code, "HTML")
        else:
            print(Fore.RED + f"Failed to retrieve the webpage at {url}" + Fore.RESET)
    elif choice == "2":
        
        html_code = get_html_code(url)
        if html_code:
            soup = BeautifulSoup(html_code, 'html.parser')
            css_links = soup.find_all('link', rel='stylesheet')
            if css_links:
                for css_link in css_links:
                    css_url = css_link.get('href')
                    if css_url:
                        css_code = get_css_code(url, css_url)
                        if css_code:
                            print(f"CSS Code from {css_url}:\n{css_code}\n")
                            
                            css_file_name = os.path.join(css_folder, f"{website_name}.css")
                            with open(css_file_name, 'w', encoding='utf-8') as file:
                                file.write(css_code)
                            print(Fore.GREEN + f"CSS code saved to '{css_file_name}'" + Fore.RESET)

                            
                            code_analysis(css_code, "CSS")
                        else:
                            print(Fore.RED + f"Failed to retrieve CSS from {css_url}" + Fore.RESET)
            else:
                print(Fore.YELLOW + "No CSS links found on the webpage." + Fore.RESET)
        else:
            print(Fore.RED + f"Failed to retrieve the webpage at {url}" + Fore.RESET)
    elif choice == "3":
        
        html_code = get_html_code(url)
        if html_code:
            soup = BeautifulSoup(html_code, 'html.parser')
            js_scripts = soup.find_all('script', src=True)
            if js_scripts:
                for js_script in js_scripts:
                    js_url = js_script.get('src')
                    if js_url:
                        js_code = get_js_code(url, js_url)
                        if js_code:
                            print(f"JavaScript Code from {js_url}:\n{js_code}\n")

                            
                            js_file_name = os.path.join(js_folder, f"{website_name}.js")
                            with open(js_file_name, 'w', encoding='utf-8') as file:
                                file.write(js_code)
                            print(Fore.GREEN + f"JavaScript code saved to '{js_file_name}'" + Fore.RESET)
                            
                            code_analysis(js_code, "JavaScript")
                        else:
                            print(Fore.RED + f"Failed to retrieve JavaScript from {js_url}" + Fore.RESET)
            else:
                print(Fore.YELLOW + "No JavaScript scripts found on the webpage." + Fore.RESET)
        else:
            print(Fore.RED + f"Failed to retrieve the webpage at {url}" + Fore.RESET)
    elif choice == "4":
        
        html_code = get_html_code(url)
        if html_code:
            download_images(url, html_code, image_folder)
        else:
            print(Fore.RED + f"Failed to retrieve the webpage at {url}" + Fore.RESET)
    else:
        print(Fore.RED + "Invalid choice. Please enter 1, 2, 3, or 4." + Fore.RESET)
