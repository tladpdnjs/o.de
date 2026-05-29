import streamlit as str

# 1. 앱 제목 및 소개
str.title("💖 AI 연애 코칭 룸")
str.subheader("당신의 연애 고민을 해결해 드립니다.")
str.write("현재 겪고 있는 고민의 유형을 선택하고, 조언을 얻어보세요!")

# 2. 사용자 입력 받기
category = str.selectbox(
    "어떤 고민이 있으신가요?",
    ["선택하세요", "짝사랑/썸", "연애 중/갈등", "이별/재회"]
)

user_question = str.text_input("자세한 고민을 한 줄로 적어주세요 (예: 카톡 답장이 너무 느려요...)")

# 3. '코칭 받기' 버튼 클릭 시 로직
if str.button("코칭 시작하기"):
    if category == "선택하세요" or not user_question:
        str.warning("⚠️ 고민 유형을 선택하고 질문을 입력해주세요!")
    else:
        str.success("💌 코치님의 맞춤 조언이 도착했습니다!")
        
        # 조건문으로 간단한 답변 매칭
        if category == "짝사랑/썸":
            str.info(f"🤔 '{user_question}'에 대한 조언:")
            str.markdown("""
            * **밀당보다는 당당함!** 상대방의 반응에 일희일비하기보다 나의 매력을 자연스럽게 보여주세요.
            * 선톡이나 가벼운 약속 제안으로 상대방의 마음을 살짝 떠보는 것을 추천합니다.
            """)
            
        elif category == "연애 중/갈등":
            str.info(f"🤔 '{user_question}'에 대한 조언:")
            str.markdown("""
            * **'너'가 아닌 '나'를 주어로 말해보세요.** (예: "너 왜 연락 안 해?" ❌ -> "나는 연락이 안 되면 걱정돼" ⭕)
            * 서운한 점은 감정이 가라앉은 후에 차분하게 대화로 풀어야 오해가 생기지 않습니다.
            """)
            
        elif category == "이별/재회":
            str.info(f"🤔 '{user_question}'에 대한 조언:")
            str.markdown("""
            * **지금은 자신에게 집중할 시간입니다.** 감정이 앞서서 먼저 연락하는 것은 독이 될 수 있습니다.
            * 상대방과 나 자신에게 충분한 생각의 시간을 준 뒤, 이성적으로 판단해도 늦지 않습니다.
            """)
