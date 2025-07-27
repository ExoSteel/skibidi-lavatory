// Fetch and display all existing accounts on page load
fetch("/api/accounts")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("account-list");
    if (list && Array.isArray(data.accounts)) {
      data.accounts.forEach(acc => {
        const li = document.createElement("li");
        li.textContent = `#${acc.id} | 📧 ${acc.email} | 🔑 ${acc.password}`;
        list.appendChild(li);
      });
    }
  });

// Listen for new accounts in real-time via socket.io
const socket = io();
socket.on("new_acc", data => {
  const li = document.createElement("li");
  li.textContent = `#${data.id} | 📧 ${data.email} | 🔑 ${data.password}`;
  const list = document.getElementById("account-list");
  if (list) list.appendChild(li);
});
