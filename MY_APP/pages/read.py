import streamlit as st
import pandas as pd
#=============================
#doc du lieu
#=============================
data = pd.read_csv("travel.csv")
#=============================
#tieu de
#=============================
st.title("Nhat ky chuyen di")
st.write("Danh sach cac chuyen di cua toi")
#=============================
#Hien thi du lieu
#=============================
st.subheader("Tat ca chuyen di")
st.dataframe(data)
#=============================
#Tong so chuyen di
#=============================
st.subheader("thong ke")
st.write("Tong so chuyen di:", len(data))
#=============================
#danh sach dia diem
#=============================
st.write("cac dia diem da di: ")
diadiem_list = data["diadiem"].unique()
st.write("dia diem list")
# =========================
# Chọn địa điểm
# =========================
st.subheader("🔎 Tìm kiếm chuyến đi")
diadiem = st.selectbox(
    "Chọn địa điểm:",
    diadiem_list
)
# =========================
# Lọc dữ liệu
# =========================
result = data[data["diadiem"] == diadiem]
# =========================
# Hiển thị kết quả
# =========================
st.write("cac chuyen di den", diadiem)
st.dataframe(result)
# =========================
# So chuyen di tai dia diem
# =========================
st.write(
    "So chuyen di:",
    len(result)
)