// Get search form and page links
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

// Ensure search form exits
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();
      // Get data attribute
      let page = this.dataset.page;

      // Add hidden search input to form
      searchForm.innerHTML += `<input value=${page} name='page' hidden />`;

      // Submit form
      searchForm.submit();
    });
  }
}
