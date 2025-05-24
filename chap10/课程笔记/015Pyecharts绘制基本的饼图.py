# 导入
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 准备数据
lst=[['华为',1000],['OPPO',1200],['苹果',300],['小米',400],['vivo',200]]
c = (
    Pie()
    .add("", lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
) 

""" c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
) """
# print([list(z) for z in zip(Faker.choose(), Faker.values())])