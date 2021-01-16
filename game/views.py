from django.shortcuts import render, redirect, get_object_or_404
from .models import CardBattle
import random
from .forms import *
# Create your views here.

def main(request):
    return render(request, 'game/main.html')

def login(request):
    return render(request, 'game/login.html')



# for i in range(5):
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
            cardBattle.from_user_num = request.user.id
            # from_user_num으로 대응하는 게임번호를 찾을 수 있나?
            cardBattle.save()
        return redirect("game_list")

    else:
        form = AttackForm(initial=initial)
        ctx = {
            "form": form
        }
        return render(request, "game/game.html", ctx)
   

def game_alone(request):
    return render(request, 'game/game_alone.html')

def game_option(request):
    return render(request, 'game/game_option.html')

def ranking(request):
    return render(request, 'game/ranking.html')

def accept(request, pk):
    if request.method == "POST":
        cardBattle = CardBattle.objects.get(pk=pk)
        form = DefenseForm(request.POST).save()
        cardBattle.to_user_card_num = form.to_user_card_num
        cardBattle.save()

        # random_result()에 들어갈 인자 
        to_user_card_num = cardBattle.to_user_card_num
        from_user_card_num = cardBattle.from_user_card_num
        
        '''
        주목 여기 model 바꿔야 해요 (updown_choice뭐 이런거 하나 생성해야 함)
        '''
        # 여기에 랜덤으로 해야할듯??! ---> up_or_down ( 0 up / 1 down )
        cardBattle.to_user_result = random_result(to_user_card_num, from_user_card_num, 0)
        cardBattle.from_user_result = random_result(from_user_card_num, to_user_card_num, 0)

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
    


