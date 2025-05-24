from datetime import datetime,timedelta 
dt1_str=input('请输入开始日期(20281001)后按回车：')
dt1=datetime.strptime(dt1_str,'%Y%m%d')
days=int(input('请输入间隔数：'))
td=timedelta(days)
dt2=dt1+td
dt2_str=dt2.strftime('%Y-%m-%d %H:%M:%S')
print(f'您推算的日期是:{dt2_str}')
