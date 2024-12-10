import requests
from bs4 import BeautifulSoup
import streamlit as st

# Streamlitアプリのタイトル
st.title('Python公式ブログの最新記事')
st.markdown('[Visit Python Blogs](https://www.python.org/blogs/)', unsafe_allow_html=True)
st.image('scraping_demo.png', width=600)

# データ取得関数
def fetch_blog_titles():
    url = 'https://www.python.org/blogs/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3')
        return [title.get_text(strip=True) for title in titles]
    else:
        st.error(f'ページの取得に失敗しました。ステータスコード: {response.status_code}')
        return []

# ボタンが押されたときにデータを取得
if st.button('最新記事を取得'):
    with st.spinner('データを取得中...'):
        titles = fetch_blog_titles()
        if titles:
            st.success('データの取得に成功しました。')
            for idx, title in enumerate(titles, start=1):
                st.write(f"{idx}. {title}")
        else:
            st.warning('記事が見つかりませんでした。')
