{% extends "album.html" %}
{% block topnav %}
   <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="explore">Explore</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="album">Learn</a>
        </li>
        <li class="nav-item">
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
{% endblock %}