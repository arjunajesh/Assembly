from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from events.models import Event

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_reccomended_events(request):
    user = request.user
    user_flags = user.profile.flags.all()
    recc_events_for_user = Event.objects.filter(flags__in = user_flags).values_list("id","name")
    return Response({
        'events':list(recc_events_for_user)
    })


