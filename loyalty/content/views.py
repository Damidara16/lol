from django.shortcuts import render
from .models import Reward, Deal
from rest_framework.generics import ListAPIView

class ListReward(ListAPIView):
    serializer_class = RewardSerializer
    queryset = Reward.objects.filter(store=request.user.store)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RewardSerializer(queryset, many=True)
        return Response(serializer.data)

def CreateReward(request):
    if request.method == 'POST':
        form1 = RewardCreationForm(request.POST)
        form = CriteriaCreationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            reward = form.save(commit=False)
            form1.save()
            reward.criteria = form1
            reward.save()
            return redirect(reverse('home:home'))
        else:
            return render
    else:
        form1 = RewardCreationForm()
        form = CriteriaCreationForm()
        return render(request, 'content/create.html', {'form':form, 'form1':form1})
        
def DeleteReward(request):
    if request.method == 'POST':
        form = RewardCreationForm(request.POST)
        form = CriteriaCreationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            reward = form.save(commit=False)
            form1.save()
            reward.criteria = form1
            reward.save()
            return ...
        else:
            return ...

class ListDeal(ListAPIView):
    serializer_class = DealSerializer
    queryset = Deal.objects.filter(store=request.user.store)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DealSerializer(queryset, many=True)
        return Response(serializer.data)

def CreateDeal(request):
    if request.method == 'POST':
        form = RewardCreationForm(request.POST)
        form = CriteriaCreationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            reward = form.save(commit=False)
            form1.save()
            reward.criteria = form1
            reward.save()
            return ...
        else:
            return ...

def DeleteDeal(request):
    if request.method == 'POST':
        form = RewardCreationForm(request.POST)
        form = CriteriaCreationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            reward = form.save(commit=False)
            form1.save()
            reward.criteria = form1
            reward.save()
            return ...
        else:
            return ...
