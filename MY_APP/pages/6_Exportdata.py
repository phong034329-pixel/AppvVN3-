import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.set_page_config(page_title="Xuất dữ liệu online ra Excel", layout="wide")
st.title("Lấy dữ liệu online và xuất ra online")
st.markdown("Ứng dụng lấy dữ liệu online và cho phép tải file excel")
#Hàm lấy dữ liệu online
def load_data():
    url ="https://api.gold-api.com/price/XAU"
    respond = requests.get(url)
    data = respond.json()
    rows = [{
        "Loại vàng": data.get("metal", "XAU"),
        "Gía hiện tại": data.get("price", 0),
        "Đơn vị tiền": data.get("currency", "USD"),
        "Sàn giao dịch": data.get("exchange", "Global"),
        "Thời gian cập nhật": data.get("timestamp", "N/A")
    }]
    return pd.DataFrame(rows)
##############################################################
#hiển thị dữ liệu
df = load_data()
st.subheader("dữ liệu online")
st.dataframe(df, use_container_width=True)

#=================
#Tiềm kiếm
st.subheader("Dữ liệu giá vàng")
filtered_df = df
st.dataframe(filtered_df, use_container_width=True)

#xuất dữ liệu
def convert_to_excel(dataframe):
    output = BytesIO()
    with pd.ExcelWriter(output, engine = "openpyxl") as write:
        dataframe.to_excel(write, index = False, sheet_name = 'Data')
    processed_data = output.getvalue()
    return processed_data
excel_data = convert_to_excel(filtered_df)

