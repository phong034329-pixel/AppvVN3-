import streamlit as st
import feedparser

st.header("TIN TUC MOI NHAT")
tabA, tabB, tabC = st.tabs(["TIN TUC MOI NHAT", "Gia Vang","the thao"])
with tabA:
        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

with tabB:
    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_value = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "Giá vàng" in entry.summary.lower()]
        
    if gold_value:
        for entry in gold_value[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
            st.warning("khong tim thay gia vang hien nay")
with tabC:
        feed =  feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")
        for entry in feed.entries[:10]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
