from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def conversation_list(request):
    """
    GET /api/conversations/
    List all conversations for the authenticated user.
    """

    return Response(
        {
            "message": "Conversation list endpoint."
        }
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def conversation_create(request):
    """
    POST /api/conversations/
    Start a new conversation.
    """

    return Response(
        {
            "message": "Create conversation endpoint."
        },
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def conversation_detail(request, pk):
    """
    GET /api/conversations/<id>/
    Get conversation details.
    """

    return Response(
        {
            "conversation_id": pk
        }
    )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def conversation_delete(request, pk):
    """
    DELETE /api/conversations/<id>/
    Delete (or archive) a conversation.
    """

    return Response(
        {
            "message": "Conversation deleted."
        },
        status=status.HTTP_204_NO_CONTENT,
    )