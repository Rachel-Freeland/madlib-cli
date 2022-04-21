file_name = "assets/dark_and_stormy_night_template.txt"
def read_template(file_name):
  try:
    with open(file_name, 'r') as f:
      text = f.read()
  except:
    pass
  finally:
    pass
