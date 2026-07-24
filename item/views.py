from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        List all categories.
        """

        return Response({
            "message": "Category list endpoint."
        })


class ItemListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        List all items.
        """

        return Response({
            "message": "Item list endpoint."
        })

    def post(self, request):
        """
        Create a new item.
        """

        return Response(
            {
                "message": "Item created successfully."
            },
            status=status.HTTP_201_CREATED,
        )


class ItemDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        """
        Retrieve item details.
        """

        return Response({
            "item_id": pk
        })

    def put(self, request, pk):
        """
        Update an item.
        """

        return Response({
            "message": "Item updated successfully."
        })

    def delete(self, request, pk):
        """
        Delete an item.
        """

        return Response(
            {
                "message": "Item deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )