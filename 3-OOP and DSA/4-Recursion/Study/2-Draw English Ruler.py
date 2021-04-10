def draw_line(ticks_len,label=''):
    line='-' * ticks_len
    if label:
        line+=' '+label
    print(line)

def draw_interval(intermidate):
    if intermidate >0:
        draw_interval(intermidate-1)
        draw_line(intermidate)
        draw_interval(intermidate-1)

def draw_ruler(inch,major_len):
    draw_line(major_len,"0")
    for i in range(1,inch+1):
        draw_interval(major_len-1)
        draw_line(major_len,str(i))

draw_ruler(4,5)