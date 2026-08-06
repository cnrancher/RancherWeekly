import os
import subprocess
import requests
from datetime import datetime  # 导入 datetime 模块

FORUM_URL = os.environ.get("RANCHER_FORUM_URL", "https://forums.rancher.cn").rstrip("/")
API_KEY = os.environ.get("RANCHER_FORUM_API_KEY")
API_USERNAME = os.environ.get("RANCHER_FORUM_USER")
CATEGORY_ID = int(os.environ.get("RANCHER_FORUM_CATEGORY", 0))

HEADERS = {
    "Api-Key": API_KEY,
    "Api-Username": API_USERNAME,
    "Content-Type": "application/json"
}

def get_changed_md_files():
    """获取本次 commit 新增或修改的 md 文件列表"""
    try:
        cmd = ["git", "diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd).decode("utf-8")
        files = output.splitlines()
        return [f for f in files if f.endswith(".md") and not f.startswith(".github")]
    except Exception as e:
        print(f"获取变更文件列表失败: {e}")
        return []

def publish_to_discourse(file_path):
    """提取 md 内容并在标题前自动拼接日期发布"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.strip().split("\n")
    raw_title = lines[0].lstrip("# ").strip() if lines else os.path.basename(file_path)
    body = "\n".join(lines[1:]).strip() if len(lines) > 1 else content

    # 1. 获取当前日期 (格式: YYYY-MM-DD)
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # 2. 拼接标题，形成：[2026-08-06] Rancher 社区双周报 | Harvester 双版本重磅发布...
    formatted_title = f"[{today_str}] {raw_title}"

    payload = {
        "title": formatted_title,
        "raw": body,
        "category": CATEGORY_ID
    }

    response = requests.post(f"{FORUM_URL}/posts.json", headers=HEADERS, json=payload)
    if response.status_code == 200:
        res_data = response.json()
        print(f" Successfully published: {file_path} -> Title: {formatted_title}")
    else:
        print(f" Failed to publish {file_path}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    if not CATEGORY_ID:
        print("警告: 未检测到有效的 RANCHER_FORUM_CATEGORY 环境变量。")

    changed_files = get_changed_md_files()
    if not changed_files:
        print("没有可同步的 Markdown 文件变更。")
    else:
        for file in changed_files:
            print(f"正在同步: {file}")
            publish_to_discourse(file)