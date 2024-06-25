
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import contacts
from contacts.serializers import contactSerializers


# Create your views here.

@api_view(['GET'])
def getContacts(request):
    contacts_obj = contacts.objects.all()
    serializer_obj = contactSerializers(contacts_obj, many=True)
    return Response(serializer_obj.data)


@api_view(['POST'])
def saveContacts(request):
    serializer_obj = contactSerializers(data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response(serializer_obj.data, status=201)
    return Response(serializer_obj.errors, status=400)


@api_view(['GET'])
def getContact(request, id):
    try:
        contact_obj = contacts.objects.get(pk=id)
    except contacts.DoesNotExist:
        return Response({"message": "Contact not existed"}, status=404)

    serializer_obj = contactSerializers(contact_obj)
    return Response(serializer_obj.data)


@api_view(['DELETE'])
def deleteContact(request, id):
    try:
        contact_obj = contacts.objects.get(pk=id)
    except contacts.DoesNotExist:
        return Response({"message": "Contact not found"}, status=404)

    contact_obj.delete()
    return Response({"message": f"{id} contact deleted"}, status=204)


@api_view(['PUT'])
def updateContact(request, id):
    try:
        contact_obj = contacts.objects.get(pk=id)
    except contacts.DoesNotExist:
        return Response({"message": "Contact not found"}, status=404)

    serializer_obj = contactSerializers(contact_obj, data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response(serializer_obj.data)
    return Response(serializer_obj.errors, status=400)
