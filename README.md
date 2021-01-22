# piro14_card_game 💌
연합 웹 프로그래밍 동아리 피로그래밍 14기 마지막 팀과제 제작 결과물입니다.
****
## 1. 프로젝트 소개
>  피로그래밍 14기 마지막 팀과제 공지를 위해 제작된 웹사이트입니다. 12기 팀과제 주제였던 가위바위보 게임에서 아이디어를 발전시켜 웹 내에서 숫자카드게임을 진행할 수 있도록 구현하였습니다. </br></br> 게임방식은 단순하나, 다양한 기능을 갖추고 있습니다. 먼저, 소셜로그인 구현을 통해 유저 n이 로그인을 하면 유저는 다른 유저들을 선택하고 자신이 낼 숫자를 랜덤카드 중에서 고름으로써 게임을 시작할 수 있게 됩니다. 유저 n이 유저 m을 선택했다고 가정하고 유저m의 계정으로 웹사이트를 접속하면, 유저 n이 게임을 걸어온 것을 알 수 있습니다. 이때 유저 m은 해당 게임에 반격할 수 있으며, 이는 자신이 낼 숫자를 랜덤카드 중에서 고른다는 의미이기도 합니다. </br> 대결이 성사가 되었으니 게임 결과를 확인할 수 있습니다. 결과창을 통해 서로가 선택한 카드의 값과 결과, 그리고 게임에서 획득/차감 된 점수를 확인 할 수 있습니다. 각 게임별로 숫자가 큰 사람이 이길수도, 숫자가 작은 사람이 이길 수도 있습니다. 이는 랜덤입니다. 마지막으로 랭킹보기 기능을 통해 지금까지 진행된 모든 게임에서 얻은(잃은) 점수가 합산되어 유저별로 랭킹화되어 나타납니다. 

## 2. 개발환경
> Django, Python, HTML, CSS, SQLite

## 3. 실행 방법 설명
* 서버 접속하기까지 

```
  git clone https://github.com/Koeunseooooo/piro14_card_game.git .
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
* SECRET_KEY 관련 error에 관한 설정
```
  settings.py 파일 주석 설명 참고

  < 클론 후 단순 프로그램 실행을 하고 싶은 경우에 해당합니다 >
    1. setting.py 내 start~finish 내용을 주석처리
    2. SECRET_KEY = '.'  <- 왼쪽의 코드를 한 줄 추가
```

* 소셜로그인 관련 error에 관한 설정
```
  < runserver 후 소셜로그인 관련 error가 난 경우 >
    1. python manage.py createsuperuser -> admin페이지 접속
    2. 각 소셜로그인에 관한 자신의 API 값을 적용
```
  ( API값 설정 참고 ) https://egg-money.tistory.com/117  

## 4. 주요 기능 설명 
- 1 **메인 페이지**
  + 로그인 전/후의 화면이 상이함
  + 소셜로그인(네이버,구글) 후에는 nav-bar에 게임하기, 랭킹보기, 로그아웃 버튼 생성
  + 현재 로그인한 유저의 username 표기
> ![main화면 - 로그인 전](https://user-images.githubusercontent.com/65647080/105223347-ff3bc680-5b9e-11eb-9e92-f856996f0b47.GIF)
> ![main화면 - 로그인 후](https://user-images.githubusercontent.com/65647080/105223351-006cf380-5b9f-11eb-90d5-69fdf66535d5.GIF)

- 2 **공격하기 페이지** 
  + 1~10 사이의 숫자중 랜덤하게 5개의 숫자가 선택지로 보여짐. 그 중 하나의 숫자를 고름
  + 공격할 상대(다른 유저)를 고름
 
> ![공격하기 화면](https://user-images.githubusercontent.com/65647080/105223355-019e2080-5b9f-11eb-9acf-6e1865f3e693.GIF)

- 3 **반격하기 페이지** 
  + 공격당한 상대는 자신이 로그인하였을 때 반격할 수 있음
  + 위와 같이 카드를 고름

> ![반격하기](https://user-images.githubusercontent.com/65647080/105223359-0236b700-5b9f-11eb-8117-afb911dbf7ad.GIF)
  
- 4 **전적보기 페이지** 
  + 로그인한 유저가 공격하거나 공격당한(=반격해야하는) 게임의 목록을 볼 수 있음
  + 자신이 공격하였지만 상대가 반격을 안했을 경우 진행중...표시, 상대가 자신에게 공격한 게임은 대응하기 표시, 이미 끝이 난 게임은 결과화면이 중앙에 표기됨 (= 경우의 수가 3개 있는 꼴입니다.)

> ![전적보기](https://user-images.githubusercontent.com/65647080/105223360-0236b700-5b9f-11eb-98a0-f48b1e989f4f.GIF)

- 5 **게임디테일 페이지** 
  + 특정 하나의 게임에 대한 게임정보화면 구성
  + 게임 유형, 서로의 카드 숫자 값, 결과, 획득하거나 잃은 점수가 보여지게 됨

> ![게임 디테일](https://user-images.githubusercontent.com/65647080/105223354-01058a00-5b9f-11eb-8e33-9f650a75e05b.GIF)

- 6 **랭킹보기 페이지** 
  + 유저별로 지금껏 진행해온 게임의 점수를 모두 합산한 값이 랭킹화되어(=정렬되어) 나타남

> ![랭킹화면](https://user-images.githubusercontent.com/65647080/105223356-019e2080-5b9f-11eb-998f-bfdf6144ea96.GIF)


## 5. 만든이
> 고은서 ( 피로그래밍 13기 활동, 14기 운영진 교육팀 ) </br>