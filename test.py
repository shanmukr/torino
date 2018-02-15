#!/usr/bin/python3
import re

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


"""
def torino_data():
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
"""

"""
project      = input("Enter the Project Name : ")
revision     = input("Enter the Revision Name : ")
block        = input("Enter the Block Name : ")
comments     = input("Enter the Comments : ")
test         = input("Enter the Test Name : ")

c = []
line = open("project.xml", "r")
if project:# and revision and block and test and comments:
  for i in line.readlines():
    if (re.match(r'\s*\<(project)\>\<\/\1\>', i)):
      #i = re.sub(r'(\s*\<project\>)(\<\/project\>)', r'\1'+project+r'\2', i)
      i = re.sub(r'(\s*\<project\>)(\<\/project\>)', r'\1{}\2'.format(project), i)
      c.append(i)
      continue
    if (re.match(r'\s*\<(project_rev)\>\<\/\1\>', i)):
      i = re.sub(r'(\s*\<project_rev\>)(\<\/project_rev\>)', r'\1{}\2'.format(revision), i)
      c.append(i)
      continue
    if (re.match(r'\s*\<(block_name)\>\<\/\1\>', i)):
      i = re.sub(r'(\s*\<block_name\>)(\<\/block_name\>)', r'\1{}\2'.format(block), i)
      c.append(i)
      continue
    if (re.match(r'\s*\<(comments)\>\<\/\1\>', i)):
      i = re.sub(r'(\s*\<comments\>)(\<\/comments\>)', r'\1{}\2'.format(comments), i)
      c.append(i)
      continue
    if (re.match(r'\s*\<(testname)\>\<\/\1\>', i)):
      i = re.sub(r'(\s*\<testname\>)(\<\/testname\>)', r'\1{}\2'.format(test), i)
      c.append(i)
      continue
    c.append(i)
line.close()

line_a = open("a.txt", "r+")
for i in line_a.readlines():
  match = re.match(r'.*\<\w+_type\>\w+\<\/\w+_type\>', i)
  if match:
    for j in c: 
      line_a.write(j)
line_a.close()
"""
"""
l = open("a.txt", "w")
for i in lines_a:#.readlines():
  l.write(i)
  match = re.match(r'.*\<\w+_type\>\w+\<\/\w+_type\>', i)
  if match:
    for j in lines: 
      l.write(j)
l.close()
"""
