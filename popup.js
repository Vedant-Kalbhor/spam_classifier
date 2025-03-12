document.getElementById("checkSpam").addEventListener("click", function () {
    let message = document.getElementById("message").value;
    let resultDiv = document.getElementById("result");

    if (message.trim() === "") {
        resultDiv.innerHTML = "Please enter a message.";
        return;
    }

    // Replace this URL with your deployed Streamlit API endpoint
    let apiUrl = "https://your-streamlit-app-url.com/predict";

    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result === 1) {
            resultDiv.innerHTML = "🚨 SPAM";
            resultDiv.style.color = "red";
        } else {
            resultDiv.innerHTML = "✅ NOT SPAM";
            resultDiv.style.color = "green";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        resultDiv.innerHTML = "Error checking spam.";
    });
});
