from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response 
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.
class manage_art_view(APIView):
    
    def get(self,request):
        list_art=ARTTable.objects.all()
        json_art=art_serializers(list_art,many=True)

        return Response(json_art.data)
    
    def post(self,request):
        request.data.get('art_name')

    #user_id = request.user.user_id


class manage_team_member_view(APIView):
    

    # 🔹 GET all team members
    def get(self, request):
        team_members = TeamMembersTable.objects.all()
        serializer = TeamMemberSerializer(team_members, many=True)
        return Response(serializer.data)

    # 🔹 POST create team member
    def post(self, request):

        serializer = TeamMemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Team member created successfully",
                    "data": serializer.data
                },
                status=201
            )

        return Response(serializer.errors, status=400)
    