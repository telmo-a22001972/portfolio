document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("input").onchange = function () {
    document.querySelector("#hello").style.color = this.value;
  };
});