# Strings 

text = "X-DSPAM-Confidence:    0.8475"

post=text.find(":")
end=text[post+1:]
number=float(end)
print(number) 