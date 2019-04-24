from django.shortcuts import render


#SEND THE REWARD UUID AND CUSTOMER UUID TO THIS FUNCTION TO VALIDATE THE REWARD AND CUSTOMER AND REDEEM
#SO A SEPERATE FUNCTION TO GATHER DATA TO SEND TO THIS FUNCTION

def RedeemReward(request, content_uuid, customer_uuid, store_uuid):
    try:
        reward = Reward.objects.get(uuid=content_uuid)
        customer = Customer.objects.get(uuid=customer_uuid)
        if reward in customer.rewards:
            if reward.criteria.expires > datetime.today():
                if reward.criteria.single_use == 'True':
                    customer.rewards.remove(reward)
                    customer.used_rewards.add(reward)
                    return Response({'outcome':'rewards was validate and successfully used'})
                else:
                    return Response({'outcome':'rewards was validate and successfully used'})
            else:
                customer.rewards.remove(reward)
                return Response({'outcome':'reward is expired and can no longer be redeem and has been removed'})
        else:
            return Response({'outcome':'reward can not be applied to this customer'})
    except Reward.DoesNotExist:
        raise Http404('cannot find reward')


def validateReward(request):
    pass
