from django.contrib.auth import models
from django.db.models import Sum
from rest_framework import serializers
from store.models import Box
from django.contrib.auth.models import User
import datetime


def Area_validator(validated_data,user_id):
    l,w,h=int(validated_data['length']),int(validated_data['width']),int(validated_data['height'])
    validated_data['volume']=l * w * h
    validated_data['area']=2*(l * w + w * h + l * h)
    TotalArea=Box.objects.aggregate(Sum('area'))
    if TotalArea['area__sum']:
        Area=TotalArea['area__sum']
    else:
        Area=0
    number_of_boxes=len(Box.objects.all())+1
    average=(Area+validated_data['area'])/number_of_boxes
    return average


def Volume_validator(validated_data,user_id):
    if user_id!=-1:    
        id_user=Box.objects.filter(id=user_id).values('user')[0]
        original_user=User.objects.get(id=id_user['user'])
    elif user_id==-1:
        original_user=user_id
    l,w,h=int(validated_data['length']),int(validated_data['width']),int(validated_data['height'])
    validated_data['volume']=l * w * h
    validated_data['area']=2*(l * w + w * h + l * h)
    TotalVolume=Box.objects.filter(user=original_user).aggregate(Sum('volume'))
    if TotalVolume['volume__sum']:
        Volume=TotalVolume['volume__sum']
    else:
        Volume=0
    number_of_boxes=len(Box.objects.filter(user=original_user))+1
    average=(Volume+validated_data['volume'])/number_of_boxes
    return average


def Week_validator(validated_data,user_id):
    original_user=validated_data['user']
    days={'Monday':1,'Tueday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    today_date=datetime.date.today()
    today_day=today_date.strftime("%A")
    delta=days[today_day]-days['Monday']
    days=datetime.timedelta(delta)
    start_week_date=today_date-days
    total_boxes=Box.objects.filter(created_on__range=[start_week_date,today_date])
    boxes_by_user=total_boxes.filter(user=original_user)
    number_of_boxes=len(total_boxes)
    number_of_user_boxes=len(boxes_by_user)
    if number_of_boxes>100 and number_of_user_boxes>50:
        return True
    else:
        return False



class ShowBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box
        fields=['id','area','volume','length','width','height','created_on',
                'last_modified_on','user','last_modified_by',]


        
class ShowMyBoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box
        fields=['id','area','volume','length','width','height','created_on',
                'last_modified_on','user','last_modified_by',]
        


class EditBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box
        fields=['id','length','width','height','created_on',
                'last_modified_on']
    
    
    def update(self, instance, validated_data):
        id=self.instance.id
        if Area_validator(validated_data,id)>100 and Volume_validator(validated_data,id)>1000:
            raise serializers.ValidationError("Average volume/area limit exceeded")
        else:
            return super().update(instance,validated_data)

     
class DeleteBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box
        fields=['id','area','volume','length','width','height','created_on',
                'last_modified_on','user','last_modified_by']
    
       
class AddBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box
        fields=['id','length','width','height','created_on','last_modified_on']
        
    def create(self, validated_data):
        if Week_validator(validated_data,-1):
            raise serializers.ValidationError("Number of boxes added in a week exceeded")
        elif Area_validator(validated_data,-1)>100 or Volume_validator(validated_data,-1)>1000:
            raise serializers.ValidationError("Average volume/area limit exceeded")
        else:
            return super().create(validated_data)
        
        
