from django.db import models
from django.contrib.auth.models import User 
import random
# Create your models here.

class Profile(models.Model):
    sum_point = models.PositiveIntegerField(default=0)
    

class CardBattle(models.Model):
    list = []
    ran_num = random.randint(1,10)
    for i in range(5):
        while ran_num in list :
            ran_num = random.randint(1,10)
        list.append(ran_num)

    CARD_CHOICES = (
        (list[0], list[0]),
        (list[1], list[1]),
        (list[2], list[2]),
        (list[3], list[3]),
        (list[4], list[4]),
    )
    # 10개 중 무작위 5개 선택 - 그 중 한 개 선택 )
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user", null=True, blank=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user",null=True, blank=True)
    from_user_num = models.IntegerField(null=True , blank=True)
    to_user_card_num = models.IntegerField( null=True, blank=True, choices=CARD_CHOICES)
    # to_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='to_user_rsp', null=True, blank=True)
    from_user_card_num = models.IntegerField( null=True, blank=True, choices=CARD_CHOICES)
    # from_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='from_user_rsp', null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    # 진행중 표시를 위한 result
    to_user_result = models.CharField(max_length=255, null=True, blank=True)
    # 게임 종료후 result
    from_user_result = models.CharField(max_length=255, null=True, blank=True)
    # 게임 종료후 result
    to_user_point = models.IntegerField(null=True, blank=True)
    # 게임 종료 후 포인트
    from_user_point = models.IntegerField(null=True, blank=True)
    # 게임 종료 후 포인트
    

    # from_user_num=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.to_user}에게 {self.from_user}가"