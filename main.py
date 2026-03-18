import spider
import analyzer
import time

def main():
    print("=" * 50)
    print("arXiv爬虫机器人启动")
    print("=" * 50)

    print("\n开始执行数据抓取与增量更新...")
    spider.run_spider()
    
    time.sleep(2) 

    print("\n开始执行近7天数据分析与可视化...")
    analyzer.run_analyzer()

    print("\n" + "=" * 50)
    print("全部执行完毕！")
    print("请前往 data/ 文件夹查看最新的 papers.csv 和 weekly_report.png")
    print("=" * 50)

if __name__ == "__main__":
    main()