import utils
import sys

command = ""
if len(sys.argv) > 1:
  command = sys.argv[1]

if command == "build":
  print("Build was specified")
  utils.main()
elif command == "new":
  print("New page was specified")
  utils.create_placeholder()
else:
  print("Please specify 'build' or 'new'")

