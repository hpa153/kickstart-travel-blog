import os
from jinja2 import Environment, FileSystemLoader, Template
# print("Hello world!")

# Jinja variables
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

# File paths 
# to read
directory_path = "./content"
# and write
file_path = "./docs"

# Function to get file information
def get_files():
  # File paths 
  # to read
  directory_path = "./content"
  # and write
  file_path = "./docs"

  # Fill content list with information dictionaries of each page
  html_files = []

  for file in os.listdir(directory_path):
    # Create new dictionary from file information
    html_file = {}
    
    html_file["filename"] = os.path.join(directory_path, file)
    html_file["output"] = os.path.join(file_path, file)
    html_file["title"] = "Home" if file[:-5].strip() == "index" else file[:-5].strip().capitalize()
    
    html_files.append(html_file)
  
  return html_files

# Function to create content files in docs directory
def create_content(files):
  
  # Create nav items
  items = []
  index = 0
  icon_list = ["fa-address-book", "fa-house-chimney", "fa-plane-departure"]

  for file in os.listdir(directory_path):
    item = {}
    item["path"] = file

    if file[:-5].strip() == "index":
      item["name"] = "Home"
      active = "current--home"
    else:
      item["name"] = file[:-5].strip().capitalize()
      active = "current--" + file[:-5].strip()
    
    icon = icon_list[index]
    item["class"] = "fa-solid menu-icon " + icon + " " + active
    item["span_class"] = "menu-text " + active
    
    index += 1
    items.append(item)
  
  for file in files:
    # Get original content
    template = open("./templates/base.html").read()
    content = open(file["filename"]).read()

    # Use Jinja to replace content and title
    template_file = Template(template)
    output = template_file.render(
      nav_items=items,
      title=file["title"],
      content=content,
    )

    # Set current page active
    output = output.replace("current--" + file["title"].lower(), "current")
  
    open(file["output"], "w").write(output)

# Main function for creating content
def main():
  content_files = get_files()
  create_content(content_files)

# Function to create a html placeholder file
def create_placeholder():
  template = """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    
  </body>
  </html>
  """
  open("./content/new_content_page.html", "w").write(template)