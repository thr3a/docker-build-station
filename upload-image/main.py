import os
import sys
import hashlib
from github import Github
from pathlib import Path


def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def main():
    if len(sys.argv) != 2:
        print("使用方法: python script.py <画像のパス>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print("指定されたファイルが見つかりません")
        sys.exit(1)

    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        print("GITHUB_TOKEN環境変数が設定されていません")
        sys.exit(1)

    g = Github(github_token)
    repo = g.get_repo("thr3a/images")

    file_hash = calculate_sha256(image_path)
    file_extension = Path(image_path).suffix
    new_filename = f"{file_hash}{file_extension}"

    with open(image_path, "rb") as file:
        content = file.read()

    try:
        repo.create_file(
            path=new_filename,
            message=f"Upload file {new_filename}",
            content=content,
            branch="master",
        )
        print(
            f"![image](https://cdn.jsdelivr.net/gh/thr3a/images@master/{new_filename})"
        )
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
