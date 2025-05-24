from wordcloud import WordCloud,STOPWORDS
import jieba

# 读取文件
with open('华为笔记本电脑评论.txt', 'r', encoding='utf-8') as file:
    tex = file.read()

# 分词
lst=jieba.lcut(tex)

# 合并 
# 注意：这里的空格是为了让词云图中的词语分开，否则会连在一起
text=' '.join(lst)

# 添加自定义停用词
stopwords = set(STOPWORDS)
stopwords.update(["的", "也",'了','我','很'])  # 过滤掉的词语 
# 生成词云
wordcloud = WordCloud(
    font_path="msyh.ttc",
    stopwords=stopwords,
    width=800, height=400, 
    background_color="white",
    colormap="viridis"
    ).generate(text)
# 保存为图片
wordcloud.to_file("wordcloud.png")