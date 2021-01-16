from allauth.account.utils import user_username, user_email, user_field
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import valid_email_or_none
from django.contrib.auth.models import UserManager as DefaultUserManager

'''
< 해당 파일의 기능 + 추가한 이유 >
해당 프로젝트는 소셜계정으로 로그인이 가능하도록 구성되어있다.
소셜로그인은 구글, 네이버, 카카오(는,,아직) 총 3개인데 각각 로그인한 유저의 필드명, 필드값이 
다르게 저장되어 있음을 알 수 있다.

예) 구글 로그인은 first_name과 last_name이라는 필드명 존재
예) 네이버 로그인은 위의 필드명이 존재하지 않음. username또한 따로 지정해주지 않으면
    네이버 닉네임이 들어가는 것이 아니라 uesr N 형식으로 들어가기 때문에 식별하기 어려움(헷갈림). 이건 구글도 마찬가지

결국 하고 싶은 말은, 구글/네이버/카카오가 주는 프로필 정보가 달랐기 때문에 이를 입맛에 맞게 조정하여 
통일성을 갖추도록 user.save()를 진행하고 싶었다!!

필수 선택은 아니나, 구글로그인했을때 은서 고 -> 고은서 이렇게 바꾸고 싶었고, 
user1 -> 고은서 이렇게 바꿔야 유저이름의 통일성을 갖출 수 있다고 생각했기에.. 생성한 파일!

https://whatisthenext.tistory.com/130 <= 해당 블로그 참고하였음


- 2021 1월 15일 금요일 : 카카오 로그인 구현 5시간 삽질하다 최종 error 해결 못해서 현타오니 이따 할거임..
'''


