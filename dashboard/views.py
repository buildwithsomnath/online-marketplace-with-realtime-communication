from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Dashboard overview.
        """

        return Response({
            "message": "Dashboard overview."
        })


class MyItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        List all items created by the authenticated user.
        """

        return Response({
            "message": "My items endpoint."
        })