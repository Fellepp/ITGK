import time

# a)
def enter_line(prompt, length):
    sentence = input(prompt)
    while (len(sentence) != 30):
        print("The text must be", length, "characters long")
        sentence = input(prompt)
    return sentence


# text = enter_line("Enter line 1: ", 30)
# print(text)

# b)
def adjust_string(text, length):
    sentence = text
    if length < len(text):
        sentence = text[:length]
    elif length > len(text):
        difference = length - len(text)
        if difference % 2 == 0:
            sentence = " " * (difference//2) + text + " " * (difference//2)
        else:
            sentence = " " * (difference//2) + text + " " * (difference//2 +1)
    return sentence

print(adjust_string("This is a test on writing nicely and cooly!", 30))
print(adjust_string("ITGK is the best!", 30))
print(adjust_string("ITGK", 30))

# c)
def enter_line_smart(prompt, length):
    sentence = input(prompt)
    return adjust_string(sentence, length)

#print(enter_line_smart("Enter line 1: ", 30))
#print(enter_line_smart("Enter line 2: ", 30))
#print(enter_line_smart("Enter line 3: ", 30))

# d)
def show_display(content):
    for line in content:
        print(line)

def enter_show_text():
    text = ["" for x in range(0, 6)]
    for i in range(len(text)):
        text[i] += enter_line_smart("Enter line " + str((i+1)) + ": ", 30)
    return text

#content = enter_show_text()
#show_display(content)

# e)
def scroll_display(content, line):
    show_display(content)
    for i in range(0, 30):
        text = list(content[line - 1])
        temp = text[0]
        for j in range(0, 29):
            text[j] = text[j+1]
        text[-1] = temp
        text = "".join(text)
        content[line-1] = text
        show_display(content)
        print("\n\n")
        time.sleep(0.5)

#scroll_display(content, 6)

# f)
def display_from_file(filename):
    message = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            message.append(line)
    for i in range(len(message)):
        message[i] = adjust_string(message[i], 30)
    for i in range(0, len(message), 6):
        messageDisplay = []
        for j in range(i, i+6):
            messageDisplay.append(message[j])
        show_display(messageDisplay)
        time.sleep(10)


display_from_file("message.txt")


