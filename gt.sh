#!/bin/bash

# Define the global templates directory
GLOBAL_TEMPLATES_DIR="templates"

# Create the global templates directory if it doesn't exist
mkdir -p $GLOBAL_TEMPLATES_DIR

# Function to create and populate HTML files in the global templates directory
create_global_html_templates() {
    echo "Creating and populating global HTML templates..."

    # Base template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}E-commerce{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include 'navbar.html' %}
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    {% include 'footer.html' %}
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
EOL

    # Navbar template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/navbar.html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="{% url 'home' %}">E-commerce</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item">
        <a class="nav-link" href="{% url 'products:product_list' %}">Products</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'cart:cart_detail' %}">Cart</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:profile' %}">Profile</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'wishlist:wishlist_detail' %}">Wishlist</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'vendors:vendor_dashboard' %}">Vendor Dashboard</a>
      </li>
    </ul>
  </div>
</nav>
EOL

    # Footer template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/footer.html
<footer class="footer mt-auto py-3 bg-light">
  <div class="container text-center">
    <span class="text-muted">© 2024 E-commerce Platform</span>
  </div>
</footer>
EOL

    # Home page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/home.html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
  <div class="jumbotron text-center">
    <h1>Welcome to Our E-commerce Platform</h1>
    <p>Explore the best products from our vendors.</p>
    <a class="btn btn-primary btn-lg" href="{% url 'products:product_list' %}" role="button">Shop Now</a>
  </div>

  <h2 class="text-center">Featured Collections</h2>
  <div class="row">
    {% for category in categories %}
      <div class="col-md-4">
        <div class="card mb-4">
          <img src="{{ category.image.url }}" class="card-img-top" alt="{{ category.name }}">
          <div class="card-body">
            <h5 class="card-title">{{ category.name }}</h5>
            <p class="card-text">{{ category.description }}</p>
            <a href="{% url 'categories:category_detail' category.slug %}" class="btn btn-primary">Explore</a>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
EOL

    # SEO template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/seo.html
<meta name="description" content="Welcome to our E-commerce Platform. Find the best products from top vendors.">
<meta name="keywords" content="ecommerce, shopping, products, vendors">
<meta name="author" content="E-commerce Platform">
EOL

    # Scripts template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/scripts.html
<script>
  // Add your custom JavaScript here
  console.log('Welcome to our E-commerce Platform');
</script>
EOL

    # Styles template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/styles.html
<style>
  /* Add your custom CSS here */
  body {
    padding-top: 56px;
  }
  .jumbotron {
    background-color: #f8f9fa;
  }
</style>
EOL

    # Social share template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/social_share.html
<div class="social-share">
  <a href="https://www.facebook.com/sharer/sharer.php?u={{ request.build_absolute_uri }}" target="_blank">Share on Facebook</a>
  <a href="https://twitter.com/intent/tweet?url={{ request.build_absolute_uri }}&text=Check%20out%20this%20awesome%20site!" target="_blank">Share on Twitter</a>
</div>
EOL

    # 404 Error page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/404.html
{% extends 'base.html' %}

{% block title %}Page Not Found{% endblock %}

{% block content %}
  <div class="container text-center mt-5">
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{% url 'home' %}" class="btn btn-primary">Go to Home</a>
  </div>
{% endblock %}
EOL

    # About page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/about.html
{% extends 'base.html' %}

{% block title %}About Us{% endblock %}

{% block content %}
  <div class="container mt-5">
    <h2>About Our Platform</h2>
    <p>We are a leading e-commerce platform, connecting customers with top vendors and the best products. Our mission is to provide a seamless shopping experience with a wide range of products and reliable customer service.</p>
  </div>
{% endblock %}
EOL

    # Contact page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/contact.html
{% extends 'base.html' %}

{% block title %}Contact Us{% endblock %}

{% block content %}
  <div class="container mt-5">
    <h2>Contact Us</h2>
    <form method="POST">
      {% csrf_token %}
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" name="name" required>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" class="form-control" id="email" name="email" required>
      </div>
      <div class="form-group">
        <label for="message">Message</label>
        <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Send Message</button>
    </form>
  </div>
{% endblock %}
EOL

    # FAQ page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/faq.html
{% extends 'base.html' %}

{% block title %}FAQ{% endblock %}

{% block content %}
  <div class="container mt-5">
    <h2>Frequently Asked Questions</h2>
    <h5>Q: How can I track my order?</h5>
    <p>A: You can track your order by logging into your account and visiting the "Orders" section.</p>
    <h5>Q: What is the return policy?</h5>
    <p>A: Our return policy allows you to return products within 30 days of receipt for a full refund.</p>
    <!-- Add more FAQs as needed -->
  </div>
{% endblock %}
EOL

    # Privacy Policy page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/privacy_policy.html
{% extends 'base.html' %}

{% block title %}Privacy Policy{% endblock %}

{% block content %}
  <div class="container mt-5">
    <h2>Privacy Policy</h2>
    <p>We take your privacy seriously. This policy outlines how we collect, use, and protect your personal information.</p>
    <!-- Add detailed privacy policy here -->
  </div>
{% endblock %}
EOL

    # Terms of Service page template
    cat <<EOL > $GLOBAL_TEMPLATES_DIR/terms.html
{% extends 'base.html' %}

{% block title %}Terms of Service{% endblock %}

{% block content %}
  <div class="container mt-5">
    <h2>Terms of Service</h2>
    <p>By using our platform, you agree to the following terms and conditions.</p>
    <!-- Add detailed terms of service here -->
  </div>
{% endblock %}
EOL
}

# Create global HTML templates
create_global_html_templates

echo "Global HTML templates have been created and populated."

# Create and populate views.py for the home page in the ecommerce app
echo "Creating and populating views.py for the home page in the ecommerce app..."

cat <<EOL >> ecommerce/views.py
from django.shortcuts import render
from categories.models import Category

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
EOL

echo "Home page view has been added to ecommerce/views.py."

# Add URL pattern for the home page in ecommerce/urls.py
echo "Updating ecommerce/urls.py with the home page URL pattern..."

cat <<EOL >> ecommerce/urls.py

from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    # Other URL patterns...
]
EOL

echo "Home page URL pattern has been added to ecommerce/urls.py."
