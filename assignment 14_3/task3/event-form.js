const form = document.getElementById("regForm");
const nameInp = document.getElementById("name");
const emailInp = document.getElementById("email");
const phoneInp = document.getElementById("phone");
const deptSel = document.getElementById("department");
const eventSel = document.getElementById("event");
const successMessage = document.getElementById("successMessage");

const fields = [
  { input: nameInp, errorId: "nameError", validator: v => v.trim() !== "", message: "Name is required." },
  { input: emailInp, errorId: "emailError", validator: v => /^\S+@\S+\.\S+$/.test(v), message: "Enter a valid email." },
  { input: phoneInp, errorId: "phoneError", validator: v => /^\d{10}$/.test(v), message: "Phone must be 10 digits." },
  { input: deptSel, errorId: "deptError", validator: v => v !== "", message: "Select a department." },
  { input: eventSel, errorId: "eventError", validator: v => v !== "", message: "Select an event." },
];

function showError(input, errorId, message) {
  const el = document.getElementById(errorId);
  el.textContent = message;
  el.classList.add("visible");
  input.setAttribute("aria-invalid", "true");
}

function clearError(input, errorId) {
  const el = document.getElementById(errorId);
  el.textContent = "";
  el.classList.remove("visible");
  input.removeAttribute("aria-invalid");
}

function validateField(field) {
  const value = field.input.value;
  if (!field.validator(value)) {
    showError(field.input, field.errorId, field.message);
    return false;
  }
  clearError(field.input, field.errorId);
  return true;
}

fields.forEach(field => {
  field.input.addEventListener("input", () => {
    validateField(field);
    successMessage.textContent = "";
  });
});

form.addEventListener("submit", function(event) {
  event.preventDefault();
  let valid = true;
  fields.forEach(field => { if (!validateField(field)) valid = false; });

  if (!valid) {
    successMessage.textContent = "";
    return;
  }

  successMessage.textContent = "Registration successful! 🎉";
  form.reset();
  fields.forEach(field => clearError(field.input, field.errorId));
});
