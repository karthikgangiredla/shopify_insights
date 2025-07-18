import re

def extract_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)

def extract_phone_numbers(text):
    return re.findall(r'\+?\d[\d\s().-]{7,}\d', text)

def find_links(soup, keywords):
    links = []
    for a in soup.find_all('a', href=True):
        if any(keyword in a.text.lower() for keyword in keywords):
            links.append(a['href'])
    return links
