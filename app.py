import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="달달한 연애상담소", page_icon="💖")
st.title("💖 달달한 연애상담소")
st.caption("연애 고민, 썸, 이별 이야기까지 무엇이든 편하게 이야기해보세요.")

# 2. 시스템 인스트럭션 설정 (챗봇의 페르소나/주제 변경 시 이 부분을 수정하세요)
SYSTEM_INSTRUCTION = """
당신은 따뜻하고 공감 능력이 뛰어난 전문 연애 상담사입니다.
사용자의 연애 고민(썸, 연애, 이별, 인간관계 등)을 듣고 친구처럼 다정하게 공감해주며, 
때로는 현명하고 객관적인 조언을 제공해야 합니다.
답변은 너무 길지 않고 친근한 말투(반말이나 존댓말 중 자연스러운 톤앤매너)로 작성해주세요.
"""

# 3. Streamlit Secrets에서 API 키 불러오기 및 초기화
try:
    # Streamlit Cloud 환경 또는 로컬 .streamlit/secrets.toml 환경에서 키를 가져옵니다.
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("API 키를 찾을 수 없습니다. Streamlit Secrets에 'GEMINI_API_KEY'를 설정해주세요.")
    st.stop()

# 4. 세션 상태(Session State)로 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. 기존 채팅 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 6. 사용자 입력 및 챗봇 답변 처리
if user_input := st.chat_input("고민을 이야기해주세요..."):
    # 사용자 메시지 저장 및 화면 표시
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 챗봇 답변 생성 및 화면 표시
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # gemini-2.5-flash-lite 모델 설정
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash-lite",
                system_instruction=SYSTEM_INSTRUCTION
            )
            
            # API 요청을 위한 대화 기록 포맷 변환 (Gemini 형식에 맞춤)
            chat_history = []
            for msg in st.session_state.messages[:-1]: # 현재 입력 직전까지의 기록
                role = "user" if msg["role"] == "user" else "model"
                chat_history.append({"role": role, "parts": [msg["content"]]})
            
            # 대화 시작 및 답변 생성
            chat = model.start_chat(history=chat_history)
            response = chat.send_message(user_input)
            
            # 답변 출력 및 저장
            ai_response = response.text
            message_placeholder.write(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception as e:
            # API 오류 및 기타 예외 처리
            error_msg = f"죄송합니다. 답변을 생성하는 중 오류가 발생했습니다. (오류 내용: {str(e)})"
            message_placeholder.write(error_msg)
