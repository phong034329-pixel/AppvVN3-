import streamlit as st
import random
import time

tabG, tabI, tabJ, tabK, tabL = st.tabs(["Game đoán số", "Game tung xúc xắc", "Game kéo búa bao","Đuổi hình bắt chữ","Gacha số"])
with st.sidebar:
    st.video("https://dn720301.ca.archive.org/0/items/rpreplay-final-1680875953/RPReplay_Final1680875953.mp4", autoplay=True, muted=True)
    with tabG:
        st.header("Game đoán số bí mật từ 1- 100")
        st.image("https://m.media-amazon.com/images/I/71Agu95C-jL._AC_UF894,1000_QL80_.jpg")
        st.write("luật chơi")
        st.write("đoán 1 số bất kì giữa 1 đến 100, nhập số để biết số chính xác lớn hơn hay nhỏ hơn,"
        "cố gắng đoán ít nhất có thể")
        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
        guess = st.number_input("Nhập số dự đoán 1- 100", min_value = 1, max_value = 100, step = 1)
        if st.button("Đoán !!!!!"):
            st.session_state.tries += 1
            if guess < st.session_state.secret:
                st.warning("😀 Số bí mật lớn hơn ")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            elif guess > st.session_state.secret:
                st.warning("😀 Số bí mật nhỏ hơn ")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            else:
                st.success(f"🏆 chính xác ! Bạn đoán đúng sau {st.session_state.tries} lần. ")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2pBfdCwgvKb7E8RBYkSluf3u3EdNxv54GuQ&s")
    with tabI:
        st.header("Game tung xúc xắc")
        st.write("luật chơi:" \
        "")
        st.write("Ấn lắc xúc xắc để quay ra số từ 1-6")
        if st.button("Lắc xúc xắc"):
            roll = random.randint(1,6)
            st.success(f"bạn ra được số {roll}")
            if roll == 1:
                st.image( 
                    "http://www.clker.com/cliparts/m/v/m/J/4/V/dice-1-md.png"
                ) 
            if roll == 2:
                st.image( 
                    "https://www.clker.com/cliparts/a/Y/E/o/z/t/dice-2-md.png"
                )
            if roll == 3:
                st.image(
                "https://www.clker.com/cliparts/O/I/r/9/W/x/dice-3-md.png"
                ) 
            if roll == 4:
                st.image(
                    "https://www.clker.com/cliparts/r/z/d/a/L/V/dice-4-md.png"
                ) 
            if roll == 5:
                st.image(
                    "https://www.clker.com/cliparts/U/N/J/F/T/x/dice-5-md.png"
                ) 
            if roll == 6:
                st.image(
                    "https://www.clker.com/cliparts/l/6/4/3/K/H/dice-6-md.png"
                )
    with tabJ:
        st.header("Kéo- Búa- Bao")
        st.image("https://static.tvtropes.org/trope_videos_transcoded/images/sd/q7uwxt.jpg")
        st.write("luật chơi: ")
        st.write("Bấm nút để ra kéo, búa, bao. Cố gắng để thắng con bot")
        st.write("Kéo thắng Bao")
        st.write("Búa thắng Kéo")
        st.write("Bao thắng Búa")
        user = st.selectbox("bạn chọn: ", ["kéo","búa","bao"])
        bot = random.choice(["kéo","búa","bao"])
        if st.button("ra tay !!!"):
            st.write(f"bot chọn ra {bot}")
            if user == bot:
                st.warning("hòa")
                st.image("https://i1.sndcdn.com/artworks-ecyyzfetWzmHLDpo-X7ICfQ-t500x500.jpg")
            elif (user == "kéo" and bot == "bao") or (user == "bao" and bot == "búa") or (user == "Búa" and bot == "kéo"):
                st.success("bạn thắng")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1MBsQ9GnV0RNq9b_rJA63UN8m4e0Xq6HpGQ&s")
            else:
                st.error("Bạn thua")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGlF-k_0Gsm39dJSSZCSEJUF-UsSkm_SAkHg&s")
    with tabK:
        st.header("Đuổi hình bắt chữ")

        puzzles = [
            {
                "image" : "https://cdn.lazi.vn/storage/uploads/dhbc/1469120972_tra-hoi.jpg",
                "Key": "Tra hỏi"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120797_khoa-so.jpg",
                "answer": "khóa sổ"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933422_xa-hoa.jpg",
                "answer": "Xa Hoa"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469011991_vai-tro.jpg",
                "answer": "Vai Trò"
            }, 
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469118011_tam-giac-can.jpg",
                "answer": "Tam Giác Cân"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120698_dan-bau.jpg",
                "answer": "Đàn Bầu"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120723_dien-anh.jpg",
                "answer": "Điện Ảnh"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120735_dong-co.jpg",
                "answer": "Động cơ"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120751_hau-cung.jpg",
                "answer": "Hậu cung"
            },
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120766_hau-dau.jpg",
                "answer": "Hậu đậu"
            }, 
            {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120813_sieu-nhan.jpg",
                "answer": "Siêu Nhân"
            },


        ]

        if "dhbc_index" not in st.session_state:
            st.session_state.scored = 0
            st.session_state.dhbc_index = random.randint(0,len(puzzles)-1)
            st.session_state.start_time = time.time()
            st.session_state.duration = 45
            st.session_state.finished = False
            st.session_state.result = ""
        score_box = st.empty()
        score_box.info(f"Điểm số của bạn là: {st.session_state.scored}")

        puzzle = puzzles[st.session_state.dhbc_index]
        st.image(puzzle["image"], width = 300)

        elapsed = int(time.time() - st.session_state.start_time)
        remaining = st.session_state.duration - elapsed

        if remaining > 0 and not st.session_state.finished:
            st.warning(f"Còn lại: {remaining} giây")
        else:
            st.session_state.finished = True
            st.error("Hết giờ")
        if remaining == 0:
            st.session_state.scored -=2

        Guess = st.text_input("nhập đáp án:", disabled = st.session_state.finished)

        if st.button("kiểm tra") and not st.session_state.finished:
            if Guess.lower().strip() == puzzle["answer"].lower():
                st.session_state.result = "correct"
                st.session_state.finished = True
                st.session_state.scored += 10
            else:
                st.session_state.result = "wrong"
                st.session_state.scored -= 2
            st.session_state.finished = True
            score_box.info(f"Điểm số của bạn là: {st.session_state.scored}")
            
        if st.session_state.result == "correct":
            st.success("Chính xác")
            st.balloons()
        elif st.session_state.result == "wrong":
            st.error("Sai")

        if st.session_state.finished and remaining <=0:
            st.info(f"đáp án đúng là:**{puzzle['answer']}**")

        if st.button("vòng mới"):
            st.session_state.dhbc_index = random.randint(0, len(puzzles)-1)
            st.session_state.start_time = time.time()
            st.session_state.finished = False
            st.session_state.result = ""
            st.rerun()
    with tabL:
        st.title("Gacha số may mắn")
        if "new_prizes" not in st.session_state:
            st.session_state.new_prizes = []
        if "weights" not in st.session_state:
            st.session_state.weigths = []

        st.subheader("thêm phần thưởng")
        col1, col2 = st.columns(2)
        with col1:
            new_prize = st.text_input("tên phần thưởng")
        with col2:
            weight = st.number_input(" tỷ lệ trúng (%)", 1, 100, 10)
        if st.button("thêm"):
            if new_prize:
                st.session_state.new_prizes.append(new_prize)
                st.session_state.weights.append(weight)
                st.success(f"Đã thêm: {new_prize}")
        
        st.subheader("danh sách phần thưởng")
        if st.session_state.new_prizes:
            for i, prize in enumerate(st.session_state.new_prizes):
                st.write(
                    f"{i+1}. {prize} | Tỷ lệ: {st.session_state.weights[i]}%"
                )
        else:
            st.info("Chưa có phần thưởng")

        st.subheader("Quay số")
        if st.button("Quay ngay"):
            if st.session_state.new_prizes:
                spin_placeholder = st.empty()

                for i in range(15):
                    spin_placeholder.markdown(
                        f"## Đang quay ... {random.choice(st.session_state.new_prizes)}"
                    )
                    time.sleep(0.1)

                result = random.choice(
                    st.session_state.new_prizes,
                    weights = st.session_state.weights,
                    k=1
                )[0]
                spin_placeholder.empty()

                st.balloons()
                st.success(f"Chúc mừng! Bạn trúng: **{result}**")

            else:
                st.warning("Chưa có phần thưởng")