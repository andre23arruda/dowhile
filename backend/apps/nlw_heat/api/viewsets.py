from django.shortcuts import redirect
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action, permission_classes, authentication_classes
from rest_framework.response import Response

import datetime, requests, jwt, os

from .serializers import MessageSerializer, ProfileSerializer
from .utils.wordcloud import create_word_cloud
from ..models import Message, Profile

CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
CLIENT_ID = os.environ['GITHUB_CLIENT_ID']

def create_token(profile: Profile):
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    minutes = datetime.timedelta(minutes=60)
    token = jwt.encode(
        {
            'id': profile.id,
            'exp':  now + minutes
        },
        key=CLIENT_SECRET,
    )
    return token


def decode_token(token: str):
    try:
        result = jwt.decode(token, CLIENT_SECRET, leeway=10, algorithms=['HS256'])
    except:
        result = {'message': 'Signature has expired'}
    return result


@api_view(['GET'])
def github_token(request):
    url = f'https://github.com/login/oauth/authorize?client_id={ CLIENT_ID }'
    return redirect(url)


@api_view(['GET'])
def signin_callback(request):
    code = request.GET.get('code')
    return Response({
        'auth_token': code
    })


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def github_auth(request):
    code = request.query_params.get('code')
    url = 'https://github.com/login/oauth/access_token'
    headers = {'Accept': 'application/json'}
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code
    }
    response = requests.post(
        url,
        headers=headers,
        params=params
    )
    response = response.json()

    access_token = response.get('access_token', None)
    if access_token:
        url_user = 'https://api.github.com/user'
        headers_user = {'authorization': f'Bearer { access_token }'}
        response_user = requests.get(
            url_user,
            headers=headers_user,
        )
        response_user = response_user.json()

        profile, _ = Profile.objects.get_or_create(
            name=response_user['name'],
            username=response_user['login'],
            github_id=response_user['id'],
            avatar=response_user['avatar_url'],
        )
        token = create_token(profile)
        serializer = ProfileSerializer(profile)
        return Response({'token': token, **serializer.data})

    return Response(response)


class MessagesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Message to be viewed or created.'''
    authentication_classes = []
    permission_classes = []
    http_method_names = ['get', 'post']
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageSerializer

    def create(self, serializer):
        '''Create Message'''
        token = self.request.headers['Authorization']
        token_info = decode_token(token)
        profile_id = token_info.get('id', None)
        if profile_id:
            data = serializer.data
            message = Message.objects.create(
                text=data['text'],
                user_id=profile_id,
            )
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        return Response({'message': 'ERROR in token'}, status=status.HTTP_401_UNAUTHORIZED)


    @action(detail=False, methods=['get'])
    def last_3(self, request, *args, **kwargs):
        '''Clona projeto, exclui projeto atual e arquivos do bucket'''
        queryset = self.get_queryset()
        last_messages = queryset[:3]
        serializer = MessageSerializer(last_messages, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def word_cloud(self, request, *args, **kwargs):
        '''Retorna nuvem de palavras mais comentadas'''
        messages = self.get_queryset()
        image = create_word_cloud(messages)
        return Response({'image': image})


class ProfilesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Profile to be viewed'''
    authentication_classes = []
    permission_classes = []
    http_method_names = ['get']
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request):
        token = request.headers['Authorization']
        token_info = decode_token(token)
        profile_id = token_info.get('id', None)
        if profile_id:
            queryset = self.get_queryset()
            profile = queryset.get(id=profile_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        return Response({'message': 'ERROR in token'}, status=status.HTTP_401_UNAUTHORIZED)
