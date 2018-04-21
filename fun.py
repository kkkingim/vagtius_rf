#############################
# translate binary to ascii #
# eg. In : 01100011         #
#    Out : c                #
#     In : 0110001101100111 #
#    Out : cg               #
#############################
def bin2asc(s):
    if len(s) % 8 != 0:
        return ''
    if s.replace('1','') .replace('0','') != '':
        return ''
    sls = [s[i:i+8] for i in range(0, len(s) , 8)]
    return ''.join([str(chr(int(i, 2))) for i in sls])
