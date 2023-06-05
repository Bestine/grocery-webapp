// scripts.js

// Function to toggle chat window visibility
function toggleChatWindow() {
    var chatWindow = document.getElementById("chat-window");
    chatWindow.classList.toggle("visible");
  }
  
  // Add event listener to chat launcher button
  var chatLauncherButton = document.querySelector(".chat-launcher");
  chatLauncherButton.addEventListener("click", toggleChatWindow);
  