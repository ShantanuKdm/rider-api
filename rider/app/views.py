from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

class SignupView(APIView):
    def post(self, request):
        data={**request.POST.dict(), **{k:v.read() for k,v in request.FILES.items()}}
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Profile created successfully.", "profile_created": user.name}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(APIView):
    def put(self, request):
        try:
            data={**request.POST.dict(), **{k:v.read() for k,v in request.FILES.items()}}
            user_profile = User.objects.get(id=data.get("user_id"))
        except User.DoesNotExist:
            return Response({"message": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user_profile,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
