import re

all_data = {}
prj_name = ""
prj_rev = ""
prj_block = ""
prj_comment = ""
prj_test = ""
prj_field = ""
prj_value = ""
test = {}

lines = open("torino.acc.block.xml", "r")
for i in lines.readlines():
  match_obj = re.match(r'\s+\<project\>(\w+).*', i)
  if match_obj:
    prj_name = match_obj.group(1)
    all_data[prj_name] = {}
  pro_rev = re.match(r'\s+\<project_rev\>(\w+).*', i)
  if pro_rev:
    prj_rev = pro_rev.group(1)
    all_data[prj_name]["revision"] = prj_rev
  pro_block = re.match(r'\s+\<block_name\>(\w+).*', i)
  if pro_block:
    prj_block = pro_block.group(1)
    all_data[prj_name]["block"] = prj_block
  pro_comments = re.match(r'\s+\<comments\>(\w+.*)\<.*', i)
  if pro_comments:
    prj_comment = pro_comments.group(1)
    all_data[prj_name]["comments"] = prj_comment
  pro_test = re.match(r'\s+\<(testname)\>(\w+)\<\/\1\>', i)
  if pro_test:
    prj_test = pro_test.group(2)
    if prj_test:
      all_data[prj_name][prj_test] = {} 
  pro_fields = re.match(r'\s+\<(\w+)\>(.*)\<\/\1\>', i)
  if pro_fields:
    prj_field = pro_fields.group(1)
    prj_value = pro_fields.group(2)
  #if prj_field:
    #all_data[prj_name][prj_test][prj_field] = prj_value
lines.close()

print ( all_data )
