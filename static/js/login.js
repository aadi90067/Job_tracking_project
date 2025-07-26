  document.getElementById('loginForm').addEventListener('submit', function(ev) {
    ev.preventDefault();
    window.location.href = "{% url 'login' %}";
  });