st.download_button(
    label = "Tải dữ liệu file excel",
    data = excel_data,
    file_name="Du_lieu_online.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
st.title("Phân tích tỷ giá USD/VND")
@st.cache_data(ttl=10)
def load_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response=requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"]["VND"]
    return None
exchange_rate = load_exchange_rate()
if exchange_rate:
    st.metric(
        label="1 USD",
        value = f"{exchange_rate:,.0f} VND"
    )
    st.caption("Tự động cập nhật 10 giây")
    usd_amount = st.number_input(
        "Nhập số USD",
        min_value=1.0,
        value = 1.0,
        step = 1.0
    )
    vnd_value = usd_amount * exchange_rate
    st.success(
        f"{usd_amount:,.2f} USD = {vnd_value:,.0f} VND"
    )
else:
    st.error("Không thể tải tỷ giá.")

st.header("Lịch sử USD/VND qua các năm")
history_data = {
    "Năm": [1985, 1990, 1995, 2000, 2005, 2010,
            2015, 2020, 2023, 2024, 2025, 2026],

    "Tỷ giá": [15, 6500, 11000, 14000, 15800, 19000,
               22500, 23200, 23800, 25000, 26000, 26300],

    "Nhận xét": [
        "Sau đổi tiền",
        "Lạm phát rất cao",
        "Bắt đầu ổn định hơn",
        "Kinh tế mở cửa mạnh",
        "Tăng chậm",
        "Áp lực phá giá VND",
        "USD mạnh lên toàn cầu",
        "Khá ổn định",
        "USD tăng mạnh hậu COVID",
        "VND mất giá khá nhanh",
        "Lập đỉnh mới",
        "Dao động quanh 26.3k"
    ]
}
df = pd.DataFrame(history_data)
df = pd.DataFrame(history_data)
st.dataframe(df, use_container_width=True)

#Table
st.header("Biểu đồ mất giá của VND")
chart_df = df.set_index("Năm")
st.line_chart(chart_df["Tỷ giá"])

#Analysis
st.header("Nhận xét xu hướng")
st.markdown("""
# Giai đoạn từ 1985 đến 1995
- VND mất giá cực mạnh do lạm phát cao
- Sau khi đổi tiền, tỷ giá tăng cao từ khoảng 15 lên hơn 11000VND/USD

# giai đoạn từ 2000 - 2015
Việt Nam mở cửa kinh tế mạnh hơn"""
)
start_rate = df["Tỷ giá"].iloc[0]
end_rate = df["Tỷ giá"].iloc[-1]
increase = end_rate / start_rate
st.warning(
    f"Từ 1985 đến 2026, USD tăng khoảng {increase:.0f} lần so với VND"
)
df = pd.DataFrame(history_data)

st.subheader("Dữ liệu tỷ giá USD/VND")
st.dataframe(df,use_container_width = True)

st.header("Lịch sử giá bạc thế giới qua các năm")

silver_data = {
    "Năm": [
        1985, 1990, 1995, 2000, 2005, 2010,
        2015, 2020, 2023, 2024, 2025, 2026
    ],
    "Giá bạc (USD/oz)": [
        6.0, 5.0, 5.2, 5.0, 7.3, 20.2,
        15.7, 20.5, 25.0, 35.0, 55.0, 57.75
    ],
    "Nhận xét": [
        "Giai đoạn giá thấp",
        "Ổn định",
        "Đi ngang",
        "Vùng đáy dài hạn",
        "Bắt đầu tăng",
        "Bùng nổ sau khủng hoảng",
        "Điều chỉnh",
        "Hồi phục mạnh",
        "Nhu cầu công nghiệp tăng",
        "Xu hướng tăng mạnh",
        "Phá đỉnh nhiều năm",
        "Lập đỉnh mới"
    ]
}

df = pd.DataFrame(silver_data)
st.dataframe(df, use_container_width=True)

#Biểu đồ
st.subheader("Biểu đồ bạc thế giới")

chart_df = df.set_index("Năm")
st.line_chart(chart_df["Giá bạc (USD/oz)"])

# Phân tích về xu hướng
st.header("Nhận xét xu hướng")

st.markdown("""
### Giai đoạn từ 1985 - 2005
- Giá bạc duy trì ở vùng thấp trong nhiều năm
- Nguyên cung khá dồi dào
- Nhu cầu công nghiệp chưa bùng nổ

### Giai đoạn 2005 - 2015
- Khủng hoảng tài chính 2008 thúc đẩy nhu cầu tài sản trú ẩn
- Giá bạc tăng mạnh từ 7 USD lên hơn 20 USD/oz
- Có thời điểm vượt 40 USD/oz trong năm 2011

### Giai đoạn 2020 - 2026
- Chính sách tiền tệ nới lỏng hậu COVID
- Nhu cầu sản xuất pin mặt trời và điện tử tăng cao
- Bạc trở thành kim loại hưởng lợi từ xu hướng năng lượng xanh
- Duy trì giá trên vùng 30 USD/oz
""")
start_price = df["Giá bạc (USD/oz)"].iloc[0]
end_price = df["Giá bạc (USD/oz)"].iloc[-1]

st.success(
    f"✨ Từ 1985 đến 2026, giá bạc tăng khoảng {increase:.1f} lần"
)

st.header("Lịch sử giá vàng Việt Nam (1985-2026)")

history_data = {
    "Năm": [
        1985, 1990, 1995, 2000,
        2005, 2010, 2015, 2020,
        2021, 2022, 2023, 2024,
        2025, 2026
    ],

    # đơn vị VND/lượng
    "Giá vàng": [
        15_000,
        500_000,
        5_200_000,
        7_000_000,
        8_700_000,
        26_500_000,
        35_000_000,
        56_000_000,
        61_000_000,
        67_000_000,
        74_000_000,
        85_000_000,
        95_000_000,
        191_000_000
        ],
    "Nhận xét": [
        "ước tính thời bao cấp",
        "Lạm phát cao",
        "Thị trường ổn định hơn",
        "Kinh tế tăng trưởng",
        "Tăng chậm",
        "Chu kì tăng mạnh",
        "Ổn định quanh 35 triệu",
        "Covid-19",
        "Duy trì mức cao",
        "Tiếp tục tăng",
        "Biến động nhanh",
        "Lập mặt bằng giá mới",
        "Tiếp tục tăng",
        "Có thời điểm gần 191 triệu",
    ]
}

gold_df = pd.DataFrame(history_data)
# Hiển thị bảng giá
st.dataframe(gold_df, use_container_width=True)
# Biểu đồ
st.subheader("Biểu đồ giá vàng qua các năm")
G_chart_df = gold_df.copy()
G_chart_df["Giá vàng (triệu đồng/lượng)"] = (
    G_chart_df["Giá vàng"] / 1_000_000
)

st.line_chart(
    G_chart_df.set_index("Năm")["Giá vàng (triệu đồng/lượng)"]
)

# Thống kê
st.subheader("Thống kê nhanh")
col1, col2, col3 = st.columns(3)
price_1985 = gold_df.iloc[0]["Giá vàng"]
price_2026 = gold_df.iloc[-1]["Giá vàng"]

with col1:
    st.metric(
        "Giá năm 1985",
        f"{price_1985:,.0f} VND/lượng",
    )

with col2:
    st.metric(
        "Giá năm 2026",
        f"{price_2026 / 1_000_000:.1f} triệu VND/lượng",
    )
with col3:
    growth =  price_2026 / price_1985
    st.metric(
        "Tăng so với 1985",
        f"{growth:,.0f} lần"
    )
 # Phân tích
st.header("Nhận xét xu hướng")
st.markdown("""
### Giai đoạn từ 1985 - 1995
- Giá vàng còn ở mức thấp theo mặt bằng tiền tệ thời kỳ bao cấp và đầu thời kỳ đổi mới.
- Lạm phát cao khiến sức mua và giá trị đồng tiền biến động mạnh.
- Các số liệu giai đoạn này chủ yếu mang tính chất tham khảo.

### Giai đoạn từ 2000 - 2010
- Giá vàng tăng dần cùng với sự phát triển của nền kinh tế.
- Ảnh hưởng từ xu hướng tăng của thị trường vàng thế giới.
            """)   