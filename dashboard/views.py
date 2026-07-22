from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        GET /api/dashboard/
        Return dashboard summary.
        """

        return Response({
            "message": "Dashboard endpoint."
        })


class MyItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        GET /api/dashboard/items/
        List authenticated user's items.
        """

        return Response({
            "message": "My items endpoint."
        })


class MyItemDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        """
        PUT /api/dashboard/items/<id>/
        Update one of the user's items.
        """

        return Response(
            {
                "message": "Item updated successfully."
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk):
        """
        DELETE /api/dashboard/items/<id>/
        Delete one of the user's items.
        """

        return Response(
            {
                "message": "Item deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )