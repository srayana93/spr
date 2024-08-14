#!/bin/bash

# Function to create and populate HTML templates for an app
create_html_templates() {
    local app=$1

    echo "Creating and populating HTML templates for $app..."

    mkdir -p $app/templates/$app

    # Creating and populating common HTML files based on typical views
    case $app in
        accounts)
            cat <<EOL > $app/templates/$app/profile.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>User Profile</h2>
    <form method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ profile_form.as_p }}
      <button type="submit" class="btn btn-primary">Save Changes</button>
    </form>
  </div>
{% endblock %}
EOL
            ;;

        analytics)
            cat <<EOL > $app/templates/$app/analytics_dashboard.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Analytics Dashboard</h2>
    <p>View your order data and product views here.</p>
    <!-- Add more detailed analytics data here -->
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/report_list.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Reports</h2>
    <ul>
      {% for report in reports %}
        <li><a href="{% url 'analytics:report_detail' report.id %}">{{ report.user.email }} - {{ report.total_orders }} Orders</a></li>
      {% endfor %}
    </ul>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/report_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Report Detail</h2>
    <p>User: {{ report.user.email }}</p>
    <p>Total Orders: {{ report.total_orders }}</p>
    <p>Total Spent: {{ report.total_spent }}</p>
    <!-- Add more detailed report data here -->
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/report_generate.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Generate Report</h2>
    <form method="POST">
      {% csrf_token %}
      <button type="submit" class="btn btn-primary">Generate</button>
    </form>
  </div>
{% endblock %}
EOL
            ;;

        cart)
            cat <<EOL > $app/templates/$app/cart_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Your Cart</h2>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Product</th>
          <th>Quantity</th>
          <th>Price</th>
          <th>Total</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {% for item in cart.items.all %}
          <tr>
            <td>{{ item.product.name }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.total_price }}</td>
            <td>
              <a href="{% url 'cart:remove_from_cart' item.id %}" class="btn btn-danger">Remove</a>
            </td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
    <a href="{% url 'cart:checkout' %}" class="btn btn-primary">Checkout</a>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/checkout.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Checkout</h2>
    <form method="POST">
      {% csrf_token %}
      {{ checkout_form.as_p }}
      <button type="submit" class="btn btn-primary">Place Order</button>
    </form>
  </div>
{% endblock %}
EOL
            ;;

        categories)
            cat <<EOL > $app/templates/$app/categories_list.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Categories</h2>
    <ul>
      {% for category in categories %}
        <li><a href="{% url 'categories:category_detail' category.slug %}">{{ category.name }}</a></li>
      {% endfor %}
    </ul>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/categories_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>{{ category.name }}</h2>
    <p>{{ category.description }}</p>
    <!-- Display category-specific products or subcategories here -->
  </div>
{% endblock %}
EOL
            ;;

        chat)
            cat <<EOL > $app/templates/$app/chat_window.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Chat Window</h2>
    <div class="row">
      <div class="col-md-4">
        <ul class="list-group">
          {% for room in chat_rooms %}
            <li class="list-group-item">
              <a href="{% url 'chat:chat_history' room.id %}">Chat Room {{ room.id }}</a>
            </li>
          {% endfor %}
        </ul>
      </div>
      <div class="col-md-8">
        {% if chat_room %}
          <h3>Chat History</h3>
          <ul class="list-group">
            {% for message in chat_room.messages.all %}
              <li class="list-group-item">
                <strong>{{ message.sender.email }}:</strong> {{ message.message }}
              </li>
            {% endfor %}
          </ul>
        {% endif %}
      </div>
    </div>
  </div>
{% endblock %}
EOL
            ;;

        orders)
            cat <<EOL > $app/templates/$app/order_list.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Your Orders</h2>
    <ul>
      {% for order in orders %}
        <li><a href="{% url 'orders:order_detail' order.order_number %}">Order #{{ order.order_number }}</a> - {{ order.status }}</li>
      {% endfor %}
    </ul>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/order_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Order #{{ order.order_number }}</h2>
    <p>Status: {{ order.status }}</p>
    <p>Total Amount: \${{ order.total_amount }}</p>
    <p>Order Date: {{ order.created_at }}</p>
    <h3>Items:</h3>
    <ul>
      {% for item in order.items.all %}
        <li>{{ item.product.name }} x {{ item.quantity }} - \${{ item.price }}</li>
      {% endfor %}
    </ul>
  </div>
{% endblock %}
EOL
            ;;

        payments)
            cat <<EOL > $app/templates/$app/payment_form.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Payment Form</h2>
    <form method="POST">
      {% csrf_token %}
      <!-- Include payment gateway form fields here -->
      <button type="submit" class="btn btn-primary">Pay Now</button>
    </form>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/payment_success.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Payment Successful</h2>
    <p>Your payment was processed successfully.</p>
    <a href="{% url 'orders:order_list' %}" class="btn btn-primary">View Orders</a>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/payment_failure.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Payment Failed</h2>
    <p>There was an issue processing your payment. Please try again.</p>
    <a href="{% url 'payments:payment_form' %}" class="btn btn-danger">Try Again</a>
  </div>
{% endblock %}
EOL
            ;;

        products)
            cat <<EOL > $app/templates/$app/product_list.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Products</h2>
    <div class="row">
      {% for product in products %}
        <div class="col-md-4">
          <div class="card mb-4">
            <img src="{{ product.image.url }}" class="card-img-top" alt="{{ product.name }}">
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <p class="card-text">\${{ product.price }}</p>
              <a href="{% url 'products:product_detail' product.slug %}" class="btn btn-primary">View Product</a>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/product_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-6">
        <img src="{{ product.image.url }}" class="img-fluid" alt="{{ product.name }}">
      </div>
      <div class="col-md-6">
        <h2>{{ product.name }}</h2>
        <p>{{ product.description }}</p>
        <p>\${{ product.price }}</p>
        <a href="{% url 'cart:add_to_cart' product.id %}" class="btn btn-primary">Add to Cart</a>
      </div>
    </div>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/product_create.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Create Product</h2>
    <form method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit" class="btn btn-primary">Create Product</button>
    </form>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/bulk_upload.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Bulk Upload Products</h2>
    <form method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit" class="btn btn-primary">Upload</button>
    </form>
  </div>
{% endblock %}
EOL
            ;;

        vendors)
            cat <<EOL > $app/templates/$app/vendor_dashboard.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Vendor Dashboard</h2>
    <p>Welcome to your dashboard, {{ vendor.company_name }}!</p>
    <a href="{% url 'vendors:vendor_product_list' %}" class="btn btn-primary">Manage Products</a>
  </div>
{% endblock %}
EOL

            cat <<EOL > $app/templates/$app/vendor_product_list.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Manage Products</h2>
    <a href="{% url 'vendors:vendor_product_create' %}" class="btn btn-primary mb-3">Add New Product</a>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Stock</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {% for product in products %}
          <tr>
            <td>{{ product.name }}</td>
            <td>\${{ product.price }}</td>
            <td>{{ product.stock_quantity }}</td>
            <td>
              <a href="{% url 'vendors:vendor_product_update' product.slug %}" class="btn btn-secondary">Edit</a>
              <a href="{% url 'vendors:vendor_product_delete' product.slug %}" class="btn btn-danger">Delete</a>
            </td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
{% endblock %}
EOL
            ;;

        wishlist)
            cat <<EOL > $app/templates/$app/wishlist_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="container mt-5">
    <h2>Your Wishlist</h2>
    <ul>
      {% for item in wishlist.items.all %}
        <li>{{ item.product.name }} <a href="{% url 'wishlist:remove_from_wishlist' item.id %}">Remove</a></li>
      {% endfor %}
    </ul>
  </div>
{% endblock %}
EOL
            ;;
    esac
}

# Populate HTML templates for each app
for app in "accounts" "analytics" "cart" "categories" "chat" "orders" "payments" "products" "vendors" "wishlist"; do
    create_html_templates $app
done

echo "HTML templates have been created and populated for all apps."
