# piro14_card_game
연합 웹 프로그래밍 동아리 피로그래밍 14기 마지막 팀과제 제작 결과물


## 1. 프로젝트 소개
- 라이프기록 및 대시보드 열람 서비스
<br/>
<br/>
<br/>

## 2. 실행 방법

'''
git clone 어쩌구 .
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
'''

소셜로그인
'''
admin에서 클라이언트 키 값 설정 후 저장해야함
'''

<br/>

## 3. 주요 기능 설명 <br/>
- 1 **메인페이지** <br/><br/>
-각 주요 서비스에 대한 상세 설명<br/>
-각각의 서비스로 이동할 수 있는 상단 고정 메뉴바 존재<br/><br/><br/>

- 2 **마이페이지** <br/><br/>
  2-1)회원가입 및 로그인 ( 마이페이지 열람 전 ) <br/>
-로그인을 해야 열람 가능 : 웹서비스 내 자체 회원가입 및 구글소셜로그인 후, 프로필작성까지 완료시 완전한 로그인상태로 인정 <br/>
-프로필 작성 : 닉네임,직업,한줄메세지,관심분야,목표라이프뱃지개수 등록 가능 <br/>
-비밀번호 찾기 : 회원가입할때 입력했던 이메일 주소로 비밀번호 변경할 수 있는 메일이 가도록 구현 <br/><br/>
  2-2) 마이페이지<br/>
  -좌측 : 내가 설정한 프로필이 보여짐<br/>
  -우측 : 커뮤니티에서 내가 쓴 글만 최신포스팅순으로 정렬하여 나열됨<br/><br/><br/>

- 3 **캘린더** <br/><br/>
  -캘린더 : 이전달,다음달로 넘어갈 수 있도록 실제 달력과 유사하게 구현, 현월로 default되어있음<br/>
  -라이프기록 등록하기 : 라이프 제목, 라이프 시간, 라이프 카테고리, 라이프 뱃지(score) 등록 시 캘린더에 일정이 기록됨<br/>
  -일별 라이프기록 확인 : 우측에 일별 기록들과 라이프뱃지 total값을 한눈에 볼 수 있도록 정렬.<br/><br/><br/>
  
- 4 **대시보드** <br/><br/>
-대시보드는 지난 7일간 라이프기록이 7개 이상이여야 열람 가능함 <br/>
-한눈에 보기 : 대시보드 내 그래프를 한눈에 볼 수 있도록 그래프를 re-sizing하여 보여줌<br/><br/>
-통계그래프/메세지는 크게 7개로 구성됨 ( 아래 상세 설명 ) <br/>
-1) 이번달 라이프 현황: 프로필 설정 시 등록했던 목표라이프뱃지와 현재까지 모은 라이프뱃지 현황 확인 가능<br/>
-2) 뱃지 어디까지 모아봤니?: 현재 날짜로부터 지난 7일간 모든 라이프뱃지 개수를 일별로 나타냄 <br/>
-3) 지난 7일간 최고의 순간!: 라이프뱃지 total값이 가장 많았던 날을 보여줌 <br/>
-4) 내가 주로 즐기는 라이프는 뭐지?: 라이프뱃지 개수를 카테고리별로 정리하여 그래프로 나타냄 <br/>
-5) 아 궁금해 궁금해!: 라이프 뱃지 개수당 몇개의 라이프 기록을 줬는지 알 수 있음. 도넛그래프를 활용해 갯수당 비율 쉽게 측정 가능 <br/>
-6) oh!happyday!: weekday기준 ) 가장 라이프뱃지가 많았던 요일을 알 수 있음 <br/>
-7) 월별 라이프 비교: 지난달과 이번달의 일별 라이프기록을 한눈에 확인 가능. 총 뱃지 개수와 평균 뱃지 개수를 계산하여 저번달과 이번달을 비교하여 조건에 따라 각기 다른 메세지를 줄 수 있도록 함.br/>
<br/>

<br/><br/>
- 5 **커뮤니티**<br/><br/>
-자신의 라이프기록에 대한 사진기록 및 공유 커뮤니티 서비스<br/>
-사진은 포스팅한 시간순으로 나열, 게시물 30개 이상시 다음 페이지로 넘어가도록 구현<br/>
-글 등록하기: 게시물 제목 및 사진등록하여 업로드, 글쓰기 에디터기능 탑재 <br/>
-좋아요한 사진보기: 각 게시물에 대한 좋아요 버튼을 누르면 내가 좋아요한 사진들만 모아 볼 수 있는 기능 구현 (스크랩 기능과 실제 좋아요 기능 동시 구현)<br/>
-댓글달기: 각 게시물에 대한 댓글을 달 수 있음<br/>
-다른유저프로필페이지 보기: 다른 유저가 올린 게시물의 프로필을 누르면 내가 누른 유저의 프로필 페이지 열람 가능(유저의 관심분야와 닉네임,프로필 사진, 해당 유저가 쓴 글을 볼 수 있음)<br/>

<br/><br/><br/>

## 5. 만든이
> 고은서 ( 피로그래밍 13기 활동, 14기 운영진 교육팀 )
