def parse_address(address):
  keys = ["street", "city", "state", "zip"]
  my_dict = dict.fromkeys(keys)
  parse_address = address.split(",")
  #print(parse_address)
  zip_code = parse_address[2].strip().split(" ")
  #print(keys)
  #print(zip_code)
  my_dict.update(
    {
      "street": parse_address[0].strip(),
      "city": parse_address[1].strip(), 
      "state": zip_code[0], 
      "zip": zip_code[1]
    }
  )
  return my_dict
  
