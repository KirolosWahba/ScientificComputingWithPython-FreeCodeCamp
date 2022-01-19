def add_time(start, duration, day=""):
  daysAfter = 0
  appendix = ""
  #
  hour, temp = start.split(":")
  minutes, referance = temp.split(" ")
  hourDur, minutesDur = duration.split(":")

  # Calculating the time
  minutes =int(minutes) + int(minutesDur)
  hour = int(hour) + int(hourDur) + minutes//60
  minutes %= 60

  if(hour>=12):
    halfDays = hour // 12
    hour %= 12
    if(hour==0):
      hour = 12

    if(referance == 'AM'):
      if(halfDays>3):
        daysAfter = halfDays//2
        appendix = " ({} days later)".format(daysAfter)
      elif(halfDays>1):
        daysAfter = 1
        appendix = " (next day)"

    else:
      if(halfDays>2):
        daysAfter = (halfDays+1)//2
        appendix = " ({} days later)".format(daysAfter)
      else:
        daysAfter = 1
        appendix = " (next day)"

    # Toggle the AM to PM and vice versa if needed
    if(halfDays%2 != 0):
      if(referance == 'AM'):
        referance = 'PM'
      else:
        referance = 'AM'

  # Showing the day if required
  if(day != ""):
    days=("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

    dayID = days.index(day.title())
    day = ", " + days[(dayID+daysAfter)%7]
  
  # Formating the result
  new_time = "{}:{:02} {}{}{}".format(hour, minutes, referance, day, appendix)
  
  return new_time