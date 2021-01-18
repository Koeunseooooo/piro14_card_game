from django.shortcuts import render, redirect, get_object_or_404
from .models import CardBattle, Profile
import random
from django.contrib.auth.models import User 
from .forms import *
# Create your views here.

def main(request):
    return render(request, 'game/main.html')

def login(request):
    return render(request, 'game/login.html')

    
def ranking(request):
    users=User.objects.all()
    games_all=CardBattle.objects.all()

    all_user_points=[]
    each_user_points=[]

    # 이 알고리즘은 정말 최악이야.. 그냥 game view 에서 바로 update 하면될것을... 난 똥이야 ...
    for user in users:
        game_all_to = games_all.filter(to_user=user)
        game_all_from = games_all.filter(from_user=user)
        if game_all_to.exists() or game_all_from.exists():
            for game_to in game_all_to:
                all_user_points.append(game_to.to_user_point)
            for game_from in game_all_from :
                all_user_points.append(game_from.from_user_point)
            each_user_points.append(sum(all_user_points))
            all_user_points.clear()
    

    for user,each_user_point in zip(users, each_user_points) :
        Profile.objects.filter(user_me=user).update(sum_point=each_user_point)

    profiles=Profile.objects.all()
    profiles_order=profiles.order_by("-sum_point")

    num=[]
    for i in range(1,len(users)+1):
        num.append(i)

    for profile,n in zip(profiles_order, num) :
        Profile.objects.filter(user_me=profile.user_me).update(rank=n)
        
    ctx = {
        "users": users,
        "games" : games_all , 
        "ranking" : profiles_order ,

    }
    # each도 clear해야하는지..
    return render(request, 'game/ranking.html', ctx)

def game_list(request):
    game_list = CardBattle.objects.all()
    game_list_filter = game_list.filter(to_user=request.user) | game_list.filter(from_user=request.user)
    ctx = {
        "game_list": game_list_filter.order_by("-id"),
        "current_user": request.user,
    }
    return render(request, 'game/game_list.html', ctx)

def game(request):
    initial = {
        "current_user": request.user.id
    }
    if request.method == "POST":
        form = AttackForm(request.POST, initial=initial)
        if form.is_valid():
            cardBattle=form.save()
            cardBattle.from_user = request.user
            cardBattle.result = "진행중..."
            # cardBattle.from_user_num = request.user.id
            # from_user_num으로 대응하는 게임번호를 찾을 수 있나?
            # 왜 하는 거임 이거 ???
            cardBattle.save()
        return redirect("game_list")

    else:
        form = AttackForm(initial=initial)
        ctx = {
            "form": form
        }
        return render(request, "game/game.html", ctx)
   

def accept(request, pk):
    if request.method == "POST":
        cardBattle = CardBattle.objects.get(pk=pk)
        form = DefenseForm(request.POST).save()
        cardBattle.to_user_card_num = form.to_user_card_num
        cardBattle.save()

        # random_result()에 들어갈 인자 
        to_user_card_num = cardBattle.to_user_card_num
        from_user_card_num = cardBattle.from_user_card_num
        
       
        # 여기에 랜덤으로 해야할듯??! ---> up_or_down ( 0 up / 1 down )
        cardBattle.up_or_down = random.randint(0, 2)
        up_or_down=cardBattle.up_or_down
        if up_or_down == 0 :
            cardBattle.game_option= " 숫자가 더 큰 사람이 대결에서 이깁니다 "
        else :
            cardBattle.game_option= " 숫자가 더 작은 사람이 대결에서 이깁니다"
        

        
        
        cardBattle.to_user_result = random_result(to_user_card_num, from_user_card_num, up_or_down) 
        cardBattle.from_user_result = random_result(from_user_card_num, to_user_card_num, up_or_down)

        # save_point
        if cardBattle.to_user_result == "승리" :
                cardBattle.to_user_point = to_user_card_num
                cardBattle.from_user_point = -(from_user_card_num)
        elif cardBattle.to_user_result == "패배" :
            cardBattle.to_user_point = -(to_user_card_num)
            cardBattle.from_user_point = from_user_card_num
        else : # 무승부
            cardBattle.to_user_point = to_user_card_num
            cardBattle.from_user_point = from_user_card_num


        cardBattle.save()
        form.delete() 

        return redirect("detail", pk=pk)

    else:
        form = DefenseForm()
        game = CardBattle.objects.get(pk=pk)
        ctx = {
            "form": form,
            "game": game,
        }
        return render(request, "game/accept.html", ctx)

def detail(request, pk):
    game = CardBattle.objects.get(pk=pk)
    ctx = {
        "game": game,
        "current_user": request.user
    }
    return render(request, "game/detail.html", ctx)

def delete(request, pk):
    game = CardBattle.objects.get(pk=pk)
    if request.method == "POST":
        game.delete()
    return redirect("game_list")


def random_result(user1,user2,choice):
    if choice==0:
        if user1==user2:
            return "비김"
        elif user1>user2:
            return "승리"
        else :
            return "패배"
    else :
        if user1==user2:
            return "비김"
        elif user1>user2:
            return "패배"
        else :
            return "승리"
    


