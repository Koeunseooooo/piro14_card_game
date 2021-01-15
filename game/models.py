from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class CardBattle(models.Model):
    CARD_CHOICES = (
        ("가위", "가위"),
        ("바위", "바위"),
        ("보", "보"),
    )
    #  카드 섞는게 관건임 ( 카드 10장을 보여주고 4개 선택 - 그 중 한 개 선택 )
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user", null=True, blank=True)
    # from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user",null=True, blank=True)
    to_user_card_num = models.CharField(max_length=255, null=True, blank=True, choices=CARD_CHOICES)
    # to_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='to_user_rsp', null=True, blank=True)
    from_user_card_num = models.CharField(max_length=255, null=True, blank=True, choices=CARD_CHOICES)
    # from_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='from_user_rsp', null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    # 진행중 표시를 위한 result
    to_user_result = models.CharField(max_length=255, null=True, blank=True)
    # 게임 종료후 result
    from_user_result = models.CharField(max_length=255, null=True, blank=True)
    # 게임 종료후 result
    to_user_point = models.PositiveIntegerField(default=0)
    # 게임 종료 후 포인트
    from_user_point = models.PositiveIntegerField(default=0)
    # 게임 종료 후 포인트
    

    # from_user_num=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.to_user}에게 {self.from_user}가"