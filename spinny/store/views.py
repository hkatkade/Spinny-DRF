from django.contrib.auth.models import Permission
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework import authentication
from store.models import Box
from store.serializer import AddBoxSerializer,EditBoxSerializer,ShowBoxSerializer,ShowMyBoxesSerializer,DeleteBoxSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import django_filters

class AddBox(generics.CreateAPIView):
    queryset=Box.objects.all()
    serializer_class=AddBoxSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    
    def perform_create(self, serializer):      
        serializer.save(user=self.request.user)
    
class FilterClass(django_filters.FilterSet):
    min_length = django_filters.NumberFilter(field_name="length",lookup_expr="gte")
    max_length = django_filters.NumberFilter(field_name="length",lookup_expr="lte")
    min_width = django_filters.NumberFilter(field_name="width",lookup_expr="gte")
    max_width = django_filters.NumberFilter(field_name="width",lookup_expr="lte")
    min_height = django_filters.NumberFilter(field_name="height",lookup_expr="gte")
    max_height = django_filters.NumberFilter(field_name="height",lookup_expr="lte")
    min_area = django_filters.NumberFilter(field_name="area",lookup_expr="gte")
    max_area = django_filters.NumberFilter(field_name="area",lookup_expr="lte")
    min_volume = django_filters.NumberFilter(field_name="volume",lookup_expr="gte")
    max_volume = django_filters.NumberFilter(field_name="volume",lookup_expr="lte")
    before_date=django_filters.DateFilter(field_name="created_on",lookup_expr='lte')
    
    class Meta:
        model = Box
        fields = ['user','min_length', 'max_length','min_width','max_width','min_height',
                  'max_height','min_area','max_area','min_volume','max_volume']


class ShowBox(generics.ListAPIView):
    queryset=Box.objects.all()
    serializer_class=ShowBoxSerializer
    filter_class=FilterClass
    filter_backends=[django_filters.rest_framework.DjangoFilterBackend]
    
    
    
class ShowMyBoxes(generics.ListAPIView):
    queryset=Box.objects.all()
    serializer_class=ShowMyBoxesSerializer
    filter_class=FilterClass
    filter_backends=[django_filters.rest_framework.DjangoFilterBackend]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    
    def get_queryset(self):
        user=self.request.user
        return Box.objects.filter(user=user)
        
class EditBox(generics.RetrieveUpdateAPIView):
    queryset=Box
    serializer_class=EditBoxSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    
    def perform_update(self,serializer):
        serializer.save(last_modified_by=self.request.user)
    
    
class DeleteBox(generics.DestroyAPIView):
    queryset=Box
    serializers_class=DeleteBoxSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    
    def destroy(self, request, pk,*args, **kwargs):
        user_created=Box.objects.filter(id=pk).values_list('user',flat=True).get()
        if user_created==self.request.user.id:
            return super().destroy(request,*args,**kwargs)
        else:
            raise serializers.ValidationError("You are not the creator of the box")
    