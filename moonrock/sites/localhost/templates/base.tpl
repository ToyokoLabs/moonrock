<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v4.1.1">
    <title>
    {% if blog %}
    MoonRock: Blog
    {% endif %}
    {% if home %}
    MoonRock
    {% endif %}
    {% if checkout %}
    MoonRock: Checkout
    {% endif %}
    {% if learn %}
    MoonRock: Learn
    {% endif %}
    {% if subscribe %}
    MoonRock: Subscribe
    {% endif %}

    </title>


    <link rel="canonical" href="https://getbootstrap.com/docs/4.5/examples/carousel/">

    <!-- Bootstrap core CSS -->
<link href="static/assets/dst/css/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    {% if blog %}
     <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900" rel="stylesheet">	
    <!-- Custom styles for this template -->	
    <link href="static/blog/blog.css" rel="stylesheet">
    {% endif %}
    {% if home %}
    <link href="static/carousel/carousel.css" rel="stylesheet">
    {% endif %}

  </head>
  <body>
      {% if blog %}
 <div class="container">
      {% endif %}

    <header>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="#">MoonRock</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item {% if home %}active{% endif %}">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item {% if blog %}active{% endif %}">
          <a class="nav-link" href="explore">Explore</a>
        </li>
        <li class="nav-item {% if learn %}active{% endif %}">
          <a class="nav-link" href="learn">Learn</a>
        </li>
        <li class="nav-item {% if subscribe %}active{% endif %}">
          <a class="nav-link" href="subscribe">Subcribe</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/#Contact">Contact</a>
        </li>
      </ul>
      <form class="form-inline mt-2 mt-md-0">
        <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</header>

{% block main %}{% endblock %}


<!-- FOOTER -->
<div class="pt-4"></div>
<footer class="container">
  <p class="float-right"><a href="#">Back to top</a></p>
  <p>&copy; 2020 MoonRock, Inc. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
</footer>
</body>
{% block checkoutjs %}{% endblock %}
</html>
