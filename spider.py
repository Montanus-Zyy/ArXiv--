import arxiv
import pandas as pd
import os

def run_spider(): 
    csv_file = "data/papers.csv"
    existing_ids = set()

    if os.path.exists(csv_file):
        df_existing = pd.read_csv(csv_file)
        existing_ids = set(df_existing['entry_id'].astype(str))
        print(f"本地仓库已有 {len(existing_ids)} 篇历史论文")
    else:
        print("正在创建本地仓库...")

    print("正在向 arXiv 请求最新的 50 篇 Agent 论文...")
    client = arxiv.Client()
    search = arxiv.Search(
        query="cat:cs.AI AND all:agent",
        max_results=50,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    new_papers = []

    for paper in client.results(search):
        paper_id = paper.entry_id
        if paper_id in existing_ids:
            continue

        paper_data = {
            "entry_id": paper_id,
            "Title": paper.title.replace('\n', ' '),
            "Authors": ", ".join([author.name for author in paper.authors]),
            "Published_Date": paper.published.strftime("%Y-%m-%d %H:%M:%S"),
            "Summary": paper.summary.replace('\n', ' '),
            "PDF_Link": paper.pdf_url
        }
        new_papers.append(paper_data)

    if new_papers:
        print(f"发现 {len(new_papers)} 篇全新论文，正在追加写入本地仓库...")
        df_new = pd.DataFrame(new_papers)
        write_header = not os.path.exists(csv_file)
        df_new.to_csv(csv_file, mode='a', index=False, header=write_header, encoding='utf-8-sig')
        print("数据追加成功！")
    else:
        print("最新 50 篇已存在于本地仓库，无需追加")

if __name__ == "__main__":
    run_spider()  