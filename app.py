import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu
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

# Bảng điểm
st.subheader("Bảng điểm")
st.dataframe(df)

# Thống kê
st.subheader("Thống kê")
st.write("Điểm trung bình lớp:", round(df['Tong_ket'].mean(), 2))
st.write("SV cao nhất:", df.loc[df['Tong_ket'].idxmax()]['Họ tên'])
st.write("SV thấp nhất:", df.loc[df['Tong_ket'].idxmin()]['Họ tên'])
st.write("Số SV đạt:", (df['Tong_ket'] >= 5.0).sum())

# Chọn xem từng SV
st.subheader("Xem chi tiết sinh viên")
ten = st.selectbox("Chọn sinh viên:", df['Họ tên'])
sv = df[df['Họ tên'] == ten].iloc[0]
st.write(f"Chuyên cần: {sv['Chuyên cần']} | Giữa kỳ: {sv['Giữa kỳ']} | Cuối kỳ: {sv['Cuối kỳ']} | Tổng kết: {sv['Tong_ket']} | Xếp loại: {sv['Xep_loai']}")

# Biểu đồ
st.subheader("Biểu đồ điểm")
fig, ax = plt.subplots()
ax.barh(df['Họ tên'], df['Tong_ket'])
st.pyplot(fig)

# Thông tin tác giả ở cuối trang
st.caption("Người thực hiện: Hoàng Nguyễn Thế Công - MSSV:030208014434")
