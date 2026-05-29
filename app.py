import streamlit as st

# 제목
st.title("💖 심리 고민 상담 앱")

# 설명
st.write("편하게 고민을 적어보세요.")

# 세션 상태 만들기
if "chat" not in st.session_state:
    st.session_state.chat = []

# 감정 선택
emotion = st.selectbox(
    "지금 기분은 어떤가요?",
    ["🙂 보통", "😢 슬픔", "😡 화남", "😰 불안", "😊 행복"]
)

# 고민 입력
user_input = st.text_area("고민 입력", height=150)

# 상담 버튼
if st.button("상담받기"):

    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:

        # 간단한 답변 생성
        if "힘들" in user_input or "우울" in user_input:
            answer = "많이 힘들었겠어요. 혼자 너무 참지 않아도 괜찮아요."
        
        elif "친구" in user_input:
            answer = "친구 관계는 누구에게나 어려울 수 있어요. 너무 자신을 탓하지 마세요."

        elif "공부" in user_input:
            answer = "지금 당장 완벽하지 않아도 괜찮아요. 조금씩 해나가면 돼요."

        else:
            answer = "당신의 마음은 충분히 소중해요. 천천히 이야기해봐요."

        # 대화 저장
        st.session_state.chat.append(
            {
                "emotion": emotion,
                "question": user_input,
                "answer": answer
            }
        )

# 대화 기록 출력
st.subheader("🗂 상담 기록")

for chat in reversed(st.session_state.chat):
    st.write(f"기분: {chat['emotion']}")
    st.write(f"고민: {chat['question']}")
    st.success(chat['answer'])
    st.write("---")
