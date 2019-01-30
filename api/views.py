from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import permissions
# Users
from users.models import User
from users.serializers import UserSerializer
# Counterparts
from counterparties.models import Counterpart, Bank
from counterparties.serializers import CounterpartSerializer, BankSerializer


class BankList(APIView):
    """
    List all banks, or create a new bank.
    """

    @staticmethod
    def get_object():
        try:
            return Bank.objects.all()
        except Bank.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        banks = self.get_object()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        banks = self.get_object()
        if banks.is_valid():
            banks.save()
            return Response(banks.data, status=status.HTTP_201_CREATED)
        return Response(banks.errors, status=status.HTTP_400_BAD_REQUEST)


class BankDetail(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @staticmethod
    def get_object(pk):
        try:
            return Bank.objects.get(pk=pk)
        except Bank.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bank = self.get_object(pk)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CounterpartList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @staticmethod
    def get_object():
        try:
            return Counterpart.objects.all().order_by('-name')
        except Counterpart.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        counterparts = self.get_object()
        serializer = CounterpartSerializer(counterparts, many=True)
        return Response(serializer.data)


class CounterpartDetail(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @staticmethod
    def get_object(pk):
        try:
            return Counterpart.objects.get(pk=pk)
        except Counterpart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        counterpart = self.get_object(pk)
        serializer = CounterpartSerializer(counterpart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        counterpart = self.get_object(pk)
        serializer = CounterpartSerializer(counterpart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        counterpart = self.get_object(pk)
        counterpart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @staticmethod
    def get_object():
        try:
            return User.objects.all().order_by('-pseudonym')
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        users = self.get_object()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @staticmethod
    def get_object(pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Удалять пока запретим
    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
