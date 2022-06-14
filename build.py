import os
# print("Hello world!")

#  Read in file content
topContent = open('./templates/top.html', encoding="utf8").read()
bottomContent = open('./templates/bottom.html', encoding="utf8").read()

# File paths 
# to read
directory_path = "./content"
# and write
file_path = "./docs"
index = 0

for file in os.listdir(directory_path):
  # Get content of content file
  content_file = os.path.join(directory_path, file)
  main_content = open(content_file, encoding="utf8").read()
  writing_content = topContent + main_content + bottomContent

  # Create new file
  newFile = os.path.join(file_path, file)
  open(newFile, "w").write(writing_content)

  index += 1
