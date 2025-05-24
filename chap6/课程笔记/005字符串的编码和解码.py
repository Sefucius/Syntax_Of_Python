s='伟大的汉族'
# 编写 str->bytes
scode=s.encode(errors='replace')
# 默认是utf-8，因为utf-8中文占3个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace')
# gbk中文占2个字节
print(scode_gbk)

# 编码中的出错问题
s2='耶✌'
scode2=s2.encode('gbk',errors='ignore')
print(scode2)
scode2=s2.encode('gbk',errors='replace')
# scode2=s2.encode('gbk',errors='strict') # 报错
print(scode2)

# 解码过程bytes->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))