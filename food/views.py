from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Food
from .serializers import CategorySerializer, FoodSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .models import Order,OrderItem,Food
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.core.mail import EmailMessage

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class PlaceOrderView(APIView):

    def post(self, request):
        try:
            order = Order.objects.create(
            user_id=request.data["user"],
            full_name=request.data["full_name"],
            email=request.data["email"],
            mobile=request.data["mobile"],
            address=request.data["address"],
            city=request.data["city"],
            pincode=request.data["pincode"],
            total_amount=request.data["total_amount"]
        )

        for item in request.data["items"]:
            OrderItem.objects.create(
                order=order,
                food_id=item["food"],
                quantity=item["quantity"],
                price=item["price"]
            )

        # Send confirmation email
        msg_body = f"""Hello {order.full_name},Your order has been placed successfully.

         Order Details:
            -------------------------
Name: {order.full_name}
Total Amount: ₹{order.total_amount}

Thank you for ordering with us!

Food Delivery Team
"""

        email_msg = EmailMessage(
            subject="Order Placed Successfully",
            body=msg_body,
            to=[order.email]
        )
        email_msg.send(fail_silently=False)

        return Response({
            "message": "Order placed successfully!"
        })
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=500
            )
        
class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "username": user.username,
            "email": user.email,
            "date_joined": user.date_joined
        })
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def food_list(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True,
    context={"request": request}
    )
    return Response(serializer.data)

class DashboardView(APIView):

    def get(self, request):

        total_users = User.objects.count()
        total_foods = Food.objects.count()
        total_orders = Order.objects.count()

        total_revenue = sum(
            order.total_amount
            for order in Order.objects.all()
        )

        return Response({
            "total_users": total_users,
            "total_foods": total_foods,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
        })
    

#         later protect the dashboard
#         from rest_framework.permissions import IsAdminUser

# class DashboardView(APIView):

#     permission_classes = [IsAdminUser]
