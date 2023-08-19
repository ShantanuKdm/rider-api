from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,Tour, Task
from .serializers import UserSerializer, TaskSerializer

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

class TaskListByTourView(APIView):
    def get(self, request, tour_id):
        try:

            tasks = Task.objects.filter(tour_id=tour_id)
            
            # Get the 'status' query parameter from the URL, if present
            status_filter = request.query_params.get('status',None)
            print(status_filter)
            if status_filter:
                tasks = tasks.filter(status=status_filter)
            
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except Tour.DoesNotExist:
            return Response({"message": "Tour not found."}, status=status.HTTP_404_NOT_FOUND)
        except Task.DoesNotExist:
            return Response({"message": "Tasks not found for the given tour."}, status=status.HTTP_404_NOT_FOUND)

class UpdateTaskStatusView(APIView):
    def put(self, request, task_id):
        try:
            task = Task.objects.get(task_id=task_id)
        except Task.DoesNotExist:
            return Response({"message": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task status updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

