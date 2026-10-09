import streamlit as st
import pandas as pd

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Dữ liệu bảng điểm
data = {
    'Họ tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.5, 9.0, 7.0, 9.5, 8.0, 6.5, 9.0, 7.5, 8.0, 9.5],
    'Giữa kỳ':    [7.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Cuối kỳ':    [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0]
}
df = pd.DataFrame(data)
df['Tong_ket'] = (df['Chuyên cần']*0.2 + df['Giữa kỳ']*0.3 + df['Cuối kỳ']*0.5).round(2)

def xep_loai(d):
    if d >= 8.5: return 'Giỏi'
    elif d >= 7.0: return 'Khá'
    elif d >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 2. Hiển thị bảng điểm
st.subheader("Bảng điểm")
st.dataframe(df)

# 3. Thống kê
st.subheader("Thống kê")
st.write("Điểm trung bình lớp:", round(df['Tong_ket'].mean(), 2))
st.write("SV cao nhất:", df.loc[df['Tong_ket'].idxmax()]['Họ tên'])
st.write("SV thấp nhất:", df.loc[df['Tong_ket'].idxmin()]['Họ tên'])
st.write("Số SV đạt:", (df['Tong_ket'] >= 5.0).sum())

# 4. Xem chi tiết từng sinh viên
st.subheader("Xem chi tiết sinh viên")
ten = st.selectbox("Chọn sinh viên:", df['Họ tên'])
sv = df[df['Họ tên'] == ten].iloc[0]
st.write(f"Chuyên cần: {sv['Chuyên cần']} | Giữa kỳ: {sv['Giữa kỳ']} | Cuối kỳ: {sv['Cuối kỳ']} | Tổng kết: {sv['Tong_ket']} | Xếp loại: {sv['Xep_loai']}")

# 5. Biểu đồ điểm (Dùng biểu đồ cột có sẵn của Streamlit)
st.subheader("Biểu đồ điểm tổng kết")
chart_data = df.set_index('Họ tên')['Tong_ket']
st.barh_chart(chart_data, horizontal=True)
st.caption("Người thực hiện: Hoàng Nguyễn Thế Công - MSSV:030208014434")
