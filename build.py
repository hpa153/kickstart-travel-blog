import os
# print("Hello world!")

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
    html_file["title"] = "Home" if file[:-5].strip().capitalize() == "Index" else file[:-5].strip().capitalize()
    
    html_files.append(html_file)
  
  return html_files

# Function to create content files in docs directory
def create_content(files):
  index = 0
  for file in files:
    # Get original content
    template = open("./templates/base.html").read()
    content = open(file["filename"]).read()

    # Replace placeholders and create file in docs directory with finalized content
    replaced_title = template.replace("{{title}}", file["title"])

    # Get current page to set active
    current_page = "current--" + file["title"].lower()
    active = replaced_title.replace(current_page, "current")
    finalized_content = active.replace("{{content}}", content)
    open(file["output"], "w").write(finalized_content)
    index += 1

# Main function
def main():
  content_files = get_files()
  create_content(content_files)

main()
