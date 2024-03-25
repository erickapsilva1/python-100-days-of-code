from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# Full document
print(soup)

# Full formatted document
print(soup.prettify())

# Tag and content
print(soup.title)

# Content
print(soup.title.string)

# First <a> element
print(soup.a)

# Get all anchor elements
all_anchor_tags = soup.findAll(name="a")
for tag in all_anchor_tags:
    print(tag.getText() + " - " + tag.get("href"))

# By id
heading = soup.find(name="h1", id="name")
print(heading)

# By class
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# By using CSS selector
company_url = soup.select_one(selector="p a")
print(company_url)