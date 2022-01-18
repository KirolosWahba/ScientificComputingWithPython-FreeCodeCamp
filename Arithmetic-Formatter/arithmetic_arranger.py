def arithmetic_arranger(problems, result=False):
  if(len(problems) > 5):
    return "Error: Too many problems."
  else:
    fItems = []
    lItems = []
    operators = []
    fLengths = []
    lLengths = []
    rlengths = []
    dashes = []
    results = []
    for problem in problems:
      fItem, operator, lItem = problem.split()

      if(operator not in ['+', '-']):
        return "Error: Operator must be '+' or '-'."
      
      length = len(fItem) - len(lItem)
      maxLength = max(len(fItem),len(lItem))
      if(maxLength > 4):
        return "Error: Numbers cannot be more than four digits."
      
      try:
        fItem = int(fItem)
        lItem = int(lItem)
      except:
        return "Error: Numbers must only contain digits."
      
      if(operator == '+'):
        resultTmp =str(fItem + lItem)
      else:
        resultTmp =str(fItem - lItem)

      fItems.append(fItem)
      lItems.append(lItem)
      operators.append(operator)
      dashes.append((maxLength+2) * '-')
      rlengths.append(maxLength + 2 - len(resultTmp))
      results.append(resultTmp)
      if(length<0):
        fLengths.append(-length)
        lLengths.append(0)
      else:
        fLengths.append(0)
        lLengths.append(length)

    for i in range(len(fLengths)):
     fItems[i] = (fLengths[i]+2) * " " + str(fItems[i])
     lItems[i] = operators[i] + (lLengths[i]+1) * " " + str(lItems[i])
     results[i] = rlengths[i] * " " + str(results[i])

    arranged_problems = "    ".join(fItems) + "\n"
    arranged_problems += "    ".join(lItems) + "\n"
    arranged_problems += "    ".join(dashes)
    
    if(result):
      arranged_problems += "\n" + "    ".join(results)

  return arranged_problems