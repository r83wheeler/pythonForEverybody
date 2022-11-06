text = "X-DSPAM-Confidence:      0.8475"

pos = text.find('.')
new = text[pos:pos+5]

print(float(new))

