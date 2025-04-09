
  document.addEventListener("DOMContentLoaded", () => {
    const pathParts = window.location.pathname.split("/");
    const username = pathParts[pathParts.length - 2]; // because the URL ends with "/username/"
  
    fetch(`/api/profile/${username}/`)
      .then((res) => res.json())
      .then((data) => {
        if (data.error) {
          document.body.innerHTML = `<h2>Profile not found</h2>`;
          return;
        }
  
        document.getElementById("profile-img").src = data.image;
        document.getElementById("profile-name").textContent = data.name;
        document.getElementById("profile-role").textContent = data.designation;
        document.getElementById("profile-email").innerHTML = `<a href="mailto:${data.email}">${data.email}</a>`;
        document.getElementById("profile-phone").innerHTML = `<a href="tel:${data.phone}">${data.phone}</a>`;
        document.getElementById("profile-address").textContent = data.address;
        document.getElementById("profile-linkedin").innerHTML = `<a href="${data.linkedin}" target="_blank">${data.name}</a>`;
        document.getElementById("company-link").href = data.company_link;
      })
      .catch((err) => {
        console.error(err);
        document.body.innerHTML = `<h2>Something went wrong.</h2>`;
      });
  });
  