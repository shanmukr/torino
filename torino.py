#!/usr/bin/python3
import re

def remove_data():
  a = input("enetr the project name : ")
  lines = open("sample.xml", 'r')
  line = lines.readlines()
  lines.close()
  b = ""
  c = 0

  for i in line:
    m = re.match(r'.*\<(project)\>(.*)\<\/\1\>', i)
    if m and m.group(2) == a:
      b = m.group(2)
    if b:
      if re.match(r'.*\<\/testlist\>', i):
        c = 1
      if c != 1:
        i = re.sub(r'(\<.*\>).*(\<\/.*\>)', r'\1\2', i)
    f = open("a.xml", 'a')
    f.write(i)
    f.close

def projects_data():
  all_data = {}
  prj_name = ""
  prj_rev = ""
  prj_block = ""
  prj_comment = ""
  prj_test = ""
  prj_field = ""
  prj_value = ""

  lines = open("projects.xml", "r")
  for i in lines.readlines():
    if re.match(r'\s+\<xml_file_type\>.*', i):
      continue
    match_obj = re.match(r'\s+\<project\>(\w+).*', i)
    if match_obj:
      prj_name = match_obj.group(1)
      all_data[prj_name] = {}
      all_data[prj_name]["test"] = []
      continue
    pro_rev = re.match(r'\s+\<project_rev\>(\w+).*', i)
    if pro_rev:
      prj_rev = pro_rev.group(1)
      all_data[prj_name]["revision"] = prj_rev
      continue
    pro_block = re.match(r'\s+\<block_name\>(\w+).*', i)
    if pro_block:
      prj_block = pro_block.group(1)
      all_data[prj_name]["block"] = prj_block
      continue
    pro_comments = re.match(r'\s+\<comments\>(\w+.*)\<.*', i)
    if pro_comments:
      prj_comment = pro_comments.group(1)
      all_data[prj_name]["comments"] = prj_comment
      continue
    pro_test = re.match(r'\s+\<(testname)\>(\w+)\<\/\1\>', i)
    if pro_test:
      prj_test = pro_test.group(2)
      all_data[prj_name]["test"].append(prj_test)
      continue
  lines.close()
  return all_data

def torino_data():
  all_data = {}
  prj_name = ""
  prj_rev = ""
  prj_block = ""
  prj_comment = ""
  prj_test = ""
  prj_field = ""
  prj_value = ""
  
  lines = open("torino.acc.block.xml", "r")
  for i in lines.readlines():
    if re.match(r'\s+\<xml_file_type\>.*', i):
      continue
    match_obj = re.match(r'\s+\<project\>(\w+).*', i)
    if match_obj:
      prj_name = match_obj.group(1)
      all_data[prj_name] = {}
      continue
    pro_rev = re.match(r'\s+\<project_rev\>(\w+).*', i)
    if pro_rev:
      prj_rev = pro_rev.group(1)
      all_data[prj_name]["revision"] = prj_rev
      continue
    pro_block = re.match(r'\s+\<block_name\>(\w+).*', i)
    if pro_block:
      prj_block = pro_block.group(1)
      all_data[prj_name]["block"] = prj_block
      continue
    pro_comments = re.match(r'\s+\<comments\>(\w+.*)\<.*', i)
    if pro_comments:
      prj_comment = pro_comments.group(1)
      all_data[prj_name]["comments"] = prj_comment
      continue
    pro_test = re.match(r'\s+\<(testname)\>(\w+)\<\/\1\>', i)
    if pro_test:
      prj_test = pro_test.group(2)
      all_data[prj_name][prj_test] = {} 
      continue
    pro_fields = re.match(r'\s+\<(\w+)\>(.*)\<\/\1\>', i)
    if pro_fields:
      prj_field = pro_fields.group(1)
      prj_value = pro_fields.group(2)
      all_data[prj_name][prj_test][prj_field] = prj_value
  lines.close()
  return all_data

def write_data():
  line = open("project.xml", "r")
  lines = line.readlines()
  line.close()
  
  line_a = open("a.txt", "r+")
  for i in line_a.readlines():
    match = re.match(r'.*\<\w+_type\>\w+\<\/\w+_type\>', i)
    if match:
      for j in lines: 
        line_a.write(j)
    break
  line_a.close()

def add_project():
  project      = input("Enter the Project Name : ")
  revision     = input("Enter the Revision Name : ")
  block        = input("Enter the Block Name : ")
  comments     = input("Enter the Comments : ")
  test         = input("Enter the Test Name : ")
  if project and revision and block and test and comments:
    old_data = projects_data()
    if old_data and project not in old_data.keys():
      print("added data\n")
    else:
      print("the given project '{}' is already exists. please enter the unique data.".format(project))
  else:
    print("all values are mandatory\n")

opt = input("Choose the below options.\n\t\t\t1.Add Project.\n\t\t\t2.Update Project.\n\t\t\t3.Delete Project.\n")

if opt and opt.isdigit():
  opt = int(opt)
  if( opt == 1 ):
    opt_add = input( "Choose the below options.\n\t\t\t1.Add Project\n\t\t\t2.Add Revision\n\t\t\t3.Add Block\n\t\t\t4.Add Comments\n\t\t\t5.Add Test\n" )
    if opt_add and opt_add.isdigit():
      opt_add = int(opt_add)
      if( opt_add == 1 ):
        add_project()
      else:
        print(type(opt_add), opt_add)
  elif( opt == 2 ): 
    print( "Choose the below options.\n\t\t\t1.Update Project\n\t\t\t2.Update Revision\n\t\t\t3.Update Block\n\t\t\t4.Update Comments\n\t\t\t5.Update Test\n" )
  elif( opt == 3 ):
    print( "Choose the below options.\n\t\t\t1.Delete Project\n\t\t\t2.Delete Revision\n\t\t\t3.Delete Block\n\t\t\t4.Delete Comments\n\t\t\t5.Delete Test\n" )
else:
  print ( "Choose the valid Options\n" )

