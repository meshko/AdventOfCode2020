#!/usr/bin/env python3
import sys

op_priority = {'(': 0, ')': 1, '+': 2, '*': 2}

def line_to_rpn(line):
  cur_num = None
  result = []
  operations = []
  for c in '(' + line + ")":
    if c == ' ': continue
    if c.isdigit():
      cur_num = cur_num * 10 if cur_num else 0
      cur_num += int(c)
      continue
    if c == '(':
      operations.append(c)
      continue
    if cur_num:
      result.append(cur_num) 
      cur_num = None
    if c in ['*', '+', ')']:
      while operations and op_priority[operations[-1]] >= op_priority[c]:
        result.append(operations.pop())
      if c == ')':
        operations.pop()
      else:
        operations.append(c)
    else:
      print("unexpected character %s" % c)   
  return result

def eval_rpn(rpn):
  result = []
  for n in rpn:
    if n == '*':
       result.append(result.pop() * result.pop())
    elif n == '+':
       result.append(result.pop() + result.pop())
    else:
       result.append(n)
  return result[0]

def main():
  global op_priority
  if len(sys.argv) > 1 and sys.argv[1] == '2':
    op_priority['+'] = 3

  sum = 0    
  for line in map(str.rstrip, sys.stdin):
    res = eval_rpn(line_to_rpn(line)) 
    sum += res
  print(sum)

if __name__ == "__main__":
  sys.exit(main())

