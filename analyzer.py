import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from datetime import datetime, timedelta
import os
import random
import numpy as np

def professional_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ['#1A5276', '#943126', '#1D8348', '#34495E'] 
    return random.choice(colors)

def run_analyzer():
    csv_file = "data/papers.csv"
    output_image = "data/weekly_report.png"

    if not os.path.exists(csv_file):
        print("找不到 papers.csv，请先运行 spider.py！")
        return

    try:
        df = pd.read_csv(csv_file)
        df['Published_Date'] = pd.to_datetime(df['Published_Date'])
    except Exception as e:
        print(f"读取CSV文件失败: {e}")
        return
    
    seven_days_ago = datetime.now() - timedelta(days=7)
    
    df_recent = df[df['Published_Date'] >= seven_days_ago]
    
    if df_recent.empty:
        print("7 天内暂无新数据，无法生成词云")
        dummy_wc = WordCloud(width=800, height=600, background_color='white').generate("No Data Yet")
        dummy_wc.to_file(output_image)
        return
        
    print(f"提取到 {len(df_recent)} 篇近 7 天论文...")

    text_data = " ".join(df_recent['Title'].astype(str).tolist()) + " " + " ".join(df_recent['Summary'].astype(str).tolist())
    text_data = text_data.lower()

    if not text_data.strip():
        print("文本为空，无法生成词云")
        return

    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update([
        "model", "paper", "method", "approach", "propose", "proposed",
        "result", "show", "agent", "agents", "based", "using", "task",
        "system", "framework", "study", "new", "two", "via", "state",
        "performance", "use" # 常见但信息量低的词
    ])

    print("正在渲染词云图...")
    
    font_path_setting = 'arial.ttf' # 默认尝试 Arial

    try:
        wc = WordCloud(
            width=2000,                  # 宽度
            height=1200,                 # 高度
            background_color='white',    # 背景
            margin=25,                   # 间距
            max_font_size=180,           # 最大字体大小
            min_font_size=60,            # 最小字体大小
            relative_scaling=0.6,        # 平滑系数
            max_words=60,                # 总词数
            # ----------------
            prefer_horizontal=0.9,       # 90% 水平排版
            font_path=font_path_setting, # 字体
            color_func=professional_color_func, # 4色主题
            stopwords=custom_stopwords,  # 降噪词表
            random_state=42,             # 锁定排版
            collocations=False           # 关闭词组搭配
        )
        
        wc.generate(text_data)
        
        if not wc.words_:
             print("降噪后无剩余有效词汇，无法生成词云")
             return

        wc.to_file(output_image)
        print(f"词云图生成完毕！已保存至 {output_image}")

    except Exception as e:
         print(f"词云生成过程中发生错误: {e}")

if __name__ == "__main__":
    run_analyzer()