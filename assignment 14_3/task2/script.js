document.addEventListener("DOMContentLoaded", () => {
  const slider = document.getElementById("slider");
  const slides = slider.querySelector(".slides");
  const images = slides.querySelectorAll("img");
  const prev = document.getElementById("prev");
  const next = document.getElementById("next");
  const menuToggle = document.getElementById("menuToggle");
  const nav = document.getElementById("nav");
  let index = 0;
  const total = images.length;
  let autoSlide = null;

  const move = () => { slides.style.transform = `translateX(-${index * 100}%)`; };
  const goNext = () => { index = (index + 1) % total; move(); };
  const goPrev = () => { index = (index - 1 + total) % total; move(); };

  next.addEventListener("click", () => { goNext(); resetAuto(); });
  prev.addEventListener("click", () => { goPrev(); resetAuto(); });

  function startAuto() { autoSlide = setInterval(goNext, 4200); }
  function resetAuto() { clearInterval(autoSlide); startAuto(); }
  startAuto();

  menuToggle.addEventListener("click", () => { nav.classList.toggle("open"); });
});