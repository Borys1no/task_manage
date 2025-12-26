from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])

def task_list_api(request):
    if request.method == 'GET':
        status_param = request.GET.get('status')
        task = Task.objects.filter(user=request.user)

        if status_param == 'peding':
            task = task.filter(completed=False)
        elif status_param == 'completed':
            task = task.filter(completed=True)
        
        serializer = TaskSerializer(task, many= True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data )
        if serializer.is_valid():
            task=serializer.save(user=request.user)
            return Response(
                TaskSerializer(task).data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])

def task_detail_api(request, id):
    task = Task.objects.filter(id=id, user=request.user).first()

    if not task:
        return Response(
            {'error': 'Tarea no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        