from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, api_view
from .serializers import ProjectSerializer
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project_view(request):
    user = request.user
    data = request.data
    title = data.get("title", None)
    favorite = data.get("favorite", None)
    description = data.get("description", None)

    try:
        Project.objects.create(
            user=user,
            title=title,
            favorite=favorite,
            description=description
        )
        return Response({"message": "Your project created successfully "}, status=status.HTTP_200_OK)
    except:
        return Response({"error": "something went wrong while creating the project"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project_list(request):
    user = request.user

    projects = user.project_set.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
