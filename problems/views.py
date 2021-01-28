from django.shortcuts import render
from rest_framework.response import Response
from problems.models import Problem
from problems.serializers import ProblemSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, SAFE_METHODS

@api_view(['GET'])
@permission_classes([AllowAny])
def problem_list(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def problem_detail(request, pk):
    problems = Problem.objects.get(id = pk)
    serializer = ProblemSerializer(problems, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def problem_add(request):
    serializer = ProblemSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({'error':True,'message':serializer.errors}, 400)
    else:
        serializer.save()
        return Response({'error':None,'message':'success', 'data':serializer.data}, 201)

@api_view(['POST'])
def problem_update(request, pk):
    problem = Problem.objects.get(id = pk)
    serializer = ProblemSerializer(instance=problem, data=request.data)

    if not serializer.is_valid():
        return Response({'error':True,'message':serializer.errors}, 400)
    else:
        serializer.save()
        return Response({'error':None,'message':'update success', 'data':serializer.data}, 201)

@api_view(['DELETE'])
def problem_delete(request, pk):
    try:
        problem = Problem.objects.get(id = pk)
        problem.delete()
        return Response(f"Problem with ID:{pk} has been deleted.")
    except:
        return Response({'error':True,'message':'ID not found'}, 400)
