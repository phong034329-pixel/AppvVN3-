import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
st.set_page_config(
    page_title="Quản lý chi tiêu cá nhân",
    layout="wide"
)
st.title("💰 Quản lý chi tiêu cá nhân")
st.markdown("""
Ứng dụng giúp:
- Ghi lại khoản thu
- Ghi lại khoản chi
- Thống kê
- Biểu đồ
- Xuất Excel
""")
# ==========================
# Session State
# ==========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Ngày",
        "Loại",
        "Danh mục",
        "Số tiền",
        "Ghi chú"
    ])
# ==========================
# Sidebar
# ==========================
st.sidebar.header("➕ Thêm giao dịch")
date = st.sidebar.date_input(
    "Ngày",
    datetime.today()
)
transaction_type = st.sidebar.selectbox(
    "Loại",
    ["Thu", "Chi"]
)

category = st.sidebar.selectbox(
    "Danh mục",
    [
        "Ăn uống",
        "Đi lại",
        "Lương",
        "Mua sắm",
        "Giải trí",
        "Tiền điện",
        "Tiền nước",
        "Tiền mạng",
        "Khác"
    ]
)

amount = st.sidebar.number_input(
    "Số tiền",
    min_value=0,
    step=1000
)

note = st.sidebar.text_input(
    "Ghi chú"
)

if st.sidebar.button("Lưu"):

    new_row = {
        "Ngày": str(date),
        "Loại": transaction_type,
        "Danh mục": category,
        "Số tiền" : amount,
        "Ghi chú" : note
    }

    st.session_state.data = pd.concat(
        [
            st.session_state.data,
            pd.DataFrame([new_row])
        ],
        ignore_index= True
    )

    st.success("Đã lưu giao dịch!")

# ========================================
# data
# ========================================

df = st.session_state.data

st.header("Danh sách giao dịch")

st.dataframe(
    df,
    use_container_width=True
)
#==========================
#Xóa giao dịch
#==========================

st.header("Xóa giao dịch")
if len(df) > 0:

    row = st.selectbox(
        "Chọn dòng cần xóa",
        df.index
    )

    if st.button("Xóa giao dịch"):

        st.session_state.data = (
            st.session_state.data
            .drop(row)
            .reset_index(drop=True)
        )

        st.success("Đã xóa thành công")
        st.rerun()
#=======================================
# Bộ lọc
#=======================================

st.header("bộ lọc")
col1, col2 = st.columns(2)

with col1:

    filter_type = st.selectbox(
        "loại",
        ["Tất cả", "Thu", "Chi"]
    )

with col2:

    categories = ["Tất cả"] + list(df["Danh mục"].unique())

    filter_category = st.selectbox(
        "Danh mục",
        categories
    )

filtered_df = df.copy()

if filter_type != "Tất cả":
    filtered_df = filtered_df[
        filtered_df["Loại"] == filter_type
    ]

if filter_category != "Tất cả":
    filtered_df = filtered_df[
        filtered_df["Danh mục"] == filter_category
    ]