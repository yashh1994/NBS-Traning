def timeConversion(s):
    step = s[8:]
    print(step)
    hour = int(s[:2])
    if step == "PM":
        if hour!=12:
            hour += 12
    else:
        if hour == 12:
            hour -= 12
            return f"00{s[2:-2]}"
    if hour<10:
        return f"0{hour}{s[2:-2]}"
    return f"{hour}{s[2:-2]}"
    